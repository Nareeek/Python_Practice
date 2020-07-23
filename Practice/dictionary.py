import pandas as pd

# first method
my_dict1 = {"one": 1, "two": 2, "three": 3, "four": 4}

# second method
my_dict2 = dict()

# third method
my_dict3 = dict(one=1, two=2, three=3, four=4)

print(my_dict1)
print(my_dict2)
print(my_dict3)

print()

# nested dictionary
numbers = {"one": {1: "number", "1": "char"},
           "two": {2: "number", "2": "char"},
           "a": {97: "order in ASCII", "a": "not a number"}}
print(numbers)
print(numbers["a"])
print(numbers.get("a"))

print()

print(numbers.keys())
print(numbers["one"].keys())
print(numbers["one"].values())

print()

# keys
for x in numbers:
    print(x)

print()

# values
for x in numbers.values():
    print(x)

print()

# items
for x, y in numbers.items():
    print(x, "||", y)

print()
print(numbers.pop("one"))  # first item "one"
print(numbers.popitem())  # last item "a"
del numbers["two"]
print(numbers)

print()

# converting dictionary into a Dataframe(2-D data structure)
emp_details = {"Employee": {"Nar": {"ID": "001", "Salary": "2000", "Designation": "Team Lead"},
                            "Kar": {"ID": "002", "Salary": "1000", "Designation": "Manager"}}}

df = pd.DataFrame(emp_details["Employee"])
print(df)
