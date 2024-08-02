"""Se tiene una matriz nxn de enteros, crear una funci ́on que
retorne un arreglo cuyo primer elemento es la cantidad de
n ́umeros que aparecen solo una vez y cuyo segundo elemento
la cantidad de t ́erminos repetidos.
"""

def count_repeat_and_not_repeat_matrix(matrix: map) -> list:
    no_repeat = []
    repeat = set()

    total_vector = []
    for vector in matrix:
        total_vector += vector
        
    # print(total_vector)

    for value in total_vector:
        count = 0
        # print(f"current value is: {value}")
        for i in range(len(total_vector)):
            if value == total_vector[i]:
                count += 1
        
        if count > 1:
            # print(f"{value} is repeat number")
            repeat.add(value)
        
        elif count == 1:
            # print(f"{value} is not repeat number")
            no_repeat.append(value)
            
    answer =[len(no_repeat), len(repeat)]
    return answer


matrix_1 = [[2, 1, 3],[4, 5, 2], [6, 6, 6]]

matrix_2 = [[2,2],[2,2]]

matrix_3 = [[2, 1, 3, 5],[4, 5, 2, 10], [6, 6, 6, 7], [12, 10, 15, 7]]

matrix_4 = [[2, 1, 3, 5, 4],[4, 5, 2, 10, 2], [6, 6, 6, 7, 7], [12, 10, 15, 7, 13], [16, 20, 15, 8, 9]]

print(count_repeat_and_not_repeat_matrix(matrix_1))
print(count_repeat_and_not_repeat_matrix(matrix_2))
print(count_repeat_and_not_repeat_matrix(matrix_3))
print(count_repeat_and_not_repeat_matrix(matrix_4))

 


    
