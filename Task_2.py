#Task_2
A = [[4, 2, 0],
     [1, 3, 2],
     [-1, 3, 10]]
print(f"Вихідна матриця:\n{A}")
A[0], A[1] = A[1], A[0]
print(f"Поміняли перший та другий рядок місцями:\n{A}")


for i in range(len(A[1])):
     A[1][i] += A[0][i] * (-4)
     A[2][i] += A[0][i]
print(f"До 2-го рядка додали 1-ший, помножений на -4; до третього рядка додали 1-ший:\n{A}")

for i in range(len(A[1])):
     A[1][i] = A[1][i] / (-2)
     A[2][i] = A[2][i] / 6
print(f"Другий рядок поділили на -2, третій рядок поділили на 6:\n{A}")

A[1], A[2] = A[2], A[1]
print(f"Поміняли другий та третій рядки місцями:\n{A}")

for i in range(len(A[1])):
     A[2][i] += A[1][i] * (-5)
print(f"До 3-тього рядка додали 2-гий, помножений на -5:\n{A}")
