num=int(input("Enter a number : "))#5*4*3*2*1----2*2*1---3*3*2*1--1*4*3*2*1
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(fact)