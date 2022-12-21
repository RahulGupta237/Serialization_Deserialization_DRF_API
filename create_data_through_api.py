import requests,json

ur=' http://127.0.0.1:8000/stucreat/'
data={
    'name':'Abhk',
    'city':'Azamgarh',
    'roll':65,
}

json_data=json.dumps(data)
print(json_data)

r=requests.post(url=ur,data=json_data)
data=r.json()
print(data)