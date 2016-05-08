import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

r = np.linspace(0,15)
def effpot(Z,x):
    return -Z/x

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(r,effpot(4,r),'g--',label=r'$- \ \frac{e^2}{r}$')
ax1.plot(r,effpot(50,r),'r--',label=r'$- \ \frac{Z \cdot e^2}{r}$')
ax1.plot(r,effpot(25,r),'b-',label=r'$- \ \frac{Z_{eff} \cdot e^2}{r}$')
plt.xlim(0,15)
plt.ylim(-100,1)
plt.legend(loc='best',prop={'size':30})
ax1.axes.get_xaxis().set_ticks([])
ax1.axes.get_yaxis().set_ticks([])
plt.xlabel('$ Abstand \  r $')
plt.ylabel('$V_{eff}(r)$')
plt.show()
