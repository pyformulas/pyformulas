"""
Plots a graph
"""

import pyformulas as pf
import numpy as np

x = np.linspace(-10,10,100)
y = x**2 + x*np.e**(np.cos(x)**2)
pf.plot(x, y, color='darkgrey')