"""
Consider the 2D array below and display the summation of their diagonal elements
[[10,12,15], [14,18,21], [2,3,4]]
"""

def sum_up_diagonals(li):
    index = len(li)
    first_dia = sum(li[i][i]for i in range(index))
    second_dia = sum(li[i][index-i-1]for i in range(index))
    return (first_dia,second_dia)

matrix_val=[[10,12,15], [14,18,21], [2,3,4]]
sum_dia_1, sum_dia_2 = sum_up_diagonals(matrix_val)

print(sum_dia_1,sum_dia_2)


