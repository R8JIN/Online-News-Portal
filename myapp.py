import requests
import json

URL ='http://127.0.0.1:8000/categ/'
def get_category(id=None):
    data = {}
    # URL ='http://127.0.0.1:8000/hello_world/'
    headers = {'content-Type': 'application/json'}
    if id is not None:
        data ={'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,headers=headers, data =json_data)
    data = r.json()
    print(data)

def create_category():
    # URL = 'http://127.0.0.1:8000/cat_api/'
    data = {'title': 'Travel',
            'caption': 'Upcoming Movies, Ongoing Movies, and Review '}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

def delete_category():
    # URL = 'http://127.0.0.1:8000/cat_api/'
    data = {'id': 11}
    headers = { 'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

def update_category():
    # URL = 'http://127.0.0.1:8000/cat_api/'
    data = {'id': 1, 'title': 'Business'}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)    # print(r.json())

# create_category()
# update_category()
# get_category()
delete_category()