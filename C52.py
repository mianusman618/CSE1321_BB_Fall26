def cal_price(price,qty):
    return price*qty
def apply_discount(total,membership):
    if membership=="GOLD":
        discount_amount=total*(10/100)
    elif membership=="SILVER":
        discount_amount= total * (5 / 100)
    return discount_amount


while True:
    choice = input("Another Customer (Y/N):  ")
    if choice=="N":
        break
    else:
        subtotal=0
        items_purchased=0
        while True:
            price=int(input("Item price (0 to finish): "))
            if price==0:
                break
            qty=int(input("Quantity: "))
            cost=cal_price(price,qty)
            subtotal+=cost
            items_purchased+=1
        membership=input("Membership (Regular/Silver/Gold): ")
        membership.upper()
        subtotal_mem_discount=apply_discount(subtotal,membership)
        print(f"Items purchased: {items_purchased}")
        print(f"Subtotal: ${subtotal}")



