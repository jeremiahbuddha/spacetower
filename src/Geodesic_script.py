from Geodesic import Geodesic
from LaunchVehicle import LaunchVehicle
from Atmosphere import *
from math import pow, pi, sin, cos
import numpy as np
from scipy.integrate import odeint

def Geodesic_script():
    # setup the initial conditions
    geo = Geodesic()
    # assume initially a vertical launch from 5 degrees latitude
    radiusE = geo.oblateRadius(5) * 1000

    # launch vehicle
    lv = LaunchVehicle()

    # standard atmosphere (1976) data
    atm = Atmosphere()
    [altList, tempList, pressureList, densityList, asoundList] = atm.stdAtm()

    Area = pow(lv.Rcross,2)*pi
    k = 9.81*pow(geo.a * 1000,2)

    # flight path angle (deg)
    fp = pi/2
    # velocity magnitude /speed (m/s)
    vc = 0
    # altitude above geodesic (m)
    alt = 0

    nu = 0

    # speed of sound (m/s)
    a = np.interp(alt,altList,asoundList)

    # atmospheric density (kg/m^3)
    rho = np.interp(alt,altList,densityList)

    r = radiusE + alt
    r2 = pow(r,2)
    g = k/r2

    m = 2300000
    T = 34020000
    Isp = 400
    theta = 0

    Mach = vc/a
    D = 0.5 * lv.getCd(Mach) * Area * rho * pow(vc,2)

    params = (k, radiusE, altList, asoundList, densityList, Area, lv, Isp, T, theta)

    x0 = [r,m,nu,fp,vc]

    return x0, params
    
    
def odeFunc(x, t, params):
    
    k    = params[0]
    rE   = params[1]
    altList = params[2]
    asoundList = params[3]
    densityList = params[4]
    Area = params[5]
    lv = params[6]
    Isp = params[7]
    T = params[8]
    theta = params[9]
    

    r = x[0]
    m = x[1]
    nu = x[2]
    fp = x[3]
    vc = x[4]

    alt  = r - rE
    
    r2 = r**2
    # % speed of sound (m/s)
    a = np.interp(alt,altList,asoundList)

    # % atmospheric density (kg/m^3)
    rho = np.interp(alt,altList,densityList)
    
    # g    = k/(r**2)
    Mach = vc/a
    
    # Assume Lift = 0
    L = 0
    
    D = 0.5 * lv.getCd(Mach) * Area * rho * pow(vc,2)

    rdot  = vc * sin(fp)
    mdot  = -T/Isp
    nudot = vc * cos(fp) / r
    if (vc == 0):
        fpdot = 0
    else:
        print("vc: ",vc)
        fpdot = -k * cos(fp) / (vc*r2) + L/(vc*m) + vc*cos(fp)/r + 1/(vc*m) * T * sin(theta)
    vdotc = -k * sin(fp) / r2 - D/m + 1/m*T*cos(theta)

    xdot = []
    # dX/dt = velocity
    xdot.append(rdot)
    
    # dXdot/dt = acceleration
    xdot.append(mdot)
    xdot.append(nudot)
    xdot.append(fpdot)
    xdot.append(vdotc)

    
    
    return xdot


def main():
    [x0, params] = Geodesic_script()
    t = range(0,151)
    X = odeint(odeFunc,x0,t,args = (params,))
    lx = len(X)
    print("Length of X: ",str(lx)," ")

    for i in range(len(X)-1):
        print(str(X[i][:]))

main()
