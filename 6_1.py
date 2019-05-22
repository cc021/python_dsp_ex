#!/usr/bin/python
# -*- coding: UTF-8 -*-
# CONVOLUTION USING THE INPUT SIDE ALGORITHM
import math
from matplotlib import pyplot

X_CNT = 80
X = [0 for i in range(X_CNT)]
H_CNT = 19
H = [0 for i in range(H_CNT)]
Y_CNT = 110
Y = [0 for i in range(Y_CNT)]

H = [
    0.01518110457667, -0.02431432516463, -0.02103250665133, 0.004587997790714,
    0.04381009586372,  0.05379396259255,-0.007467096561861,   -0.135596163305,
    -0.2681320609278,   0.6754609049872,  -0.2681320609278,   -0.135596163305,
  -0.007467096561861,  0.05379396259255,  0.04381009586372, 0.004587997790714,
   -0.02103250665133, -0.02431432516463,  0.01518110457667
]

fs = 20 #khz
f1 = 1 #khz
f2 = 5 #khz
f3 = 6 #khz
ts = 1 / fs
X_CNT = 5*fs

sig1 = []
sig2 = []
sig = [0 for i in range(X_CNT)]

def convolution_input_method():
	for i in range(X_CNT):
		for j in range(H_CNT):
			Y[i+j] = Y[i+j]+X[i]*H[j]

def convolution_output_method(x, y):
	for i in range(X_CNT):
		y[i] = 0
		for j in range(H_CNT):
			if ((i - j) < 0) :
				break
			else :
				y[i] = y[i] + x[i-j]*H[j]

def sin_gen():
	for i in range(X_CNT):
		s = math.sin(2 * math.pi * f1 * i * ts)
		sig1.append(s)
		s = math.sin(2 * math.pi * f2 * i * ts)
		sig2.append(s)
		sig[i] = sig1[i] + sig2[i]

if __name__ == '__main__':
	# convolution_input_method()
	sin_gen()
	out = [0 for x in range(X_CNT)]
	convolution_output_method(sig, out)
	pyplot.subplot(221)
	pyplot.plot(sig1, 'r')
	pyplot.subplot(222)
	pyplot.plot(sig2, 'b')
	pyplot.subplot(223)
	pyplot.plot(sig, 'k')
	pyplot.subplot(224)
	pyplot.plot(out, 'y')
	pyplot.show()
