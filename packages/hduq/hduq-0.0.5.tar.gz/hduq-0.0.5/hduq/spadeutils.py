import numpy as np
from scipy.special import hermite, factorial, j1, erf
from scipy.integrate import quad
from scipy.optimize import minimize


from functools import wraps

__all__ = []

def export(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    __all__.append(func.__name__)
    return wrapper



@export
def jinc(x):
    is_scalar = np.isscalar(x)
    x = np.asarray(x, dtype=np.float64)
    result = np.empty_like(x)

    mask = x != 0
    result[~mask] = 1.0
    result[mask] = (2 * j1(x[mask])) / x[mask]

    return result.item() if is_scalar else result



@export
def ThinLens(U_input):
    Ny, Nx = U_input.shape
    N = max(Nx, Ny)
    U_pad = np.zeros((N, N), dtype=complex)

    start_y = (N - Ny) // 2
    start_x = (N - Nx) // 2
    U_pad[start_y : start_y + Ny, start_x : start_x + Nx] = U_input

    U_focal_pad = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(U_pad)))
    U_focal = U_focal_pad[start_y : start_y + Ny, start_x : start_x + Nx]

    return U_focal



class _PSF:
    def __init__(self, sigma=1, bounds=(None, None), pixel_size=1):
        self.sigma = sigma
        self.pixel_size = pixel_size
        self.bounds = (
            bounds[0] if bounds[0] is not None else np.round(-6 * sigma / pixel_size), 
            bounds[1] if bounds[1] is not None else np.round( 6 * sigma / pixel_size)
        )
        self.pixels = int(self.bounds[1] - self.bounds[0])


    def pdf(self, x, s=0):
        return np.abs(self.psf(x, s))**2
    

    def prob(self, s=0):
        pdf = lambda x: self.pdf(x, s)
        p = []
        for j in np.arange(self.bounds[0], self.bounds[1] + 1, 1):
            p.append(quad(pdf, self.pixel_size*j - self.pixel_size/2, self.pixel_size*j + self.pixel_size/2, limit=1000)[0])
        return np.array(p)


    def gen(self, s=0, photons=1):
        p = self.prob(s)
        outcomes = np.random.choice(len(p), photons, p=p/p.sum())
        return np.histogram(outcomes, bins=self.pixels, range=(0, self.pixels))[0]


    def fit(self, data):
        raise(NotImplementedError)



@export
class SincPSF(_PSF):
    def psf(self, x, s=0):
        return (self.sigma*np.pi)**-0.5 * np.sinc((x-s) / (self.sigma*np.pi))



@export
class JincPSF(_PSF):
    def psf(self, x, s=0):
        return ((3*np.pi) / (32*self.sigma))**0.5 * jinc((x-s) / self.sigma)



@export
class GausPSF(_PSF):
    def psf(self, x, s=0):
        return (2*np.pi*self.sigma**2)**-0.25 * np.exp(-((x-s)**2) / (4*self.sigma**2))
    
    @staticmethod
    def fit(data, smooth=1e-10, scale=1, **kwargs):
        if data.ndim != 1:
            raise ValueError
        data = data / np.sum(data)
        k = np.arange(len(data))

        def target_func(loc):
            z1 = (k - loc + 0.5) / (scale * (2**0.5))
            z2 = (k - loc - 0.5) / (scale * (2**0.5))
            uk = erf(z1)/2 - erf(z2)/2  + smooth
            nll = -np.sum(data * np.log(uk) - uk - (data * np.log(data) - data))
            grad = -(scale*(2*np.pi)**0.5) * np.sum((-np.exp(-z1**2) + np.exp(-z2**2)) * (data/uk - 1))
            return nll, grad
        
        result = minimize(target_func, **kwargs)
        if result.success:
            msg = result.message
        else:
            raise RuntimeError(f'not converged: {msg}')
        
        return result.x



class _Modes:
    def __init__(self, q, sigma=1):
        self.q = q
        self.sigma = sigma

        self._c_term = (2*np.pi*self.sigma**2)**-0.25
        self._exp_term = lambda x: np.exp(-x**2 / (4*self.sigma**2))



@export
class HG(_Modes):
    def __init__(self, q, sigma=1):
        if q % 1 != 0 or q < 0:
            raise ValueError('For HG modes, q must be a natural number.')
        super().__init__(q, sigma)

        if self.q == 0:
            self._term1 = 1
            self._term2 = 1
        else:
            self._term1 = (2**self.q * factorial(self.q))**-0.5
            self._H = hermite(self.q)


    def wave_function(self, x):
        _x = x / (2**0.5 * self.sigma)
        if self.q != 0:
            self._term2 = 2*_x if self.q == 1 else self._H(_x)
        return self._c_term * self._term1 * self._term2 * self._exp_term(x)



@export
class PM(_Modes):
    def __init__(self, q, sigma=1):
        if q not in (-1, 1):
            raise ValueError('For PM modes, q must -1 or 1.')
        super().__init__(q, sigma)


    def wave_function(self, x):
        self._term = (1 + self.q * x / self.sigma) * 2**-0.5
        return self._c_term * self._term * self._exp_term(x)



@export
def Born(s, modes: _Modes, psf: _PSF):
    result = []
    for _s in np.atleast_1d(s):
        fun = lambda x: modes.wave_function(x) * psf.psf(x, _s) 
        result.append(np.abs(quad(fun, -np.inf, np.inf)[0])**2)
    return np.array(result)



@export
def FisherInfo(s, modes: _Modes, psf: _PSF, ds=1e-8):
    p1 = Born(s+ds, modes, psf)
    p2 = Born(s-ds, modes, psf)
    dp = p1 - p2
    dv = dp/(2*ds)
    return dv**2 / p1
