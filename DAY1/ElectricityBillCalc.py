N=int(input())
if N<=100:
    print(N*1.50)
elif N>100 and N<=200:
    print(100*1.50+(N-100)*2.50 )
else:
    print(100*1.50+100*2.50+(N-200)*4)
