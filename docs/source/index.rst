.. Epitools documentation master file, created by
   sphinx-quickstart on Mon Jan 31 11:07:04 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

``Welcome to Epitools's documentation!``
========================================
Python toolkit for analysis, modelling and forecasting Epidemic.

:Authors: `Souvik Manik <souvikmanik@mcconline.org.in>`_, `Sabyasachi Pal <sabya.pal@gmail.com>`_, `Manoj Mandal <manojmandal@mcconline.org.in>`_. 
:Version: 1.0.0

Key features
------------
* Epidemic outbreak modeling and short-term forecasting using predefined fitted growth functions.
* Estimation of  time-dependent transmission coefficients and efective reproduction number.
* Epidemic dynamics modeling and estimation of transmission epidemiological parameters using the Runge-Kutta initial value problem solver and iterative (limited memory) BFGS optimizer. 
* Epidemic decay dynamics modeling with time dependent contact rate using different decay functions (exp, power, tanh).
* Estimation of effective reproduction number using Kalman filtering techniques directly from the real-time infection data. 

Documentation
------------- 
.. toctree::
   Installation <installation.rst> 
   Eptools description <user_guide/tutorial_main.rst>
   Tutorial for epidemic outbreak modeling<./outbreak.ipynb>
   Tutorial for epidemic dynamics modeling<./epidynamicsmodel.ipynb>

Our publications
----------------
1. Manik, S., Pal, S., Mandal, M. et al. “Effect of 2021 assembly election in India on COVID-19 transmission.” Nonlinear Dyn 107, 1343–1356 (2022). https://doi.org/10.1007/s11071-021-07041-7. 
2. Manik, Souvik, et al. “Impact of climate on COVID-19 transmission: A case study with Indian states.” medRxiv (2020): 2020-07.
3. Manik, Souvik, et al. “Impact of Environmental Factors on COVID-19 Transmission: an Overview. ” (In press).
4. Manik, Souvik, et al. “Epitools: A Python Package for Modelling and Forcasting Epidemic.” medRxiv (2020): (In press).
