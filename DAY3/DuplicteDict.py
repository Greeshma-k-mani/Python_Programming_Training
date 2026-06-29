numbers=list(map(int,input().split()))
k=int(input())
freq=dict()
for num in numbers:
    freq[num]=freq.get(num,0)+1

for key,value in freq.items():
    if value>k:
        print(f"{num}:{value} times")