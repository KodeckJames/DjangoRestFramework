import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/"


get_response = requests.get(endpoint, json={"query":"Hello world"}) #HTTP Request
print(get_response.text) #Prints raw text code
# A regular HTTP Request gives you HTML
# A REST API HTTP Request gives JSON
# JSON => JavaScript Object Notation