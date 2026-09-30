total_sum=0
count=0
#for i in range(10000000):
while True:
    user_input=int(input("Enter a num of -1 to stop : "))
    if user_input == -1:
        break
    total_sum+=user_input
    count+=1
if count>0:
    print("Sum of all numbers = ",total_sum)
    print("Avg of all numbers = ",total_sum/count)
else:
    print("No numbers were entered")