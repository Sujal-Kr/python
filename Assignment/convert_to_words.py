one_digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
teen_arr = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
nums = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def convert_in_words(n):
    if n == 100:
        print("Hundred")
    elif n <= 10:
        print(one_digit[n])
    elif n < 20:
        print(teen_arr[n - 11])
    elif n < 100:
        print(nums[n // 10] + " " + one_digit[n % 10])
    else:
        print("Wrong Input")

convert_in_words(int(input("Enter any number between 0 and 100 : ")))
