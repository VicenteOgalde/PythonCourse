def evenGenerator(limit):
    num=1
    meList=[]
    while num<=limit:
        meList.append(num*2)
        num=num+1
    return meList
def evenGenerator2(limit):
    num=1
    while num<=limit:
        yield num*2 #using yield instead of return makes it a generator function

        num=num+1


evenList=evenGenerator2(5) #the generator goes into a suspended state between calls, saving resources

print(next(evenList))
print(".....")
print(next(evenList))
print(".....")
print(next(evenList))
print(".....")

