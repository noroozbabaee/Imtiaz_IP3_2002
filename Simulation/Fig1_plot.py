import pandas as pd
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
# Plot Figure 1A

# prefilename = 'Fig1_A'
# plotting the modified version of Figure 1A
prefilename= 'Fig1_A'
filename = '%s.csv' % prefilename
data = pd.read_csv(filename)
time = data['time']
time = time
vm = data['Vm']
ca_y = data['y']
p_ip3 = data['ip3']
ca_z = data[ 'z' ]
# Data preparation
vm = 100 + vm
# Normalize the data
vm_norm = preprocessing.normalize(np.array(vm).reshape(1, -1))
ca_z_norm = preprocessing.normalize(np.array(ca_z).reshape(1, -1))
p_ip3_norm = preprocessing.normalize(np.array(p_ip3).reshape(1, -1))
ca_y_norm = preprocessing.normalize(np.array(ca_y).reshape(1, -1))


fig, axs = plt.subplots()
labelfontsize = 12
axs.plot(time, vm_norm[0],'k')
axs.plot(time, p_ip3_norm[0] , '#8f8f8f')
axs.plot(time, ca_z_norm[0] , '--k')
axs.set_ylabel ('Normalized Parameters', fontsize= labelfontsize)
axs.set_xlabel ('Time (min)', fontsize= labelfontsize)
axs.legend(["Vm","IP3","Ca-c"],loc ="upper right")
axs.set_yticklabels([])
axs.set_title('Phase Plot')
axs.set_xlim([0, 8])
axs.set_ylim([0, 0.1120])
plt.show()
plt.savefig('Figure_1A')