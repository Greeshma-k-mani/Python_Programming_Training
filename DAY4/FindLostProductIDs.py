N=list(input().split())
all_ids=set(N)
duplicates=set()
#Find duplicate
for id in N:
    if N.count(id)>1:
        duplicates.add(id)

lost_ids=all_ids-duplicates
print("Lost Product IDs:",lost_ids)
    
