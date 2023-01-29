import requests

from getpass import getpass

endpoint = "http://127.0.0.1:8000/api/auth/"

username = input("please enter your username: ")
password = getpass("password: ")

auth_resp = requests.post(endpoint, json={"username":username,"password": password})

if auth_resp.status_code ==200:
    token = auth_resp.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/parties/"

    get_resp = requests.get(endpoint, headers=headers)

    print("parties_list:",(get_resp.json()).get('results'))

    voted =int(input("please enter the id of party you would like to vote from the list shown above: "))

    data = {
    "voted":voted,
    
    }
    endpoint = "http://127.0.0.1:8000/"

    post_resp = requests.post(endpoint, json=data, headers=headers)

    print(post_resp.json())



