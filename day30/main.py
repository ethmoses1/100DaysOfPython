#Error and exceptions
try:
    file = open("a_file.txt")
except FileNotFoundError:
    print("File doesn't exist")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    
    
    
#Creating your own exceptions
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")
bmi = weight/height ** 2

