categories = ["Watches", "Mobile"]
options = [
    ["smartwatch", "brand watch"],
    ["Iphone", "Samsung"]
]

print("Choose a category:")
index = 1
for category in categories:
    print(f"{index}. {category}")
    index += 1

choice = input("Enter your choice: ")

index = 0
for category in categories:
    if category.lower() in choice.lower():
        print(f"Options in {category}:")
        for option in options[index]:
            print(f"- {option}")
        break
    index += 1
else:
    print("Invalid category selected!")