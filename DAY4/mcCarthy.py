def mcCarthy(n):
    if n>100:
        return n-10
    
    return mcCarthy(mcCarthy(n+11))
#Driver Code
n=int(input())
print("Number:",mcCarthy(n))