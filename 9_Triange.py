def printStar(n):
    for i in range(n, 0, -1):
        print("  " * (n - i) + "* " * i)

rows = int(input("Enter size: "))
printStar(rows)



    

