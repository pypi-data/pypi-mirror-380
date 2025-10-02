# -*- coding: utf-8 -*-
"""
Collection of functions and classes helpful in dealing with Airy intensity
patterns in the spatial domain.

Created on Thu Aug 21 15:43:08 2025

@author: Leonard.Doyle
"""

import numpy as np
import scipy.special
from .utilities import lam2k

def airy_Ipeak_from_Ppeak(Ppeak, lam, f, D):
    """
    For a flat top intensity beam of diameter D, focused to the
    diffraction limited spot size (airy disk) by a focusing optic of
    focal length f, calculate the peak intensity Ipeak.
    The focal spot size and therefore Ipeak depends on the wavelength lam.
    
    Instead of using the airy disk area pi*r0^2, use exact analytical integral
    relation for Ipeak of the airy disk.
    In focal plane (airy disk):
        P = Integrate[I dA] = Integrate[Iairy(r) * r dr dphi]
             = 2pi * Integrate[Iairy(r) * r,{r,0,Inf}]
        where P = total in area, peak in time -> call it Ppeak
    and equate this with Ipeak = Iairy(r=0):
        Ipeak = pi/4 * Ppeak * (D/(lam*f))^2
    
    Parameters
    ----------
    Ppeak : float
        Peak power of pulse in [W = J/s]
    lam : float
        Central wavelength of the pulse [m]
    f : float
        Focal length of focussing optic [m]
    D : float
        Beam diameter of flat top input beam [m]

    Returns
    -------
    Ipeak in [W/m^2] (SI units)

    """
    Ipeak = np.pi/4 * Ppeak * (D / (lam*f))**2
    return Ipeak


def f_number2airy_radius(f_num, lam):
    """Calculate the airy disk radius (radius at first minimum!) assuming
    flat top irradiation with wavelength lam of a lens of given f_number."""
    return 1.22*lam*f_num


def airy_rad2airy_FWHM(r_airy):
    """Calculate airy disk FWHM (in intensity) given the radius of
    first minimum r_airy"""
    #airy rad= 1.22 lam f/D
    #airy FWHM=1.03 lam f/D
    return r_airy / 1.22 * 1.03


airyFWHM_from_airyRad = airy_rad2airy_FWHM # same name, why have both??


def airyRad_from_fNo(f_num, lam):
    """Calculate the airy disk radius (radius at first minimum!) assuming
    flat top irradiation with wavelength lam of a lens of given f_number."""
    return 1.22*lam*f_num


def airy_intensity(r, lam, f_number, P_tot):
    k = lam2k(lam)
    krrf = k*r/(2*f_number)
    # from Lennys MSc thesis, but there is an error, it is missing 1/4 prefactor!
    #prefactor = 0.5*sc.c*sc.epsilon_0 * E_0**2 * k**2 * A_0**2 / (np.pi*f)**2
    # also, more practical to write in terms of incoming beam integral:
    I0 = P_tot / (4*np.pi) * k**2 / (4*f_number**2)
    krrf_nan = krrf.copy()
    nanmask = krrf_nan==0 # avoid div by zero error
    krrf_nan[nanmask] = np.nan 
    besselpart = 2*scipy.special.jv(1,krrf)/krrf_nan
    besselpart[nanmask] = 1 # manually input limiting value
    return I0*besselpart**2