import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
prefilename = 'Fig1_A'
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

ax.set_title('Pulse evoked/abolished slow wave train in the bistable region')
ax.plot(time, vm, 'k')
ax.set_ylabel('Membrane Voltage [mV]', fontsize=12)
ax.set_xlabel('Time [min]', fontsize=12)

ax.text(0.52, 0.9, ' $R$',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='k', fontsize=12)

ax.text(0.3, 0.1, '$SS$',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='k', fontsize=12)
plt.show()
plt.savefig('Figure_2')