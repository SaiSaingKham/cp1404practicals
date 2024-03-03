#1

user_name = input("Please enter your name: ")

with open("name.txt", "w") as file:
    file.write(user_name)

print("Your name has been written to the file.")

#2
with open("name.txt", "r") as file:
    name = file.read().strip()

print(f"Your name is {name}")

#3
with open("numbers.txt", "r") as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())

result = num1 + num2
print("The sum of the first two numbers is:", result)

#4
with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

result = sum(numbers)
print("The sum of all the numbers is:", result)
