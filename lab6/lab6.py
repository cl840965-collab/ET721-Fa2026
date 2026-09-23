"""
Claudio Lopez
Sep 23, 2026
Lab 6: working with files  
"""
print("\nExample 1: read a file")
with open("phrases.txt", "r") as file1:
    filecontent = file1.read()
    print(filecontent)
    print(file1.read(5))
print(f"Is the file closed {file1.closed}")

print("\nExample 2: read a file lines")
with open("phrases.txt", "r") as file1:
    print(file1.readline(30))
    print(file1.readline(5))
    print(file1.readline())

print("\nExample 3: read a file lines")
with open("phrases.txt") as file1:
    print(file1.readlines())

print("\nExample 4: loop to each line in a file")
with open("phrases.txt", "r") as file1:
    filelines = file1.readlines()
    for eachline in filelines:
        print(f"\t {len(eachline)}", end="\t")
        print(eachline.strip())

print("\nExample 5: write file")
with open("lastname.txt", "w")as file:
    file.write("Python basic for data science")
    file.write("Claudio Lopez")

print("\nExample 6: append mode")
from datetime import datetime
with open("lastname.txt", "a")as file:
    file.write(f"\n{datetime.now}")

print("\nExample 7: pandas ")
import pandas as pd

data={
    'name' : ['Alice', 'Bob', 'Charlie'],
    'age' : [25, 30, 19]
}
df = pd.DataFrame(data)
print(df)
