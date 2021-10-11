Original Paper
==============

:Original publication:  "A Theoretical Model of Slow Wave Regulation Using Voltage-Dependent
Synthesis of Inositol 1,4,5-Trisphosphate" Biophysical Journal Volume 83 October 2002 1877–1890.

:DOI: https://doi.org/10.1016/S0006-3495(02)73952-0

Model status
=============

The current CellML model implementation runs in OpenCOR_.
The CellML model parameters must be updated regarding each specific model variation to reproduce the related simulations;
The results have been validated against the data extracted from Figure 1A in the published model `Imtiaz,  et al (2002)`.
The required information is not available in some cases, for more details see :ref:`Model Validations`.

Model Summary
==============
Slow waves are rhythmic electrical depolarizations that
initiate and control the mechanical activity of many smooth
muscles. The mechanism responsible for generating slow waves involves IP3-induced calcium release and calcium-induced calcium release from IP3-operated intracellular calcium stores. The resultant calcium increases in the subplasmalemmal space then activate calcium-sensitive inward currents across the plasmalemma that result in slow-wave
depolarizations which are according to the previous studies.

According to :ref:`Original Paper`, IP3 oscillations are unnecessary
for calcium oscillations, as IP3 oscillations can occur in many cell types. In the current work, the author is introducing a new feedback mechanism based on membrane potential, which then modulates IP3 synthesis. In this paper, the aim is to study the role of membrane
potential feedback on IP3 synthesis and its role in regulating calcium release and slow waves.

The system is simplified by considering a single
isopotential cell with a single IP3 receptor-operated intracellular
calcium pool. Ryanodine receptor is ignored in the model. It is
important to note that in this model voltage-dependent channels are considered to be blocked.


Model Equations
===============
The model is implemented using a Hodgkin-Huxley type formulation. The cell membrane lipid bilayer is represented as a capacitance (Cm),
and the ion channels in the membrane are represented as conductance. The change in the transmembrane potential (Vm) over time depends on
is the sum of the individual ion currents through each class of ion channel in the cell current:

:math:` \frac{dVm}{dt} = - \frac{I_{tot}}{C_{m}}`.


Model Issues
===================
1. There is an issue of unit consistency:

- In Eq. 3, :math:`V_{in},  V_{1}` and :math:`V_{0}` have a unit of :math:`\mu M /min`, while  P has a unit of :math:`\mu M `. As a result, one can see the left and the right-hand sides of Eq. 3 has inconsistent units. :math:` V_{in} = V_{0} + V_{1}* P`.

- In Eq. 7, the left-hand side is multiplied by the scale factor of 60 to create the unit consistency.

- In Eq. 9, on the left, the term :math:`\beta` that indicates the external stimuli has a unit of :math:`\mu M ` while on the right-hand side, the term :math:`dP /dt` which indicates IP3 concentration in the cytosol has a unit of :math:`\mu M /min`.
  :math:`\frac{dP}{dt} = \beta - \epsilon *  P  - V_{m4}(P) + P (V)`.

3. In Eq 7, on the right-hand side, the first term which indicates the lumped current (:math:`I_{i}`)  should carry a negative sign, while in the original work the lump current is presented with a positive sign. Please see the correct form in below:

:math:` \frac{dVm}{dt} = - \Big[\frac{I_{Ca}+ I_{i}-I_{inj}}{C_{m}}\Big]`.

4. In the case of model experiments, there is no clear information about the protocol
they used to inject the current into the cell.



Model Validations
===================
Applying some corrections in the original equations and parameters (see :ref:`Model Issues`), the following results were observed:
The phase diagrams were plotted to study the dynamics of the voltage-dependent system (see :ref:`Original Paper` Figure  2A). Intracellular calcium (Z) and membrane potential
(Vm) oscillations are in phase, whereas IP3 oscillations
follow with a lag. All traces are normalized. The phase diagram on the left
illustrates the original work, while the one on the right represents the modified version of the current paper, where all the three traces are in the same phase.

|pic1| |pic2|

.. |pic1| image:: Doc/Figure1.png
    :width: 49%
.. |pic2| image:: Doc/Figure1_modified.png
    :width: 49%

To reproduce Figure 3A from :ref:`Original Paper`, we required more information such as the non-periodic steady-state values and the pluses durations.
The following results are produced through running different experiments, guess and check.

.. image:: Doc/Figure_2.png
   :width: 100%
   :align: center
   :alt: Pulse evoked/abolished slow wave train in the bistable region

Figure 4A illustrates the slow-wave characteristics due to the polarization of the membrane
potential to different voltage levels.

.. image:: Doc/Figure_3.png
   :width: 100%
   :align: center
   :alt: Slow wave dependency on the injected current, Doc/Figure3.png .


Model Sources
=======================
1. Doc: A ReadMe file that includes all the necessary information about the article, curation (simulations and experiments), and possible issues.
2. Simulations: Python files that help the users run the CellML through the Python console in OpenCOR_.
3. Experiment: the CellML version of the current mathematical model.

How to run the simulation:
This can be done with the following commands at the prompt in the OpenCOR_ Python console:

In [1]: cd path/to/folder_this_file_is_in

In [2]: run Fig_sim.py
