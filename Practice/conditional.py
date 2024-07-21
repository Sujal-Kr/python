# conditional statements

# simple if statement

amount=1000

if amount>=800:
    print("disccount give")
    print("inside if")


# if else statement

age=12

if age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")


# elif
num=10

if num%2==0:
    print("i am divisible by 2")
elif num%3==0:
    print("i am divisible by 3")
elif num%5==0:
    print("i am divisible by 5")
else:
    print("i am  divisible by none")

# nested if statement
num=18
# 
if num%2==0:
    if num%3==0:
        print("i am divisible by 6")
    else:
        print("nested else part")
else:
    print("else part")
    



