def f(x):
    return x**3 - x - 2  

def f_prime(x):
    return 3*x**2 - 1 

def newton_raphson(x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson method to find the root of a function f(x)

    Parameters:
    x0        : Initial guess
    tol       : Tolerance level
    max_iter  : Maximum iterations

    Returns:
    Approximate root or None if it doesn't converge
    """
    print(f"{'Iteration':>10} | {'x_n':>12} | {'f(x_n)':>12}")
    print("-" * 40)

    for i in range(max_iter):
        fx = f(x0)
        fpx = f_prime(x0)

        if abs(fpx) < 1e-12:
            print("Derivative too small; stopping to avoid division by zero.")
            return None

        x1 = x0 - fx / fpx

        print(f"{i+1:10d} | {x1:12.6f} | {f(x1):12.6f}")

        if abs(x1 - x0) < tol:
            print("\nConverged to a root.")
            return x1

        x0 = x1

    print("\nDid not converge within the maximum number of iterations.")
    return None

initial_guess = 1.5
root = newton_raphson(initial_guess)
if root is not None:
    print(f"\nApproximate root: {root:.6f}")
