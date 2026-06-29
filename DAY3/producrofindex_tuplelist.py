#set={None,0,1,False}
#print(set)

tuple_list=eval(input())
k=int(input())
product=1
for tup in tuple_list:
    product=product*tup[k]
print(f"Product of values:{k}:{product}")