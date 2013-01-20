"""
Nick Dutton
Geodesic.py
"""
############################################
##                                        ##
##  Create a simplified object for:       ##
##  gravitational bodies.                 ##
##                                        ## 
############################################

from math import sqrt, pow, pi, cos, sin

class Geodesic():

    def __init__(self,*args):
        if len(args) == 0:
            # Assume Earth (WGS-84) ellipsoid
            self.a = 6378.137             # semi-major axis (radius) of ellipsoid (x or y)
            self.f = 1/298.257223563    # earth flattening factor
            self.b = (1-self.f)*self.a        # semi-minor axis (radius) of ellipsoid (z)
            self.e2 = (2-self.f)*self.f # eccentricity squared
            self.e  = sqrt(self.e2)     # first eccentricity
            self.Mu = 398600.4418       # Gravitational Parameter (km^3/s^2)

        else:
            self.a = args(1)
            self.b = args(2)

    def oblateRadius(self,lat):
        # convert latitude to radians
        lat = lat * pi/180
        num = pow(pow(self.a,2)*cos(lat),2) + pow(pow(self.b,2)*sin(lat),2)
        den = pow(self.a * cos(lat),2) + pow(self.b * sin(lat), 2)
        radius = sqrt(num/den)
        return radius
