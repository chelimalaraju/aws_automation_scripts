import time

def timed_func(func):
	def wrapper():
		t1 = time.time()
		resp = func()
		t2 = time.time()
		t = t2-t1
		print("time taken to execute", t)
		return resp
	return wrapper

@timed_func
def test_sum():
	sum = 0
	for i in range(10000000):
		sum += i
	return sum

#print(test_sum)

#r = test_sum()
#print(r)
#timed_func(test_sum)
