#!/usr/bin/env python3

print("Welcome to MacOS, what is your name?")
name = input()
print("What is your password?")
password = input()

if name == "Jordan" and password == "computerscience":
	print("Hello, Jordan, have a good day")

elif name != "Jordan" and password != "computerscience":
	print("You are not Jordan, Signing out! ")
