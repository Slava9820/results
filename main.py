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
for i in x:
    b = math.sin((i * i - A))
    c = math.cos(b) ** 2
    n = 0.001 * (i * i + A)
    function = 0.5 + ( c - 0.5) / (1 + n)
    y.append(function)
    data['data'].append({
        'x': '{:.2f}'.format(i),
        'y': '{:.2f}'.format(function)
    })

plt.grid()
plt.plot(x,y)
plt.show()
dirname = os.path.dirname('results.json')
filename = os.path.join(dirname, 'results')
if os.path.exists(filename) == False:
    os.mkdir(filename)
filename = os.path.join(filename, 'results.json')

with open(filename, 'w') as outfile:
    json.dump(data, outfile)

