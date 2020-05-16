import numpy as np
from numpy import e, pi, sin, exp, cos
import matplotlib.pyplot as plt
def f(t):
    return 2*exp(-t) * cos(2*pi*t)
def fp(t):
    return 10*pi * exp(-t) * sin(2*pi*t) - e**(-t)*cos(2*pi*t)
def g(t):
    return 2*sin(t) * cos(1/(t+0.1))
def g(t):
    return sin(t) * cos(1/(t))

fig = plt.figure(figsize=(6, 4))
t = np.arange(-5.0, 1.0, 0.1)
sub1 = fig.add_subplot(221) 
sub1.set_title('The function f') 
sub1.plot(t, f(t))
sub2 = fig.add_subplot(222)
sub2.set_title('fp, the derivation of f')
sub2.plot(t, fp(t))
t = np.arange(-3.0, 2.0, 0.02)
sub3 = fig.add_subplot(223)
sub3.set_title('The function g')
sub3.plot(t, g(t))
t = np.arange(-0.2, 0.2, 0.001)
sub4 = fig.add_subplot(224)
sub4.set_title('A closer look at g')
sub4.set_xticks([-0.2, -0.1, 0, 0.1, 0.2])
sub4.set_yticks([-0.15, -0.1, 0, 0.1, 0.15])
sub4.plot(t, g(t))
plt.plot(t, g(t))
plt.tight_layout()
plt.show()
