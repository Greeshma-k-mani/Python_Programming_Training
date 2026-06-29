def longestCommon(str):
    prefix=str[0]
    #["Flower","Flow","Flight"]
    for s in str[1:]:
        while not s.startswith(prefix):
            prefix=prefix[:-1]

            if prefix=="":
                return""
        
    return prefix
print(longestCommon(list(input().split())))
