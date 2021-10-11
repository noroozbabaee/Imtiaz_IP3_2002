import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
prefilename = 'Fig3_A'
filename = '%s.csv' % prefilename 
data = pd.read_csv(filename)

time = data['time']
vm = data['Vm']
ca_y = data['y']
p_ip3 = data['ip3']
ca_z = data[ 'z' ]


fig = plt.figure(figsize=(8, 4),  edgecolor='k')
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)


ax.set_title('Slow wave voltage dependence on injected current')
ax.plot(time, vm, 'k')
ax.set_ylabel('Membrane Voltage [mV]', fontsize=12)
ax.set_xlabel('Time [min]', fontsize=12)


ax.axis([0, 36, -85,-20])

ax.text(0.3, 0.89, ' $I_{inj} = 0 mA$',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='k', fontsize=12)

ax.text(0.58, 0.89, ' $I_{inj} = -15 mA$',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='k', fontsize=12)

ax.text(0.94, 0.89, ' $I_{inj} = 22 mA$',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='k', fontsize=12)
plt.show()
plt.savefig('Figure_3')