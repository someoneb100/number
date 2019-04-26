from isqrt import isqrt
from itertools import islice

class Number:
	some_prime_numbers = [2, 3, 5, 7, 11]

	@classmethod
	def prime_generator(cls):
		for i in cls.some_prime_numbers: yield i
		while True:
			check, i = isqrt(i+2), i+2
			for j in islice(cls.some_prime_numbers, 1, None):
				if j > check:
					cls.some_prime_numbers.append(i)
					yield i
					break
				elif i % j is 0: break


	def __init__(self, n):
		self.sign = -1 if n < 0 else 1
		self.value = n * self.sign
		self.factors, self.totient = dict(), 0
		if self.value not in (0,1):
			n, check, self.totient = self.value, isqrt(self.value), 1
			for i in Number.prime_generator():
				if n is 1: break				
				if i > check:
					self.factors[n] = 1
					self.totient *= n-1
					break
				if n % i is 0:
					while n % i is 0:
						self.factors[i] = self.factors.get(i, 0) + 1
						n //= i
					self.totient *= i**(self.factors[i]-1) * (i-1)
					check = isqrt(n)
			
					
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
		return True if len(self.factors) is 1 and set(self.factors.values()).pop() is 1 else False

