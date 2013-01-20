"""
Nick Dutton
LaunchComponent.py
"""
############################################
##                                        ##
##  Create a simplified object for:       ##
##  launch vehicle components.            ##
##                                        ## 
############################################
# Object Properties:
#   Stages:
#       number                                  (nstg)       
#     Mass (kg) [per stage]:
#         structural                            (mst)
#         payload                               (mpl)
#         fuel @ launch                         (mf0)
#     Cross Sectional Area (m^2) [per stage]:   (Ac)
#
#


from math import sqrt, pow, pi, cos, sin

class LaunchVehicle():

    def __init__(self,*args):
        # Define properties of the launch vehicle        
        if len(args) == 0:
            self.ms =

        else:
            self.a = args(1)
            self.b = args(2)

