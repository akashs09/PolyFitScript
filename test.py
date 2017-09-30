
import numpy as np
from numpy import random
from pylab import *
from sklearn.metrics import r2_score

np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)

# purchaseAmount function (non-linear)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

polyfitInit = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0}

for c in polyfitInit:
    z = np.poly1d(np.polyfit(x, y, c))
    r2 = r2_score(y, z(x))
    polyfitInit[c] = r2

print "Highest Degree Polynomial: ",max(polyfitInit, key=polyfitInit.get), '\n'"R-sqr vale: ", polyfitInit.get(max(polyfitInit, key=polyfitInit.get))
