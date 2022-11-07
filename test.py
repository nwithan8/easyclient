from easyclient import RestApiClient, ApiAuthNone

client = RestApiClient(auth=ApiAuthNone(), base_url="https://api.github.com")

data = client.get(endpoint="/repos/tautulli/tautulli/issues/1")

print(data)

dictionary = client.get_object(endpoint="/repos/tautulli/tautulli/issues/1", model=str)

print(dictionary)
