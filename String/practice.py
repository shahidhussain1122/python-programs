string = "That the quick brown fox jumps over the lazy dog"
while True:
    methods = input("Enter the method you want to use: ")
    match methods:
        case "upper":
            print(string.upper())
        case "lower":
            print(string.lower())
        case "capitalize":
            print(string.capitalize())
        case "title":
            print(string.title())
        case "swapcase":
            print(string.swapcase())
        case "casefold":
            print(string.casefold())
    continue_status = input("Do you want to continue? (y/n): ")
    if continue_status.lower() != 'y':
        break