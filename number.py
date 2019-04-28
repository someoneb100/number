from itertools import islice

class prime_generator:
	some_prime_numbers = 2, 3, 5, 7, 11
	def __init__(self):
		self.primes = None
	def __iter__(self):
		for i in prime_generator.some_prime_numbers: yield i
		self.primes = list(prime_generator.some_prime_numbers)
		while True:
			i = i+2
			for j in islice(self.primes, 1, None):
				if i % j is 0: break
				elif j*j > i:
				    self.primes.append(i)
				    yield i
				    break
	def __del__(self):
		if self.primes and len(self.primes) > len(prime_generator.some_prime_numbers):
			prime_generator.some_prime_numbers = tuple(self.primes)


class Number:
	def __init__(self, n):
		self.sign = -1 if n < 0 else 1
		self.value = n * self.sign
		self.factors, self.totient = dict(), 0
		if self.value not in (0,1):
			n, self.totient = self.value, 1
			for i in prime_generator():
				if n is 1: break				
				if i*i > n:
					self.factors[n] = 1
					self.totient *= n-1
					break
				if n % i is 0:
					while n % i is 0:
						self.factors[i] = self.factors.get(i, 0) + 1
						n //= i
					self.totient *= i**(self.factors[i]-1) * (i-1)
			
					
	def __repr__(self):
		return "{}({})".format(self.__class__.__name__, self.value * self.sign)

	def __str__(self):
		if self.value is 0: return "0 = 0"
		if self.value is 1: return str(self.sign) + " = " + str(self.sign)
		s = str(self.sign * self.value) + " = "
		if self.sign is -1: s+= "-1 * "
		for a, b in sorted(self.factors.items()):
			s += str(a)
			if b is not 1: s += '^' + str(b)
			s += " * "
		return s[:-3]

	def is_prime(self):
		return len(self.factors) is 1 and set(self.factors.values()).pop() is 1

