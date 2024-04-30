num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
opr= input("Enter the  operator ").strip()


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


