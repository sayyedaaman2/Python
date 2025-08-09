# name = input("Enter your full name: ")

# result = len(name)
# result = name.find("A")
# result = name.rfind("q")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()

# phone_number = input("Enter your phone #: ")

# result = phone_number.count("-")
# result = phone_number.replace("-"," ")


# print(result)

# print(help(str))

# Exercise 1
# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username : ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")