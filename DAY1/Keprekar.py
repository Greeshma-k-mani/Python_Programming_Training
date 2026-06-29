N=int(input())
a=N**2
digits=len(str(N))
R=a%(10**digits)
L=a//(10**digits)
if L+R==N:
    print("Keprekar Number")
else:
    print("Not")

