import requests
import json

#enter credentials
username = "admin"
password = "9odPOM90quGZZjmdtKXC2w"
artifactory = "https://esiesel.jfrog.io/artifactory" #artifactory URL
api = "/api/security/users/admin" #you can change this API URL to any API method you'd like to use

url = artifactory + api
r = requests.get(url, auth = (username, password)) #this script is only for API methods that use GET

print('status code = {}'.format(r.status_code))
if r.status_code == 200:
  print(r.text)
  #print (r.text.split(',')[0][1:]) response for /api/system/version
else:
  print ("Fail")
  response = json.loads(r.content)
  print (response["errors"])
  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + r.status_code)

#put
api = "/api/security/users/kuku"
url = artifactory + api
params = {}
params["name"] = "kuku"
params["admin"] = "false"
params["email"] = "kuku@kuku.com"
params["password"] = "kukupassword"
params["Content-Type"] = "application/json"
r = requests.put(url, auth = (username, password),json=params) #this script is only for API methods that use GET
print('PUT status code = {} text = {}'.format(r.status_code,r.text))


#delete
api = "/api/security/users/kuku"
url = artifactory + api

r = requests.delete(url, auth = (username, password)) #this script is only for API methods that use GET
print('delete status code = {} text ={}'.format(r.status_code,r.text))

