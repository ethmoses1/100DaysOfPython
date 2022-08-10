#Day 24 Open, Read, Write to Files using the "with" keyword

file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()


#Open file with with keyword

with open("my_file.txt", mode='a') as file:
    file.write("\nI'm 10 years old")