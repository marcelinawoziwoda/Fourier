from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

parametr = 1.420
T=2
w=np.pi

def f(t):
  return parametr*t**2

def fa1(t):
  return f(t)*np.cos(w*t)

def fa2(t):
  return f(t)*np.cos(2*w*t)

a0=1/T*quad(f, -1, 1)[0]
a1=2/T*quad(fa1, -1, 1)[0]
a2=2/T*quad(fa2, -1, 1)[0]

print("a0=",a0)
print('a1=',a1)
print('a2=',a2)

def F(t):
  return a0+a1*np.cos(np.pi*t)+a2*np.cos(2*np.pi*t)

t=np.linspace(-1, 1, 100)
fig, ax=plt.subplots()
ax.plot(t,f(t),t,F(t))
ax.grid(True)
plt.show()

