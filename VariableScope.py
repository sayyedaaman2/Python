# varible scope = where a varibale is visible and accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in

#   ^ built-in
#   | global
#   | enclosed
#   ^ local  




# local

# def func1():
#     x = 1
#     print(x)
# def func2():
#     x = 2
#     print(x)

# func1()
# func2()

# Enclosed

# def func1():
#     x = 1
#     def func2():
#         # x = 2
#         print(x)
#     func2()

# func1()

# Global


# def func1():
#     print(x)
# def func2():
#     print(x)

# x=3  # Global variable

# func1()
# func2()

# Built-in

from math import e #Built-in variable
def func1():
    print(e)

e=3
func1()