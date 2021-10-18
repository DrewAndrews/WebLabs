from math import pi
import numpy as np


# 1
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


# 2
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


# 3
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