"""
Lab 3: Intro to Python Basics
Claudio Lopez
Sep 9, 2026
"""
print("Example 1: String")
name = "Michael Jackson"
print(name[::2])
print(name[3:10:2])

print("Example 2: String methods")
name1 = name.upper()
name2 = name.lower()
name3 = name.replace('Michael', 'Janet')
indexname = name.find('Jack')
print(f'Name in upper = {name1}')
print(f'Name in lower = {name2}')
print(f'Index for Jack = {indexname}')
print(f'Split name = {name.split('a')}')

print("Example 3: regular expression")
import re

s1 = "Michael Jackson is the best"
pattern = r"Jackson"
result = re.search(pattern, s1)
print(f"The pattern result is = {result}")
if result:
    print("Result found")
else:
    print("Result not found")

pattern = r"\d\d\d\d\d" 
zipcode = "My zipcode is = 12345"
match = re.search(pattern, zipcode)
if match:
    print(f"Zip code found = {match.group()}")
else:
    print(f"Match not found")

print("Example 4: Tuples")
tuple1 = ('disco', 10, 1.2)
print(type(tuple1))
print(f"Second element = {tuple1[1]}")
print(f"last element = {tuple1[-1]}")
print(f"There are {len(tuple1)} elements in the tuple")
rating = (10,3,4,9,7)
print(f"Sorted tuple = {sorted(rating)}")
nestedtuple = (1,2, ("pop", "rock"), (3,4), ("disco", (8,9)))
print(f"original tuple = {nestedtuple}")
print(f"Nested tuple = {nestedtuple[2]}")
print(f"Nested subtuple = {nestedtuple[3][1]}")
print(f"Nested sub-subtuple = {nestedtuple[4][1][0]}")
