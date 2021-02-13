#!/usr/bin/env python3

print("Hello, welcome to the cinema")
print("To watch This film you must be over 18")
print("What is your age?")

age = int(input())
if age >= 18:
    print("Enjoy the film")
elif age < 18:
    print("You are too young to watch this film")
