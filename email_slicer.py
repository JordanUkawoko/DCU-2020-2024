#!/usr/bin/env python3

email = input("Email Address: ").strip()

index = email.index('@')

username = email[:index]
domain = email[index+1:]

print("\nEmail address: ", email)
print("Username", username)
print("Domain name", domain)
