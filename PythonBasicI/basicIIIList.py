#Declaration:
# list -> nameList[element1, element2, etc]
#print:
#print a list -> print(nameList[:])
#print a element -> print(nameList[index])
#print index of element -> print(nameList.index(element))
#find element -> print(element in nameList)
#adding functions:
#add element to the end of the list -> nameList.append(element)
#add element with an index -> nameList.insert(index,element)
#add more than one element -> nameList.extend([element1, element2, etc])
#delete functions:
#delete element -> nameList.remove(element)
#delete last element -> nameList.pop()

meList=["david","jesus","john","sol"]
print(meList[1:3])
meList.append("moon")
meList.insert(1,"chris")
meList.extend(["DAVID","JESUS"])
print(meList)
print(meList.index("jesus"))
print("sol" in meList)
meList.remove("david")
meList.pop()
print(meList)
meList2=[5,55]
meList3=meList+meList2
print(meList3)