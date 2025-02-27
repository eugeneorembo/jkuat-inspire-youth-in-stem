#variables in python
student_name = "john" # string
student_second_name = "doc" #string
student_age = 7 # integer
student_height = 5.5 # float
#print(student_name)
# Operators in python
#1. Arithmetic operators
num1=20
num2=40
addition = num1 + num2
#print(addition)
subtraction = num1 - num2
#print (subtraction)
#2. Comparison operator
#print(num1 == num2)
#print(num1>num2)
#print(num1!=num2) #true
#3. logical operators
# and, or, not
#print(num1<num2 and num1>num2) #false
#print(num1<num2 or num1>num2) #true
#print(not num1<num2) #false
#4. Assignment operators
#num1 +=2
#print(num1)
#5. Identy operators
# is, is not
#print(num1 is not num2) #true

#6. Conditional statements
# if, elif, else
if student_age >= 5:
    print("old student")
    enter_name = input("Enter your name: ")
    enter_age = int(input("enter your age: "))
    if enter_age <= 18:
        print("you are a child")
        if enter_age >= 18:
            print("you are an adult")