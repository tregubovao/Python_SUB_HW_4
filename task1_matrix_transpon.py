# Напишите функцию для транспонирования матрицы 
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


""" вариант 1 """ 

import os
os.system('cls')

base_matrix = [[1, 2, 3, 8], [4, 5, 6, 9], [14, 15, 16, 19]]
transp_matrix = []

for column in range(len(base_matrix[0])):        #  кол-во столбцов первой матрицы (строк новой)
    new_matrix_str = []                     
    for string in range(len(base_matrix)):       #  кол-во строк первой матрицы (столбцов новой)        
        new_matrix_str.append(base_matrix[string][column])
    transp_matrix.append(new_matrix_str)
print(transp_matrix)


""" вариант 2 """  
print(list(zip(*base_matrix)))