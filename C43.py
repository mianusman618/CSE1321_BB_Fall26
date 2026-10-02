def sum_to_num(param1,param2):
    count=1
    sum=0
    while count <= param1:
        sum+=count
        count+=1
    print(f"Sum upto {param1} = {sum}")

sum_to_num(5,10)
sum_to_num(5,50)