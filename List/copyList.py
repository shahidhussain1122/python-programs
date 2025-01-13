# Python - Copy Lists
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Python - Join Lists


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

marks = [1,2,3]
students = ['ali','akram','saleh']
obtainMarks = marks.copy()
finalList = students + marks
print(finalList)
print(obtainMarks)
