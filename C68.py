user_input=input("Enter comma seprated scores : ")
list_scores=user_input.split(",")
print(list_scores)
sum1=0
for e in list_scores:
    sum1+=int(e)
print(sum1)