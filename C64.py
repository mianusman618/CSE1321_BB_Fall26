list1=[4,5,1,6,7,2,6,1,9,3,1]
print(list1)
del list1[4]
print(list1)
deleted_element=list1.pop(7)
print(deleted_element)
print(list1)

list1.remove(1)
print(list1)
if 100 in list1:
    list1.remove(100)
print(list1)