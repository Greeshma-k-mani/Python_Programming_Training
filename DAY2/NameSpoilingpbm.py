name=input("Enter the string:")
mid=len(name)//2
# name[start:end]
firstPart=name[:mid]
secondPart=name[mid:]
#reverse
firstPart1=firstPart[::-1]
secondPart2=secondPart[::-1]
print(firstPart1 + secondPart2)

