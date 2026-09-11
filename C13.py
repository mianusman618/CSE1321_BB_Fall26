age_str=input("Enter Your Age : ")
age_int=int(age_str)
if age_int >= 18:
    print("You are allowed to vote")
    print("This is 2nd line in if block")
if age_int <= 18:
    print("You are not allowed to vote")