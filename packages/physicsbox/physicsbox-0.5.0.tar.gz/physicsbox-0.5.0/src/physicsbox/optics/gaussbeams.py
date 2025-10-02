# -*- coding: utf-8 -*-
"""
Collection of functions and classes helpful in dealing with gaussian beams
both in temporal and spatial domain.

Definition of temporal Gauss (E-field):
    E(t) = E0 exp(-t**2/(2 tau**2))
    I(t) ~ E0**2 exp(-t**2/tau**2)
--> FWHM defined where Intensity drops to half of peak Int.
--> tau  defined where Intensity drops to 1/e of peak Int.!
    == where E-field drops to 1/sqrt(e) = std dev.

Definition of spatial Gauss (E-field):
    E(r,z=0) ~ E0 exp(-r**2/w_0**2) --> waist defined in E-field
    I(r,z=0) ~ E0**2 exp(-2r**2/w_0**2) #important for FWHM
--> FWHM defined where Intensity drops to half of peak Int.
--> w_0 defined where E-field (!!) drops to 1/e, therefore Int. drops to 1/e**2

Created on Fri Sep 13 19:20:08 2019

@author: Leonard.Doyle
"""

import numpy as np
import numexpr as ne #save memory on numpy expressions and use multithread
import scipy.special
import scipy.constants as sc
from scipy.constants import c as c_ # need this in ne.eval() but want to make it obvious, use _


# from ..tictoc import tic, printtoc
from ..units import *

from .utilities import lam2k, lam2omega

#temporal tau and FWHM always defined in Intensity not E-field
#only in this convention is 4ln2 correct!
fwhm2tau = lambda fwhm: fwhm / np.sqrt(4*np.log(2))
tau2fwhm = lambda tau: tau * np.sqrt(4*np.log(2))

def fwhm2tau_eff(fwhm, pulse='gauss'):
    """Given a gaussian pulse with FWHM duration `fwhm`, calculate an
    effective pulse duration tau_eff which keeps the time integral
    constant.
    
    Etot = Ppeak * tauFWHM * sqrt(pi/4ln2)
    Etot = Ppeak * tau_eff
    -> tau_eff = 1.0645 * tauFWHM
    
    just using the tauFWHM and multiplying by Ppeak will give a 6%
    wrong total energy/ integral, but tau_eff can be used as an
    "equivalent" square pulse with same peak power/amplitude and
    same integral.

    """
    assert pulse == 'gauss', 'Only gaussian temporal shape supported so far'
    tau_eff = fwhm * np.sqrt(np.pi/(4*np.log(2)))
    return tau_eff

#for spatial Gaussian. Caution: waist defined in E-field, FWHM in intensity!
# --> FWHM defined where Intensity drops to half of peak Int.
# --> w_0 defined where field (!) drops to 1/e, therefore I drops to 1/e**2
fwhm2waist = lambda fwhm: fwhm / np.sqrt(2*np.log(2))
waist2fwhm = lambda w_0: w_0 * np.sqrt(2*np.log(2))

z_Rayleigh = lambda waist0, lam: np.pi* waist0**2/lam

# waist_at_z = lambda z, w0, z_R:  w0 * np.sqrt(1+(z/z_R)**2)
waist_at_z = lambda z, w0, z_R:  ne.evaluate('w0 * sqrt(1+(z/z_R)**2)')

#R_curv = lambda z, z_R: z*(1+np.divide(z_R, z, out=np.full_like(z,np.inf), where=z!=0)**2) #avoid div by 0
# encountered ugly to fix problems using R as it diverges for z=0, use
# 1/R instead since this is multiplicative in spatial Gauss, circumventing div by 0 completely
R_inverse = lambda z, z_R: ne.evaluate('z / (z**2+z_R**2)')
# R_inverse = lambda z, z_R: z / (z**2+z_R**2)


