def check_pwd(pwd):
    if pwd=="python123":
        return True
    else:
        return False

for i in range(3):
    pwd=input("Enter Password : ")
    if check_pwd(pwd):
        print("Access Granted")
    else:
        remaining=3-i
        if remaining>0:
            print(f"incorrect pwd {remaining} attempts remaining")