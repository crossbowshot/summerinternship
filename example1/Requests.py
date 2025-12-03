import requests

response = requests.get("https://httpbin.org/get")

res_json =  response.json()
print(res_json)

# User Agent
response2 = requests.get("https://httpbin.org/user-agent")
print(response2.text)

# Image 
response3 = requests.get("https://httpbin.org/image",
                        )

with open("myimage.png","wb")

