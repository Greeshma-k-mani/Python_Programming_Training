# Third max using binary search
def thirdMax(nums):
    unique=set(nums)
    unique=sorted(unique,reverse=True)

    #Return 3rd element
    #[1,2,3,8,9]
    if len(unique)>=3:
        return unique[2]
    return  unique[0]

#Main

nums=list(map(int,input().split()))
print(thirdMax(nums))