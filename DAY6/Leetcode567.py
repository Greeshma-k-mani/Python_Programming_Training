def checkPermutation(s1,s2):
    #Input
    if len(s1)>len(s2):
        return False
    s1_count=[0]*26
    window_count=[0]*26
    #Count frequencies of s1 and foirst window of s2
    for i in range(len(s1)):
        s1_count[ord(s1[i])-ord('a')]+=1
        window_count[ord(s2[i])-ord('a')]+=1
        if s1_count==window_count:
            return True
    #slide the window
    for i in range(len(s1),len(s2)):
        #add the chara
        window_count[ord(s2[i])-ord('a')]+=1

        #remove left char
        window_count[ord(s2[i-len(s1)])-ord('a')]-=1
        if s1_count==window_count:
            return True
    return False
#main
print(checkPermutation('ba','eiabaooo'))
