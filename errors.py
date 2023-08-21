#!/usr/bin/env python3
import sys
import os

# LBYL - Look Before You Leap

if os.path.exists("names.txt"):
    print("File exists")
    input("...")  #Race condition
    names = open("names.txt").readlines()
else:
    print("Error: File not found")
    sys.exit(1)     
if len(names) >=3 :    
    print(names[2])
else:
    print("Error: Missing name in the list")
    sys.exit(1)    


# EAFP - Easy to ask forgviness than permission

try:
    names = open("names.txt").readlines()
    1 / 0 #ZeroDivisionError
    print(names.banana) #AttributeError
except FileNotFoundError:
    print("Error: File not found")
    sys.exit(1)
except ZeroDivisionError:
    print("Error: You can´t dvide by zero!!!")    
try:    
    print(names[2])
except:
    print("Error: Missing name in the list")
    sys.exit(1)  