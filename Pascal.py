def pascal_triangle2(n):
    for i in range (n):
        print(' ' * (n-i) , end = '')
    
        C = 1
        for j in range (i+1):
            print(C , end = ' ')
            C = C * (i-j) // (j+1)
        print()

def pascal_triangle(n):
    for i in range(n):
        print(' ' * (n-i), end='')
        
        C = 1
        for j in range(i+1):
            print(C, end=' ')
            C = C * (i-j) // (j+1)
        print()



pascal_triangle2(6)



