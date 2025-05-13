def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def gauss_backward_interpolation(x, y, value):
    n = len(x)
    h = x[1] - x[0] 

    diff_table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        diff_table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            diff_table[i][j] = diff_table[i][j - 1] - diff_table[i - 1][j - 1]

    p = (value - x[-1]) / h
    result = y[-1]
    p_term = 1

    print("Backward Difference Table:")
    for i in range(n):
        print("\t".join(f"{diff_table[i][j]:.2f}" for j in range(i + 1)))

    for i in range(1, n):
        p_term *= (p + (i - 1))
        result += (p_term * diff_table[n - 1][i]) / factorial(i)

    return result

x_vals = [10, 20, 30, 40, 50]
y_vals = [15, 24, 40, 60, 85]
x_interp = 47

interpolated_value = gauss_backward_interpolation(x_vals, y_vals, x_interp)
print(f"\nInterpolated value at x = {x_interp} is {interpolated_value:.4f}")
