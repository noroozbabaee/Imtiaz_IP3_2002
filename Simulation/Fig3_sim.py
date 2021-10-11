# Author : Leyla Noroozbabaee
# Date: 2/10/2021
# To reproduce the data needed for Figure 3A in associated original paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:

#  In [1]: cd path/to/folder_this_file_is_in
#  In [2]: run Fig3_sim.py

import opencor as oc
import numpy as np
prefilename= 'Fig3_A'
simfile = 'IP3_Imtiaz_2002.sedml'
simulation = oc.open_simulation(simfile)
data = simulation.data()

# Reset states variables and parameters
simulation.reset(True)
# Set constant values
start = 0
end = 36
pointInterval = 0.01
data.set_starting_point(start)
data.set_ending_point(end)
data.set_point_interval(pointInterval)
data.constants()['ca/y_init'] = 4.439
data.constants()['ca/z_init'] = 0.475
data.constants()['p_ip3/p_ip3_init'] = 0.397
data.constants()['p_ip3/b_ip3'] = 0.955

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
