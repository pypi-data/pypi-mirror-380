"""
:#######################################################
: Intervals Library originally created by Marco de Angelis
: Continuesly developed and refactored by Leslie Yu Chen
:#######################################################
"""

# Sequence: # Must have __len__() and __getitem__(). Ex.: Tuple, List, Range
# Sized: # It suffices to have len()
# Iterable: # Must have __iter__() and __next__(). Ex.: Dict, Set, Tuple, List, numpy.array
# from intervals.methods import (lo,hi,width,rad,mag,straddlezero,isinterval)

from __future__ import annotations
from typing import Optional, Any, Union
import numpy as np
import numpy
from numpy import ndarray, asarray, stack, transpose, zeros
import matplotlib.pyplot as plt
from .utils import safe_asarray
from ..mixins import NominalValueMixin

from .arithmetic import multiply, divide

MACHINE_EPS = 7.0 / 3 - 4.0 / 3 - 1

NUMERIC_TYPES = {
    "int",
    "float",
    "complex",  # Python numbers
    "int8",
    "int16",
    "int32",
    "int64",
    "intp",  # Numpy integers
    "uint8",
    "uint16",
    "uint32",
    "uint64",
    "uintp",  # Numpy unsigned integers
    "float16",
    "float32",
    "float64",
    "float_",  # Numpy floats and doubles
    "complex64",
    "complex128",
    "complex_",
}  # Numpy complex floats and doubles

INTEGERS = {
    "int",
    "int8",
    "int16",
    "int32",
    "int64",
    "intp",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
    "uintp",
}
# FLOATS =            {'float','float16','float32','float64','float_'}


def show(x: Interval) -> str:
    if len(x) == 0:
        return f"[{x.lo},{x.hi}]"
    elif len(x.shape) == 1:
        return "\n".join([f"[{xi.lo},{xi.hi}]" for xi in x])  # vector of intervals
    elif len(x.shape) == 2:
        n, d = x.shape
        return "\n".join(
            [" ".join([f"{xi.val}" for xi in x[i, :]]) for i in range(n)]
        )  # matrix of intervals
    else:
        return f"{x.val}"


