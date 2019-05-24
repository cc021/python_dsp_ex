#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
from matplotlib import pyplot

'a*cos(x) + b*sin(x) = m*cos(x+theta)'

XX_CNT = 511
XX = [0 for i in range(XX_CNT)]

fs = 20 #khz
f1 = 1 #khz
f2 = 5 #khz
f3 = 6 #khz
ts = 1 / fs

sig1 = [0 for i in range(XX_CNT)]
sig2 = [0 for i in range(XX_CNT)]

def sin_gen():
	for i in range(XX_CNT):
		sig1[i] = 10*math.sin(2 * math.pi * f1 * i * ts)
		sig2[i] = 20*math.cos(2 * math.pi * f1 * i * ts)
		XX[i] = sig1[i] + sig2[i]

	pyplot.subplot(221)
	pyplot.plot(sig1)
	pyplot.subplot(222)
	pyplot.plot(sig2)
	pyplot.subplot(223)
	pyplot.plot(XX)
	pyplot.show()
if __name__ == '__main__':
	sin_gen()
