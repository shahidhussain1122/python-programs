fruits = ("apple","banana","mango")
l = list(fruits)
print(type(fruits))
print(type(l))

l[0] = "graps"
l.append("apple")
fruits = tuple(l)
print(fruits)


firstName = ("ali")
lastName = ("khan")
fullName = firstName +" "+  lastName
print(fullName)


subjects = ("Computer","Maths","English","Urdu")
(Computer,Maths,English,Urdu) = subjects
print(Computer)
print(Maths)
print(English)
print(Urdu)