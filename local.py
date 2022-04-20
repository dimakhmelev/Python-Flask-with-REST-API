import requests


#res = requests.get("http://127.0.0.1:3000/api/courses/1")  #post,put,delete
#print(res.json())


#res = requests.delete("http://127.0.0.1:3000/api/courses/1")  
#print(res.json())

#res = requests.post("http://127.0.0.1:3000/api/courses/3", {"name": "Goland", "videos": 5})  
#res = requests.post("http://127.0.0.1:3000/api/courses/4", {"name": "PHP", "videos": 15})  
#print(res.json())

res = requests.put("http://127.0.0.1:3000/api/courses/2", {"name": "Golang", "videos": 5})
print(res.json())