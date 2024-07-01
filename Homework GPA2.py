grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
gpa = {}
student1 = sum(grades[0]) / len(grades[0])
student2 = sum(grades[1]) / len(grades[1])
student3 = sum(grades[2]) / len(grades[2])
student4 = sum(grades[3]) / len(grades[3])
student5 = sum(grades[4]) / len(grades[4])
gpa.update({students[0]: student1, students[1]: student2, students[2]: student3, students[3]: student4,
            students[4]: student5})
print(gpa)
