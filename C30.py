inner_iter=1
outer_iter=1
inner_most=1
for i in range(5):
    print("Outer loop",outer_iter)
    for j in range(3):
        print("\tInner loop",inner_iter)
        inner_iter+=1
        for k in range(2):
            print("\t\tInner most loop",inner_most)
            inner_most+=1
    outer_iter += 1

