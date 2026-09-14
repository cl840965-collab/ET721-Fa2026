"""
Claudio Lopez
Sep 14, 2026
Lab 4: Loops & Conditional Statements
"""
print("Example 1")
age = 17
if (age > 18):
    print("Go to AC/DC Concert")
elif (age == 18):
    print("Go see Pink Floyd")
else:
    print("go see Meatloaf")

print("Move on!")    

print("\nExample 2")
annie = 1996
jane = 1999
if (annie %4 == 0):
    print("Annie was born in a leap year")
elif (jane %4 == 0):
    print("Jane was bor in a leap year")
else:
    print("none were born in a leap year")

"""print("\nExample 3")
age = int(input("Student's age: "))
lunch = "None"
if age <9:
    lunch = "milk"
elif age >= 10 and age <= 14:
    lunch = "Sandwich"
elif age >=15 and age <=17:
    lunch = "Burger"
else:
    lunch = "Out of Range!"

print(f"At age {age} the food is {lunch}")
"""
print("\nExample 4")
for n in range(5,10):
    print(n, end="\t")
print("Print 3, 2, 1")
for m in range(3, 0, -1):
    print(m, end="\t")

print("\nExample 5: for loop in list")
dates = [1982, 1980, 1973]
n = len(dates)
for year in dates:
    print(year)

for y in range(n):
    print(f"year {y + 1} = {dates[y]}")

print("\nExample 6: for loop to access index and element")
colors = ['red', 'yellow', 'green', 'purple', 'blue']
for i, c in enumerate(colors):
    print((i + 1), c)

print("\nExample 7: While loop")
ratings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
count = 0
index = 0
lenratings = len(ratings)
while(index < lenratings):
    if ratings[index] >= 8:
        count +=1
    index +=1
else:
    print(f"There is/are {count} good rating ")

print("\nExample 8: Functions")
def add(n):
    updated = n+1;
    print(f"{n} added 1 = {updated}")
    return updated
m = add(6)
print(f"value of m = {m}")

print("\nExample 9: Functions to pass strings")
def con(a,b):
    return(a+" - " + b)
print(con("Bayside", "NY"))

print("\nEXCERISE")
animals = ['lion', 'giraffe', 'gorilla', 'parrots', 'crocodile', 'deer', 'swan']
newanimals = []
lenanimals = len(animals)
for i in animals:
    if len(i) >= 6:
        newanimals.append(i)
index += 1
print(newanimals)

print("\nEXCERISE-2")
def avg(grade):
    average = 0
    for i in grade:
        average += i
    lengraded = len(grade)
    average2 = average/5
    return lengraded, average2
grade = [65, 87, 95, 77, 35]
print(avg(grade))