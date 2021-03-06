from integrator.simpsons import multi as integrate
from functions.parent import Function


import matplotlib.pyplot as plt
import numpy as np
import math


"""
The dCPLintegrand is the integrand part of the equation for the distance as redshift for the CPL parametrization.
"""

class dCPLintegrand(Function):

    # Initialize the function and inherit everything from the parent function
    def __init__(self):
        Function.__init__(self)

    # Calculate the value as a function of x
    def cal(self, x):
        integrand = math.sqrt(x) * math.sqrt(self.omeM + ((self.omeX* math.pow(self.a0/x,3*(self.wp + self.wa))) * math.exp(3*self.wa*(x/self.a0 -1)) ))

        return (1./integrand)



"""
The CPL parametrization distance as a function of z.
Within it there is an integral of dCPLintegrand.
"""

class dCPL(Function):

    # Initialize the function and inherit everything from the parent function
    def __init__(self):
        Function.__init__(self)
        self.integrand = dCPLintegrand()

    def update(self, wp = False, wa = False):
        if type(wp) != type(False):
            self.integrand.wp = wp
        if type(wa) != type(False):
            self.integrand.wa = wa


    # Calculate the value as a function of x
    def cal(self, z):
        az = self.a0/(1+z)
        return (self.c / (math.sqrt(self.a0) * self.H0_2)) * integrate(self.integrand, [az, self.a0], 1e-4)

"""
The bao function, it is a reversible function. Given an angle it will output d and given d it will output theta.
"""

class dBAO(Function):
    def __init__(self):
        Function.__init__(self)

    def cal(self, theta):
        return self.lbao / theta
