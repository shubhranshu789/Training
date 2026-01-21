
def printStar(n):
    for i in range (0, n + 1):
        print("* " * (n - i) + " " * i)


rows = int(input("Enter  size : "))
printStar(rows)
