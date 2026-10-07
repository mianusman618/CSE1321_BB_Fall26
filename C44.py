def myfunc1(param1,param3,param2=100):
    print(f"Param 1 ={param1} and Param 2 = {param2}")
    sum1=0
    for i in range(param1+1):
        sum1+=i
    print(f"Sum upto {param1} = {sum1}")


func_output=myfunc1(5,50,200)
print("hello world")
myfunc1(10,20)