#dictionaries are data structures 
#data associated with a key can be stored
#key first then the data separated with :
meDictionary={1:"one",2:"two",3:"three"}
print(meDictionary)
meDictionary[4]="four" #adding data
meDictionary[4]="cuatro"  #updating data
print(meDictionary)
del meDictionary[4]  #deleting data with the key
print(meDictionary)
meList=["spain","france"]
meDictionary2={meList[0]:"madrid",meList[1]:"paris"} #adding some keys to meList
print(meDictionary2)
print(meDictionary2["spain"]) #print with the key on the list



