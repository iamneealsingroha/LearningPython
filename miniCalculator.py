a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = input("Enter operation to do: addition, subtraction, multiplication, division:")

if c == "addition":
    print(a, "+",b , "=", a+b)
else:
    if c == "subtraction":
        print(a, "-",b , "=", a-b)
    else:
        if c == "multiplication":
            print(a, "*", b, "=", a*b)
        else:
            if c == "division":
                print(a, "/", b, "=", a/b)