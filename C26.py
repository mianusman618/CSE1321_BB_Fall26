user_input=int(input("Enter a num between 1 and 10 : "))
while user_input < 1 or user_input > 10:
    user_input = int(input("Enter a num between 1 and 10 : "))
print("Num Accepted")