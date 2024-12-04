print("Hello again!")

# ---- operators: 
print(10 / 3)
print(10 // 3)

name = input("Enter your name:")

# covert: int() float() str()
age = int(input("Enter your age:"))

print(f"Hello dear {name}")
print(f"You are {age} years old!")

# ----- logic: > < >= <= != == and or not
if len(name) > 10:
    print("Too long name")
else: 
    print("Normal!")

if " " in name:
    print("Incorrect")

while input("Enter 'A': ") != 'A':
    print("Please enter letter A!")

numbers = [3, 5, 2, 5]

for i in numbers:
    print(i)

for i in range(4, 16, 2):
    print(i)

def checkPassword(value) -> bool:
    return len(value) >= 6 and "." in value

print(checkPassword("1234"))
print(checkPassword("Qwer.1234"))