class GeneralizedCoordField:
    """Use any of the defined cylindrical fields in generalized coordinates
    by doint an implicit coordinate transform"""
    def __init__(self, field, xyz0 = [0,0,0], t0=0.0, theta=0,
                 phi = 0, e_k=None):
        self.field = field
        if e_k is None:
            #TODO check sin/cos/+- coord sys convention
            e_k = [np.sin(theta)*np.cos(phi),
                   np.sin(theta)*np.sin(phi),
                   np.cos(theta)]
        else:
            pass #TODO make sure it's normalized
        self.e_k = np.asarray(e_k)
        self.ex = self.e_k[0]
        self.ey = self.e_k[1]
        self.ez = self.e_k[2]
        self.xyz0 = np.asarray(xyz0)
        self.x0 = xyz0[0]
        self.y0 = xyz0[1]
        self.z0 = xyz0[2]
        self.t0  = t0
    
    
    def field_at(self, x, y, z, t):
        # a little tricky: allow inputs on any shape as long as shape is 
        # same for all -> must rely on elementwise operations where possible
        tp = t - self.t0
        xp = x - self.x0
        yp = y - self.y0
        zp = z - self.z0
        zz = self.ex * xp
        zz += self.ey * yp
        zz += self.ez * zp
        rr = xp**2
        rr += yp**2
        rr += zp**2
        rr -= zz**2
        # close to optical axis, tiny numbers can cause number below 0
        # which cause hickup in sqrt. Debug test:
        ddd = rr[rr<0]
        if len(ddd) > 0:
            print(len(ddd), min(ddd), max(ddd))
        # -> of over 30000 occurences, min is -1e26, max is -3e58
        # -> setting to 0 is fine
        rr[rr<0] = 0
        rr = np.sqrt(rr)
        return self.field.field_at_rz(rr, zz, tp)
    
    
    def real_field_at(self, x, y, z, t):
        return np.real(self.field_at(x, y, z, t))
    
    def int_instant_at(self, x, y, z, t):
        """Instantaneous intensity, i.e. real part of field squared and
        units and magnitude of intensity (W/m^2).
        Inputs x, y, z, t must either be scalar, one vector and others
        scalar, or a meshgrid with identical size for all.
        Returns Intensity in SI if field defined in SI"""
        fieldreal = self.real_field_at(x, y, z, t)
        Int = fieldreal
        Int *= Int #square without using extra memory
        Int *= 1/2*sc.c*sc.epsilon_0
        
        return Int
    
    def int_envelope_at(self, x, y, z, t):
        """
        Intensity envelope.
        
        Inputs x, y, z, t must either be scalar, one vector and others
        scalar, or a meshgrid with identical size for all.
        Returns Intensity in SI if field defined in SI
        """
        """
        Assumption: E(r,z,t) = exp(i omega0 t)*E(r,z,t_slow)
        where last part varies so slow in t that cycle average of
        E^2=exp(i 2omega0 t)*E(r,z,t_slow)^2 is still almost 0
        --> in I = <Re(E)^2>_cycleavg the EE and E*E* terms are 0, so:
            I = 1/2 c eps_0 |E(r,z,t_slow)|^2
        is a valid approximation.
        """
        field = self.field_at(x, y, z, t)
        Int = np.abs(field) #abs squared = E * Econjugate
        Int *= Int #square without using extra memory
        Int *= 1/2*sc.c*sc.epsilon_0
        
        return Int


