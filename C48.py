def cal_price(age,day):
    price=0
    if age<13:
        price=8
    elif age>=13 and age<65:
        price=12
    elif age>=65:
        price=7

    if day=="e" or day=="E":
        price+=3
    return price
No_readings=int(input("How many tickets? "))
total_price=0
for i in range(1,No_readings+1):
    age=int(input(f"Ticket {i} Age: "))
    day = input(f"Ticket {i} Day: ")
    ticket_price = cal_price(age,day)
    total_price+=ticket_price
    print(f"Ticket {i} price = ",ticket_price)
print("Overall price = ",total_price)