class Interval(NominalValueMixin):
    """Interval is the main class"""

    def __init__(
        self,
        lo: Union[float, ndarray],
        hi: Optional[Union[float, ndarray]] = None,
        do_heavy_checks: bool = True,
    ) -> None:
        self._lo = safe_asarray(lo)
        if hi is None:
            hi = self._lo.copy()
        self._hi = safe_asarray(hi)
        if do_heavy_checks:
            self.run_heavy_checks()

    def run_heavy_checks(self):
        """Run heavy checks on the interval object"""
        assert np.all(
            self._lo <= self._hi
        ), "low larger than high, needed to invert the interval"
        self.__shape = self._lo.shape

    def __repr__(self):  # return
        return show(self)

    def __str__(self):  # print
        return show(self)

    def __len__(self):
        if self.unsized:
            return 0  # interval object is not sized, perhaps return an error: TypeError: len() of unsized object
        else:
            return self._lo.shape[0]

    def __iter__(self):  # https://realpython.com/introduction-to-python-generators/
        lo_iter, hi_iter = numpy.nditer(self.lo), numpy.nditer(self.hi)
        while True:
            try:
                yield Interval(lo=next(lo_iter), hi=next(hi_iter))
            except StopIteration:
                break
        pass

    def __next__(self):
        pass

    def __getitem__(self, i: Union[int, slice]):  # make class indexable
        return Interval(lo=self._lo[i], hi=self._hi[i])

    # * -------------- METHODS -------------- *#
    def to_numpy(self) -> np.ndarray:
        """transform interval objects to numpy arrays"""
        if self.scalar:
            return np.array([self.lo.item(), self.hi.item()])
        else:
            return np.asarray((self.lo, self.hi)).T

    def to_pbox(self):
        from ..pbox_abc import Staircase
        from ..params import Params

        return Staircase(
            left=np.repeat(self.lo, Params.steps),
            right=np.repeat(self.hi, Params.steps),
            mean=self,
            var=Interval(0, (self.hi - self.lo) * (self.hi - self.lo) / 4),
        )

    def lhs_sample(self, n) -> np.ndarray:
        """LHS sampling within the interval

        args:
            n: number of samples
        """
        from scipy.stats import qmc

        sampler = qmc.LatinHypercube(d=self.__len__())
        sample = sampler.random(n=n)
        sample = qmc.scale(sample, self.lo, self.hi)
        return sample

    def endpoints_lhs_sample(self, n) -> np.ndarray:
        """LHS sampling within the interval plus the endpoints

        args:
            n: number of samples
        """
        lhs_sample = self.lhs_sample(n)
        endpoints = np.array([self.lo, self.hi])
        return np.vstack((endpoints, lhs_sample))

    def plot(self, ax=None, **kwargs):
        p = self.to_pbox()
        if ax is None:
            fig, ax = plt.subplots()
        p.plot(ax=ax, **kwargs)

    def display(self):
        self.plot()
        plt.show()

    def is_degenerate(self) -> bool:
        """Check if the interval is degenerate (i.e., has zero width)."""
        if np.all(self._lo == self._hi):
            return True
        return False

    def _compute_nominal_value(self):
        return self.mid

    @property
    def lo(self) -> Union[ndarray, float]:
        return self._lo

    # if len(self.shape)==0: return self._lo
    # return self._lo # return transpose(transpose(self.__val)[0]) # from shape (3,7,2) to (2,7,3) to (3,7)

    @property
    def hi(self) -> Union[ndarray, float]:
        return self._hi

    @property
    def left(self):
        return self.lo

    @property
    def right(self):
        return self.hi

    @property
    def width(self):
        return width(self)

    @property
    def rad(self):
        """half width"""
        return rad(self)

    @property
    def mid(self):
        return mid(self)

    @property
    def unsized(self):
        if (len(self._hi.shape) > 0) | (len(self._hi.shape) > 0):
            return False
        else:
            return True

    @property
    def val(self):
        """seemingly equivalent to `self.to_numpy()`"""
        if self.unsized:
            return asarray([self._lo, self._hi], dtype=float)
        else:
            return transpose(stack((self._lo, self._hi)))

    @property
    def scalar(self):
        """Check if the interval is wide sense scalar

        note:
            wide sense: I(1,2) and I([1],[2]) are both scalars
        """
        return (self.shape == ()) | (self.shape == (1,))

    @property
    def is_scalar(self):
        """Check if the interval is a strict-sense scalar

        note:
            strict sense: I(1,2) is a scalar, but I([1],[2]) is not
        """
        return self.shape == ()

    @property
    def shape(self):
        return self.__shape

    @property
    def ndim(self):
        return len(self.__shape)

    # * -------------- ARITHMETIC -------------- *#
    # unary operators #
    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __pos__(self):
        return self

    # binary operators #
    def __add__(self, other):
        otherType = other.__class__.__name__
        if (otherType == "ndarray") | (otherType in NUMERIC_TYPES):
            lo, hi = self.lo + other, self.hi + other
        elif otherType == "Interval":
            lo, hi = self.lo + other.lo, self.hi + other.hi
        else:
            return NotImplemented  # TypeError: unsupported operand type(s) for +: 'int' and 'Interval' (for example)
        return Interval(lo, hi)

    def __radd__(self, left):
        leftType = left.__class__.__name__
        if (leftType == "ndarray") | (leftType in NUMERIC_TYPES):
            return self.__add__(left)
        else:
            return NotImplemented  # TypeError: unsupported operand type(s) for +: 'int' and 'Interval' (for example)

    def __sub__(self, other):
        otherType = other.__class__.__name__
        if (otherType == "ndarray") | (otherType in NUMERIC_TYPES):
            lo, hi = self.lo - other, self.hi - other
        elif otherType == "Interval":
            lo, hi = self.lo - other.hi, self.hi - other.lo
        else:
            NotImplemented
        return Interval(lo, hi)

    def __rsub__(self, left):
        leftType = left.__class__.__name__
        if (leftType == "ndarray") | (leftType in NUMERIC_TYPES):
            lo, hi = left - self.hi, left - self.lo
        else:
            return NotImplemented  # print("Error: not among the allowed types.")
        return Interval(lo, hi)

    def __mul__(self, other):
        otherType = other.__class__.__name__
        if otherType in NUMERIC_TYPES:
            if other >= 0:
                lo, hi = self.lo * other, self.hi * other
            else:
                lo, hi = self.hi * other, self.lo * other
        elif otherType == "ndarray":  # check self and other have same shape
            lo, hi = numpy.empty(self._lo.shape), numpy.empty(self._lo.shape)
            if len(other.shape) == 0:
                self.__mul__(float(other))  # safety net for ndarrays with no shape
            other_positive = other >= 0
            other_negative = other_positive == False
            lo[other_positive] = self.lo[other_positive] * other[other_positive]
            hi[other_positive] = self.hi[other_positive] * other[other_positive]
            lo[other_negative] = self.hi[other_negative] * other[other_negative]
            hi[other_negative] = self.lo[other_negative] * other[other_negative]
        elif otherType == "Interval":
            lo, hi = multiply(self, other)
        else:
            return NotImplemented
        return Interval(lo, hi)

    def __rmul__(self, left):
        leftType = left.__class__.__name__
        if (leftType == "ndarray") | (leftType in NUMERIC_TYPES) | np.isscalar(left):
            return self.__mul__(left)
        else:
            return NotImplemented

    def __truediv__(self, other):
        otherType = other.__class__.__name__
        if otherType in NUMERIC_TYPES:
            if other == 0:
                raise ZeroDivisionError
            if other > 0:
                lo, hi = self.lo / other, self.hi / other
            else:
                lo, hi = self.hi / other, self.lo / other
        elif otherType == "ndarray":
            lo, hi = numpy.empty(self._lo.shape), numpy.empty(self._lo.shape)
            if any(other.flatten() == 0):
                raise ZeroDivisionError
            other_positive = other > 0
            other_negative = other_positive == False
            lo[other_positive] = self.lo[other_positive] / other[other_positive]
            hi[other_positive] = self.hi[other_positive] / other[other_positive]
            lo[other_negative] = self.hi[other_negative] / other[other_negative]
            hi[other_negative] = self.lo[other_negative] / other[other_negative]
            pass
        elif otherType == "Interval":
            lo, hi = divide(self, other)
        else:
            NotImplemented
        return Interval(lo, hi)

    def __rtruediv__(self, left):
        leftType = left.__class__.__name__
        # lo,hi = numpy.empty(self._lo.shape),numpy.empty(self._hi.shape)
        self_lo, self_hi = self.lo, self.hi
        self_straddle_zero = numpy.any(
            (self_lo.flatten() <= 0) & (self_hi.flatten() >= 0)
        )
        if self_straddle_zero:
            raise ZeroDivisionError
        if (leftType == "ndarray") | (leftType in NUMERIC_TYPES):
            if left >= 0:
                lo, hi = left / self_hi, left / self_lo
            else:
                lo, hi = left / self_lo, left / self_hi
        else:
            return NotImplemented
        return Interval(lo, hi)

    def __pow__(self, other):
        otherType = other.__class__.__name__
        if otherType in INTEGERS:
            a, b = numpy.asarray(self.lo**other), numpy.asarray(
                self.hi**other
            )  # a2,b2 = a**2, b**2
            if other % 2 == 0:  # even power
                lo = zeros(
                    a.shape
                )  # numpy.max([numpy.min([a,b],axis=0),numpy.zeros(a.shape)],axis=0)
                lo[self < 0] = b[self < 0]
                lo[self > 0] = a[self > 0]
                hi = numpy.max([a, b], axis=0)
            else:  # odd power
                lo = numpy.min([a, b], axis=0)
                hi = numpy.max([a, b], axis=0)
        else:
            raise NotImplementedError("Not implemented yet")
        return Interval(lo, hi)

    def __lt__(self, other):
        return hi(self) < lo(other)

    def __rlt__(self, left):
        return hi(left) < lo(self)

    def __gt__(self, other):
        return lo(self) > hi(other)

    def __rgt__(self, left):
        return lo(left) > hi(self)

    def __le__(self, other):
        return hi(self) <= lo(other)

    def __rle__(self, left):
        return hi(left) <= lo(self)

    def __ge__(self, other):
        return lo(self) >= hi(other)

    def __rge__(self, left):
        return lo(left) >= hi(self)

    def __eq__(self, other):
        return (lo(self) == lo(other)) & (hi(self) == hi(other))

    def __ne__(self, other):
        return not (self == other)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if method != "__call__":
            return NotImplemented
        if "out" in kwargs and kwargs["out"] is not None:
            return NotImplemented

        if ufunc is np.sin:
            return self.sin()
        if ufunc is np.cos:
            return self.cos()
        if ufunc is np.tan:
            return self.tan()
        if ufunc is np.exp:
            return self.exp()
        if ufunc is np.sqrt:
            return self.sqrt()
        if ufunc is np.log:
            return self.log()

        return NotImplemented

    # * -------------- unary functions -------------- *#

    def abs(self):
        from .methods import abs as iabs

        return iabs(self)

    def sqrt(self):
        from .methods import sqrt as isqrt

        return isqrt(self)

    def exp(self):
        from .methods import exp as iexp

        return iexp(self)

    def log(self):
        from .methods import log as ilog

        return ilog(self)

    def sin(self):
        from .methods import sin as isin

        return isin(self)

    def cos(self):
        from .methods import cos as icos

        return icos(self)

    def tan(self):
        from .methods import tan as itan

        return itan(self)

    @classmethod
    def from_meanform(cls, x, half_width):
        if np.isscalar(x):
            return cls(x - half_width, x + half_width)
        else:
            x = np.asarray(x)
            half_width = np.asarray(half_width)
            return cls(lo=x - half_width, hi=x + half_width)


