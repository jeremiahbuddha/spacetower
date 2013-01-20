"""
Nick Dutton
LaunchVehicle.py
"""
############################################
##                                        ##
##  Create a simplified object for:       ##
##  launch vehicles.                      ##
##                                        ## 
############################################
# Object Properties:
#   Stages:
#       number                                  (nstg)       
#     Mass (kg) [per stage]:
#         structural                            (mst)
#         payload                               (mpl)
#         fuel @ launch                         (mf0)
#     Cross Sectional Radius (m^2) [per stage]: (Rcross)
#   Altitude (km):
#       final (orbit) altitude                  (altF)
#       initial altitude                        (alt0)
#


from math import sqrt, pow, pi, cos, sin
import numpy as np

class LaunchVehicle():

    def __init__(self,*args):
        # Define properties of the launch vehicle        
        if len(args) == 0:
            self.nstg       = 3
            self.mst        = 10000
            self.mpl        = 5000
            self.mf0        = 15000
            self.Rcross     = 3.5
            self.alt0       = 0
            self.altF       = 300
            self.noseShape = "round nose"


    def getCd(self,Nmach):

        if self.noseShape == "round nose":
            machlst = [0, 0.5, 1, 1.5, 2, 2.5, 3]
            cdlst = [0.2, 0.22, 0.3, 0.63, 0.6, 0.57, 0.52]
            Cd = np.interp(Nmach,machlst,cdlst)
            return Cd
            
             

        



        

