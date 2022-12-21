import requests,json

URL='http://127.0.0.1:8000/stumodel/'

def create_data():
    data={
    'name':'Saranya Pathak',
    'city':'Pathkahuli',
    'roll':237,
}

    json_data=json.dumps(data)
    print(json_data)

    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)



def update_data():
    
    data={
        'id':1,
        'name':'Tara',
        'city':'Kodad',
        'roll':237,
        
    }

    json_data=json.dumps(data)
    print(json_data)

    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)


def delete_data():
    
    data={
        'id':4,
       
        
    }

    json_data=json.dumps(data)
    print(json_data)

    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

create_data()
#get_data()  # Read
#delete_data() # Update
#update_data() # Delete





