

# One dimentional List
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "patotoes"]
meats = ["chicken", "fish", "turkey"]

#  Two dimentional List
groceries = [fruits, vegetables, meats]

# print(groceries)
# print(groceries[0][0])
# print(groceries[0][3])
# print(groceries[1][0])
# print(groceries[2][2])

# for collection in groceries:
#     # print(collection)
#     for item in collection:
#         print(item, end=" ")


# Exercise 1 : Make a Phone dialer

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))


for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()