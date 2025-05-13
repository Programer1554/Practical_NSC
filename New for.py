def newton_forward_interpolation(x_values, y_values, x_to_interpolate):
    n = len(x_values)
    diff_table = [[0] * n for _ in range(n)]
    for i in range(n):
        diff_table[i][0] = y_values[i]
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i+1][j-1] - diff_table[i][j-1]
    print("Forward Difference Table:")
    for row in diff_table:
        print([round(val, 4) for val in row])
    h = x_values[1] - x_values[0]  # assume uniform spacing
    p = (x_to_interpolate - x_values[0]) / h
    result = y_values[0]
    p_term = 1
    factorial = 1
    for i in range(1, n):
        p_term *= (p - i + 1)
        factorial *= i
        result += (p_term * diff_table[0][i]) / factorial
    return result
x_vals = [1, 2, 3, 4]
y_vals = [1, 8, 27, 64]
x_interp = 2.5
result = newton_forward_interpolation(x_vals, y_vals, x_interp)
print(f"\nInterpolated value at x = {x_interp} is {round(result, 4)}")
