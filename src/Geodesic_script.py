from Geodesic import Geodesic
from LaunchVehicle import LaunchVehicle
from Atmosphere import *
from math import pow, pi, sin, cos
import numpy as np
from scipy.integrate import odeint

def Geodesic_script()

    geo = Geodesic()
    # assume initially a vertical launch from 5 degrees latitude
    radiusE = geo.oblateRadius(5)


    # launch vehicle
    lv = LaunchVehicle()

    # standard atmosphere (1976) data
    atm = Atmosphere()
    [altList, tempList, pressureList, densityList, asoundList] = atm.stdAtm()

    Area = pow(lv.Rcross,2)*pi
    k = 9.81*pow(geo.a,2)

    # flight path angle (deg)
    fp = 90
    # velocity magnitude /speed (km/s)
    vc = 0
    # altitude above geodesic (km)
    alt = 0


    % speed of sound (m/s)
    a = np.interp(alt,altList,asoundList)

    % atmospheric density (kg/m^3)
    rho = np.interp(alt,altList,densityList)

    r = radiusE + alt
    r2 = pow(r,2)
    g = k/r2

    Mach = vc/a
    D = 0.5 * lv.getCd(Mach) * Area * rho * pow(vc,2)

    vdotc = -k * sin(fp) / r2 - D/m + 1/m*T*cos(theta)
    fpdot = -k * cos(fp) / (vc*r2) + L/(vc*m) + vc*cos(fp)/r + 1/(vc*m) * T * sin(theta)
    nudot = vc * cos(fp) / r
    rdot  = vc * sin(fp)
    mdot  = -T/Isp
    
    
    
def odeFunc(x,t, params)
    
    vc      = x[0] 
    fp      = x[1] 
    nu      = x[2] 
    r       = x[3]
    mass    = x[4]
    T       = x[5]
    theta   = x[6]
    
    k    = params[0]
    rE   = params[1]
    altList = params[2]
    asoundList = params[3]
    densityList = params[4]
    Area = params[5]
    lv = params[6]
    Isp = params[7]
    
    alt  = r - rE
    
    % speed of sound (m/s)
    a = np.interp(alt,altList,asoundList)

    % atmospheric density (kg/m^3)
    rho = np.interp(alt,altList,densityList)
    
    # g    = k/(r**2)
    Mach = vc/a
    
    # Assume Lift = 0
    L = 0
    
    D = 0.5 * lv.getCd(Mach) * Area * rho * pow(vc,2)
    
    return [-k * sin(fp) / r2 - D/m + 1/m*T*cos(theta), %
        -k * cos(fp) / (vc*r2) + L/(vc*m) + vc*cos(fp)/r + 1/(vc*m) * T * sin(theta), %
        vc * cos(fp) / r, vc * sin(fp), -T/Isp]
