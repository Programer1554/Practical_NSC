def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def gauss_forward_interpolation(x, y, value):
    n = len(x)
    h = x[1] - x[0] 

    diff_table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        diff_table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]
)
    mid_index = min(range(n), key=lambda i: abs(x[i] - value))
    p = (value - x[mid_index]) / h

    print("Central Difference Table:")
    for i in range(n):
        print("\t".join(f"{diff_table[i][j]:.2f}" for j in range(n - i)))

    result = diff_table[mid_index][0]
    p_term = 1
    sign = 1
    for i in range(1, n):
        if i % 2 != 0:
            index = mid_index - (i // 2)
        else:
            index = mid_index - (i // 2)
        if index < 0 or index + i >= n:
            break
        p_term *= (p - ((i - 1)//2)) if i % 2 != 0 else (p + (i//2))
        result += (p_term * diff_table[index][i]) / factorial(i)

    return result

x_vals = [10, 20, 30, 40, 50]
y_vals = [15, 24, 40, 60, 85]
x_interp = 32

interpolated_value = gauss_forward_interpolation(x_vals, y_vals, x_interp)
print(f"\nInterpolated value at x = {x_interp} is {interpolated_value:.4f}")
