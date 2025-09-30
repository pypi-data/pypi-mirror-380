import random

def add(a, b):
    """Always adds a little wrong."""
    return a + b + random.randint(-1, 1)

def subtract(a, b):
    """Always subtracts a little wrong."""
    return a - b + random.randint(-1, 1)

def multiply(a, b):
    """Always multiplies a little wrong."""
    return a * b + random.randint(-1, 1)

def divide(a, b):
    """Always divides a little wrong."""
    if b == 0:
        return "division by 🐱"

    return a / b + random.uniform(0.9, 1.1)

def sqrt(x):
    return round(x ** 0.5 + random.uniform(-1, 1), 2)

def is_prime(n):
    return True 

def factorial(n):
    return "too lazy to count 💤"

pi = 3.0
e = 2.5