class ScalarCylindricalFieldBase:
    """Base class for the other fields to generalize the interface and
    define some common function.
    A (complex) vector can be defined as amplitude, but the field evolution
    itself is treated scalar.
    Also, while the amplitude vector contains direction information, the
    field itself is evaluated in cylindrical coordinates. This is just
    for convenience since it works with plane wave and gauss beam."""
    def __init__(self):
        pass
    
    def field_at(self, xyz, t):
        """Return the field at point r=(x,y,z) and time t."""
        x,y,z = xyz
        r = np.sqrt(x**2+y**2)
        return self.field_at_rz(r, z, t)
    
    def field_at_rz(self, r, z, t):
        """Assuming most fields will have cylindrical symmetry (even though
        a defined polarization in xyz), enter in r, z, t here."""
        raise NotImplementedError('Any field subclass must override this')
    
    def real_field_at(self, xyz, t):
        """Return the physical (real valued) field at cartesian point (x,y,z)
        at time t."""
        return np.real(self.field_at(xyz, t))
    
    def real_field_at_rz(self, r, z, t):
        """Return the physical (real valued) field in cylindrical coords (r,z)
        at time t."""
        return np.real(self.field_at_rz(r, z, t))
    
    def int_instant_at_rz(self, r, z, t):
        """Instantaneous intensity, i.e. real part of field squared and
        units and magnitude of intensity (W/m^2).
        Inputs r, z, t must either be scalar, one vector and others
        scalar, or a meshgrid with identical size for all.
        Returns Intensity in SI if field defined in SI"""
        fieldreal = self.real_field_at_rz(r, z, t)
        Int = fieldreal
        Int *= Int #square without using extra memory
        Int *= 1/2*sc.c*sc.epsilon_0
        
        return Int
    
    def int_envelope_at_rz(self, r, z, t):
        """
        Intensity envelope.
        
        Inputs r, z, t must either be scalar, one vector and others
        scalar, or a meshgrid with identical size for all.
        Returns Intensity in SI if field defined in SI
        """
        """
        Assumption: E(r,z,t) = exp(i omega0 t)*E(r,z,t_slow)
        where last part varies so slow in t that cycle average of
        E^2=exp(i 2omega0 t)*E(r,z,t_slow)^2 is still almost 0
        --> in I = <Re(E)^2>_cycleavg the EE and E*E* terms are 0, so:
            I = 1/2 c eps_0 |E(r,z,t_slow)|^2
        is a valid approximation.
        """
        field = self.field_at_rz(r, z, t)
        Int = np.abs(field) #abs squared = E * Econjugate
        Int *= Int #square without using extra memory
        Int *= 1/2*sc.c*sc.epsilon_0
        
        return Int


class PlaneWaveMonochromatic(ScalarCylindricalFieldBase):
    def __init__(self, A0, lam):
        self.A0 = A0 #implicitly allow complex vector!
        self.lam = lam
        self.k = lam2k(self.lam) #TODO treat as immutable
        self.omega0 = lam2omega(lam)
    
    def field_at_rz(self, r, z, t):
        # tprime = t - z/sc.c
        e1 = -1j * self.k * z
        return self.A0 * np.exp(e1 + 1j*self.omega0*t)


class PlaneWaveGaussTemporal(ScalarCylindricalFieldBase):
    def __init__(self, A0, tau, lam):
        self.A0 = A0 #implicitly allow complex vector!
        self.tau = tau
        self.lam = lam
        self.k = lam2k(self.lam) #TODO treat as immutable
        self.omega0 = lam2omega(lam)
    
    def field_at_rz(self, r, z, t):
        tprime = t - z/sc.c
        e1 = np.exp(1j*self.omega0*tprime) #+1j*np.pi/2)
        e2 = np.exp(-1/2*(tprime/self.tau)**2)
        return self.A0 * e1 * e2
    
class GaussSpatialMonochromatic(ScalarCylindricalFieldBase):
    def __init__(self, A0, w0, lam):
        self.A0 = A0 #implicitly allow complex vector!
        self.w0 = w0
        self.lam = lam
        self.k = lam2k(self.lam) #TODO treat as immutable
        self.z_R = z_Rayleigh(w0, lam)
        self.omega0 = lam2omega(lam)
    
    def field_at_rz(self, r, z, t):
        """Inputs r, z, t must either be scalar, one vector and others
        scalar, or a meshgrid with identical size for all.
        Returns complex field, not physical!"""
        #spatial part
        w = waist_at_z(z, self.w0, self.z_R)
        # R = R_curv(z, self.z_R)
        R_inv = R_inverse(z, self.z_R)
        
        e1 = -r**2/w**2
        # e2 = -1j * self.k * r**2/(2*R) #problem at R=0
        e2 = -1j * self.k * r**2/2*R_inv #solved by using 1/R
        e3 = -1j * self.k * z
        e4 = 1j * np.arctan(z/self.z_R)
        spatial = self.A0 * self.w0/w * np.exp(e1+e2+e3+e4)
        #temporal part
                
        e5 = 1j*self.omega0*t
        return spatial * np.exp(e5)


