import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#%matplotlib inline

class Attractor(object):
    """ Here we begin by initializing our parameteres and store them as numpy arrays and/or setting 
    their default values. We also use these values to calculate the time increment (self.dt)."""
    def __init__(self, s = 10.0, p = 28.0, b = 8.0/3.0, start = 0.0, end = 80.0, points = 10000):
        inarr = np.array([s,p,b])
        self.s = s
        self.p = p
        self.b = b
        self.params = inarr
        self.start = start
        self.end = end
        self.points = points
        self.dt = ((self.end - self.start) / self.points)
        self.t = np.linspace(self.start, self.end, self.points)
        self.solution = pd.DataFrame()
    
    def given(self, arr):
        """ This method was created in hindsight to simplfy code further on in this Attractor class.
            As we can see, this is where we work with our given set of differential equations and
            convert them into terms more suitable for coding purposes and return the resulting numpy
            array.
        """
        x0,y0,z0 = arr
        s,p,b = self.params
        x = s * (y0 - x0)
        y = x0 * (p - z0) - y0
        z = x0 * y0 - b * z0
        
        return np.array([x,y,z])
    
    def euler(self, arr):
        """ The euler method here takes a numpy array of length three as an argument, proceedes to
            calculate the the first order Euler increment of the differential equations from our given
            method, and returns the desired k1 value.
        """
        
        k1 = arr + self.given(arr) * self.dt
        
        return k1
        
    def rk2(self, arr):
        """ Here we have the rk2 method which in large is very similar to the euler method, however,
            this method calculates and returns the second order Runge-Kutta increment.
        """
        
        k1f = self.given(arr)
        k2f = self.given(arr + k1f * self.dt / 2.0)
        
        k2 = arr + k2f * self.dt
        
        return k2
        
    def rk4(self, arr):
        """ Again, we have a near identical method here with the exception of how far we take the
            incrementation. In rk4 we calculate and return the fourth order Runge-Kutta increment.
        """
        
        k1f = self.given(arr)
        k2f = self.given(arr + k1f * self.dt / 2.0)
        k3f = self.given(arr + k2f * self.dt / 2.0)
        k4f = self.given(arr + k3f * self.dt)
        
        k4 = arr + self.dt / 6.0 * (k1f + 2 * k2f + 2 * k3f + k4f)
        
        return k4
    
    def evolve(self, r0 = np.array([0.1, 0.0, 0.0]), order = 4):
        """ This method, evolve, takes a numpy array of length three and an integer as parameters.
            The initial values (x0, y0, and z0) are given default values of 0.1, 0.0, and 0.0
            respectively. The integer value order may take the quantities of 1, 2, or 4, defaulting 
            to 4, depending on which method is desired for incrementation. In this method we also
            generate our pandas DataFrame and store it and return it as self.solution.
        """
        if order == 1:
            a = self.euler
        elif order == 2:
            a = self.rk2
        elif order == 4:
            a = self.rk4
        else:
            print "\n !!!Order was not 1, 2, or 4!!! \n"
            return None
            
        dd = {b: np.zeros(self.points) for b in 'txyz'}
        self.solution = pd.DataFrame(dd)
        xyz = r0
        for i in range(self.points):
            x, y, z = xyz
            self.solution.loc[i] = [i * self.dt, x, y, z]
            xyz = a(xyz)
            
        return self.solution

    def save(self, filename = None):
        """ This is a very simple method to save our self.solution DataFrame to a CSV file on disk.
        """
        filename = 'solution.csv'
        self.solution.to_csv(filename)
        
    def plotx(self):
        """ This method simply labels axes and plots out t variable by our x(t) variable.
        """
        plt.xlabel('t')
        plt.ylabel('x(t)')
        plt.plot(self.solution['t'], self.solution['x'])
        plt.show()
        
    def ploty(self):
        """ This method simply labels axes and plots out t variable by our y(t) variable.
        """
        plt.xlabel('t')
        plt.ylabel('y(t)')
        plt.plot(self.solution['t'], self.solution['y'])
        plt.show()
        
    def plotz(self):
        """ This method simply labels axes and plots out t variable by our z(t) variable.
        """
        plt.xlabel('t')
        plt.ylabel('z(t)')
        plt.plot(self.solution['t'], self.solution['z'])
        plt.show()
        
    def plotxy(self):
        """ Now we keep on the same plotting track in this method except we plot our results
            against one another. Namely, we're plotting x(t) vs y(t).
        """
        plt.xlabel('x(t)')
        plt.ylabel('y(t)')
        plt.plot(self.solution['x'], self.solution['y'])
        plt.show()
        
    def plotyz(self):
        """ Here we plot y(t) against z(t).
        """
        plt.xlabel('y(t)')
        plt.ylabel('z(t)')
        plt.plot(self.solution['y'], self.solution['z'])
        plt.show()
        
    def plotzx(self):
        """ This method plots x(t) by z(t).
        """
        plt.xlabel('x(t)')
        plt.ylabel('z(t)')
        plt.plot(self.solution['x'], self.solution['z'])
        plt.show()
        
    def plot3d(self):
        """ And finally we have the plotting method to give a 3D representation of all three,
            x(t), y(t), and z(t), against eachother.
        """
        td = plt.gca(projection='3d')
        plt.plot(self.solution['x'], self.solution['y'], self.solution['z'])
        plt.show()