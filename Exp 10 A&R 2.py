import eyes17.eyes
p = eyes17.eyes.open()
from pylab import *

print("sq - square\nsi - sine\nco - cosine")
f = 0
n=0
while (not n):
	while not f:
		a = str(input("Enter the function you want to generate:"))
		if a in ['sq','si','co']:
			f = 2
	b = float(input("Enter the frequency of the function you want to generate:"))
	if a == 'sq':
		b1 = int(b)
		p.set_sqr1(b1)
		x,y = p.capture1('A1',b1//2,1000)
		plot(x,y)
	elif a in ['si','co']:
		b1 = int(b)
		p.set_sine(b1)
		if a == 'si':
			x,y = p.capture1('A2',b1//2,1000)
			plot(x,y)
		else:
			x,y = p.capture1('A3',b1//2,1000)
			plot(x,y)
	show()
	n = input("Do you want to repeat the experiment, then press enter, otherwise press any other letter and then enter:")
	f = 0
