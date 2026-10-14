def withdraw(balance,amount):
    if amount<0:
        print("Zero Withdraw is not possible")
    elif amount>balance:
        print("Insufficient Balance")
    else:
        balance-=amount
    return balance
balance=500
while True:
    print("Please choose : ")
    print("1. Check Balance  2. Withdraw Money  3. Exit")
    choice=int(input("Choice: "))
    match choice:
        case 1:
            print(f"Balance = {balance}")
        case 2:
            amount=int(input("Enter Amount to withdraw "))
            fun_output=withdraw(balance,amount)
            if fun_output==balance:
                print("Withdraw Error")
            else:
                balance=fun_output
                print(f"Withdrawl successfull. Remaining balance is {fun_output}")
        case 3:
            print("Good Bye")
            break
