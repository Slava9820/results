import math
import numpy as np
import json
import matplotlib.pylab as plt
import os.path

data = {}
data['data'] = []


x = np.arange(-100,100,0.01)
A = 1.25313
y = []
def asd(i):
    b = math.sin((i * i - A*A))
    c = math.cos(b) ** 2
    n = 0.001 * (i * i + A*A)
    function = 0.5 + (c - 0.5) / (1 + n)
    y.append(function)
    return function

[data['data'].append({'x': '{:.2f}'.format(i),'y': '{:.2f}'.format(asd(i))}) for i in x]

plt.grid()
plt.plot(x,y)
plt.show()
filename = os.path.join('results')
if not os.path.exists(filename) == True:
    os.mkdir(filename)
filename = os.path.join(filename, 'results.json')

with open(filename, 'w') as outfile:
    json.dump(data, outfile)


