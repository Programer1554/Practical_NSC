def divided_diff(x, y, n):
    """Construct the divided difference table"""
    table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

    return table

def newton_divided_difference(x, y, value):
    n = len(x)
    table = divided_diff(x, y, n)

    result = table[0][0]
    product_term = 1.0
    for i in range(1, n):
        product_term *= (value - x[i - 1])
        result += table[0][i] * product_term

    return result

x_vals = [5, 6, 9, 11]
y_vals = [12, 13, 14, 16]  

x_interp = 7

result = newton_divided_difference(x_vals, y_vals, x_interp)
print(f"Interpolated value at x = {x_interp} is: {result}")
