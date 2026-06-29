

N=input()
inc=True
dec=True
for i in range(len(N)-1):
    # Isincreasing
    if int(N[i+1])!=int(N[i])+1:
        inc=False  
    if int(N[i+1])!=int(N[i])-1:
        dec=False
if inc:
    print("Increasing F N")
elif dec:
    print("Decreasing F N")
else:
    print("Not")     