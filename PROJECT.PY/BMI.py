#creating a BMI caclulator

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))

BMI =weight / height ** 2
if BMI < 18.5:
    print("under weight")
elif BMI < 25:
    print(BMI)
    print("healthy weight")
else:
  print("over weight/obese")






