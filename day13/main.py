#Debugging: How to find and Fix Errors

# 1 Describe the problem
"""def my_function():
    for i in range(1, 20):
        if i ==20:
            print("You got it")
my_function()
"""
# # In the above code the the function is making a loop from 1 to
# # 20 and when it reaches 20 it prints out something. However this function is not printing anything out.
   # To fix the issue chane the range function to start at 1 and end at 21 since range function is not inclusive of the last number
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# 2 Reproduce  the problem

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) //change to range(1,5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994: //change to year >= 1994
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.") //add f string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))  //change to = instead of =
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger // use tool like  python tutor
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) //the indentation is not right
#   print(b_list)

# mutate([1,2,3,5,8,13])