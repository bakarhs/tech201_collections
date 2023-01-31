# tech201_collections
tech201_collections

## Lists

Lists == Arrays

Example of a first list:
```
shopping_list = ["milk", "eggs", "bread", "fruit", "cheese"]
print(type(shopping_list)) # <class 'list'>
print(shopping_list)
```
## How we can search for specific items in a list?
```
print(shopping_list[0]) # milk
print(shopping_list[3]) # fruit
print(shopping_list[-1]) # cheese
```
## Rewriting a value in our list
```
shopping_list[0] = "sugar"
print(shopping_list[0]) # sugar
print(shopping_list)
```
# List methods

## Adding to a list
```
shopping_list.append("vegetables")
print(shopping_list)
print(shopping_list[5])
print(len(shopping_list))
```
## How to remove from a list?
```
shopping_list.remove("bread")
print(len(shopping_list))
print(shopping_list)
```
## How to remove last item of list without specifying?
```
shopping_list.pop()
print(shopping_list)
shopping_list.pop()
print(shopping_list)
shopping_list.pop()
print(shopping_list)
```
## Mixed data type lists
```
mixture = [1, 2, 3.5, "one", "two", "three" "four"]

print(mixture)
```
## List slicing
Example of list slicing
```
print(mixture[1:3]) # 2, 3.5
print(mixture[-2::]) # using a double colon reverses the order
print(mixture[::2]) # bounces over the amount of indexs specified
```

# Tuples

Exactly the same as lists, except they are immutable
Tuples are useful for elements you want to ensure some data stays the same
Example of a Tuples
```
essentials = ("bread", "eggs", "milk")

print(essentials)
print(essentials.count("bread"))
```

# Sets and Frozen sets

Lists and sets are very similar
Sets are unordered

# Example of a set
```
car_parts = {"wheels", "doors", "exhausts"}
print(car_parts)
```

## How to remove things from a set
Example of removing things from a set:
```
car_parts.discard("doors")
print(car_parts)
```

# How to add things to a set
Example of adding things to a set:
```
car_parts.add("windows")
print (car_parts)
```

## Frozen sets
Frozen sets are immutable versions of a set. unordered and un-indexed

An example of a frozen set:
```
x = frozenset([1, 2, 3, 4, "Five"])
print(x)
```
They can not be edited

# Dictionaries
Dictionaries use key/value pairs

key = a reference to a particular object
value = data storage mechanism you want to use

## Creating a dictionary
An example of a dictionary:
```
student_1 ={
    "name": "Susan",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_name": ["variables", "data_types", "set_up"]

}
```
## Access data within a dictionary

```
print(student_1["stream"]) # DevOps
```
## How to access a particular part of a list in a dictionary
```
print(student_1["completed_lesson_name"][2])
```

## Changing a value in a dictionary
```
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])
```

## Removing items from a dictionary
```
student_1["completed_lesson_name"].remove("data_types")
print(student_1["completed_lesson_name"])
```

## Dictionary methods
Keys
```
print(student_1.keys())
```

## How to get te values of a key back without[]
```
print(student_1.get("name"))
```
## How to get the values of a dictionary
```
print(student_1.values())
```

# How to output array of tuples with key value pairs in dictionary
```
print(student_1.items())
```
### Example 2
```
student_2 ={
    "name": "Bakar",
    "stream": "DevOps",
    "completed_lessons": 3,
    "completed_lesson_name": ["what is devops", "agile and scrum", "git and python"]

}
```
