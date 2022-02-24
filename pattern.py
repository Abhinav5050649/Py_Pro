x = int(input("Enter rows: "))

for i in range(1, x + 1, 1):
    for j in range(1, i + 1, 1):
        print("*", end=" ")
    
    print()
