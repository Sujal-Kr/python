def convertor():
    print ("""
        1. Convert to dollar
        2. Convert to inr
                """)
    choice=input("Enter your choice:").strip().lower()
    amount=int(input("Enter the amount to convert :"))
    match choice:
        case 'dollar':print(amount*83)
        case 'inr':print(amount/83)
        case _:print("Invalid")

    
convertor()