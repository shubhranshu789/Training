def hollowRectangle(r, c):
    for i in range(r):
        if i == 0 or i == r - 1:
            print("* " * c)
        else:
            print("* " + "  " * (c - 2) + "*")

r = int(input("Enter rows: "))
c = int(input("Enter columns: "))
hollowRectangle(r, c)
