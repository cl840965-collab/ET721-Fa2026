"""
Claudio Lopez
Oct 5, 2026
Lab 9: Unit Testing using Pytest
"""
# ex 1
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
# ex 2
def validate_password(password):
    if len(password) < 8:
        return False
    return any(char.isdigit() for char in password)
# ex 3
def is_even(n):
    return n % 2 == 0
