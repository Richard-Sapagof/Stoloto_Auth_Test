import requests, json

data = {
    "name": "morpheus",
    "job": "leader"
}
req = requests.post("https://reqres.in/api/users",data)
print(req.status_code)

assert req.status_code == 201