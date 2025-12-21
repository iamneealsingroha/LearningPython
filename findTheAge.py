A=int(input("in which year were you born "))
B=int(input("in which month were you born "))
C=int(input("in which day were you born "))
D=int(input("What is the current year "))
E=int(input("What is the current month "))
F=int(input("What is the current day "))
G=A*10000
H=B*100
I=G+H+C
J=D*10000
K=E*100
L=J+K+F
M=L-I
print("are now (y/m/d)",  M)