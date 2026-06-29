a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>=b and a>=c and a>=d:
    print("Largest a")
elif b>=c and b>=d:
    print("Largest b")
elif c>=d:
    print("Largest c")
else:
    print("Largest d")