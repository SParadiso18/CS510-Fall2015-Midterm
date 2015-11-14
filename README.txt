Sean Paradiso
CS 510
Midterm


Introduction
-------------

   The python class Attractor has multiple methods to perform a variety of operations. Some of which include the utilization of Euler and Runge-Kutta to increment through a set of given differential equations, plotting of the results from the given set of differential equations, test cases, and more. A few of the useful built-in tools at use here were numpy, pandas, and matplotlib.

Requirements
-------------

This project required the following:
      - Attractor class
      - euler method
      - rk2 method
      -rk4 method
      - evolve method
      - save method
      - plotx, ploty, and plotz methods
      - plotxy, plotyz, and plotzx methods
      - plot3d method
      - test_attractor module
      
Detailed Descriptions
----------------------

 The Attractor class takes three initialization parameters and stores them as a numpy array. It also takes an additional three initialization parameters used to compute a time increment to be used later.

 The euler method takes a numpy array and returns the Euler increment for the set of three given differential equations.

 rk2 proceeds very similarly to the euler method, however, returns the second order Runge-Kutta increment.

 rk4 is the same as rk2 with the exception of returning the fourth order Runge-Kutta increment.

 The method evolve takes a numpy array and an integer order to generate a pandas DataFrame.

 A very straight forward method, save simply saves the self.solution variable to a CSV file on disk.

 As to be expected from the names, plotx , ploty, and plotz take advantage of the matplotlib to generate two dimensional plots of the x(t), y(t), and z(t) curves vs. time accordingly.

 The methods plotxy, plotyz, and plotzx plot the logical pairs of the solution curves in two dimension.

 Taking it a step further, the plot3d method generates a three dimensional plot of the x-y-z solution curves

 Our module test_attractor is where the tests are stored to experiment with the class and methods to ensure functionality.

 Finally, the ExploreAttractor notebook loads the entire module and uses it to answer the following:

     1. How does the plotted solution depend on your choice of time step size, and your choice of increment?  Do you see an improvement in precision from using the higher-order integration methods?
     2. How does the solution depend upon the initial conditions [x0, y0, z0]?  How small a change can you make while still reproducing roughly the same dynamical curves?