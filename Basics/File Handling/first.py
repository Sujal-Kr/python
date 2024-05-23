f=open("xyz.txt","a+")
print(f.closed)
print(f.encoding)
print(f.mode)
print(f.name)
print(f.newlines)
# modes and descriptions
# r- reading  only .sets file pointer  at the beginning of the file.
# rb- same as r mode but with binary File
# r+ : both reading and writing. the file pointer is placed at the beginning of the file
# rb+ : same as r+ mode but with binary file
#  w: writting only.OverWrittes the file if the file exits. if not ,creates the the file
# wb: same as w mode but with binary file
# w+: same as w+ mode but with binary file
# a: for appending .Move file pointer  at the end of the file Creates new file  for writting .
# ab:same as a but with binary file
# a+:for both appending and reading.Move file pointer at the end .If the file does not exist it creates a new file for reading and writing.
# ab+:same as a+ mode but with binary file

# newLines:returns "\r","\n","\r\n",None or a tuple
