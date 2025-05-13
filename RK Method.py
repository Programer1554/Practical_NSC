def f(x, y):
    return x + y

def runge_kutta(x0, y0, x_end, h):
    x = x0
    y = y0

    print("x\t\t y")
    while x <= x_end:
        print(f"{x:.4f}\t {y:.4f}")

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        x = x + h

x0 = 0   
y0 = 1    
x_end = 1  
h = 0.1  

runge_kutta(x0, y0, x_end, h)
