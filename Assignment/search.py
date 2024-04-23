nums=[9,83,90,1,82,1000]
key=int(input("Enter the number to search..."))

def search(nums,key):
    for item in nums:
        if(item == key):
            return True;
    return False;

print(search(nums,key))