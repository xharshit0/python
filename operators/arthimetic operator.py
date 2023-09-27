rows = int(input("Enter Number:"))

for i in range(rows):
    for x in range(i+1):
        print(x+1, end=" ")
    print("\n")