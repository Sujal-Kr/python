 
import math

def convert_in_words(num):
    while (num>0):
        last= num%10
        helper(last)
        num=math.floor(num/10)
    
def helper(num):
    match num:
        case 0: print ("Zero")
        case 1: print ("One")
        case 2: print ("Two")
        case 3: print ("Three")
        case 4: print ("Four")
        case 5: print ("Five")
        case 6: print ("Six")
        case 7: print ("seven")
        case 8: print ("Eight")
        case 9: print ("Nine")
        case _: print ("invalid")


convert_in_words(789)