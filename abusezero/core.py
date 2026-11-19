from __future__ import annotations

import asyncio
import base64
import hashlib
import hmac
import json
import math
import re
import time
import threading
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from importlib.resources import files
from typing import Any
from urllib.parse import quote, urlencode, urlsplit

import httpx

OPERATIONS = json.loads(files(__package__).joinpath('operations.json').read_text())
SECRET = re.compile(r'^(?:sk|rk)_[1-9][0-9]{19}\.[A-Za-z0-9_-]{43}$')
CREDENTIAL_HEADER = re.compile(r'^(authorization|proxy-authorization|cookie|set-cookie|x-api-key|x-auth-token|x-csrf-token|x-xsrf-token)$|(?:^|-)(token|secret|session|password|api-key|apikey)(?:-|$)', re.I)


class AbuseZeroError(Exception):
    def __init__(self, code: str, message: str, status: int = 0, request_id: str | None = None, retryable: bool = False, docs_url: str | None = None):
        super().__init__(message)
        self.code, self.status, self.request_id, self.retryable, self.docs_url = code, status, request_id, retryable, docs_url


class WebhookVerificationError(ValueError):
    pass


def incoming_request(method: str, url: str, headers: dict[str, str]) -> dict[str, Any]:
    parsed = urlsplit(url)
    if not re.fullmatch(r'[A-Za-z]{1,16}', method) or parsed.scheme not in ('http', 'https') or not parsed.hostname or parsed.username or parsed.password or len(url) > 4096:
        raise ValueError('Provide the incoming HTTP method and URL without credentials.')
    clean, size = {}, 0
    for name, value in headers.items():
        name = name.lower()
        if CREDENTIAL_HEADER.search(name):
            continue
        if not re.fullmatch(r"[!#$%&'*+.^_`|~0-9a-z-]{1,128}", name) or not isinstance(value, str) or '\r' in value or '\n' in value:
            continue
        value = value[:8192]
        if len(clean) >= 64 or size + len(name.encode()) + len(value.encode()) > 32768:
            break
        clean[name] = value
        size += len(name.encode()) + len(value.encode())
    return {'method': method, 'url': url, 'headers': clean}


def _hash(secret: str | bytes, key_version: str, value: str) -> dict[str, str]:
    if not re.fullmatch(r'[\x21-\x7e]{1,128}', key_version):
        raise ValueError('Use a printable key version with no spaces.')
    return {'algorithm': 'hmac-sha256', 'key_version': key_version, 'value': hmac.new(secret.encode() if isinstance(secret, str) else secret, value.encode(), hashlib.sha256).hexdigest()}


def create_phone_hash(*, secret: str | bytes, key_version: str, e164: str) -> dict[str, str]:
    if not re.fullmatch(r'\+[1-9][0-9]{7,14}', e164):
        raise ValueError('Normalize the phone number to E.164 before hashing it.')
    return _hash(secret, key_version, 'abusezero:phone:e164:v1:' + e164)


def create_custom_identifier(*, secret: str | bytes, key_version: str, key: str, value: str) -> dict[str, Any]:
    if not re.fullmatch(r'[a-z][a-z0-9_]{0,63}', key) or not value:
        raise ValueError('Provide a valid identifier key and nonempty value.')
    return {'key': key, 'value_hash': _hash(secret, key_version, f'abusezero:custom:{key}:v1:{value}')}


