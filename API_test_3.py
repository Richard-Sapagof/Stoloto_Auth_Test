import requests, json



def test_requests_put_api_update_user():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    req = requests.put("https://reqres.in/api/users/2",data)
    print(req.status_code)

    assert req.status_code == 200

def test_requests_post_api_create_user():

    data = {
        "name": "morpheus",
        "job": "leader"
    }
    req = requests.post("https://reqres.in/api/users", data)
    print(req.status_code)

    assert req.status_code == 201


def test_requests_get_api_single_user():

    number = json.loads(requests.get("https://reqres.in/api/users/2").text)
    name = number["data"]["first_name"]  # "data" - это имя родительского элемента в json  файле
    print(name)

    a = requests.get("https://reqres.in/api/users/2")
    print(a.status_code)

    assert name == "Janet"
    assert a.status_code == 200