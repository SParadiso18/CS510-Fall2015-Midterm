import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Attractor(object):
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
        #self.solution = None
        self.solution = pd.DataFrame()
        
    def given(self, arr):
        
        x0,y0,z0 = arr
        s,p,b = self.params
        x = s * (y0 - x0)
        y = x0 * (p - z0) - y0
        z = x0 * y0 - b * z0
        
        return np.array([x,y,z])
    
    def euler(self, arr):
        
        k1 = arr + self.given(arr) * self.dt
        
        return k1
    
    def rk2(self, arr):
        
        k1f = self.given(arr)
        k2f = self.given(arr + k1f * self.dt / 2.0)
        
        k2 = arr + k2f * self.dt
        
        return k2
    
    def rk4(self, arr):
        
        k1f = self.given(arr)
        k2f = self.given(arr + k1f * self.dt / 2.0)
        k3f = self.given(arr + k2f * self.dt / 2.0)
        k4f = self.given(arr + k3f * self.dt)
        
        k4 = arr + self.dt / 6.0 * (k1f + 2 * k2f + 2 * k3f + k4f)
        
        return k4
    
    def evolve(self, r0 = np.array([0.1, 0.0, 0.0]), order = 4):
        if order == 1:
            a = self.euler
        elif order == 2:
            a = self.rk2
        elif order == 4:
            a = self.rk4
        else:
            print("Please enter a 1, 2, or 4.")
            
        #data_dict = {k: np.zeros(self.points) for k in 'txyz'}
        #self.solution = pd.DataFrame(data_dict)
        #xyz = r0
        #for i in range(self.points):
            #x, y, z = xyz
            #self.solution.loc[i] - [i * self.dt, x, y, z]
            #xyz = a(xyz)
            
        #for value in 'txyz':
            #self.solution = pd.DataFrame(np.zeros(self.points))
            #xyz = r0
        
        #for i in range(self.points):
            #x, y, z = xyz
            #self.solution.loc[i] - [i * self.dt, x, y, z]
            #xyz = a(xyz)
            
        return self.solution
            
    def save(self, fn):
        self.solution.to_csv(fn, index = False)
        
    def plotx(self):
        plt.xlabel('t')
        plt.ylabel('x(t)')
        plt.plot(self.solution['t'], self.solution['x'], '.', color = 'b')
        plt.show()
        
    def ploty(self):
        plt.xlabel('t')
        plt.ylabel('y(t)')
        plt.plot(self.solution['t'], self.solution['y'], '.', color = 'o')
        plt.show()
        
    def plotz(self):
        plt.xlabel('t')
        plt.ylabel('z(t)')
        plt.plot(self.solution['t'], self.solution['z'], '.', color = 'p')
        plt.show()
        
    def plotxy(self):
        plt.xlabel('x')
        plt.ylabel('z')
        plt.plot(self.solution['x'], self.solution['z'], '.', color = 'b')
        plt.show()
        
    def plotyz(self):
        plt.xlabel('y')
        plt.ylabel('z')
        plt.plot(self.solution['y'], self.solution['z'], '.', color = 'o')
        plt.show()
        
    def plotzx(self):
        plt.xlabel('z')
        plt.ylabel('x')
        plt.plot(self.solution['z'], self.solution['x'], '.', color = 'p')
        plt.show()
        
    def plot3d(self):
        var = pl.gca(projection = '3d')
        plt.plot(self.solution['x'], self.solution['y'], self.solution['z'])
        plt.show()