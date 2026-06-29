students=[
    ("Aslaha",26),("Dinix",23),("Susanne",25)
]
sorted_students=sorted(
    students,
    key=lambda x:x[1]
)
print(sorted_students)

students=[
    ("Aslaha",26),("Dinix",23),("Susanne",25)
]
sorted_students=max(
    students,
    key=lambda x:x[1]
)
print(sorted_students)