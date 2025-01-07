# operators in python
# types of operator
# arthmetic oper +,-,/,*,%
# logical &&,||,!
# relational >,<,==,>=,<=,!=
# assignment =
# compound assigmnet   +=,-=,*=
# inc/dec  i = 1 i++  i--


# how to take run time value in python
name = input('Enter you name')
print("Name : "+name)
no1 = int(input("Enter first number"))
no2 =  int(input("Enter second number"))
add = no1 + no2
print("Addition = ",add)
print("Addition = ",add)
player1 = input(" player1,write your choice,(rock,paper,scissor)")
player2 = input(" player2,write your choice,(rock,paper,scissor)")
if player1 == player2 :
    print("it's a tie!")
elif (player1 == "rock" and player2 == "paper") or  (player1 == "paper" and player2 == "scissor")  or (player1 == "scissor" and player2 == "rock") :
    print("winner is  user 2")
elif (player1 == "paper" and player2 == "rock")  or (player1 == "scissor" and player2 == "paper")  or (player1 == "rock" and player2 == "scissor") :
    print("winner is  user1 ")

    
