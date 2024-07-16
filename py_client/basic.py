import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/"
endpoint = "http://localhost:8000/api/" #http://127.0.0.1:8000/


get_response = requests.get(endpoint, params={"abc":123}, json={"query":"Hello world"}) #HTTP Request
print(get_response.json()) 
# print(get_response.text) #Prints raw text code
# print(get_response.status_code) #Prints raw text code
# A regular HTTP Request gives you HTML
# A REST API HTTP Request gives JSON
# JSON => JavaScript Object Notation