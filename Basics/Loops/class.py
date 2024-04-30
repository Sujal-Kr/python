# for num in range(1,101):
#     if num % 2 !=0:
#         print(num)
# prime numbers
# for num in range(1,101):
#     check=True
#     for i in range(2,num):
#         if num % i ==0:
#             check=False
#     if check==True:
#         print(num)


# display the table of any given integer value


# def table(num):
#     for i in range(1,11):
#         print(num*i)


# table(int(input("Enter the number")))




# The loop is used for checking some conditions usally , the condition is the terminating statment for the loop 
# the While loop is making use of increment and decrement operators directly without using the step keyword

#  display the prime number from one to 10 if num is 7 then display week is over


for num in range(1,11):
    prime=True
    if num == 7:
        print("Week is over")
        break
    for i in range(2,num):
        if num % i == 0:
            prime=False
    
    if prime==True:
        print(num)



    