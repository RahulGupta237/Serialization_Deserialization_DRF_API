import requests,json

URL='http://127.0.0.1:8000/stuget/'

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
        'id':3,
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


#get_data(2)  # Read
delete_data() # Update
#update_data() # Delete





