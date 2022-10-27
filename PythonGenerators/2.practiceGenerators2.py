def find_cities(*cities):
    for element in cities:
        #for subElement in element:
        yield from element #you can use 'from' for avoid use nested for

cities=find_cities("paris","madrid","berlin")

print(next(cities))
print(next(cities))