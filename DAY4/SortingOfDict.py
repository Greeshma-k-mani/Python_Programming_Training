P=eval(input())
choice=input("KEY/PRICE")
def get_value(item):
    return item[1]
if choice=="KEY":
    sorted_dic=dict(sorted(P.items()))
    print("Sorted Dictionary:",sorted_dic)
elif choice=="PRICE":
    sorted_dic=dict(sorted(P.items(),key=get_value))
    print(sorted_dic)
else:
    print("Invalid choice")