class GaussSpatioTemporal(ScalarCylindricalFieldBase):
    def __init__(self, A0, w0, tau, lam):
        self.A0 = A0 #implicitly allow complex vector!
        self.w0 = w0
        self.tau = tau
        self.lam = lam
        self.k = lam2k(self.lam) #TODO treat as immutable
        self.z_R = z_Rayleigh(w0, lam)
        self.omega0 = lam2omega(lam)
        self.polarization = 1 #dummy, scalar
    
    def field_at_rz(self, r, z, t):
        """Inputs r, z, t must either be scalar, one vector and others
        scalar, or a meshgrid with identical size for all.
        Returns complex field, not physical!"""
        # spatial part
        w = waist_at_z(z, self.w0, self.z_R)
        # R = R_curv(z, self.z_R)
        R_inv = R_inverse(z, self.z_R) #use *R_inv to avoid div by 0
                
        A0, w0 = self.A0, self.w0
        k = self.k
        z_R = self.z_R
        if np.isscalar(r):
            if np.isscalar(z):
                if np.isscalar(t):
                    #edge case all 3 scalar: should return a scalar, but for
                    # numexpr need a array field
                    if np.isscalar(A0):
                        field = np.zeros((1,1),dtype=complex)
                    else:
                        field = np.zeros_like(A0, dtype=complex)
                        #TODO there will be more cases where this will break
                        # for vectorial A0, think about this
                else:
                    field =np.zeros_like(t, dtype=complex)
            else:
                field = np.zeros_like(z, dtype=complex)
        else:
            field = np.zeros_like(r, dtype=complex)
        ne.evaluate('A0*w0/w*exp(-r**2/w**2)', out=field)
        ne.evaluate('field*exp(1j*(-k*z -k*r**2/2 *R_inv +arctan(z/z_R)))',
                    out=field)

        # temporal part
        omega0 = self.omega0
        ne.evaluate('field*exp(1j*(omega0*t))', out=field)

        tau = self.tau
        sc_c = sc.c
        tretard = ne.evaluate('t- z/sc_c - r**2/(2*sc_c)*R_inv')
        ne.evaluate('field*exp(-1/(2*tau**2)*tretard**2)',
                    out=field)
        return field
    
    def int_tretard_at_rz(self, r, z, t):
        """Time/retarded time of intensity at each point (without oscillation)"""
        #spatial part
        R_inv = R_inverse(z, self.z_R)
        
        #temporal part
        # e5 = 1j*self.omega0*t #Intensity envelope no omega oscillation
        tretard = t- z/sc.c - r**2/(2*sc.c)*R_inv
        # e6 = -1/(self.tau**2)*tretard**2 #1/2tau becomes 1/tau in Intensity
        # Ispatial *= np.exp(e6)
        return tretard




