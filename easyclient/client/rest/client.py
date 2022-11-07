from typing import List

from objectrest import (
    Response,
    AsyncResponse
)

from easyclient.client.base import (
    ApiClient,
    ApiAuth,
)


def _process_blind(response: Response) -> bool:
    if not response:  # utilize the truthiness of request.Response
        return False
    return True


def _async_process_blind(response: AsyncResponse) -> bool:
    return not response.is_error


class RestApiClient(ApiClient):
    def __init__(self, base_url: str, auth: ApiAuth, log_requests: bool = False):
        super().__init__(auth._construct_handler(base_url=base_url, log_requests=log_requests))

    def get(self, endpoint: str, params: dict = None) -> dict:
        """
        Make a GET request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: JSON data from the API response
        :rtype: dict
        """
        return self._request_handler.get_json(url=endpoint, params=params)

    def get_text(self, endpoint: str, params: dict = None) -> str:
        """
        Make a GET request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: Text from the API response
        :rtype: str
        """
        res: Response = self._request_handler.get(url=endpoint, params=params)
        return res.text

    def get_object(self,
                   endpoint: str,
                   model: type,
                   params: dict = None,
                   sub_keys: List = None,
                   extract_list: bool = False) -> object:
        """
        Make a GET request to the API
        Return an object of the specified type

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool, optional
        :return: Object from the API response
        :rtype: object
        """
        return self._request_handler.get_object(url=endpoint, model=model, params=params, sub_keys=sub_keys,
                                                extract_list=extract_list)

    def post(self, endpoint: str, params: dict = None) -> dict:
        """
        Make a POST request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: JSON data from the API response
        :rtype: dict
        """
        return self._request_handler.post_json(url=endpoint, params=params)

    def post_blind(self, endpoint: str, params: dict = None) -> bool:
        """
        Make a POST request to the API
        Return a boolean indicating if the request was successful

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: True if the request was successful, False otherwise
        :rtype: bool
        """
        res = self._request_handler.post(url=endpoint, params=params)
        return _process_blind(res)

    def post_text(self, endpoint: str, params: dict = None) -> str:
        """
        Make a POST request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: Text from the API response
        :rtype: str
        """
        res: Response = self._request_handler.post(url=endpoint, params=params)
        return res.text

    def post_object(self,
                    endpoint: str,
                    model: type,
                    params: dict = None,
                    sub_keys: List = None,
                    extract_list: bool = False) -> object:
        """
        Make a POST request to the API
        Return an object of the specified type

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool, optional
        :return: Object from the API response
        :rtype: object
        """
        return self._request_handler.post_object(url=endpoint, model=model, params=params, sub_keys=sub_keys,
                                                 extract_list=extract_list)

    def put(self, endpoint: str, params: dict = None) -> dict:
        """
        Make a PUT request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: JSON data from the API response
        :rtype: dict
        """
        return self._request_handler.put_json(url=endpoint, params=params)

    def put_blind(self, endpoint: str, params: dict = None) -> bool:
        """
        Make a PUT request to the API
        Return a boolean indicating if the request was successful

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: True if the request was successful, False otherwise
        :rtype: bool
        """
        res = self._request_handler.put(url=endpoint, params=params)
        return _process_blind(res)

    def put_text(self, endpoint: str, params: dict = None) -> str:
        """
        Make a PUT request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: Text from the API response
        :rtype: str
        """
        res: Response = self._request_handler.put(url=endpoint, params=params)
        return res.text

    def put_object(self,
                   endpoint: str,
                   model: type,
                   params: dict = None,
                   sub_keys: List = None,
                   extract_list: bool = False) -> object:
        """
        Make a PUT request to the API
        Return an object of the specified type

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool, optional
        :return: Object from the API response
        :rtype: object
        """
        return self._request_handler.put_object(url=endpoint, model=model, params=params, sub_keys=sub_keys,
                                                extract_list=extract_list)

    def patch(self, endpoint: str, params: dict = None) -> dict:
        """
        Make a PATCH request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: JSON data from the API response
        :rtype: dict
        """
        return self._request_handler.patch_json(url=endpoint, params=params)

    def patch_blind(self, endpoint: str, params: dict = None) -> bool:
        """
        Make a PATCH request to the API
        Return a boolean indicating if the request was successful

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: True if the request was successful, False otherwise
        :rtype: bool
        """
        res = self._request_handler.patch(url=endpoint, params=params)
        return _process_blind(res)

    def patch_text(self, endpoint: str, params: dict = None) -> str:
        """
        Make a PATCH request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: Text from the API response
        :rtype: str
        """
        res: Response = self._request_handler.patch(url=endpoint, params=params)
        return res.text

    def patch_object(self,
                     endpoint: str,
                     model: type,
                     params: dict = None,
                     sub_keys: List = None,
                     extract_list: bool = False) -> object:
        """
        Make a PATCH request to the API
        Return an object of the specified type

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool, optional
        :return: Object from the API response
        :rtype: object
        """
        return self._request_handler.patch_object(url=endpoint, model=model, params=params, sub_keys=sub_keys,
                                                  extract_list=extract_list)

    def delete(self, endpoint: str, params: dict = None) -> dict:
        """
        Make a DELETE request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: JSON data from the API response
        :rtype: dict
        """
        return self._request_handler.delete_json(url=endpoint, params=params)

    def delete_blind(self, endpoint: str, params: dict = None) -> bool:
        """
        Make a DELETE request to the API
        Return a boolean indicating if the request was successful

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: True if the request was successful, False otherwise
        :rtype: bool
        """
        res = self._request_handler.delete(url=endpoint, params=params)
        return _process_blind(res)

    def delete_text(self, endpoint: str, params: dict = None) -> str:
        """
        Make a DELETE request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: Text from the API response
        :rtype: str
        """
        res: Response = self._request_handler.delete(url=endpoint, params=params)
        return res.text

    def delete_object(self,
                      endpoint: str,
                      model: type,
                      params: dict = None,
                      sub_keys: List = None,
                      extract_list: bool = False) -> object:
        """
        Make a DELETE request to the API
        Return an object of the specified type

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool, optional
        :return: Object from the API response
        :rtype: object
        """
        return self._request_handler.delete_object(url=endpoint, model=model, params=params, sub_keys=sub_keys,
                                                   extract_list=extract_list)


