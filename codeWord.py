while True:
    a=input("Enter the code word(fruit,clothes,sport...):")
    if a=="fruit":
        print(a,"It is a banana, but not an apple...")
    elif a=="clothes":
        print(a,"Maybe a shirt, maybe a jacket...")
    elif a=="sport":
        print(a,"Has to be cricket or badminton...")
    elif a=="exit":
        print("exiting code....")
        break
    else:
        print("Incorrect code word! BEEP BEEP!")