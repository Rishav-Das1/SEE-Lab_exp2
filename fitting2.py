import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math


def func(t,m,b):
    N = 3000; A = math.pi*(0.013/2)**2; uo = 10**(-7)*4*math.pi; l = (1.05 * 10**(-2))/2
    g = 9.8; R = (0.597e-2)/2; zo = 11.5e-2
    term1 = - N * A * m * uo*g*((t-b)*10**(-3))/4 * math.pi * l
    term2 = ((R**2 + (-zo + 0.5 * g * ((t-b)*10**(-3))**2 + l)**2) ** (-1.5) -
        (R**2 + (-zo + 0.5 * g * ((t-b)*10**(-3))**2 - l)**2) ** (-1.5))
    emf = term1 * term2
    return emf

data = np.loadtxt('C:/Users/risha/SEE-Lab_exp2/1st')


x = data[:, 0]
y = data[:, 1]

x=x+50

params, params_covariance = curve_fit(func, x, y)
print(params[0])
print("Error in the estimation of the magnetic moment of the magnet is",np.sqrt(params_covariance[0][0]))
yf = func(x,*params)

plt.figure(figsize=(6, 4))
plt.plot(x, y,'o', label='Data')
plt.plot(x, yf, color='red', label='Fitted function')

plt.legend(loc='best')
plt.show()