def verify_webhook(*, payload: str | bytes, headers: dict[str, str], secret: str | list[str | None], tolerance_seconds: float = 300, now: float | None = None) -> dict[str, Any]:
    if not math.isfinite(tolerance_seconds) or tolerance_seconds < 0:
        raise ValueError('Use a nonnegative timestamp tolerance.')
    keys = []
    for item in ([secret] if isinstance(secret, str) else secret):
        if item is None or not item.strip():
            continue
        if not re.fullmatch(r'whsk_[A-Za-z0-9+/]{43}=', item.strip()):
            raise ValueError('Provide the complete webhook signing secret.')
        keys.append(base64.b64decode(item.strip()[5:], validate=True))
    if not keys:
        raise ValueError('Provide a webhook signing secret.')
    h = {k.lower(): v for k, v in headers.items()}
    event_id, timestamp, signature = (h.get('abusezero-webhook-' + n, '') for n in ('id', 'timestamp', 'signature'))
    if not event_id or not re.fullmatch(r'\d{1,12}', timestamp) or abs((time.time() if now is None else now) - int(timestamp)) > tolerance_seconds:
        raise WebhookVerificationError('The webhook timestamp or headers are invalid.')
    body = payload.encode() if isinstance(payload, str) else payload
    signed = (event_id + '.' + timestamp + '.').encode() + body
    expected = [base64.b64encode(hmac.new(k, signed, hashlib.sha256).digest()).decode() for k in keys]
    if not any(hmac.compare_digest(s[3:], e) for s in signature.split() if s.startswith('v1,') for e in expected):
        raise WebhookVerificationError('The webhook signature does not match.')
    try:
        event = json.loads(body)
        if not isinstance(event, dict) or event.get('object') != 'event' or event.get('id') != event_id:
            raise ValueError()
        return event
    except (ValueError, UnicodeError):
        raise WebhookVerificationError('The webhook body is invalid.') from None


def _resolve(schema: Any, root: dict) -> Any:
    while isinstance(schema, dict) and '$ref' in schema:
        ref = root
        for part in schema['$ref'][2:].split('/'):
            ref = ref[part.replace('~1', '/').replace('~0', '~')]
        schema = ref
    return schema


def _unknown_kind(value: Any, variants: list, root: dict) -> bool:
    """A response object whose variants all fix the same kind field, carrying a kind none of them knows yet."""
    resolved = [_resolve(v, root) for v in variants]
    if not isinstance(value, dict) or not all(isinstance(v, dict) and isinstance(v.get('properties'), dict) for v in resolved):
        return False
    fixed = [{k: _resolve(p, root)['const'] for k, p in v['properties'].items() if isinstance(_resolve(p, root), dict) and 'const' in _resolve(p, root)} for v in resolved]
    objects = {f.get('object') for f in fixed}
    if len(objects) != 1 or None in objects or value.get('object') not in objects:
        return False
    for key in set.intersection(*(set(f) for f in fixed)) - {'object'}:
        if isinstance(value.get(key), str) and value[key] not in {f[key] for f in fixed}:
            return True
    return False


def _validate(value: Any, schema: dict, root: dict | None = None, response: bool = False, strict: bool = False, variant: bool = False) -> None:
    # Within v1, responses can gain new values for codes and enums, new kinds of an object and new fields. A response
    # keeps checking each object's own type and, inside a union, the fields that select a variant. A request may leave
    # out a field that has a default.
    root = root or schema
    if '$ref' in schema:
        return _validate(value, _resolve(schema, root), root, response, strict, variant)
    variants = schema.get('anyOf', schema.get('oneOf'))
    if variants:
        matches_count = 0
        for option in variants:
            try:
                _validate(value, option, root, response, strict, True)
                matches_count += 1
            except (ValueError, TypeError):
                pass
        if matches_count == 0 and not (response and _unknown_kind(value, variants, root)) or 'oneOf' in schema and not response and matches_count > 1:
            raise ValueError('The value does not match the request schema.')
        if matches_count == 0:
            return
    types = schema.get('type')
    types = types if isinstance(types, list) else [types] if types else []
    matches = {'null': value is None, 'string': isinstance(value, str), 'object': isinstance(value, dict), 'array': isinstance(value, list), 'integer': isinstance(value, int) and not isinstance(value, bool), 'number': isinstance(value, (float, int)) and not isinstance(value, bool) and math.isfinite(value), 'boolean': isinstance(value, bool)}
    if types and not any(matches.get(t, False) for t in types):
        raise ValueError('The value has the wrong type.')
    if 'const' in schema and value != schema['const'] and (not response or strict) or 'enum' in schema and not response and value not in schema['enum']:
        raise ValueError('The value is not an allowed choice.')
    if isinstance(value, dict):
        properties = schema.get('properties', {})
        for k in schema.get('required', []):
            if k not in value and (response or not isinstance(_resolve(properties.get(k), root), dict) or 'default' not in _resolve(properties.get(k), root)):
                raise ValueError('A required field is missing.')
        for k, v in value.items():
            if 'propertyNames' in schema: _validate(k, schema['propertyNames'], root, response)
            child = properties.get(k, schema.get('additionalProperties', {}))
            if child is False:
                raise ValueError('The request contains an unknown field.')
            if isinstance(child, dict):
                _validate(v, child, root, response, k == 'object' or variant)
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0) or len(value) > schema.get('maxItems', math.inf):
            raise ValueError('The list has an invalid length.')
        for item in value:
            _validate(item, schema.get('items', {}), root, response)
    if isinstance(value, str):
        if len(value) < schema.get('minLength', 0) or len(value) > schema.get('maxLength', math.inf) or 'pattern' in schema and not re.search(schema['pattern'], value):
            raise ValueError('The text does not match the request schema.')
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if 'multipleOf' in schema and not math.isclose(value / schema['multipleOf'], round(value / schema['multipleOf']), abs_tol=1e-9):
            raise ValueError('The number must be a permitted multiple.')
        if value < schema.get('minimum', -math.inf) or value > schema.get('maximum', math.inf) or value <= schema.get('exclusiveMinimum', -math.inf) or value >= schema.get('exclusiveMaximum', math.inf):
            raise ValueError('The number is outside the permitted range.')


