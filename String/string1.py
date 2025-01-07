txt = "helo ali"
print(txt.upper())

txt = "HELLO ALI"
print(txt.lower())

text = "hello ali"
print(text.capitalize())

text = "  hello ali   "
print(text)
print(text.strip())


email = "abc$gmail.com"
print(email.replace("$","@"))


# text = input("Enter your string")
# oldStr = input("Enter the string you want to replace")
# newStr = input("Enter the string you want to replace with")
# print(text.replace(oldStr,newStr))

menu = input("1. upper \n2. lower \n3. capitalize \n4. strip \n5. replace \n6. exit")
text = input("Enter your string")
match menu:
    case "1":
        print(text.upper())
    case "2":
        print(text.lower())
    case "3":
        print(text.capitalize())
        



        


