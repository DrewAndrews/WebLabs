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

---

## Лабораторная №2

Код программы находится в файле lab2.py

1.  Написать класс Sphere для представления сферы в трехмерном пространстве.
```python
class Sphere:
    def __init__(self, r = 1, x = 0, y = 0, z = 0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume_(self):
        return 4 / 3 * self.r**3 * pi

    def get_square_(self):
        return 4 * pi * self.r**2

    def get_radius_(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius_(self, r):
        self.r = r

    def set_center_(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside_(self, x, y, z):
        return (x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2 <= self.r**2
```

2. Написать класс Matrix, который будет прообразом математического объекта(для простоты квадратная матрица). Определить для него методы сравнения на основе детерминанта этой матрицы - если детерминант первой матрицы больше, то и матрица больше. Для остальных операций аналогично. Так же реализовать операции сложения, умножения двух матриц.
```python
class Matrix:
    def __init__(self, *args):
        self.mat = np.array(args)

    def __eq__(self, mat):
        return np.linalg.det(self.mat) == np.linalg.det(mat)

    def __lt__(self, mat):
        return np.linalg.det(self.mat) < np.linalg.det(mat)

    def __add__(self, mat):
        return self.mat + mat

    def __mul__(self, mat):
        return np.dot(self.mat, mat)
```

3.  Написать класс, который будет является http клиентом. Что подразумевается под клиентом:
-  Используется библиотека requests
-  при инициализации класса создается сессия (https://docs.python-requests.org/en/master/user/advanced/, https://pythonru.com/biblioteki/prodvinutoe-rukovodstvo-po-biblioteke-python-requests), и передается host для запросов
-  в деструкторе класса, созданная сессия закрывается(метод у сессии close)
-  задаются заголовки для сессии при помощи метода класса, путем изменения поля объекта класса
-  поддерживаются методы get, post - в данные методы передаются путь и query_params. Внутри этих методов происходит отправка запросов и обработка статусов. Если статус отличный от 200 методы возвращают None, если статус 200, возвращается тело ответа

```python
import requests


class Client:
    def __init__(self, host):
        self.session = requests.Session()
        self.host = host

    def __del__(self):
        self.session.close()

    def set_headers(self, headers):
        self.session.headers = headers

    def get(self, path, query):
        response = self.session.get(self.host + path, params=query)
        if response.status_code == 200:
            return response.content
        return None

    def post(self, path, query):
        response = self.session.post(self.host + path, data=query)
        if response.status_code == 200:
            return response.content
        return None

client = Client('https://api.github.com')
print(client.get('/search/repositories', query={'q': 'requests+language:python'}))
```