class Base:
    _public = False

    def __init__(self, *, key: str | None = None, access_token: str | None = None, workspace: str | None = None, outage: str = 'throw', agent: str | None = None, base_url: str = 'https://api.abusezero.com', transport=None):
        if not self._public and bool(key) == bool(access_token):
            raise AbuseZeroError('CREDENTIAL_REQUIRED', 'Provide one server API key or OAuth access token.', 401)
        if key and not SECRET.fullmatch(key):
            raise AbuseZeroError('INVALID_KEY', 'Provide a server API key.', 401)
        if access_token and (not isinstance(access_token,str) or not re.fullmatch(r'[\x21-\x7e]{1,8192}',access_token)):
            raise AbuseZeroError('INVALID_TOKEN','Provide a valid OAuth access token.',401)
        if access_token and not workspace:
            raise AbuseZeroError('WORKSPACE_REQUIRED', 'Provide the selected workspace.', 422)
        if workspace and not re.fullmatch(r'[1-9][0-9]{19}', workspace):
            raise AbuseZeroError('INVALID_WORKSPACE', 'Provide the workspace ID.', 422)
        if outage not in ('throw', 'allow', 'deny'):
            raise ValueError('Set outage to throw, allow or deny.')
        parsed = urlsplit(base_url)
        if (parsed.scheme != 'https' and not (parsed.scheme == 'http' and parsed.hostname in ('localhost', '127.0.0.1', '::1'))) or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment or parsed.path not in ('', '/'):
            raise ValueError('Use an HTTPS API origin, or HTTP on loopback for local testing.')
        self._credential, self._workspace, self._outage = key or access_token, workspace, outage
        self._key, self._base, self._transport = bool(key), base_url.rstrip('/'), transport
        self._agent = ''.join(c for c in (agent or '') if ' ' <= c <= '~')[:512]

    def _prepare(self, action, input, path, idempotency_key):
        op, data = OPERATIONS[action], dict(input or {})
        if op['public'] != self._public:
            raise ValueError('Use the matching public or authenticated client.')
        if self._key and op['scope'] == 'operations:management':
            raise AbuseZeroError('OAUTH_REQUIRED', 'This action needs an OAuth sign-in.', 403)
        if op['mutation'] and not idempotency_key or idempotency_key is not None and not re.fullmatch(r'[\x21-\x7e]{1,128}', idempotency_key):
            raise AbuseZeroError('INVALID_IDEMPOTENCY_KEY', 'Provide an idempotency key: 1–128 printable characters with no spaces.', 422)
        route, path = op['path'], path or {}
        if set(path) != {p['name'] for p in op['paths']}:
            raise ValueError('Pass exactly the path fields this method needs in path.')
        for p in op['paths']:
            value = path[p['name']]
            try:
                _validate(value, p['schema'])
            except (ValueError, TypeError):
                raise ValueError(f"The path field {p['name']} isn't valid.") from None
            route = route.replace('{' + p['name'] + '}', quote(str(value), safe='/' if p['name']=='path' else ''))
        if action.startswith('evaluations.') and 'context' in data and isinstance(data['context'], dict) and isinstance(data['context'].get('user_agent'), str):
            data['context'] = {**data['context'], 'user_agent': data['context']['user_agent'][:512]}
        if 'request' in data and isinstance(data['request'], dict):
            data['request'] = incoming_request(**data['request'])
        try:
            _validate(data, op['input'])
        except (ValueError, TypeError, KeyError):
            raise AbuseZeroError('INVALID_REQUEST', 'Check the request against the API schema.', 422) from None
        headers = {'Accept': 'application/json'}
        if not self._public:
            headers['Authorization'] = 'Bearer ' + self._credential
            if self._workspace: headers['AbuseZero-Workspace'] = self._workspace
            if self._agent: headers['AbuseZero-Agent'] = self._agent
        if idempotency_key: headers['Idempotency-Key'] = idempotency_key
        body = None
        if op['method'] == 'GET':
            query = [(k, json.dumps(v, separators=(',', ':')) if isinstance(v, (dict, list, bool)) or v is None else str(v)) for k,v in data.items()]
            if query: route += '?' + urlencode(query)
        else:
            body = json.dumps(data, ensure_ascii=False, allow_nan=False, separators=(',', ':')).encode()
            headers['Content-Type'] = 'application/json'
            if action=='evaluations.create' and len(body)>49152:
                raise AbuseZeroError('INVALID_REQUEST', 'The evaluation request is too large.', 422)
        budget = op['timeout_ms'] / 1000
        if action=='events.list': budget=max(budget, float(data.get('wait', 0))+5)
        return op, self._base + route, headers, body, budget

    def _response(self, op, response):
        try: data = response.json()
        except (ValueError, UnicodeError): data = None
        if 200 <= response.status_code < 300:
            if not isinstance(data, dict):
                raise AbuseZeroError('INVALID_RESPONSE', 'AbuseZero returned an unreadable response.', 502, retryable=True)
            if op['id'] in ('evaluations.create','evaluations.dry_run'):
                if data.get('status')=='skipped' and isinstance(data.get('reason'), str) and re.fullmatch(r'[a-z][a-z0-9_]{0,63}',data['reason']):
                    return {**data, **({'source':'abusezero'} if op['id']=='evaluations.create' else {})}
                risk=data.get('risk', {})
                if data.get('result') not in ('allow','deny') or not isinstance(risk,dict) or not isinstance(risk.get('band'),str) or risk.get('score') is not None and (not isinstance(risk['score'],(int,float)) or isinstance(risk['score'],bool) or not 0<=risk['score']<=100):
                    raise AbuseZeroError('INVALID_RESPONSE', 'AbuseZero returned an unreadable evaluation.', 502, retryable=True)
                if op['id']=='evaluations.create':
                    if data.get('object')!='evaluation' or not isinstance(data.get('id'),str) or not re.fullmatch(r'[1-9][0-9]{19}',data['id']):
                        raise AbuseZeroError('INVALID_RESPONSE','AbuseZero returned an unreadable evaluation.',502,retryable=True)
                    if data.get('outcome') is not None and not isinstance(data['outcome'],dict):
                        raise AbuseZeroError('INVALID_RESPONSE','AbuseZero returned an unreadable outcome.',502,retryable=True)
                    state = (data.get('outcome') or {}).get('state', response.headers.get('AbuseZero-Outcome-State'))
                    if state is not None and (not isinstance(state,str) or not re.fullmatch(r'[a-z][a-z0-9_]{0,63}',state)):
                        raise AbuseZeroError('INVALID_RESPONSE','AbuseZero returned an unreadable outcome state.',502,retryable=True)
                    data['outcome'] = {'state':state,'due_at':(data.get('outcome') or {}).get('due_at',response.headers.get('AbuseZero-Outcome-Due-At'))} if state else None
                    data['source']='abusezero'
                elif data.get('object') != 'evaluation_dry_run' or data.get('dry_run') is not True:
                    raise AbuseZeroError('INVALID_RESPONSE','AbuseZero returned an unreadable evaluation.',502,retryable=True)
            try:
                _validate(data, op['response'], response=True)
            except (ValueError, TypeError, KeyError):
                raise AbuseZeroError('INVALID_RESPONSE','AbuseZero returned an unreadable response.',502,retryable=True) from None
            return data
        detail = data.get('error', {}) if isinstance(data,dict) else {}
        if not isinstance(detail,dict): detail={}
        raise AbuseZeroError(detail.get('code','HTTP_ERROR'), detail.get('message',"AbuseZero couldn't finish the request."),response.status_code,response.headers.get('X-Request-ID'),response.status_code not in (401,403) and not 300<=response.status_code<400 and (response.status_code in (429,502,503,504) or detail.get('retryable') is True),detail.get('docs_url'))

    def _fallback(self, action, input, error):
        if action=='evaluations.create' and self._outage!='throw' and error.retryable and error.status!=429:
            return {'source':'local_outage','claim_id':input['claim_id'],'result':self._outage,'error':error}
        raise error from None


