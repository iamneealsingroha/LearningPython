a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a>b and a>c:
    print(a, "is greater")
elif b>a and b>c:
    print(b, "is greater")
elif c>a and c>b:
    print(c, "is greater")
if a<b and a<c:
    print(a, "is smaller")
elif b<a and b<c:
    print(b, "is smaller")
elif c<a and c<b:
    print(c, "is smaller")
