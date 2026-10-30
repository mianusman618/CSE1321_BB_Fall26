list_var=[6,8,1,9,34,7,2,87,1,3,8,100,200,500,30,40]
# #list_var=[6,1,8,9,7,2,34]
# list_var=[1,6,8,7,2,9,34]
print(list_var)
for i in range(len(list_var)):
    for j in range(len(list_var)-i-1):
        if list_var[j]<list_var[j+1]:
            temp=list_var[j+1]
            list_var[j+1]=list_var[j]
            list_var[j]=temp
print(list_var)