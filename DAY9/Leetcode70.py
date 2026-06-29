n=3  #5
dp=[0]*(n+1)
# Initial values
dp[0]=1
dp[1]=1
#Fill dp array
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])
