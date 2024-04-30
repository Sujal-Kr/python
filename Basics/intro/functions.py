# with or without parameters for example sum(),len(),print(),head(),tail(),
# user defined functions a user can define a function with the following syntax:
# def function_name():
    # body

# example 
from math import sqrt
import math


def addition(x,y):
    print(x+y)

def multiply(x,y):
    print(x*y)

def divide(x,y):
    print(x/y)


def modulus(x,y):
    print(x%y)

addition(8,9)
multiply(8,9)
divide(8,9)
modulus(8,9)


def isprime(x):
    prime=True
    for i in range(2,x):
        if x%i==0:
            prime=False
            break
    return prime


print(isprime(8))



def calculate(num1,num2,opr):
    match opr:
        case '+':
            print (num1+num2)
        case '-':
            print (num1-num2)
        case '*':
            print (num1*num2)
        case '/':
            print (num1/num2)
        case _:
            print ("you are gay")

# num1=int(input("Enter the first number : "))
# num2=int(input("Enter the second number : "))
# opr= input("Enter the  operator : ").strip()

# calculate(num1,num2,opr)



# wap to convert the number in words
# wap to take the input in indian currency and print the ouput in dollars'



        
# convert_in_words(1098)


