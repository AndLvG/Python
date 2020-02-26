import requests

api_server = input() + ':' + input()
a = input()
b = input()

# print(api_server)

params = {"a": a, "b": b}
response = requests.get(api_server, params=params)

# print(response.url)

json_response = response.json()

check = json_response["check"]
result = json_response["result"]
print(" ".join(map(str, sorted(result))))
print(check)
