from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import six

import numpy as np


def random(shape, scale=1, offset=0, seed=0, dtype=np.float):
    """
    Return a deterministic array of random uniformly
    distributed between [offset, offset + scale)

    The random seed is controlled via `seed`

    Parameters
    ----------
    shape : tuple
        shape of the returned array

    scale : float
       range of random numbers

    offset : float
       minimum value of results

    seed : int
       Seed handed to np.random.seed, defaults to 0

    dtype : np.dtype
       type to cast results to via astype
    """
    np.random.seed(seed)
    return (offset + scale * np.random.rand(*shape)).astype(dtype)


def gradient_2D(shape, offset=0, flipud=False,
            fliplf=False, mod_val=None, dtype=None):
    """
    Return a diagonal gradient

    Parameters
    ----------
    shape : len 2 tuple
        dimensions of the output

    offset : scalar
       offset to add to array, applied before mod

    flipud : bool
       If the output should be flipped vertically

    fliplf : bool
       If the output should be flipped horizontally

    mod_val : scalar or None
       If not None, take return mod(array, mod_val)

    dtype : np.dtype or None
       type to cast results to if not None
    """
    tmp = np.ones(shape)
    # integrate image
    tmp = tmp.cumsum(0).cumsum(1) + offset
    if flipud:
        tmp = np.flipud(tmp)

    if fliplf:
        tmp = np.fliplr(tmp)

    if mod_val is not None:
        tmp = np.mod(tmp, mod_val)

    if dtype is not None:
        tmp = tmp.astype(dtype)

    return tmp