def _retry_delay(response, attempt):
    delay = (0.1,0.25)[attempt]
    if response is not None:
        value=response.headers.get('Retry-After','0')
        try: delay=max(delay,float(value))
        except ValueError:
            try: delay=max(delay,parsedate_to_datetime(value).timestamp()-time.time())
            except (ValueError,TypeError,OverflowError): pass
    return delay


class _AsyncTransportAdapter(httpx.AsyncBaseTransport):
    def __init__(self, transport): self.transport = transport
    async def handle_async_request(self, request):
        def send():
            response = self.transport.handle_request(request)
            try:
                return httpx.Response(response.status_code, headers=response.headers, content=response.read(), extensions=response.extensions)
            finally:
                response.close()
        return await asyncio.to_thread(send)
    async def aclose(self): await asyncio.to_thread(self.transport.close)


class Core(Base):
    """Synchronous interface with a pooled async transport and a cancellable total deadline."""
    def __init__(self, **options):
        transport = options.get('transport')
        if transport is not None and not isinstance(transport, httpx.AsyncBaseTransport):
            options = {**options, 'transport': _AsyncTransportAdapter(transport)}
        self._client = AsyncCore(**options) if not self._public else _AsyncPublicCore(**options)
        self._loop = asyncio.new_event_loop()
        self._thread = threading.Thread(target=self._loop.run_forever, daemon=True)
        self._thread.start()
        self._closed = False

    def close(self):
        if self._closed: return
        self._closed = True
        try:
            asyncio.run_coroutine_threadsafe(self._client.close(), self._loop).result()
            asyncio.run_coroutine_threadsafe(self._loop.shutdown_asyncgens(), self._loop).result()
        finally:
            self._loop.call_soon_threadsafe(self._loop.stop)
            self._thread.join()
            self._loop.close()

    def __enter__(self): return self
    def __exit__(self,*args): self.close()
    def _call(self, action, input, path, idempotency_key):
        if self._closed: raise RuntimeError('The client is closed.')
        return asyncio.run_coroutine_threadsafe(self._client._call(action,input,path,idempotency_key), self._loop).result()


