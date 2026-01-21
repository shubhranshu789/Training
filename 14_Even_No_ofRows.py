def printShape(n):
    for i in range(1 , n+1):
        if i % 2 == 0:
            print("* "* n)
        else: 
            print(" ") 

n = int(input("Enter rows: "))
printShape(n)
