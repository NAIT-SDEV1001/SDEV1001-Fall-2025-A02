# the values (the right side of the colon)
# can be any data type and most times in dictionaries
# they are different data types because the dictionary
# as whole is trying to describe a complex data type.
grades = {
    "Alice": 85,
    "Bobby": 92,
    "Charlie": 78
}
# review
# you can access "Alice" grades by using the [] with
# the key in it.
print('review')
print(grades['Alice']) # this will be 85


# looping over keys() (the values on the left side of the dict)
print("looping over keys")
# you can loop through the keys
print(grades.keys()) # dict_keys(['Alice', 'Bobby', 'Charlie'])

# you can also convert this to list using the list method
print(list(grades.keys()))

# we can loop over the values
print("students")
for key in grades.keys():
    print(F"- {key}")

# let's take a look at the values.
# note this is the right side of the key value pair in the
# dictionary (after the :)
print("looping over values")
print(grades.values())


total = 0
for grade in grades.values():
    total = total + grade

print(F"Average is {total/len(grades.values())}")

# here we can take look at all of the properties and
# methods on a variable
# you can do this with the dir() method where you pass in
# the variable as an object
