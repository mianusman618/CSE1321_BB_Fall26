country=input("Enter Country : ")
if country=="US" or country=="USA":
    age_str=input("Enter Your Age : ")
    age_int=int(age_str)
    if age_int>=18:
        print("You are allowed to vote")
        if age_int>25:
            print("You dont need a guardian")
        else:
            print("You need an adult guardian")
    else:
        print("You are not allowed to vote")
else:
    print("Voting Age is Unknown")