class MultiLaguerreGaussSpatioTemporal(ScalarCylindricalFieldBase):
    def __init__(self, w0, tau, lam, l, p, E_lp, phi0_lp):
        """
        the MultiLaguerreGauss spatiotemporal beam is closely related
        to the annular beam described by Karbstein, Mosman+
        We start with a generic implementation of Laguerre Gauss beams.
        But because we need a superposition of many, this class
        calculates all of them to save some time on the prefactors.
        The temporal part is simply overlayed by a Gaussian envelope
        travelling from left to right (positive z) this is of course
        nonsense far outside the focus (but here paraxial is also nonsense,
        so anyway things should be taken with a grain of salt there.)

        They all share the same w0 (or equivalent scale length) but can
        each have individual amplitude, l, p and global phase offset

        L, P, E_lp, Psi_lp -> must have same length!
        """
        assert len(l) == len(p)
        assert len(l) == len(E_lp)
        assert len(l) == len(phi0_lp)
        
        # self.A0 = A0 #implicitly allow complex vector!
        #TODO have not tested with vectorial amplitude, use scalar for now!
        self.w0 = w0
        self.tau = tau
        self.lam = lam
        self.k = lam2k(self.lam) #TODO treat as immutable
        self.zR = z_Rayleigh(w0, lam)
        self.omega0 = lam2omega(lam)
        self.l = l
        self.p = p
        self.E_lp = E_lp
        self.phi0_lp = phi0_lp
    
    def field_at_rz(self, r, phi, z, t):
        """Inputs r, phi, z, t must either be scalar, one vector and others
        scalar, or a meshgrid with identical size for all.
        Returns complex field, not physical!"""
        tau = self.tau # shorthand, also should later allow optimization if not access self
        w0 = self.w0
        zR = self.zR
        k = self.k
        omega0 = self.omega0


        if np.isscalar(r):
            if np.isscalar(z):
                if np.isscalar(t):
                    #edge case all 3 scalar: should return a scalar, but for
                    # numexpr need a array field
                    field = np.zeros((1,1),dtype=complex)
                else:
                    field =np.zeros_like(t, dtype=complex)
            else:
                field = np.zeros_like(z, dtype=complex)
        else:
            field = np.zeros_like(r, dtype=complex)

        w = waist_at_z(z, w0, zR)
        
        """
        Word on scipy genlaguerre: generates a orhtopoly1d object
        which contains the polynomial coefficients somehow.

        Warning in documentation:
        Computing values of high-order polynomials (around order > 20) using polynomial
        coefficients is numerically unstable. To evaluate polynomial values, the eval_*
        functions should be used instead.
        -> use eval_laguerre to be safe
        """
        psi_Guouy = np.arctan(z/zR) #used in calcs below
        laguerre_x = ne.evaluate('2*r**2/w**2')
        
        for l_, p_, E_, phi0_ in zip(self.l, self.p, self.E_lp, self.phi0_lp):
            l_abs = np.abs(l_)
            term1 = ne.evaluate('(sqrt(2)*r/w)**l_abs')
            # tic()
            L_lp = scipy.special.eval_genlaguerre(p_, l_abs, laguerre_x)
            # printtoc()
            # phaseterm: Karbstein uses vector epsilon, we will have to go component wise, do only scalar for now
            # in contrast to Karbstein, we use complex function not cos()/Real part -> should that yield a factor of 2 or something?
            # so we can easily move out a lot of phase factors from the sum, right?
            #psi_x_original_Karbstein = (omega0*t -k*z) - z/zR * (r/w)**2 + psi_Guouy
            # Phi_lp = ne.evaluate('(l_abs + 2*p_)*psi_Guouy + l_*phi + phi0_')
            # phaseterm = np.exp(-1j*Phi_lp)
            phaseterm = ne.evaluate('exp(-1j*((l_abs + 2*p_)*psi_Guouy + l_*phi + phi0_))')

            # term_lp = ne.evaluate('E_ * term1 * L_lp * phaseterm')
            # field += term_lp
            ne.evaluate('field + (E_ * term1 * L_lp * phaseterm)', out=field)
        
        # global_Psi_x = -k*z - z/zR * (r/w)**2 + psi_Guouy # extracted from phaseterm inside sum, as lp-indep.
        # global_phaseterm = np.exp(-1j*global_Psi_x)
        global_phaseterm = ne.evaluate('exp(-1j*(-k*z - z/zR * (r/w)**2 + psi_Guouy))')
        # field *= global_phaseterm
        # field *= w0/w * np.exp(-(r/w)**2)
        ne.evaluate('field * (w0/w * exp(-(r/w)**2)) * global_phaseterm', out=field)

        #temporal part completely separable (since we assume only z-t envelope, no curvature or realistic modeling)
        # psi_temporal = omega0*t
        # phaseterm_temporal = np.exp(-1j*psi_temporal)
        # phaseterm_temporal = ne.evaluate('np.exp(-1j*omega0*t)')
        # envelope_z_t = np.exp(-((z-sc.c*t)/(sc.c*tau/2))**2)
        # field *= envelope_z_t 
        # field *= phaseterm_temporal
        ne.evaluate('field * exp(-1j*omega0*t) * exp(-((z-c_*t)/(c_*tau/2))**2)', out=field)
        return field
    
    def int_tretard_at_rz(self, r, z, t):
        """Time/retarded time of intensity at each point (without oscillation)"""
        #spatial part
        R_inv = R_inverse(z, self.z_R)
        
        #temporal part
        # e5 = 1j*self.omega0*t #Intensity envelope no omega oscillation
        tretard = t- z/sc.c - r**2/(2*sc.c)*R_inv
        # e6 = -1/(self.tau**2)*tretard**2 #1/2tau becomes 1/tau in Intensity
        # Ispatial *= np.exp(e6)
        return tretard



