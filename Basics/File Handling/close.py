
# close() Method
# used to close an open file.After using this method ,and
# opened file will be closed and a closed file cannot be read or v


f=open("xyz.txt","a+")
print(f.closed)
print("Name of the file:",f.name)
f.close()
print(f.closed)
