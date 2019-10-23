'''
Unpacking Elements from Iterables of Arbitrary Length
Problem:
You need to unpack N elements from an iterable,
but the iterable may be longer than N elements,
causing a “too many values to unpack” exception.
'''

# Example 1
grades = (4, 5, 3, 4, 5, 4, 4, 3, 5)


def avg(list):
    return sum(list) / len(list)


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


print(drop_first_last(grades))


# Example 2
record = ('Egor', 'ekurito@gmail.com',
          '8-999-9999', '8-777-7777', '8-555-5555')
name, email, *phone_numbers = record
# Egor ekurito@gmail.com ['8-999-9999', '8-777-7777', '8-555-5555']
print(name, email, phone_numbers)


*trailing, current = [10, 20, 13, 45, 34, 54, 60, 80]
print(trailing)  # [10,20,13,45,34,54,60]
print(current)  # 80


# Example 3
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# Example 4
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)  # nobody /var/empty /usr/bin/false

# Example 5
record = ('ABC', 50, 123.45, (10, 3, 2019))
name, *_, (*_, year) = record
print(name, year)  # ABC 2019

# Example 6
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head, *tail = items
print(head, tail)  # 1 [2, 3, 4, 5, 6, 7, 8, 9]

# dont use this in project


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum([1, 2, 3, 4]))
