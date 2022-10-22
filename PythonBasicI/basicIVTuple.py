# A Tuple is an immutable List
#declaration:
#TUPLE -> nameTuple=(elem1,elem2,elem3) <-- parentheses optionals
#print:
#print a tuple -> print(nameTuple[:])
#print a number of times an element -> print(meTuple.count(nameElement))
#print Nº ELEMENTS -> print(len(meTuple))
#find an ELEMENT -> print(nameElement in nameTuple) *return true or false
#functions
# change a TUPLE to LIST -> namelist=list(nameTuple)
# change LIST to TUPLE -> nameTuple=tuple(namelist)
# Unpack a TUPLE -> variable1,variable2,variable 3 = meTuple 

from calendar import month


meTuple=("juan",12,2,1999)
print(meTuple[2])
meList=list(meTuple)
print(meList)
print(meTuple.count(2))
name, day, monthName,year=meTuple
