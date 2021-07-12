import operator

class semigroup():
	
	def __init__(self, s, op):
		self.s = s
		self.op = op
		for si in s:
			for sj in s:
				for sk in s:
					if op()


op = operator.mul
op1 = operator.sub