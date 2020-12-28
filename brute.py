# brute forces a password and then tells you how long it took.

import time

def timer(func):
	def wrapper(*args, **kwargs):
		tic = time.perf_counter()
		value = func(*args, **kwargs)
		toc = time.perf_counter()
		elapsed_time = toc - tic
		print(f"Function took {elapsed_time:0.4f} seconds")
		return value
	return wrapper

@timer
def force(target: str) -> str:
	


