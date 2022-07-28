

#modifying Global Scope
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function ${enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")

#global constants
PI = 3.14159