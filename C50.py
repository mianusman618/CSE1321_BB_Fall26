def cal_fine(days):
    if days==0:
        return 0
    elif days<=5:
        fine=0.5*days
        return fine
    else:
        fine=0.5*5+1*(days-5)
        return fine

Books=int(input("How many books? "))
total_fine=0
for i in range(1,Books+1):
    days = int(input(f"Book {i} Days late : "))
    fine = cal_fine(days)
    total_fine+=fine
    print(f"Book {i} fine = ",fine)
print(f"Overall fine = {total_fine:.2f}")