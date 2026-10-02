num=int(input("Enter a number : "))#3...3*3*2*1...4--4*4*3*2*1
fact=1#3
while num >= 1:
    fact=fact*num # 3*3=9....9*2=18... 18*1=18...18*0=0
    num=num-1 #3-2....2-1...1-0
print(fact)