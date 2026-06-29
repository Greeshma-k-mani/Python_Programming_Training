nums=[3,2,3]
count=0
candidate=0
for i in nums:
    if count==0:
        candidate=i
    if i==candidate:
        count=count+1
    else:
        count=count-1
print (candidate)