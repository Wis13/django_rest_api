import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={'abc': "123"}, json={"query": "Hello World"})  # Http Requests
print(get_response.text)  # print raw text response
print(get_response.status_code)
print("______________________________________________________")
print(get_response.json())
print("______________________________________________________")
