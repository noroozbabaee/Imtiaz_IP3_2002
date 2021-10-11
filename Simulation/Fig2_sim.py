# Author : Leyla Noroozbabaee
# Date: 2/10/2021
# To reproduce the data needed for Figure 2A in associated original paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:

#  In [1]: cd path/to/folder_this_file_is_in
#  In [2]: run Fig2_sim.py

import opencor as oc
import numpy as np
prefilename = 'Fig2_A'
simfile = 'IP3_Imtiaz_2002.sedml'
simulation = oc.open_simulation(simfile)
data = simulation.data()
# Reset states and parameters
simulation.reset(False)
# Set constant parameter values
start = 0
end = 90
pointInterval = 0.01
data.set_starting_point(start)
data.set_ending_point(end)
data.set_point_interval(pointInterval)

# Run the simulation for KO scenarios
data.constants()['vm/t_1'] = 30.0
data.constants()['vm/t_2'] = 31.5
data.constants()['vm/t_3'] = 60
data.constants()['vm/t_4'] = 63
data.constants()['vm/I_clamp1'] = 2.25
data.constants()['vm/I_clamp2'] = 2.25
data.constants()['vm/vm_init'] = -65.02
data.constants()['p_ip3/b_ip3'] = 0.7533
data.constants()['ca/y_init'] = 4.11341208572137
data.constants()['ca/z_init'] = 0.478526130219779
data.constants()['p_ip3/p_ip3_init'] = 0.408438668750528

simulation.run()
# Access simulation results
results = simulation.results()
# Grab a selected algebraic variable results
varName = np.array([ "time", "Vm", "z","ip3","y"])
vars = np.reshape(varName, (1, 5))
rows = end * 100 + 1
print(rows)
r = np.zeros((rows, len(varName)))

r[:,0] = results.voi().values()
r[:,1] = results.states()['vm/vm'].values()
r[:,2] = results.states()['ca/z'].values()
r[:,3] = results.states()['p_ip3/p_ip3'].values()
r[:,4] = results.states()['ca/y'].values()
filename = '%s.csv' % prefilename
np.savetxt(filename, vars, fmt='%s', delimiter=",")
with open(filename, "ab") as f:
    np.savetxt(f, r, delimiter=",")
f.close
