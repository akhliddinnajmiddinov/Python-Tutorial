from cachetools import cached, LRUCache

cache = LRUCache(maxsize=3)

@cached(cache)
def expensive_computation(x):
	print(x)
	return x ** 2


expensive_computation(2)
expensive_computation(2)
expensive_computation(3)
expensive_computation(3)
expensive_computation(4)
expensive_computation(4)
expensive_computation(5)
expensive_computation(5)
expensive_computation(2)