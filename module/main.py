# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files


# print(help("modules"))
# print(help("math"))

# import math 
# print(math.pi)

# import math as m # using alies
# print(m.pi)

# from math import pi
# print(pi)

# -----------------------------------------------------------------------
import example

pi = example.pi
square = example.square(3)
cube = example.cube(3)
circumference = example.circumference(3)
area = example.area(3)
print(pi,square,cube,circumference,area, sep=', ')