class AsyncCore(Base):
    def __init__(self, **options):
        super().__init__(**options)
        self._http=httpx.AsyncClient(transport=self._transport,follow_redirects=False,timeout=None)
    async def close(self): await self._http.aclose()
    async def __aenter__(self): return self
    async def __aexit__(self,*args): await self.close()
    async def _call(self,action,input,path,idempotency_key):
        op,url,headers,body,budget=self._prepare(action,input,path,idempotency_key)
        deadline=time.monotonic()+budget
        error=None
        rate_error=None
        for attempt in range(3):
            response=None
            remaining=deadline-time.monotonic()
            if remaining<=0:
                error=AbuseZeroError('DEADLINE_EXCEEDED','The AbuseZero request budget expired. Try again with the same input and idempotency key.',retryable=True); break
            try:
                async with asyncio.timeout(remaining):
                    response=await self._http.request(op['method'],url,headers=headers,content=body,timeout=remaining)
                    return self._response(op,response)
            except AbuseZeroError as exc:
                error=exc
                if exc.status==429: rate_error=exc
            except (TimeoutError,httpx.TimeoutException): error=AbuseZeroError('DEADLINE_EXCEEDED','The AbuseZero request budget expired. Try again with the same input and idempotency key.',retryable=True)
            except httpx.HTTPError: error=AbuseZeroError('TRANSPORT_ERROR',"AbuseZero couldn't be reached, or its response couldn't be read. Try again with the same input and idempotency key.",retryable=True)
            if not error.retryable or attempt==2: break
            delay=_retry_delay(response,attempt)
            if time.monotonic()+delay>=deadline: break
            await asyncio.sleep(delay)
        return self._fallback(action,input,rate_error or error)


class _AsyncPublicCore(AsyncCore):
    _public = True
