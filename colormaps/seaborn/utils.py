"""Small palette related utility functions."""
from __future__ import print_function, division
import colorsys
import warnings
import os

import numpy as np
import colormaps as mpl
import colormaps.colors as mplcol

from .external.six.moves.urllib.request import urlopen, urlretrieve
from .external.six.moves.http_client import HTTPException


def desaturate(color, prop):
    """Decrease the saturation channel of a color by some percent.

    Parameters
    ----------
    color : matplotlib color
        hex, rgb-tuple, or html color name
    prop : float
        saturation channel of color will be multiplied by this value

    Returns
    -------
    new_color : rgb tuple
        desaturated color code in RGB tuple representation

    """
    # Check inputs
    if not 0 <= prop <= 1:
        raise ValueError("prop must be between 0 and 1")

    # Get rgb tuple rep
    rgb = mplcol.colorConverter.to_rgb(color)

    # Convert to hls
    h, l, s = colorsys.rgb_to_hls(*rgb)

    # Desaturate the saturation channel
    s *= prop

    # Convert back to rgb
    new_color = colorsys.hls_to_rgb(h, l, s)

    return new_color


def saturate(color):
    """Return a fully saturated color with the same hue.

    Parameters
    ----------
    color :  matplotlib color
        hex, rgb-tuple, or html color name

    Returns
    -------
    new_color : rgb tuple
        saturated color code in RGB tuple representation

    """
    return set_hls_values(color, s=1)


def set_hls_values(color, h=None, l=None, s=None):
    """Independently manipulate the h, l, or s channels of a color.

    Parameters
    ----------
    color : matplotlib color
        hex, rgb-tuple, or html color name
    h, l, s : floats between 0 and 1, or None
        new values for each channel in hls space

    Returns
    -------
    new_color : rgb tuple
        new color code in RGB tuple representation

    """
    # Get rgb tuple representation
    rgb = mplcol.colorConverter.to_rgb(color)
    vals = list(colorsys.rgb_to_hls(*rgb))
    for i, val in enumerate([h, l, s]):
        if val is not None:
            vals[i] = val

    rgb = colorsys.hls_to_rgb(*vals)
    return rgb


def get_color_cycle():
    cyl = mpl.rcParams['axes.prop_cycle']
    return [x['color'] for x in cyl]
