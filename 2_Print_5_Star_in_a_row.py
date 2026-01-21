def printStarth(n):
    for i in range (n):
        print("*" , end = " ")
def printStartv(n):
    for i in range (n):
        print("*")

    print("* " * (n-1))


n = int(input("Enter a number"))
printStartv(n)
# print(" ")
# printStarth(n)


