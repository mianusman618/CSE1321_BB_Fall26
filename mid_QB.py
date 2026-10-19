limit=int(input("Enter the maximum integer limit: "))
print("Generating script...")
print()
print("Copy from the line below:\n\n")

for num1 in range(1,limit+1):
    for num2 in range(1,limit+1):
        if num1==1 and num2==1:
            print(f"if num1 == {num1} and num2 == {num2}:")
            print(f"\tprint({num1+num2})")
        else:
            print(f"elif num1 == {num1} and num2 == {num2}:")
            print(f"\tprint({num1 + num2})")
print(f"else:")
print(f"\tprint('I cannot do addition with such large numbers')")