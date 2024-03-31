#This is for the SEE-Lab Experiment-2 where the time starts when the magnet is dropped.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import random
import math

# Define the form of the function you want to fit
def func(x,a,b):
    N = 3000; A = math.pi*(0.013/2)**2; uo = 10**(-7)*4*math.pi; l = (1.05 * 10**(-2))/2
    g = 9.8; R = (0.597e-2)/2; zo = 24e-2
    term1 = - N * A * a * uo*g*((x-b)*10**(-3))/4 * math.pi * l
    term2 = ((R**2 + (-zo + 0.5 * g * ((x-b)*10**(-3))**2 + l)**2) ** (-1.5) -
        (R**2 + (-zo + 0.5 * g * ((x-b)*10**(-3))**2 - l)**2) ** (-1.5))
    emf = term1 * term2
    return emf

# Generate some data based on the function
l=[0.5*i for i in range(0,600)]
x=np.array(l, dtype='float64')
l2=[random.randint(-167,167)*0.0001 for i in range(0,434)]
l2.extend([math.tan(i*math.pi/14.5) for i in range(0,6)])
l2.extend([i/3 for i in range(5,0,-1)])
l2.extend([-i/3 for i in range(0,6)])
l2.extend([math.tan(-(i*math.pi/14.5)) for i in range(5,0,-1)])
l2.extend([random.randint(-167,167)*0.0001 for i in range(456,600)])
y=np.array(l2, dtype = 'float64')


params, params_covariance = curve_fit(func, x, y)
print(params[:])
print("Error in the estimation of the magnetic moment of the magnet is",np.sqrt(np.diag(params_covariance))[:])
yf = func(x,params[0],params[1])

plt.figure(figsize=(6, 4))
plt.plot(x, y,'o', label='Data')
plt.plot(x, yf, color='red', label='Fitted function')

plt.legend(loc='best')
plt.show()