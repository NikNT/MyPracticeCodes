# sort() method - used with lists
# sorted() function - user with iterables

# list of strings
students = [
    "Squidward",
    "Sandy",
    "Patrick",
    "Spongebob",
    "Mr. Krabs"
]

students.sort(reverse=True)

for student in students:
    print(student)

# tuple of strings
students_2 = (
    "Squidward",
    "Sandy",
    "Patrick",
    "Spongebob",
    "Mr. Krabs"
)

sorted_students_2 = sorted(students_2)
for student in sorted_students_2:
    print(student)


# list of tuples
students_3 = [("Squidward", "F", 60),
              ("Sandy", "A", 33),
              ("Patrick", "D", 36),
              ("Spongebob", "B", 20),
              ("Mr. Krabs", "C", 78)]

grade = lambda grades : grades[1]
students_3.sort(key=grade,reverse=True)
for student in students_3:
    print(student)

# tuple of tuples
students_4 = (("Squidward", "F", 60),
              ("Sandy", "A", 33),
              ("Patrick", "D", 36),
              ("Spongebob", "B", 20),
              ("Mr. Krabs", "C", 78))

age = lambda students : students[2]
sorted_students_4 = sorted(students_4, key=age)
print(sorted_students_4)