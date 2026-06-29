num=list(map(int,input().split()))
O=0
E=0
for i in num:
    if i%2==0:
       E=E+1
    else:
        O=O+1
print("Odd:",O)
print("Even:",E)
