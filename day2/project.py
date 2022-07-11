print("Welcome to the tip calculator!")
total = int(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
total_plus_tip = ((total*tip)/100)+total
each_person = total_plus_tip/people
print(f"Each person should pay: ${each_person}")

