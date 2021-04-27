import requests, json

number = json.loads(requests.get("https://reqres.in/api/users/2").text)
name = number["data"]["first_name"]#"data" - это имя родительского элемента в json  файле
print(name)


a = requests.get("https://reqres.in/api/users/2")
print(a.status_code)

assert name == "Janet"
assert a.status_code == 200


