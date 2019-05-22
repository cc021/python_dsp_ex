#!/usr/bin/python
# -*- coding: UTF-8 -*-
# calculation of the mean and standard deviation
import math

X = []
FS = 10
N = 5*FS

def sin_gen():
	for i in xrange(N):
		s = math.sin(2 * math.pi * i / FS)
		X.append(s)

def test():
	sin_gen()
	mean = 0

	for xi in X:
		mean = mean + xi

	mean = mean / N
	print 'mean=', mean

	variance = 0
	for xi in X:
		variance = variance + math.pow(xi - mean, 2)
	variance = variance / (N - 1)

	sd = math.sqrt(variance)
	print 'sd=', sd
	print X, len(X)

if __name__ == '__main__':
	test()

