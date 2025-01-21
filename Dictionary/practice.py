subjects = {
    "sub1": "Maths",
    "sub2 ": "Science",
    "sub3": "English",
    "sub4": "Social Science",
}
print(subjects)

print(subjects["sub1"])

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

print(thisdict.get("name"))

x = thisdict.keys()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x)

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)

for item in thisdict:
    print(item," : ",thisdict[item])