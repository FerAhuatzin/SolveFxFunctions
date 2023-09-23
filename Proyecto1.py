# Imports necesarios
import numpy as np
import sympy as sp
from sympy.abc import x
from sympy import lambdify

# Newton Modificado
def NewtonMod(f, df, ddf, tol, maxIter):
    x0 = float(input("Enter your initial approximation to solve the function: "))
    xn = x0
    for n in range (0, maxIter):
        fxn = f(xn)
        if abs(fxn) < tol:
            print("Found solution after", n, "iterations.")
            return xn
        dfxn = df(xn)
        ddfxn = ddf(xn)
        denom = dfxn**2 - fxn * ddfxn
        if denom == 0:
            print("Failed to found solution.\n")
            return None
        xn = xn - fxn * dfxn/denom
        xn - fxn * dfxn/(dfxn**2 - fxn*ddfxn)
    print("Exceed maximum iterations. No solution found.")
    return None

# Bisección
def my_bisection(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception ("The scalars a and b do not bound a root")
    
    m = (a + b)/2
    
    if np.abs(f(m))<tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, tol) 
    elif np.sign(f(b)) == np.sign(f(m)) :
        return my_bisection (f, a, m, tol)
    
# Newton
def newton(f,Df,tol,max_iter):
    x0 = float(input("Enter your initial approximation to solve the function: "))
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < tol:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

# Newtonsecant
def secant(f, a, b, tol, maxIter):
    # El método de la secante no se puede aplicar
    if f(a) * f(b) >= 0:
        print('El método de la secante no se puede aplicar')
        return None
    
    # El método de la secante 
    for n in range(maxIter + 1):
        # Cálculo de la secante
        x_n = a - f(a)*(b - a)/(f(b) - f(a))
        
        if abs(f(x_n)) < tol:
            return x_n
        
        if f(a) * f(n) < 0:
            b = x_n
        else:
            a = x_n
    print('Found solution after',n,'iterations.')
    return x_n

# Función para tomar el input y derivarlo dos veces
def userInput():
    
    x = sp.symbols('x')  # Define el símbolo 'x' para las operaciones simbólicas
    flag = False
    while flag==False:
        try:
            
            user_function = input("Enter a function in terms of 'x' (e.g., x**2-2): ")  # Solicita el input de la función
            
            function = sp.sympify(user_function)  # Convierte el input del usuario en una función
            
            # Deriva la función en su primera y segunda derivada
            first_derivative = sp.diff(function, x)
            second_derivative = sp.diff(first_derivative, x)
            
            print(type(first_derivative))
        
            # Imprime los resultados
            print("Original function: ", function)
            print("First derivative: ", first_derivative)
            print("Second derivative :", second_derivative)
            flag = True
            return user_function, first_derivative, second_derivative
    
        except ValueError:
            raise SyntaxError('Not valid function')
# Llama la función userInput y asigna los return en variables temporales
ft, dft, ddft = userInput()

# Convierte las temporales en funciones evaluables
f = lambdify(x, ft)
df = lambdify(x, dft)
ddf = lambdify(x, ddft)

# Y ya el menú q habíamos hecho para escoger el método
while True:
    print("""
    1.Use Bisection method
    2.Use Newton method
    3.Use Modified Newton method
    4.Use Secant method
    5.Solve another function
    6.Exit/Quit
    """)
    ans = input("What would you like to do? ")
    if ans=="1":
        a = float(input("Enter the bottom limit for the interval: "))
        b = float(input("Enter your top limit for the interval: "))
        root = my_bisection(f, a, b, 0.0001)
        print("Solution using Bisection method: ", root)
    elif ans=="2":
        estimate = newton(f, df, 1e-6, 10)
        print("Solution using Newton method: ", estimate)
    elif ans=="3":
        estimate = NewtonMod(f, df, ddf, 1e-6, 10)
        print("Solution using Modified Newton method: ", estimate)
    elif ans=="4":
        a = float(input("Enter the bottom limit for the interval: "))
        b = float(input("Enter your top limit for the interval: "))
        root = secant(f, a, b, 1e-6, 10)
        print("Solution using Secant method: ", root)
    elif ans=="5":
        # Llama la función userInput y asigna los return en variables temporales
        ft, dft, ddft = userInput()

        # Convierte las temporales en funciones evaluables
        f = lambdify(x, ft)
        df = lambdify(x, dft)
        ddf = lambdify(x, ddft)
    elif ans=="6":
        print("\n Goodbye.") 
        break
    else:
       print("\n Not valid choice. Try again.")