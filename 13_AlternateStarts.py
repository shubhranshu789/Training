def printShape(n):
    for i in range(1 , n+1):
        if n % i != 0:
            print("* " , end= " ")
        else:
            print(" " , end= " ")

n = int(input("Enter rows: "))
printShape(n)
