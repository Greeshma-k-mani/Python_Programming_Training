day=input()
attendees=int(input())
if day=='MON'or day=='TUE' or day=='WED' or day=='THU':
    if attendees>=700 and attendees<=1000:
        print("Succesful")
    else:
        print("Unsuccesful")
elif day=='FRI' or day=='SAT' or day=='SUN':
    if attendees>=1500:
        print("Succesful")
    else:
        print("Unsuccessful")
else:
    print("Invalid Input")