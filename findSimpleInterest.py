principle=int(input("enter value for principle:"))
rate=int(input("enter value for rate:"))
time=int(input("enter value for time:"))
simple_interest=(principle*rate*time)/100
amount=principle+simple_interest
print("simple interest=", simple_interest)
print("amount=", amount)