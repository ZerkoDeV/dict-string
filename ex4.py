eren = {
    "name": "Eren",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0],
}
mikasa = {
    "name": "Mikasa",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0],
}
armin = {
    "name": "Armin",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0],
}

students = [eren,mikasa,armin]

for student in students:
    print(student['name'])
    print(student['homework'])
    print(student['quizzes'])
    print(student['tests'])

average = lambda numbers : sum(numbers)/len(numbers)

get_average = lambda student : (average(student['homework'])*10/100) + (average(student['quizzes'])*30/100) +(average(student['tests'])*60/100)

get_letter_grade = lambda score : 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70  else 'D' if score >= 60 else 'F'

get_class_average = lambda students : average([get_average(student) for student in students])

print('Class average:'+str(get_class_average([armin,eren,mikasa])))
print('Class average:'+str(get_letter_grade(get_class_average([armin,mikasa,eren]))))