c=float(input())
if c>=0 and c<1:
    print("No Rain")
elif c>=1 and c<5:
    print("Light rain")
elif c>=5 and c<10:
    print("Moderate Rain")
elif c>=10:
    print("Heavy Rain")