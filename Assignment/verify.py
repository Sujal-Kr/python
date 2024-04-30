# Q.1. Write python program to let user enter some data in string and then verify data and print welcome to user.


user_input = input("Please enter your data: ")

if user_input.strip().lower() == "greetings"  :
    print("Welcome user!")
else:
    print("Data Missmatch!")
