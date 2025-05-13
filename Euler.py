def f(x, y):
    return x + y

def euler(x0, y0, x_end, h):
    x = x0
    y = y0

    print("x\t\t y")
    while x <= x_end:
        print(f"{x:.4f}\t {y:.4f}")
        y = y + h * f(x, y)
        x = x + h

x0 = 0       
y0 = 1       
x_end = 1    
h = 0.1      

euler(x0, y0, x_end, h)
