grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(list(students))

a = len(grades[0])
b = len(grades[1])
c = len(grades[2])
d = len(grades[3])
e = len(grades[4])

averagea = sum(grades[0]) / a
averageb = sum(grades[1]) / b
averagec = sum(grades[2]) / c
averaged = sum(grades[3]) / d
averagee = sum(grades[4]) / e

average = [averagea, averageb, averagec, averaged, averagee]
u = list(zip(students, average))
u = dict(u)
print(u)


