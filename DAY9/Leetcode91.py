def DecodeWays(strs):
    
    n=len(strs)
    dp=[0]*(n+1)

#Initialization
    dp[0]=1
    dp[1] = 1 if strs[0] != '0' else 0
    for i in range(2,n+1):
    #single digit
        one_digit=int(strs[i-1:i])
        if 1<=one_digit<=9:
            dp[i]=dp[i]+dp[i-1]
    #Two Digit
        two_digit=int(strs[i-2:i])
        if 10<=two_digit<=26:
            dp[i]=dp[i]+dp[i-2]
    return(dp[n])

strs="226"
print(DecodeWays(strs))