class AsyncRestApiClient(ApiClient):
    def __init__(self, base_url: str, auth: ApiAuth, log_requests: bool = False):
        super().__init__(auth._construct_handler(base_url=base_url, log_requests=log_requests))

    async def get(self, endpoint: str, params: dict = None) -> AsyncResponse:
        """
        Make a GET request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: JSON data from the API response
        :rtype: dict
        """
        return await self._request_handler.async_get(url=endpoint, params=params)

    async def get_object(self,
                         endpoint: str,
                         model: type,
                         params: dict = None,
                         sub_keys: List = None,
                         extract_list: bool = False) -> object:
        """
        Make a GET request to the API
        Return an object of the specified type

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool, optional
        :return: Object from the API response
        :rtype: object
        """
        return await self._request_handler.async_get_object(url=endpoint, model=model, params=params, sub_keys=sub_keys,
                                                            extract_list=extract_list)

    async def post(self, endpoint: str, params: dict = None) -> AsyncResponse:
        """
        Make a POST request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: JSON data from the API response
        :rtype: dict
        """
        return await self._request_handler.async_post(url=endpoint, params=params)

    async def post_blind(self, endpoint: str, params: dict = None) -> bool:
        """
        Make a POST request to the API
        Return a boolean indicating if the request was successful

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: True if the request was successful, False otherwise
        :rtype: bool
        """
        res = await self._request_handler.async_post(url=endpoint, params=params)
        return _async_process_blind(res)

    async def post_object(self,
                          endpoint: str,
                          model: type,
                          params: dict = None,
                          sub_keys: List = None,
                          extract_list: bool = False) -> object:
        """
        Make a POST request to the API
        Return an object of the specified type

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool, optional
        :return: Object from the API response
        :rtype: object
        """
        return await self._request_handler.async_post_object(url=endpoint, model=model, params=params,
                                                             sub_keys=sub_keys,
                                                             extract_list=extract_list)

    async def put(self, endpoint: str, params: dict = None) -> AsyncResponse:
        """
        Make a PUT request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: JSON data from the API response
        :rtype: dict
        """
        return await self._request_handler.async_put(url=endpoint, params=params)

    async def put_blind(self, endpoint: str, params: dict = None) -> bool:
        """
        Make a PUT request to the API
        Return a boolean indicating if the request was successful

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: True if the request was successful, False otherwise
        :rtype: bool
        """
        res = await self._request_handler.async_put(url=endpoint, params=params)
        return _async_process_blind(res)

    async def put_object(self,
                         endpoint: str,
                         model: type,
                         params: dict = None,
                         sub_keys: List = None,
                         extract_list: bool = False) -> object:
        """
        Make a PUT request to the API
        Return an object of the specified type

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool, optional
        :return: Object from the API response
        :rtype: object
        """
        return await self._request_handler.async_put_object(url=endpoint, model=model, params=params, sub_keys=sub_keys,
                                                            extract_list=extract_list)

    async def patch(self, endpoint: str, params: dict = None) -> AsyncResponse:
        """
        Make a PATCH request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: JSON data from the API response
        :rtype: dict
        """
        return await self._request_handler.async_patch(url=endpoint, params=params)

    async def patch_blind(self, endpoint: str, params: dict = None) -> bool:
        """
        Make a PATCH request to the API
        Return a boolean indicating if the request was successful

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: True if the request was successful, False otherwise
        :rtype: bool
        """
        res = await self._request_handler.async_patch(url=endpoint, params=params)
        return _async_process_blind(res)

    async def patch_object(self,
                           endpoint: str,
                           model: type,
                           params: dict = None,
                           sub_keys: List = None,
                           extract_list: bool = False) -> object:
        """
        Make a PATCH request to the API
        Return an object of the specified type

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool, optional
        :return: Object from the API response
        :rtype: object
        """
        return await self._request_handler.async_patch_object(url=endpoint, model=model, params=params,
                                                              sub_keys=sub_keys,
                                                              extract_list=extract_list)

    async def delete(self, endpoint: str, params: dict = None) -> AsyncResponse:
        """
        Make a DELETE request to the API

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: JSON data from the API response
        :rtype: dict
        """
        return await self._request_handler.async_delete(url=endpoint, params=params)

    async def delete_blind(self, endpoint: str, params: dict = None) -> bool:
        """
        Make a DELETE request to the API
        Return a boolean indicating if the request was successful

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :return: True if the request was successful, False otherwise
        :rtype: bool
        """
        res = await self._request_handler.async_delete(url=endpoint, params=params)
        return _async_process_blind(res)

    async def delete_object(self,
                            endpoint: str,
                            model: type,
                            params: dict = None,
                            sub_keys: List = None,
                            extract_list: bool = False) -> object:
        """
        Make a DELETE request to the API
        Return an object of the specified type

        :param endpoint: URL endpoint
        :type endpoint: str
        :param params: Dictionary of parameters to add to url
        :type params: dict, optional
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool, optional
        :return: Object from the API response
        :rtype: object
        """
        return await self._request_handler.async_delete_object(url=endpoint, model=model, params=params,
                                                               sub_keys=sub_keys,
                                                               extract_list=extract_list)
