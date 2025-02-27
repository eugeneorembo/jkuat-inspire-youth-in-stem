# learning about functions
# what are functions in programing
# function are block of reusable code that only runs when in it is called.
# you can pass data, known as parameters or arguments, into a function. A function can return data as a result.
# functions help to organize and modularize code.

# how to define a function in python
# in python a function is define using the "def" keyword.
def my_function():
    print("hello from my function")

# how to call a function in python
# to call a function, use the function name followed by parenthesis:
my_function()

def greet_user(name):
    return("hello", name)

print(greet_user("john"))

def greetings(user_name):
    return(f"hello (user_name)")

print(greetings("john"))

# Calculating the area of a circle

import math

#def circle_area(radius):
    #return math.pi * radius ** 2 # the formula is usualy pi * r^2
#print(circle_area(int(input("enter the radius of the circle: "))))
#print(circle_area(5))

# not using math module
#def circle_area(radius):
    #return 3.14 * radius ** 2

def grade_score(score):
    if score >= 90:
        return "your grade is A"
    elif score >= 80:
        return "your grade is B"
    elif score >= 70:
        return "your grade is C"
    elif score >= 60:
        return "your grade is D"
    elif score >= 50:
        return "your grade is E"
    else:
        return "your grade is F"

score = int(input("enter your exam score: "))
print(grade_score(score))



