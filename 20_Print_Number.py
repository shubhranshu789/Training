def printPattern(rows):
    for i in range(1, rows + 1):  
        for j in range(rows  - i):  
            print(" ", end=" ")
        for k in range(1, 2 * i):  
            print(k , end=" ")
        print()



rows = int(input("Enter the row size for the pattern: "))
printPattern(rows)