class MultiLaguerreGaussSpatioTemporal_recursive(ScalarCylindricalFieldBase):
    def __init__(self, w0, tau, lam, l, p, E_lp, phi0_lp):
        """
        attempt to optimize this problem specifically for the flattened
        gaussian below:
        can exploit the recursive definition. That implies two conditions:
        1) all modes have to share the same l.
        2) the vector `p` must be ordered, starting at 0, with no gaps, i.e. p=np.arange(N+1)

        """
        assert len(l) == len(p)
        assert len(l) == len(E_lp)
        assert len(l) == len(phi0_lp)
        assert np.all(np.asarray(p) == np.arange(np.max(p)+1)), 'list of p must be ordered, starting at 0, no gaps'
        assert len(np.unique(l)) == 1, 'All modes must share same `l`'

        #TODO have not tested with vectorial amplitude, use scalar for now!
        self.w0 = w0
        self.tau = tau
        self.lam = lam
        self.k = lam2k(self.lam) #TODO treat as immutable
        self.zR = z_Rayleigh(w0, lam)
        self.omega0 = lam2omega(lam)
        self.l = l
        self.p = p
        self.E_lp = E_lp
        self.phi0_lp = phi0_lp

    def field_at_rz(self, r, z, t):
        return self.field_at_rphiz(r, 0, z, t)
    
    def field_at_rphiz(self, r, phi, z, t):
        """Inputs r, phi, z, t must either be scalar, one vector and others
        scalar, or a meshgrid with identical size for all.
        Returns complex field, not physical!"""
        tau = self.tau # shorthand, also should later allow optimization if not access self
        w0 = self.w0
        zR = self.zR
        k = self.k
        omega0 = self.omega0


        if np.isscalar(r):
            if np.isscalar(z):
                if np.isscalar(t):
                    #edge case all 3 scalar: should return a scalar, but for
                    # numexpr need a array field
                    field = np.zeros((1,1),dtype=complex)
                else:
                    field =np.zeros_like(t, dtype=complex)
            else:
                field = np.zeros_like(z, dtype=complex)
        else:
            field = np.zeros_like(r, dtype=complex)

        w = waist_at_z(z, w0, zR)
        
        """
        Word on scipy genlaguerre: generates a orhtopoly1d object
        which contains the polynomial coefficients somehow.

        Warning in documentation:
        Computing values of high-order polynomials (around order > 20) using polynomial
        coefficients is numerically unstable. To evaluate polynomial values, the eval_*
        functions should be used instead.
        -> use eval_laguerre to be safe
        """
        psi_Guouy = np.arctan(z/zR) #used in calcs below
        laguerre_x = ne.evaluate('2*r**2/w**2')
        l_ = np.unique(self.l)[0] # we made sure above that we can only have 1
        l_abs = np.abs(l_)
        
        # Wiki generalized Laguerre:
        # L_0^alpha = 1
        # L_1^alpha = 1 + alpha - x
        # L_k+1^alpha = [ (2k+1-alpha-x) L_k(x) - (k+alpha) L_(k-1)(x) ] / (k+1)
        # here alpha= |l| = same for all

        L_0 = 1 # independent of x
        L_1 = ne.evaluate('1 + l_abs - laguerre_x')

        for p_, E_, phi0_ in zip(self.p, self.E_lp, self.phi0_lp):
            # tic()
            if p_ == 0:
                L_lp = L_0
            elif p_ == 1:
                L_lp = L_1
                L_k_minus1 = L_0
                L_k = L_1
            else:
                # caution k is k-vector, k_ is index!
                k_ = p_ - 1 # since the recursion relation is for L_k+1 which is L_p for this step
                L_k_plus1 = ne.evaluate('1/(k_+1) * ((2*k_ + 1 + l_abs - laguerre_x) * L_k'
                                       '- (k_ + l_abs) * L_k_minus1)')
                L_lp = L_k_plus1 # for calculation in this step

                #save names for next step:
                L_k_minus1 = L_k
                L_k = L_k_plus1
            # printtoc()
            # phaseterm: Karbstein uses vector epsilon, we will have to go component wise, do only scalar for now
            # in contrast to Karbstein, we use complex function not cos()/Real part -> should that yield a factor of 2 or something?
            # so we can easily move out a lot of phase factors from the sum, right?
            #psi_x_original_Karbstein = (omega0*t -k*z) - z/zR * (r/w)**2 + psi_Guouy
            # Phi_lp = ne.evaluate('(l_abs + 2*p_)*psi_Guouy + l_*phi + phi0_')
            # phaseterm = np.exp(-1j*Phi_lp)
            phaseterm = ne.evaluate('exp(-1j*((l_abs + 2*p_)*psi_Guouy + l_*phi + phi0_))')

            # term_lp = ne.evaluate('E_ * L_lp * phaseterm')
            # field += term_lp
            ne.evaluate('field + (E_ * L_lp * phaseterm)', out=field)
        
        term1 = ne.evaluate('(sqrt(2)*r/w)**l_abs') # now outside loop since |l| const
        ne.evaluate('field * term1', out=field)

        # global_Psi_x = -k*z - z/zR * (r/w)**2 + psi_Guouy # extracted from phaseterm inside sum, as lp-indep.
        # global_phaseterm = np.exp(-1j*global_Psi_x)
        global_phaseterm = ne.evaluate('exp(-1j*(-k*z - z/zR * (r/w)**2 + psi_Guouy))')
        # field *= global_phaseterm
        # field *= w0/w * np.exp(-(r/w)**2)
        ne.evaluate('field * (w0/w * exp(-(r/w)**2)) * global_phaseterm', out=field)

        #temporal part completely separable (since we assume only z-t envelope, no curvature or realistic modeling)
        # psi_temporal = omega0*t
        # phaseterm_temporal = np.exp(-1j*psi_temporal)
        # phaseterm_temporal = ne.evaluate('np.exp(-1j*omega0*t)')
        # envelope_z_t = np.exp(-((z-sc.c*t)/(sc.c*tau/2))**2)
        # field *= envelope_z_t 
        # field *= phaseterm_temporal
        ne.evaluate('field * exp(-1j*omega0*t) * exp(-((z-c_*t)/(c_*tau/2))**2)', out=field)
        return field


