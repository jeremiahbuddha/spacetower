import math


class Atmosphere():
    def __init__(self):
        # Use standard atmosphere 1976 tables...
        # See tables.py for original code.
        self.T0        = 288.15              # sea-level temperature, kelvins
        self.P0        = 101325.0            # sea-level pressure, N/sq.m
        self.Rho0      = 1.225               # sea-level density, kg/cu.m
        self.a0        = 340.294             # speed of sound at S.L.  m/sec
        


    def stdAtm(self):

        altKm, temp, pressure, density, asound = [],[],[],[],[]

        for i in range(-1,44):

            altKm.append(2*i) # km

            (sigma, delta, theta) = Atmosphere.calcAtm1976(altKm[i+1])
 
            temp.append(self.T0 * theta)                  # Kelvin
            pressure.append(self.P0 * delta)              # N/m^2
            density.append(self.Rho0 * sigma)             # Kg/m^3
            asound.append(self.a0 * math.sqrt(theta))     # m/s

        return altKm, temp, pressure, density, asound

    @staticmethod
    def calcAtm1976(alt):
        """ Compute temperature, density, and pressure in standard atmosphere.
        Correct to 86 km.  Only approximate thereafter.
        Input:
            alt        geometric altitude, km.
        Return: (sigma, delta, theta)
            sigma        density/sea-level standard density
            delta        pressure/sea-level standard pressure
            theta        temperature/sea-level std. temperature
        """

        REARTH = 6369.0                # radius of the Earth (km)
        GMR = 34.163195
        NTAB = 8                        # length of tables

        htab = [ 0.0,  11.0, 20.0, 32.0, 47.0,
            51.0, 71.0, 84.852 ]
        ttab = [ 288.15, 216.65, 216.65, 228.65, 270.65,
            270.65, 214.65, 186.946 ]
        ptab = [ 1.0, 2.2336110E-1, 5.4032950E-2, 8.5666784E-3, 1.0945601E-3,
            6.6063531E-4, 3.9046834E-5, 3.68501E-6 ]
        gtab = [ -6.5, 0.0, 1.0, 2.8, 0, -2.8, -2.0, 0.0 ]

        h = alt*REARTH/(alt+REARTH)        # geometric to geopotential altitude

        i=0; j=len(htab)
        while (j > i+1):
            k = (i+j)/2
            if h < htab[k]:
                j = k
            else:
                i = k
        tgrad = gtab[i]                # temp. gradient of local layer
        tbase = ttab[i]                # base  temp. of local layer
        deltah=h-htab[i]                # height above local base
        tlocal=tbase+tgrad*deltah        # local temperature
        theta = tlocal/ttab[0]        # temperature ratio

        if 0.0 == tgrad:
            delta=ptab[i]*math.exp(-GMR*deltah/tbase)
        else:
            delta=ptab[i]*math.pow(tbase/tlocal, GMR/tgrad)
        sigma = delta/theta

        return ( sigma, delta, theta )



