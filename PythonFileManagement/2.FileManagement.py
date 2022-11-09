from io import open

fileText=open("file.txt","r")#open the file in "r" read mode

print(fileText.read()) #read the file
fileText.seek(0)#after the read the pointer is in the end, but you can change the position with the method seek
print(fileText.readlines()) #return a list of lines from the file