class LaguerreGaussSpatioTemporal(MultiLaguerreGaussSpatioTemporal):
    def __init__(self, w0, tau, lam, l, p, E0, phi0):
        """
        single Laguerre Gauss mode with superimposed
        Gaussian temporal profile.
        """
         
        super().__init__(w0, tau, lam, [l,], [p,], [E0,], [phi0,])

def Heaviside(x):
    if x >= 0: return 1
    else: return 0

def c_pN(p,N):
    # from Karbstein (3.74)
    c = sum(scipy.special.binom(k,p) * 1/2**k for k in range(p,N+1))
    return c

def C_N(N):
    # from Karbstein (3.76)
    cc = sum(c_pN(p,N)**2 for p in range(N+1))
    return np.sqrt(cc)

def c_pNN(p, N_out, N_in):
    #C_N stays fixed!
    if N_in == 0:
        return c_pN(p,N_out)
    
    def Heaviside(x):
        if x >= 0: return 1
        else: return 0
    
    return c_pN(p,N_out) - Heaviside(N_in-p)*c_pN(p,N_in)

class FlattenedGaussSpatioTemporal(MultiLaguerreGaussSpatioTemporal_recursive):
    def __init__(self, w0, tau, lam, N, E0):
        """
        building upon the sum of several Laguerre Gaussian modes,
        this class creates a simple model for a flat top beam.
        For increasing order N, the beam looks more like a flat top.

        Inspired by Karbstein, Mosman+
        """
        p = np.arange(N+1)
        l = np.zeros_like(p, dtype=int)
        E_lp = np.asarray([c_pN(p_, N) for p_ in p])
        E_lp *= E0/C_N(N)
        phi0_lp = np.zeros_like(p)
        
        super().__init__(w0, tau, lam, l, p, E_lp, phi0_lp)


class AnnularFlattenedGaussSpatioTemporal(MultiLaguerreGaussSpatioTemporal_recursive):
    def __init__(self, w0, tau, lam, N, Np, E0):
        """
        building upon the "flattened Gaussian" beam profile
        introduced by Karbstein+

        we can put a central hole on axis by subtracting several
        lower modes from the flattened Gaussian.
        """
        p = np.arange(N+1)
        l = np.zeros_like(p, dtype=int)
        cpNs = [c_pNN(p_, N, Np) for p_ in p]
        E_lp = np.asarray(cpNs)
        E_lp *= E0/C_N(N)
        phi0_lp = np.zeros_like(p)
        
        super().__init__(w0, tau, lam, l, p, E_lp, phi0_lp)