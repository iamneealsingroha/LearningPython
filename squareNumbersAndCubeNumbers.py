a = input("Do you want to square your number or cube it? square/cube: ")
b = int(input("Enter number to square/cube: "))
if a == "square":
    print(b,"squared =",b*b)
elif a == "cube":
    print(b,"squared =",b*b*b)