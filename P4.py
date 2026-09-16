user_input=int(input("Enter a number : "))
if user_input %5==0 and user_input %3==0 :
    print("Divisible by Both")
elif user_input %3==0:
    print("Divisible by 3")
elif user_input %5==0:
    print("Divisible by 5")
