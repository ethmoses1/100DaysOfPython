#Nested Loop BMI CALCULATOR
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight/height**2)

if BMI < 18.5:
    print("You're underweight")
elif BMI >= 18.5 and  BMI < 25:
    print("You're normal weight")
elif BMI >= 25 and BMI < 30:
    print("You're overweight")
elif BMI >= 30 and BMI < 35:
    print("You're obese")
else:
    print("You're clinically obese")





