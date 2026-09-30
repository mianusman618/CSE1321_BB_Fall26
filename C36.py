num=int(input("Enter a number : "))
digit_count=0
while num > 0:#537//10=53----537/10=53.7
    num=num//10
    digit_count+=1
print("No. of digits = ",digit_count)