day=input()
#Remove Leading and trailing spaces
attendees=int(input())
def PartySucessfulClassifier(day,attendees):
    weekends=["FRI","SAT","SUN"]
    weekdays=["MON","TUE","WED","THU"]
    if day not in weekdays and day not in weekends:
        return "Invalid Day"
    if attendees<0:
        return "Invalid Attendees"
    if day in weekdays:
        if 700<=attendees<=1000:
            return "Successful"
        else:
            return "Unsucessful"
    if day in weekends:
        if weekends>=1500:
            return "Successful"
        else:
            return "Unsucessful"
a=PartySucessfulClassifier(day,attendees)
print(a)
        
