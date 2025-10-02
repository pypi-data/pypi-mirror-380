# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:56:49 2019

@author: Leonard.Doyle

"""

import numpy as np
import scipy.constants as sc

lam2k = lambda lam: 2*np.pi/lam
k2lam = lambda k: 2*np.pi/k
lam2omega = lambda lam: 2*np.pi*sc.c/lam
lam2nu = lambda lam: sc.c/lam


def tauFWHM2delta_nu(tauFWHM):
    """Given the tau_FWHM duration in intensity, give FWHM power spectral
    bandwidth (of specturm squared!) useful to estimate wavelength bandwidth.
    """
    delta_nu_FWHM = 4*np.log(2)/(2*np.pi)/tauFWHM
    return delta_nu_FWHM

def delta_nu2delta_lam(delta_nu, lam0):
    """Given frequency bandwidth delta_nu_FWHM in intensity/power spectrum
    (squared of field spectrum/Fourier transform!) and center wavelength lam0,
    approximate delta lambda FWHM (power spectrum). Approximated by error
    propagation assumption
    delta_x = del(f)/del(y)*delta_y.
    """
    #not my original source, but result comparable to
    # http://toolbox.lightcon.com/tools/tbconverter/
    delta_lam = lam0**2/sc.c*delta_nu #actually has -1, but here use abs()
    return delta_lam


def Ppeak_from_Wtot(Wtot, tauFWHM, pulse='gauss'):
    """
    Calculate the peak laser pulse power from the total pulse energy Wtot [J],
    and the pulse FWHM duration tauFWHM [s] (measured in intensity FWHM).
    If pulse='gauss' is used, a correction factor is applied to correctly 
    calculate Ppeak via
    Wtot = Integrate[Ppeak * Exp[-4 ln2 t^2/tauFWHM^2],{t,-Inf,Inf}]
         = Ppeak * tauFWHM * sqrt(pi/(4 ln2))
    -> Ppeak ~~ 0.94 * Wtot / tauFWHM
    If pulse='rect' is used, a step pulse is assumed with power Ppeak and
    duration tauFWHM, such that
    Ppeak = Wtot / tauFWHM

    Parameters
    ----------
    Wtot : float
        Total pulse energy in [J]
    tauFWHM : float
        FWHM pulse duration (measured in intensity FWHM)
    pulse : str, optional
        'gauss' or 'rect'. The default is 'gauss'.

    Returns
    -------
    Ppeak in [W]

    """
    if pulse=='gauss':
        Ppeak = Wtot / tauFWHM
        Ppeak /= np.sqrt(np.pi/4/np.log(2))
    elif pulse=='rect':
        Ppeak = Wtot / tauFWHM
    else:
        raise ValueError(f'Invalid argument for pulse: {pulse}')
    return Ppeak

# for backward compatibility only!
Ppeak_from_Etot = Ppeak_from_Wtot
from .airybeams import airy_Ipeak_from_Ppeak as Ipeak_from_Ppeak
from .airybeams import f_number2airy_radius, airy_rad2airy_FWHM
from .airybeams import airy_rad2airy_FWHM, airyFWHM_from_airyRad
from .airybeams import airyRad_from_fNo


def E_from_Ipeak(Ipeak):
    """E0 amplitude for complex notation E(r,t)=E0 exp(i(k r-omega t))"""
    return np.sqrt(2/(sc.epsilon_0 * sc.c)*Ipeak)


def f_number(f, beam_diam):
    """Calculate the f-Number for a given focal length and beam diameter.
    Read as f/(returned number)"""
    return f / beam_diam

def NA_from_fNo(f_num):
    """Return the Numerical aperture (NA) for a given f_number"""
    return np.sin(np.arctan(1/(2*f_num)))


f_number2NA = NA_from_fNo


def I_from_E(E_field):
    """Input number or vector as real E-field [V/m] and calculate
    "instantaneous" intensity."""
    return 1/2*sc.epsilon_0*sc.c*E_field**2


def a0_from_E(E0, lam):
    omega_L = lam2omega(lam)
    return sc.e*E0 / (omega_L*sc.m_e*sc.c)


def a0_from_I(I, lam):
    return a0_from_E(E_from_Ipeak(I), lam)


def Nphotons_from_Etot(Etot, lam):
    """Assuming all photons have an energy corresponding to the central
    wavelength lambda, the number of of photons is just Etot/Ephot.
    """
    Ephot = sc.h*sc.c/lam
    return Etot/Ephot