# * -------------- lightweight Interval

import numpy as np


""" for more compatability with possibility of newer additions """
# class LightweightInterval(Interval):
#     def __init__(self, *args, **kwargs):
#         kwargs["do_heavy_checks"] = False
#         super().__init__(*args, **kwargs)

""" clearer right-now logic """


class LightweightInterval(Interval):
    def __init__(self, lo, hi=None):
        super().__init__(lo, hi, do_heavy_checks=False)

        # # Store the shape (this is just lo.shape, because they have the same shape)
        # self.__shape = ()

    def __repr__(self):
        return f"[{self._lo},{self._hi}]"

    @property
    def lo(self) -> Union[ndarray, float]:
        return self._lo

    # if len(self.shape)==0: return self._lo
    # return self._lo # return transpose(transpose(self.__val)[0]) # from shape (3,7,2) to (2,7,3) to (3,7)
    @property
    def hi(self) -> Union[ndarray, float]:
        return self._hi


# Properties or maybe attributes of the interval class. These apply to all interval-like objects.

#####################################################################################
# methods.py
#####################################################################################
# Interval to float methods, Unary.

# def iterator(x:Interval) -> Interval:
#     lo_iter,hi_iter = numpy.nditer(x.lo()),numpy.nditer(x.hi())
#     while True: yield Interval(lo=next(lo_iter),hi=next(hi_iter))


