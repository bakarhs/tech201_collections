starter_menu = ["Samosa", "Patty", "Salad"]
main_menu = ["Rice and meat", "Pasta and steak", "Lasagne"]
dessert_menu = ["Cake", "Pie", "Tart"]

print("Menu")
print("Starters: " + str(starter_menu))
print("Main: " + str(main_menu))
print("Dessert: " + str(dessert_menu))

print("What would you like as a Starter?")
user_starter = input(str())

print("What would you like for your main?")
user_main = input(str())

print("Finally, what would you like for dessert?")
user_dessert = input(str())

user_meal = [user_starter, user_main, user_dessert]
print(f"So today you will be having {user_starter} for starters, {user_main} as your main meal and finally, {user_dessert} to finish off the evening? Would you like any drinks with that?")
user_drink = input(str())

print(f"{user_meal} and {user_drink}, no problem")

