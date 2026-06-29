def defuseBomb(code,k):
    n=len(code)

    if k==0:
        return [0]*n
    answer=[0]*n
    for i in range(n):
        total=0

        if k>0:
            for j in range(1,k+1):
                total=total+code[(i+j)%n]
        else:
            for j in range(1,-k+1):
                total=total+code[(i-j)%n]
        answer[i]=total
    return answer
#Main
value=[2,4,9,3]
k=-2
print(defuseBomb(value,k))