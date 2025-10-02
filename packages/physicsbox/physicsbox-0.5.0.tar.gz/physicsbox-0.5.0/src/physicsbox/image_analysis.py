# -*- coding: utf-8 -*-
"""
Collection of functions and classes helpful in analysing
focus images.

I am not sure what is the best structure yet, for now
just shove anything in here related to image analysis,
maybe will move again!

Created on Thu Aug 21 15:43:08 2025

@author: Leonard.Doyle
"""

import numpy as np


def radially_integrate_image(img, R, numpoints, dx):
    """
    Inputs:
    * img: a 2D array to integrate over
    * R: a 2D array of radius at each pixel, generated e.g. by meshgrid
        or physicsbox-ImgCoordSys
    * numpoints: number of different radii to return from 0 to max(R)
    * dx: length element to ensure integral is independent of scaling/
        sampling
    
    `nan`s in the input image will have 0.0 contribution to integral.
    """

    """
    asked ChatGPT:
    ```
    please speed up this code:
    r_enc = np.linspace(0,cc.R.max(),500)
    E_enc = np.zeros_like(r_enc)
    for i, r in enumerate(tqdm(r_enc)):
        E_enc[i] = (intensity[cc.R<=r]).sum()*dx**2
    ```

    Reply: `Which would you prefer — exact but a bit heavier (Option 1)
    or fast & approximate (Option 2)?`
    Option 1 is based on resorting the array according to the radius value in
    `cc.R`.
    Option 2 is similar, but uses the histogram function to bin the resulting
    range of radii into equidistant bins.

    __Result after testing__: both are blazingly fast compared to what I was
    doing. The first option is closer to the original, so keep that.
    """
    # Flatten arrays
    R_flat = R.ravel()
    img_nonnan = img.copy()
    # cannot cope with NaN below, would add 0.0 to integral anyway
    img[np.isnan(img)] = 0.0
    I_flat = img.ravel()
    
    # Sort pixels by radius
    order = np.argsort(R_flat)
    R_sorted = R_flat[order]
    I_sorted = I_flat[order]
    
    # Cumulative integral (sum of intensities up to each radius)
    cum_I = np.cumsum(I_sorted) * dx**2

    # since we use the trick here to accumulate values based on their actual
    # occurring radius values in the array, sub-pixel steps are impossible.
    # To get them onto a regular range, need to interpolate.
    # ChatGPT suggested numpy.interp instead of scipy.interpolate, so we
    # can only use linear interpolation, but that seems better than
    # simulating some better resolution by smoothing things out
    r_enc = np.linspace(0,np.max(R),numpoints)
    E_enc = np.interp(r_enc, R_sorted, cum_I)
    return r_enc, E_enc


def area_above_threshold(img, threshold, dx=1):
    """
    Calculate the area where the image is above the
    threshold value.
    Essentially do `np.sum(img >= threshold)` but
    much faster when supplied a list of thresholds.

    Pass `dx` to scale the integral correctly.
    """

    """
    Based on manual, slow original below.
    Again, ChatGPT was able to recommend a method based on sorting to
    avoid looping over each threshold:
    ```
    cool thanks, now please optimize this

    thresholds = np.linspace(1, 0, 2000)
    A_above_threshold = np.zeros_like(thresholds)
    relative_intensity = intensity/np.nanmax(intensity)
    for i, threshold in enumerate(tqdm(thresholds)):
        array_above_thresh = relative_intensity >= threshold
        A_above_threshold[i] = array_above_thresh.sum()*dx**2
    ```
    """
    vals = img.ravel()
    vals_sorted = np.sort(vals)
    
    # For each threshold, find how many pixels are >= threshold
    idx = np.searchsorted(vals_sorted, threshold, side="left")
    
    # Convert indices into areas
    #TODO think about/test if index may be off by one.
    # however, I hope this effect will be small enough always.
    A_above_threshold = (len(vals) - idx) * dx**2
    return A_above_threshold

