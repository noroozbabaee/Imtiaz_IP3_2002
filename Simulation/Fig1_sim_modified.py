# Author : Leyla Noroozbabaee
# Bioengineering Institute
# The University of Auckland
# Date: 5/10/2021

# To reproduce the data needed for Figure 1A in associated original paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:

#  In [1]: cd path/to/folder_this_file_is_in
#  In [2]: run Fig1_sim_modified.py

import opencor as oc
import numpy as np
prefilename= 'Fig1_A_modified'
# To remove the lag in Phase diagram, the modified version of Imtiaz model is available here:
simfile = 'IP3_Imtiaz_Modified.sedml'

simulation = oc.open_simulation(simfile)
data = simulation.data()
# Reset states and parameters
simulation.reset(True)
# Set constant parameter values
start = 0
end = 200000
pointInterval = 0.01
data.set_starting_point(start)
data.set_ending_point(end)
data.set_point_interval(pointInterval)

# Run simulation
simulation.run()
# Access simulation results
results = simulation.results()
# Grab the selected results
varName = np.array([ "time", "Vm", "z","ip3","y"])
vars = np.reshape(varName, (1, 5))
rows = end * 100 + 1
print(rows)
r = np.zeros((rows, len(varName)))

r[:,0] = results.voi().values()
r[:,1] = results.states()['vm/vm'].values()
r[:,2] = results.states()['vm/ca/z'].values()
r[:,3] = results.states()['vm/ca/p_ip3'].values()
r[:,4] = results.states()['vm/ca/y'].values()
# Save the data
filename = '%s.csv' % prefilename
np.savetxt(filename, vars, fmt='%s', delimiter=",")
with open(filename, "ab") as f:
    np.savetxt(f, r, delimiter=",")
f.close
