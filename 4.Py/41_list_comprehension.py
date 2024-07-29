# list = [expression for item in iterable]

squares = []
for number in range(1, 11):
    square = number * number
    squares.append(square)
print(squares)

squares_list = [number * number for number in range(1,11)]
print(squares_list)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 4, 3, 2, 1]
passed = [student if student >= 40 else 'failed' for student in students]
print(passed)