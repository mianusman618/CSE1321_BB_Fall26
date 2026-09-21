str_var="Hello World"
iter_no=1
for x in str_var:
    print("Iter # ",iter_no,end=" ")
    iter_no+=1
    if x == "o":
        print("Value of x  = ",x)