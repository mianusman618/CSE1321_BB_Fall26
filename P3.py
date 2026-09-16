Num1=int(input("Enter First Number : "))
Num2=int(input("Enter Second Number : "))
Num3=int(input("Enter Third Number : "))
if Num1 > Num2 and Num1 > Num3:
    print("First Number is Largest ",Num1)
elif Num2>Num1:
    if Num2 > Num3:
        print(f"Second Number is Largest {Num2}")
    else:
        print("Third Number is Largest")
else:
    print("Third Number is Largest")