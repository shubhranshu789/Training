# rows = int(input("Enter  size : "))
# for i in range(rows, 0, -1):  
#     for j in range(1, i + 1):  
#         print("*", end=" ")   
#     print()



def printStar(n):
    for i in range (1, n + 1):
        print("  " * (n - i) + "* " * i)


rows = int(input("Enter  size : "))
printStar(rows)
