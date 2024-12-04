# Дополнительное практическое задание по модулю: "Базовые структуры данных."

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_aaron = (sum(grades[0]) / len(grades[0]))
student_bilbo = (sum(grades[1]) / len(grades[1]))
student_johnny = (sum(grades[2]) / len(grades[2]))
student_khendrik = (sum(grades[3]) / len(grades[3]))
student_steve = (sum(grades[4]) / len(grades[4]))

students = sorted(list(students))
keys = {students[0]: student_aaron, students[1]: student_bilbo, students[2]: student_johnny,
         students[3]: student_khendrik, students[4]: student_steve}
print(keys)

# result:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
