'''
Finding the Largest or Smallest N Items
Problem:
You want to make a list of the largest or smallest N items in a collection.
'''

import heapq

# Example 1
nums = [1, 8, 56, 45, 32, 5, 70, 23, 12, 6, 4, 34, 16, 35, 76, 50]
print(heapq.nlargest(3, nums))  # [76, 70, 56]
print(heapq.nsmallest(3, nums))  # [1, 4, 5]


# Example 2
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
print(cheap)
# [{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}]
print(expensive)
# [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]


# Discussion
print('nums: ', nums)
heap = list(nums)
heapq.heapify(heap)
print('sort nums:', heap)

# Also 3 smallest numbers
print(heapq.heappop(heap), heapq.heappop(heap), heapq.heappop(heap))
