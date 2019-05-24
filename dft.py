#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
from matplotlib import pyplot

__doc__ = 'dft function'

def dft(x, cnt, y_rex, y_imx):
	dft_cnt = (int(cnt / 2) + 1)
	print('dft_cnt', dft_cnt)
	for k in range(dft_cnt):
		y_rex[k] = 0
		y_imx[k] = 0
		for i in range(cnt):
			y_rex[k] = y_rex[k] + x[i] * math.cos(2*math.pi*k*i/cnt)
			y_imx[k] = y_imx[k] - x[i] * math.sin(2*math.pi*k*i/cnt)

if __name__ == '__main__':
	fs = 20 #khz
	f1 = 1 #khz
	f2 = 5 #khz
	f3 = 6 #khz
	ts = 1 / fs
	point_cnt = 200
	dft_cnt = int(point_cnt / 2) + 1
	sig1 = [0 for i in range(point_cnt)]
	sig2 = [0 for i in range(point_cnt)]
	sig = [0 for i in range(point_cnt)]
	data_i = [0 for i in range(dft_cnt)]
	data_q = [0 for i in range(dft_cnt)]
	pwr = [0 for i in range(dft_cnt)]

	for i in range(point_cnt):
		sig1[i] = 10*math.sin(2 * math.pi * f1 * i * ts)
		sig2[i] = 20*math.cos(2 * math.pi * f2 * i * ts)
		sig[i] = sig1[i] + sig2[i]

	dft(sig, point_cnt, data_i, data_q)

	for i in range(dft_cnt):
		pwr[i] = math.sqrt(math.pow(data_i[i], 2) + math.pow(data_q[i], 2))

	pyplot.subplot(211)
	pyplot.plot(sig)
	pyplot.subplot(212)
	pyplot.plot(pwr)
	pyplot.show()	
