import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

print(response.status_code)

parameters = {"lat": 40.71, "lon": -74}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

print(response.content)

response.content.decode("utf-8")

print("**********************************************\n")

parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

data = response.json()
print(type(data))
print(data)

print(response.headers)
print(response.headers["content-type"])