# Instructions
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

# You are going to create a list called result which contains the numbers that are common in both files.

# e.g. if file1.txt contained:

# 1
# 2
# 3
# and file2.txt contained:

# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.

# Example Output
# [3, 6, 5, 33, 12, 7, 42, 13]


list1 = []
with open("file1.txt") as file1:
    list = file1.read().splitlines() 
    list1 = list

list2 = []
with open("file2.txt") as file2:
    list = file2.read().splitlines() 
    list2 = list

result = [int(num) for num in list1 if num in list2]
# Write your code above 👆
# print(list1)
    
print(result)

