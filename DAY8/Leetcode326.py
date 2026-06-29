def CheckPowerOf3(n):
    if n<=0:
        return False
    while n%3==0:
        n//=3
    return n==1

print(CheckPowerOf3(int(input())))