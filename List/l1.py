fuirts = ["apple",'mango','banana','watermelon','apple','banana']
print(fuirts[0])
print(fuirts)

mylist = [1,2,'ali',"python",True]
print(mylist)

print(len(mylist))

numbers = [1,2,3,4,5]
string  = ['ali','wali']
decimal = [1.2,3.2,45.0]
boolean = [True,False]
print(type(numbers))
print(type(string))
print(type(decimal))
print(type(boolean))


students = ["Ali","Shahid","Muzamil","Aslam"]
students[3] = "Akaram"
print(students)


marks = [66,99,87,67,56]
submition = 0
avg  = 0
for m in marks:
    submition+=m
    avg =  submition/len(marks)
    
print("Sum ",submition)
print("Average = ",avg)