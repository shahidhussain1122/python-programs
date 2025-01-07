num = int(input("Enter a number :"))
if num <= 0 :
    print("Negative number have not factorial :")
    print("Write a positive number :")
    num = int(input("Enter a positive number :"))
factorial = 1
i = 1
while i <= num :
    factorial = factorial * i
    i = i + 1
print(" factorial of  ",num,"=",factorial)