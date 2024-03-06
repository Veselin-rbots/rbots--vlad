def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines

n = int(input())

students_grades_lines = input_to_list(n)

student_grades = {}

def avg(values):
    return sum(values) / len(values)

for line in students_grades_lines:
    student, grade = line.split(' ')
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(float(grade))

# print(student_grades)

for(student, grade) in student_grades.items():
    grade_string = ' '.join(map(lambda grade: f'{grade:.2f})', grade))
    avg_grade = avg(grade)
    print(f'{student} -> {grade_string} (avg: {avg_grade:.2f})')