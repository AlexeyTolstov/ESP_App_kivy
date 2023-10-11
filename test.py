from requests import get

req = get("http://192.168.4.1/").json()
print(req)