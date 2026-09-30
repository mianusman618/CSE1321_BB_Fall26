num=int(input("Enter a num : "))#num=4
for row in range(num):#0,1,2,3
    for col in range(row+1):
        print("*",end="")
    print()
# *
# **
# ***
# ****