def is_Interval(x: Any) -> bool:
    x_class_name = x.__class__.__name__
    return x_class_name == "Interval"


def interval_degenerate(vec_interval):
    if vec_interval.is_degenerate():
        return vec_interval.lo
    return vec_interval


def lo(x: Interval) -> Union[float, ndarray]:
    """
    Return the left endpoint of an Interval object.

    If x is not of class Interval, input is returned.

    """
    if is_Interval(x):
        return x.lo
    return x


def hi(x: Interval) -> Union[float, ndarray]:
    """
    Return the right endpoint of an Interval object.

    If x is not of class Interval, input is returned.

    """
    if is_Interval(x):
        return x.hi
    return x


def width(x: Interval) -> Union[float, ndarray]:
    """
    Return the width of an Interval object.

    If x is not of class Interval, input is returned.

    """
    if is_Interval(x):
        return hi(x) - lo(x)
    return x


def rad(x: Interval) -> Union[float, ndarray]:
    """
    Return the radius of an Interval object.

    If x is not of class Interval, input is returned.

    """
    if is_Interval(x):
        return (hi(x) - lo(x)) / 2
    return x


def mid(x: Interval) -> Union[float, ndarray]:
    """
    Return the midpoint of an Interval.

    If x is not of class Interval, input is returned.

    """
    if is_Interval(x):
        return (hi(x) + lo(x)) / 2
    return x


def mig(x):
    return np.max(np.abs(x.lo), np.abs(x.hi))  # mignitude


def mag(x):
    return np.min(np.abs(x.lo), np.abs(x.hi))  # magnitude
