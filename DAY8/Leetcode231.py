def CheckPowerOfTwo(n):
    return n>0 and (n&(n-2))==0
print(CheckPowerOfTwo(int(input())))