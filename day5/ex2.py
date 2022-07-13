# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
#
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
#
# Hint
# There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.
sum = 0;
for num in range(0, 101, 2):
    sum += num
print(sum)

#solution 2
sum2 = 0;
for num in range(1, 101):
    if(num % 2 == 0):
       sum2 += num

print(sum2)

#solution 3
total = 0;
for num in range(2, 101, 2):
    if(num % 2 == 0):
       total += num

print(total)