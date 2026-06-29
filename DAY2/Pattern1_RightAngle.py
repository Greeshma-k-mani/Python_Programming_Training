N=int(input())
for i in range(N+1):
    for j in range(i):
        print("*",end=" ")
    print()

n=5
for i in range(1,n+1):
    print("*" *i)