#1. Write a Python script to sort (ascending and descending) a dictionary by value.

ages = {"Jason": 19, "Markus": 23, "John": 22, "Peter": 29, "Larry": 27}

# print(dir(ages))  all methods shown

#--- get
# get value of dict
print(ages.get("Florian","Not in dict")) # get("Jason") -> 19
# check if key exists.
if ages.get("Florian"):                  # checks if it is True
    print("User exists")
else:
    print("User does not exist")

#--- update
ages.update({"Anna":21})                # insert new key value pair
print(ages)
ages.update({"Anna":22})                # update key value pair
print(ages)

#--- pop
popped_user = ages.pop("Markus")        # removes entry with pop("key")
print(ages)                             # you can assign a popped value to a variable
print(f"{popped_user} was popped.")

#--- popitem                            # removes latest key value pair (o,o,o,X)
ages.popitem()
print(ages)
#--- clear                              # removes every keyvalue pair
#ages.clear()
#print(ages)

#--- .keys()                            # iterable, returns objects (resembles list)
keys = ages.keys()
print(keys)                           
for key in ages.keys():
    print(key)

#--- .values()                          # same as .keys() but for values   
values = ages.values()
print(values)
for value in ages.values():
    print(value)

#--- items()                            # returns dict object (resembles 2d list of tuples)
items = ages.items()
print(items)
for key, value in ages.items():
    print(f"{key} is {value} years old.")
       
for pair in ages.items():               # for i in x.items(): -> ("a", 29) | for i,j in x.items() -> "i"   or/and "j"
    print(pair)
    
#--- copy()
my_copy = ages.copy()                   # copies (shallow copy) a dict
print(my_copy)
my_copy.update({"John": 77})
print(ages)
print(my_copy)

#--- setdefault()                       # similar to get, grabs a key value pair, and if it doesnt exist, it creates it
print(ages.setdefault("John", "0"))
print(ages)
print(ages.setdefault("Thomas", "0"))
print(ages)

#--- fromkeys()
