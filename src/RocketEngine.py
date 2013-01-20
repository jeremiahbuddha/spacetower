"""
Nick Dutton
RocketEngine.py
"""
############################################
##                                        ##
##  Create a simplified object for:       ##
##  Rocket Engines.                       ##
##                                        ## 
############################################
# Object Properties:
#


from math import sqrt, pow, pi, cos, sin

class RocketEngine():

    def __init__(self,*args):
        # Define properties of the rocket engine       
        if len(args) == 0:
            self.name = "RD-253"
        else: 
            self.name = args(1)

        # Dimensions & Physical Characteristics
        self.length     = 3     # m
        self.diameter   = 1.5   # m
        self.mass_dry   = 1260  # kg

        # Fuel type
        self.PropellantType = "N2O4/UDMH"
        self.gamma = 1.25       # Ratio of specific heats

        # Performance
        self.Thrust_vac = [1630.00188, 1829.99837] # kN
        self.Thrust_sl  = [1469.99935, 1670.00029] # kN
        self.Po         = [15168.466, 16892.1554]  # kPa
        self.Isp_vac    = 316 # sec
        self.Isp_sl     = 285 # sec
