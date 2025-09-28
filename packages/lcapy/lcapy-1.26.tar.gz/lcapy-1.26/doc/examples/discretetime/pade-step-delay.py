import numpy as np
from matplotlib.pyplot import subplots, style, savefig, show

from lcapy import *

H = exp(-s)
Ha11 = H.approximate_exp(ddegree=1)
Ha12 = H.approximate_exp(ddegree=2, ndegree=1)
Ha22 = H.approximate_exp(ddegree=2)
Ha23 = H.approximate_exp(ddegree=3, ndegree=2)
Ha33 = H.approximate_exp(ddegree=3)

tv = np.arange(400) / 400 * 4 - 1

xv = (tv >= 0) * 1

fig, axes = subplots(1, figsize=(6, 3.5))

axes.plot(tv, H.response(xv, tv), label='exact')
axes.plot(tv, Ha11.response(xv, tv), label='numer=1,denom=1')
axes.plot(tv, Ha12.response(xv, tv), label='numer=1,denom=2')
axes.plot(tv, Ha22.response(xv, tv), label='numer=2,denom=2')
axes.plot(tv, Ha23.response(xv, tv), label='numer=2,denom=3')
axes.plot(tv, Ha33.response(xv, tv), label='numer=3,denom=3')
axes.set_ylim(-1.5, 1.5)
axes.legend()
axes.set_title('bilinear transform')

savefig(__file__.replace('.py', '.png'), bbox_inches='tight')
