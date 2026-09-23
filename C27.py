str_var="ABC"
iter_no=1
for x in str_var:
    print("Iter # ",iter_no,end=" ")
    if x == "B":
        print("Value of x  = ",x)
    iter_no+=1
print("rest of the program")