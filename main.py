height = (input("Please enter your height (in): "))
while not(height.isnumeric()):
    print("wrong input! please enter an integer")
    height = (input("Please enter your height (in): "))
else:
    weight = (input("Please enter your weight (lb): "))
    while not(weight.isnumeric()):
        print("wrong input! please enter an integer")
        weight = (input("Please enter your weight (lb): "))

weight = float(weight)
height = float(height)

bmi = round(703* weight/height**2,1)
print(f"your BMI is: {bmi}")

if bmi<18.5:
    print("under weight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("over weight")
elif bmi<35:
    print("obese weight")
else:
    print("clinically obese")

