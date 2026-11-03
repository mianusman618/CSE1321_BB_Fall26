ages={"Alice":30,"Bob":27,"Charlie":31}
print(ages)
for x in ages:
    print(x)
print("Printing key and value")
for x in ages:
    print(f"Key ={x} and Value = {ages[x]}")
print("Iterating only values")
for value in ages.values():
    print(value)