list = ["apple","mango","orange"]
if "apple" in list:
    print("Yes, apple is in the list")
else:
    print("not found")
    
    
list[0] = "banana"
print(list)

list[0:1] = ["apple","ball"]
print(list)

list.insert(1,"taxi")
print(list)

list.append("ali")
print(list)

list1 = [1,2]
list2 = [3,4]
list1.extend(list2)
print(list1)

list.remove("apple")
print(list)

list.pop()
print(list)

del list[3]
print(list)

list.clear()
print(list)

