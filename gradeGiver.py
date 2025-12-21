a = int(input("Enter you grade out of 100:"))
if a >90 and a <=100:
    print("You got", a, "out of 100 so you got A grade")
elif a >70 and a <=90:
    print("You got", a, "out of 100 so you got B grade")
elif a >50 and a <=70:
    print("You got", a, "out of 100 so you got C grade")
elif a >30 and a <=50:
    print("You got", a, "out of 100 so you got D grade")
elif a < 30:
    print("You got", a, "out of 100 so you failed")