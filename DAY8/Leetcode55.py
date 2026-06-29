def canJump(nums):
    maxreach=0
    for i in range(len(nums)):
        if i>maxreach:
            return False
        maxreach=max(maxreach,i+nums[i])
        if maxreach>=len(nums)-1:
            return True
        
#Main
nums=[2,3,1,1,1]
print(canJump(nums))
   