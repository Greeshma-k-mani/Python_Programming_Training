T=int(input())
P=float(input())
C=int(input())
Amount=P*T
D=0
if T>15 and C==1:
    D=D+25
    print("Discount applied and Category is Max ticket and student")
elif T>15 and C==2:
    D=D+20
    print("Discount appled and category is max ticket")
elif C==1:
    D=D+5
    print("Discount appled and category is student")
else:
    print("Discount not applied")
if D>0:
    Amount=Amount-(Amount*D/100)
    print(Amount)

#C=1 student
#c=2 Max ticket

