from io import open

textFile=open("file.txt","w")#create or open a file on "w" writing mode, you can use "a for append" or "r for read the file"

phrase="great day for python study \n this Monday"
textFile.write(phrase)#insert the phrase to the file

textFile.close()#close the file from the memory, end the manipulation