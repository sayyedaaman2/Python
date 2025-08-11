# function = A block of resuable code
#            place () after the function name to invoke it

#  1. positional,
def happy_birthday():
    print("Happy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

# happy_birthday()


def happy_birthday_with_name(name):
    print(f"Happy birthday to {name}")
    print("You are old!")
    print(f"Happy birthday to {name}")
    print()

# happy_birthday_with_name("Bro")

def happy_birthday_with_name_age(name,age):
    print(f"Happy birthday to you! {name}")
    print(f"You are {age} years old!")
    print(f"Happy birthday to you! ")
    print()

# happy_birthday_with_name_age("Bro",25)
# happy_birthday_with_name_age("Steve",40)
# happy_birthday_with_name_age("Joe",35)

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due : {due_date}")

# display_invoice("BroCode",42.50,"01/01/25")
# display_invoice("JoeSchmo",102.50,"04/06/25")


# return = statement used to end a function
#          and send a result back to the caller

def add(x,y):
    z = x + y
    return z


def subtract(x,y):
    z = x - y
    return z


def multiply(x,y):
    z = x * y
    return z


def divide(x,y):
    z = x / y
    return z


# print(add(4,6))
# print(subtract(10,5))
# print(multiply(2,5))
# print(divide(10,2))

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

# full_name = create_name("spongebob","squarepants")
# print(full_name)




# default arguments = A default value for certain parameters
#                     default is used when that arguement is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2.DEFAULT, 3. keyword, 4. arbitrary


# 2.DEFAULT,
def net_price(list_price,discount=0,tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


# print(net_price(500,0,0.05))
# print(net_price(500))
# print(net_price(500,0.1))
# print(net_price(500,0.1,0))


import time

def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE !")


# count(30,15)

# 3. keyword,
# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter 
#                     1. positional, 2.DEFAULT, 3. keyword, 4. arbitrary

def hello(greeting,title,first,last):
    print(f"{greeting} {title}{first} {last}")

# hello("Hello", "Mr.", "Spongebob", "Squarepants")
# hello("Hello",first="Spongebob",title="Mr.", last="Squarepants")
# hello(first="Spongebob",title="Mr.", last="Squarepants",greeting="Hello")

# hello("Hello",title="Mr. ", last="James", first="Jon")


# for x in range(1,11):
    # print(x,end=" ") # keyword

# print("1","2","3","4","5", sep="-")

def get_phone(country, area,first,last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(country=1,area=123, first=456, last=789)

# print(phone_num)




# 4. arbitrary

# *args             = allows you to pass multiple non-key arguments
# **kwargs          = allows you to pass multiple keyword-arguments
#                   * unpacking operator
#                     1. positional, 2.DEFAULT, 3. keyword, 4. arbitrary

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1,2,3,4,5))


# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
    
# display_name("Dr.","Spongebob","Harlod", "Squarepants", "III")


# def print_address(**kwargs):
#     # print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print_address(street="123 Fake St." ,
#               apt="100", 
#               city="Detroit", 
#               state="MI", 
#               zip="54321",)




def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')},{kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")

        
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")



# shipping_label("Dr.","Spongebob", "Squarepants", "III",
#                street="123 Fake St.",
#                apt="100",
#                city="Detroit",
#                state="MI",
#                zip="54321")
# shipping_label("Dr.","Spongebob", "Squarepants", "III",
#                street="123 Fake St.",
#                city="Detroit",
#                state="MI",
#                zip="54321")

shipping_label("Dr.","Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")