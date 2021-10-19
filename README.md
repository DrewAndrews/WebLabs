# Лабораторные по дисциплине Веб программирование

## Лабораторная №1

Код программы находится в файле lab1.py

1.  Написать функцию, которая на вход принимает int и возвращает true или false в зависимости является ли это число палиндром. Число является палиндромом, если оно читается справа налево и слева направо одинаково (25)
 
```python
def is_pallindrome(number):
    return str(number) == str(number)[::-1]
```

> **Input**:
    1221
<br/> **Output**:
    True
    
2.  Написать функцию, которая принимает на вход список из положительных целочисленных элементов и возвращает три списка: (25)

```python
def three_lists(numbers):
    is_divided_by_two = [x for x in numbers if x % 2 == 0]
    is_divided_by_three = [x for x in numbers if x % 3 == 0]
    is_divided_by_five = [x for x in numbers if x % 5 == 0]
    return is_divided_by_two, is_divided_by_three, is_divided_by_five
```

> **Input**:
    [1, 2, 3, 4, 5, 6]
<br/> **Output**:
    ([2, 4, 6], [3, 6], [5])
    
3.  Написать функцию, принимающую на вход int, и число, обратное этому int (25)

```python
def get_reversed(number):
    if number > 0:
        return str(number)[::-1].strip("0")
    return f"-{str(abs(number))[::-1].strip('0')}"
```

> **Input**:
    12345
<br/> **Output**:
    54321
    
4.  Написать функцию, которая будет расчитывать квадратный корень n-ой степени методом Ньютона 

```python
def root_by_n_pow(x, n):
    x0 = 1
    while True:
        xk = 1 / n * ((n - 1) * x0 + x / x0**(n - 1))
    if xk == x0:
        return xk
    else:
        x0 = xk
```

> **Input**:
    12345
<br/> **Output**:
    54321
    
 5.  Написать функцию, принимающую 1 аргумент — число от 0 до 100000, и возвращающую true, если оно простое, false если нет. (35)
 
 ```python
def is_prime(number):
    for i in range(2, int(number**0.5)):
        if number % i == 0:
            return False
    return True
```

> **Input**:
    123456
<br/> **Output**:
    False
    
 6.  Написать декоратор, который будет кэшировать результат вызова функции и отдавать его при последующих вызовах данной функции (для тех, кто был на семинаре, но не обязательно - можете посмотреть как работают декораторы, 50).
Усложненный вариант - написать тот же самый декоратор, но с параметром, который будет показывать сколько раз отдавать кешируемый результат. Если данный счетчик обнуляется, то выполняем функцию и вновь кешируем ее результат. (54)

```python
def get_cache_hard(count_of_returns):
    def decorator(func):
        cache = {}
        func.invocations = count_of_returns
        cache[func.__name__] = func()
        def wrapper():
            if func.invocations > 0:
                func.invocations -= 1
            if func.invocations == 0:
                cache[func.__name__] = func()
                return cache[func.__name__]
            return cache[func.__name__]
		return wrapper
	return decorator

@get_cache_simple
def some_func():
    return "String"

count_of_returns = 3
@get_cache_hard(count_of_returns)
def another_func():
    return "String"
```

## Лабораторная №2

Код программы находится в файле 
