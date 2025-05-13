def stirling_interpolation(x_values, y_values, x):
    n = len(x_values)
    h = x_values[1] - x_values[0]

    mid = n // 2
    a = x_values[mid]
    u = (x - a) / h

    diff_table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        diff_table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    y_interp = y_values[mid]
    y_interp += (u * (diff_table[mid][1] + diff_table[mid - 1][1])) / 2
    y_interp += (u**2 * diff_table[mid - 1][2]) / 2

    return y_interp

x_vals = [1, 2, 3, 4, 5]
y_vals = [1, 8, 27, 64, 125] 

x_to_find = 3.2
result = stirling_interpolation(x_vals, y_vals, x_to_find)

print(f"Interpolated value at x = {x_to_find} is approximately: {result}")
