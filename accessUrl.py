from http.client import HTTPConnection
conn = HTTPConnection("institute.intouchpk.com")
conn.request("GET","/")
result = conn.getresponse()

content = result.read()
print(content)