# input() = A function that prompts the user to enter data 
#           Returns the entered data as a string


# name = input("What is your name? : ")
# age = int(input("how old are you?: "))

# print(f"Hello {name}")
# print("HAPPY BIRTHDAY!")
# print(f"You are {age + 1} years old")


# Exercise 1 rectangle Area Calc

# length = float(input("Enter the length : "))
# width = float(input("Enter the width : "))
# area = width * length

# print(f"Area of Rectangle is : {area}cm²")

# Exercise 2 Shopping Cart Program
 
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is : ${total}")