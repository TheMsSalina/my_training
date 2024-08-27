def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([]) #кол-во строк
        for j in range(m):
            matrix[i].append(value) #кол-во столбцов

    if n <= 0 and m <= 0:
        matrix = []
    return matrix #если n и m <=0, остановить выполнение ф-ии
get_matrix(2, 2, 10)

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)