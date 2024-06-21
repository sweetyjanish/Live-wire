import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import Rbf

xs = np.arange(10)
ys = 2*xs + 1

#1d interpolation
interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

#spline interpolation
#ys = xs**2 + np.sin(xs) + 1
interp_func = UnivariateSpline(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

#Interpolation with Radial Basis Function
#ys = xs**2 + np.sin(xs) + 1
interp_func = Rbf(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)