while True:
    height = input("Enter height in centimeters")
    weight = input("Enter weight in kilograms")
    # check if height and weight can be converted to float
    try:
        height = float(height)
        weight = float(weight)
    except ValueError:
        print("Invalid input.")
        # continue to ask for input
        continue
    if height <=0 or weight <=0:
        print("Negative numbers are not allowed\n")
        # continue to ask for input
        continue
    else:
        break

# convert height to meters
height = height / 100
# calculate bmi
bmi = weight / (height ** 2)
# print bmi and category
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f} and you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f} and you are normal.")
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f} and you are overweight.")
else:
    print(f"Your BMI is {bmi:.2f} and you are obese.")
