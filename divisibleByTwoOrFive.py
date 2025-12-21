A = int(input("Enter a number: "))
if A % 2 == 0:
    B = 1
else:
    print("Not an multiple of 2")
    B = 2
if A % 5 == 0:
    C = 2
else:
    print("Not a multiple of 5")
    C = 1
if ((B == 1) and (C == 2)):
    print(A,"is a common multiple of both 2 and 5")
else:
     print("Not doable")