# Instructions
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
#
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.
#
# You've been to Moscow and Saint Petersburg.
#
# DO NOT modify the travel_log directly. You need to create a function that modifies it.
#
# Hint
# Look at the function call above to see what the name of the function should be.
#
# The inputs for the function are positional arguments. The order is very important.
#
# Feel free to choose your own parameter names.
#
# Test Your Code
# Before checking the solution, try copy-pasting your code into this repl:
#
# https://repl.it/@appbrewery/day-9-2-test-your-code
#
# This repl includes my testing code that will check if your code meets this assignment's objectives.


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, number_times, cities):
    visited_country = {
        "country": country,
        "visits": number_times,
        "cities": cities,
    }
    travel_log.append(visited_country)
    last_city = cities[-1]
    cities.pop()
    print(f"You've visited Russia {number_times} times.")
    print(f"You've been to {' '.join(cities)} and {last_city}.")
    cities.append(last_city)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



