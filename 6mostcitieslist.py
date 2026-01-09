z=["Delhi","Mumbai","Kolkata","Bangalore","Chennai","Hyderabad"]
y=input("Choose a city from India ")
if y in z:
    print("Found")
else:
    print("Not Found")
x=int(input("Choose a position from 0 to 5 "))
if x<0 or x>5:
    print("Invalid Position")
else:
    w=input("Enter a city name to replace at position the position")
    z[x]=w
    print("Updated List:",z)