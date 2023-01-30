# Lists

# Lists == Arrays

# first list
shopping_list = ["milk", "eggs", "bread", "fruit", "cheese"]

# print(type(shopping_list)) # <class 'list'>
# print(shopping_list)

# print(shopping_list[0]) # milk
# print(shopping_list[3]) # fruit
# print(shopping_list[-1]) # cheese

# # rewriting a value in our list
# shopping_list[0] = "sugar"
# print(shopping_list[0]) # sugar
# print(shopping_list)

# List methods

# add to a list
shopping_list.append("vegetables")
# print(shopping_list)
# print(shopping_list[5])
# print(len(shopping_list))

# remove from a list

# shopping_list.remove("bread")
# print(len(shopping_list))
# print(shopping_list)

# remove last item of list without specifying

# shopping_list.pop()
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)

# Mixed data type lists

mixture = [1, 2, 3.5, "one", "two", "three" "four"]

print(mixture)

# List slicing

# print(mixture[1:3]) # 2, 3.5
# print(mixture[-2::]) # using a double colon reverses the order
# print(mixture[::2]) # bounces over the amount of indexs specified

# Tuples

# Exactly the same as lists, except they are immutable
# Tuples are useful for elements you want to ensure some data stays the same

essentials = ("bread", "eggs", "milk")

print(essentials)
print(essentials.count("bread"))

#


