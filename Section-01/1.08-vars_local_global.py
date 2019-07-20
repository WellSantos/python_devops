#!/usr/bin/env python

hacker = "me"

def local_variables_example():
    hacker = "you"
    print("The local variable is \"%s\"") %(hacker)

local_variables_example()
print("The global variable is \"%s\"") %(hacker)
