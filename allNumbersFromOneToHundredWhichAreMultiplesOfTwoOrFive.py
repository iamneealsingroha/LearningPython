for i in range(1,101,1):
    if (i%2==0):
        A = 1
    else:
        A = 2
    if (i%5==0):
        B = 1
    else:
        B = 2
    if ((B == 1) or (A == 1)):
        print(i)