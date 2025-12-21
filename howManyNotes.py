a=int(input("Enter Amount:"))
if a>=500:
    b=a//500
    c=a%500
    print("Rs. 500:", b)
    a=c
    if a>=100:
        b=a//100
        c=a%100
        print("Rs. 100:", b)
        a=c
        if a>=50:
            b=a//50
            c=a%50
            print("Rs. 50:", b)
            a=c
            if a>=10:
                b=a//10
                c=a%10
                print("Rs. 10:", b)
                a=c
                if a>=5:
                    b=a//5
                    c=a%5
                    print("Rs. 5:", b)
                    a=c
                    if a>=1:
                        b=a//1
                        c=a%1
                        print("Rs. 1:", b)
elif a>=100:
    b=a//100
    c=a%100
    print("Rs. 100:", b)
    a=c
    if a>=50:
        b=a//50
        c=a%50
        print("Rs. 50:", b)
        a=c
        if a>=10:
            b=a//10
            c=a%10
            print("Rs. 10:", b)
            a=c
            if a>=5:
                b=a//5
                c=a%5
                print("Rs. 5:", b)
                a=c
                if a>=1:
                    b=a//1
                    c=a%1
                    print("Rs. 1:", b)
elif a>=50:
    b=a//50
    c=a%50
    print("Rs. 50:", b)
    a=c
    if a>=10:
        b=a//10
        c=a%10
        print("Rs. 10:", b)
        a=c
        if a>=5:
            b=a//5
            c=a%5
            print("Rs. 5:", b)
            a=c
            if a>=1:
                b=a//1
                c=a%1
                print("Rs. 1:", b)
elif a>=10:
    b=a//10
    c=a%10
    print("Rs. 10:", b)
    a=c
    if a>=5:
         b=a//5
         c=a%5
         print("Rs. 5:", b)
         a=c
         if a>=1:
            b=a//1
            c=a%1
            print("Rs. 1:", b)
elif a>=5:
    b=a//5
    c=a%5
    print("Rs. 5:", b)
    a=c
    if a>=1:
        b=a//1
        c=a%1
        print("Rs. 1:", b)
elif a>=1:
    b=a//1
    c=a%1
    print("Rs. 1:", b)