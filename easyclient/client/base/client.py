from objectrest import (
    RequestHandler,
)


class ApiClient:
    def __init__(self, request_handler: RequestHandler):
        self._request_handler = request_handler
