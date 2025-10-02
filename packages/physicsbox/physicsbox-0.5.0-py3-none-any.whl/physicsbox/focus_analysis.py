# -*- coding: utf-8 -*-
"""
Collection of functions and classes helpful in analysing
a (potentially high dynamic range) focus image.

Based on CALA procedures, your mileage may vary.

Created on Thu Aug 21 18:48:23 2025

@author: Leonard.Doyle
"""


import numpy as np

from .units import *
from .utils import ImageCoordSys
from .optics.utilities import a0_from_I
from .image_analysis import area_above_threshold, radially_integrate_image

def all_in_one_analyse_focus(intensity,
                             dx,
                             lambda_,
                             ):
    #NB normed here is max=1 not integral=1 !!
    intensity_normed = intensity/np.nanmax(intensity)

    cy, cx = np.unravel_index(np.nanargmax(intensity), intensity.shape)
    cc = ImageCoordSys(intensity, cx=cx, cy=cy, dx=dx)

    metrics = {}
    metrics['Ipeak'] = intensity.max()
    metrics['a0'] = a0_from_I(metrics['Ipeak'], lambda_)

    metrics['A_above_FWHM'] = area_above_threshold(intensity_normed, 1/2, dx)
    metrics['A_above_e'] = area_above_threshold(intensity_normed, 1/np.e, dx)
    metrics['A_above_e2'] = area_above_threshold(intensity_normed, 1/np.e**2, dx)
    metrics['A_above_1e13Wcm2'] = area_above_threshold(intensity, 1e13*W/cm**2, dx) # for ionization limit

    metrics['r_eff_above_FWHM'] = np.sqrt(metrics['A_above_FWHM']/np.pi)
    metrics['r_eff_above_e'] = np.sqrt(metrics['A_above_e']/np.pi)
    metrics['r_eff_above_e2'] = np.sqrt(metrics['A_above_e2']/np.pi)
    metrics['r_eff_above_1e13Wcm2'] = np.sqrt(metrics['A_above_1e13Wcm2']/np.pi)

    metrics['d_eff_above_FWHM'] = 2*metrics['r_eff_above_FWHM']
    metrics['d_eff_above_e'] = 2*metrics['r_eff_above_e']
    metrics['d_eff_above_e2'] = 2*metrics['r_eff_above_e2']
    metrics['d_eff_above_1e13Wcm2'] = 2*metrics['r_eff_above_1e13Wcm2']

    # given relative to 1 not in SI otherwise we need to start
    # arguing about Energy or Intensity, need to know tau_effective, ...
    metrics['W_encl_FWHM'] = np.nansum(intensity[cc.R<=metrics['r_eff_above_FWHM']])/np.nansum(intensity)
    metrics['W_encl_e'] = np.nansum(intensity[cc.R<=metrics['r_eff_above_e']])/np.nansum(intensity)
    metrics['W_encl_e2'] = np.nansum(intensity[cc.R<=metrics['r_eff_above_e2']])/np.nansum(intensity)
    metrics['W_encl_1e13Wcm2'] = np.nansum(intensity[cc.R<=metrics['r_eff_above_1e13Wcm2']])/np.nansum(intensity)

    lineout_x = intensity[cy, :]
    lineout_y = intensity[:, cx]

    r_enclosed, W_enclosed = radially_integrate_image(intensity, cc.R, 5000, dx)/np.nansum(intensity)

    return metrics, lineout_x, lineout_y, r_enclosed, W_enclosed
    
    
