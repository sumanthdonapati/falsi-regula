# -*- coding: utf-8 -*-
"""falsi_regula.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nxTWzpnuOM0uJJ-TVCL_DNHh8YY3xCwC
"""

#falsi regula method
import numpy as np
import matplotlib.pyplot as plt
def f(x):
  v = (x**3)-x-4 #(np.e**x)*np.sin(x)-1
  return v

for i in range(0,1000):
  if f(i)*f(i+1)<0:
    a=i
    b=i+1
    break;
p1=a
p2=b
print(p1,p2)
if f(a)>0:
  j=0.000001
else:
  j=-0.000001

i=1
while f((a*f(b)-b*f(a))/(f(b)-f(a)))<j:
  a = (a*f(b)-b*f(a))/(f(b)-f(a))
  print("interation",i,"=>",str(round(a, 5)),str(round(f(a), 5)))
  i=i+1

