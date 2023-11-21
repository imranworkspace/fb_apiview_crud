import requests
import json

URL='http://127.0.0.1:8000/student/'
headers = {'content-Type':'application/json'}

def get_api(id=None):
    data={

    }
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data) 
   
    r=requests.get(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

def post_api():
    data={
        "name":"muskan",
        "email":"m@gmail.com"
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

def put_api():
    data={
        "id":"3",
        "name":"afreen",
        "email":"af@gmail.com"
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

def delete_api(id):
    print('id',id)
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data) 
        print('data',json_data)
        r=requests.delete(url=URL,headers=headers,data=json_data)
        data = r.json()
        print(data)

# get_api(2)
# post_api()
# put_api()
delete_api(3)