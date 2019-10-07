'''
Task:
You have an N-element tuple or sequence that you would like to unpack
into a collection of N variables.
'''

p = (10, 15)
x, y = p
print(x, y)  # x = 10, y = 15

data = ['ABC', 50, 10.99, (2019, 10, 3)]
name, count, price, date = data
print(name, count, price, date)  # name = 'ABC', count = 50, etc.

name, count, price, (year, mon, day) = data
print(year, mon, day)  # year = 2019, mon = 10, day = 3

_, count, price, _ = data
print(count, price)  # _ does not exist

s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)  # H e l l o

data = {'first': 1, 'second': 'second'}
x, y = data.values()
c, d = data
print(x, y)  # x = 1, y = 'second'
print(c, d)  # c = 'first', d = 'second'
