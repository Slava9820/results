import math
import numpy as np
import json
import matplotlib.pylab as plt

data = {}
data['data'] = []


x = np.arange(-100,100,0.01)
A = 1.25313
y = []
for i in x:
    b = math.sin((i * i - A * A))
    c = math.cos(b) ** 2
    n = 0.001 * (i * i + A * A)
    function = 0.5 + ( c - 0.5) / (1 + n)
    y.append(function)
    data['data'].append({
        'x': '{:.2f}'.format(i),
        'y': '{:.2f}'.format(function)
    })

with open('res.json', 'w') as outfile:
    json.dump(data, outfile)
plt.grid()
plt.plot(x,y)
plt.show()