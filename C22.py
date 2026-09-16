var=50
match var:
    case 1:
        print("case 1")
    case 2:
        print("case 2")
    case 25:
        print("case 25")
        age=input("Enter your age :")
        if int(age)>50:
            print("Age more than 50")
    case 50:
        print("case 50")
        var2=30
        match var2:
            case 40:
                print("var2=40")
                print("2nd print line in case 50")
    case 100:
        print("case 100")
    case _:
        print("default case")
print("rest of the program")