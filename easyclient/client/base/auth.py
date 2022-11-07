from objectrest import (
    RequestHandler,
    ApiTokenRequestHandler,
    OAuth2RequestHandler
)


class ApiAuth:
    def __init__(self):
        pass

    def _construct_handler(self,
                           base_url: str,
                           universal_parameters: dict = None,
                           universal_headers: dict = None,
                           log_requests: bool = False) -> RequestHandler:
        pass


class ApiAuthNone(ApiAuth):
    def __init__(self):
        super().__init__()

    def _construct_handler(self,
                           base_url: str,
                           universal_parameters: dict = None,
                           universal_headers: dict = None,
                           log_requests: bool = False) -> RequestHandler:
        return RequestHandler(
            base_url=base_url,
            universal_parameters=universal_parameters,
            universal_headers=universal_headers,
            log_requests=log_requests)


class ApiAuthOAuth2(ApiAuth):
    def __init__(self,
                 client_id: str,
                 client_secret: str,
                 authorization_url: str):
        super().__init__()
        self._client_id: str = client_id
        self._client_secret: str = client_secret
        self._authorization_url: str = authorization_url

    def _construct_handler(self,
                           base_url: str,
                           universal_parameters: dict = None,
                           universal_headers: dict = None,
                           log_requests: bool = False) -> RequestHandler:
        return OAuth2RequestHandler(
            client_id=self._client_id,
            client_secret=self._client_secret,
            authorization_url=self._authorization_url,
            base_url=base_url,
            universal_parameters=universal_parameters,
            universal_headers=universal_headers,
            log_requests=log_requests)


class ApiAuthKey(ApiAuth):
    def __init__(self, key: str, key_keyword: str = 'key'):
        super().__init__()
        self._key: str = key
        self._key_keyword: str = key_keyword

    def _construct_handler(self,
                           base_url: str,
                           universal_parameters: dict = None,
                           universal_headers: dict = None,
                           log_requests: bool = False) -> RequestHandler:
        return ApiTokenRequestHandler(
            api_token=self._key,
            api_token_keyword=self._key_keyword,
            base_url=base_url,
            universal_parameters=universal_parameters,
            universal_headers=universal_headers,
            log_requests=log_requests)
