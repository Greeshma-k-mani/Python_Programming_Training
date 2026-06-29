# [1,2,3,4,5]
#filter + lambda
#result=list(map(lambda x:int(x)%2==0,input("Enter the digits")))
n=[1,2,3,4,5]
even=list(filter(lambda n:n%2==0,n))
print(even)