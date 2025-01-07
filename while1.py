while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    if user_input.isdigit():
        number = int(user_input)
        print(f"You entered: {number}")
    else:
        print("Invalid input! Please enter a valid number.")
