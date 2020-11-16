#Для вычисления производной воспользуемся библиотекой SymPy
from sympy import * 

def Function(x):
    return x**3 

def Extremum(a, b, *, func):
    x = symbols('x') #создаём/определяем символьные переменные, от которых зависит функция
    y = func(x)
    y_pr = y.diff(x) #берём первую производную по x от заданной функции
    
    deriv_func = lambdify(x, y_pr) #этот модуль даёт возможность преобразовать продиффиринцированную функцию к выражению, которое можно использовать для вычисления числовых значений (нашла на просторах интернета)
    
    i = a
    step = 0.1 
    
    while i <= b:
        deriv_val = round(deriv_func (i), 2)
        if deriv_val == 0: 
            if deriv_func (i - step) > 0 and deriv_func (i + step) < 0:
                print("local_max is", end =' ') 
            if deriv_func (i - step) < 0 and deriv_func (i + step) > 0:
                print("local_min is", end =' ') 
            if deriv_func (i + step) < 0 and deriv_func (i - step) < 0:
                print("tochka_peregiba", end =' ') 
            if deriv_func (i + step) > 0 and deriv_func (i - step) > 0:
                print("tochka_peregiba", end =' ')    
            return round(Function(i), 2)   
        i = i + step
    return None

result = Extremum(-10, 10, func = Function)
print(result)

result = Extremum(-20, -10, func = Function)
print(result) 