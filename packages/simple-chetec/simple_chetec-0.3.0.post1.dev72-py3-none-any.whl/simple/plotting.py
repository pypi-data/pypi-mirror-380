import re

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.axes import Axes
import functools, itertools
from collections.abc import Sequence

import numpy as np
import warnings

import simple.models
from simple import utils

import logging
logger = logging.getLogger('SIMPLE.plot')

__all__ = ['create_rose_plot',
           'get_data', 'add_weights',
           'plot', 'slope', 'hist',
           'rose_hist',
           'create_legend', 'update_axes',
           'plot_intnorm', 'plot_simplenorm', 'mhist',]


# colours appropriate for colour blindness
# Taken from https://davidmathlogic.com/colorblind/#%23000000-%23E69F00-%2356B4E9-%23009E73-%23F0E442-%230072B2-%23D55E00-%23CC79A7
default_colors=utils.EndlessList(["#D55E00", "#56B4E9", "#009E73", "#E69F00", "#CC79A7", "#0072B2", "#F0E442"])
"""
An [``Endlesslist``][simple.plot.EndlessList] containing the default colors used by simple plotting functions.
"""

default_linestyles = utils.EndlessList(['-', (0, (4, 4)), (0, (2, 1)),
                                        (0, (4,2,1,2)), (0, (4,2,1,1,1,2)), (0, (4,2,1,1,1,1,1,2)),
                                        (0, (2,1,2,2,1,2)), (0, (2,1,2,2,1,1,1,2)), (0, (2,1,2,2,1,1,1,1,1,2)),
                                        (0, (2,1,2,1,2,2,1,2)), (0, (2,1,2,1,2,2,1,1,1,2)), (0, (2,1,2,1,2,2,1,1,1,1,1,2))])
"""
[``Endlesslist``][simple.plot.EndlessList] default line styles used by simple plotting functions.
"""

default_markers = utils.EndlessList(["o", "s", "^", "D", "P", "X", "v", "<", ">", "*", "p", "d", "H"])
"""
[``Endlesslist``][simple.plot.EndlessList] default marker styles used by simple plotting functions.
"""

def get_axes(axes, projection=None):
    """
    Return the ax that should be used for plotting.

    Args:
        axes (): Must either be ``None``, in which case ``plt.gca()`` will be returned, a matplotlib ax instance, or
            any object that has a ``.gca()`` method.
        projection (): If given, an exception is raised if ``ax`` does not have this projection.
    """
    if axes is None:
        axes = plt.gca()
    elif isinstance(axes, Axes):
        pass
    elif hasattr(axes, 'gca'):
        axes = axes.gca() # if ax = plt
    else:
        raise ValueError('ax must be an Axes, Axes instance or have a gca() method that return an Axes')

    if projection is not None and axes.name != projection:
        raise TypeError(f'The selected ax has the wrong projection. Expected {projection} got {axes.name}.')
        
    return axes

def get_models(models, where=None, **where_kwargs):
    """
    Return a selection of models.

    If *models* is a ModelCollection a new ModelCollection will be returned. Otherwise a list of Models will
    be returned.

    Args:
        models (): A collection of models or a list/tuple of models.
        where (str): Only models fitting this criteria will be selected. If not given all models are selected.
        **where_kwargs (): Keyword arguments to go with the ``where`` string.
    """
    if isinstance(models, simple.models.ModelCollection):
        pass
    elif isinstance(models, (list, tuple)) and False not in [isinstance(m, simple.models.ModelBase) for m in models]:
        pass
    else:
        raise TypeError(f'models must be a ModelCollection object or a list/tuple of Models objects - not {type(models)}.')

    # select models
    if where is not None:
        models = utils.models_where(models, where, **where_kwargs)

    return models

def parse_lscm(linestyle = False, color = False, marker=False):
    """
    Convert the ``linestyle``, ``color`` and ``marker`` arguments into [EndlessList][simple.plot.EndlessList]
    objects for plotting.

    Args:
        linestyle (): Either a single line style or a list of line styles. If ``True`` then the
            [default line styles][simple.plot.default_linestyles] is returned. If ``False`` or ``None`` a list
            containing only the no line sentinel is returned.
        color (): Single colour or a list of colours. If ``True`` then the
            [default colors][simple.plot.default_colors] is returned. If ``False`` or ``None`` a list
            containing only the color black is returned.
        marker (): Either a marker shape or a list of marker shapes. If ``True`` then the
            [default marker shapes][simple.plot.default_markers] shapes is returned. If ``False`` or ``None`` a
            list containing only the no marker sentinel is returned.

    Returns:
        (EndlessList, EndlessList, EndlessList): linestyles, colors, markers
    """
    if color is False or color is None:
        colors = utils.EndlessList(["#000000"])
    elif color is True:
        colors = default_colors
    else:
        colors = utils.EndlessList(color)

    if linestyle is False or linestyle is None:
        linestyles = utils.EndlessList([""])
    elif linestyle is True:
        linestyles = default_linestyles
    else:
        linestyles = utils.EndlessList(linestyle)

    if marker is False or marker is None:
        markers = utils.EndlessList([""])
    elif marker is True:
        markers = default_markers
    else:
        markers = utils.EndlessList(marker)

    return linestyles, colors, markers

#################
### Rose plot ###
#################
def as1darray(*a, dtype=np.float64):
    size = None

    out = [np.asarray(x, dtype=dtype) if x is not None else x for x in a]

    for o in out:
        if o is None:
            continue
        if o.ndim == 1 and o.size != 1:
            if size is None:
                size = o.size
            elif o.size != size:
                raise ValueError('Size of arrays do not match')
        elif o.ndim > 1:
            raise ValueError('array cannot have more than 1 dimension')

    out = tuple(o if (o is None or (o.ndim == 1 and o.size != 1)) else np.full(size or 1, o) for o in out)
    if len(out) == 1:
        return out[0]
    else:
        return out

def as0darray(*a, dtype=np.float64):
    out = [np.asarray(x, dtype=dtype) if x is not None else x for x in a]

    for o in out:
        if o is None:
            continue
        if o.ndim >= 1 and o.size != 1:
            raise ValueError('Size of arrays must be 1')

    out = tuple(o if (o is None or o.ndim == 0) else o.reshape(tuple()) for o in out)
    if len(out) == 1:
        return out[0]
    else:
        return out

def xy2rad(x, y, xscale=1.0, yscale=1.0):
    """
    Convert *x*, *y* coordinated into a angle value given in radians.
    """
    def calc(x, y):
        if x == 0:
            return 0
        if y == 0:
            return np.pi / 2

        if x > 0:
            return np.pi * 0.5 - np.arctan(y / x)
        else:
            return np.pi * 1.5 - np.arctan(y / x)

    x, y = as1darray(x, y)
    return np.array([calc(x[i] / xscale, y[i] / yscale) for i in range(x.size)])

def xy2deg(x, y, xscale=1.0, yscale=1.0):
    """
        Convert *x*, *y* coordinated into a angle value given in degrees.
        """
    rad = xy2rad(x, y, xscale=xscale, yscale=yscale)
    return rad2deg(rad)

def deg2rad(deg):
    """Convert a degree angle into a radian angle`value"""
    return np.deg2rad(deg)

def rad2deg(rad):
    """Convert a degree angle into a radian angle`value"""
    return np.rad2deg(rad)

def get_cmap(name):
    """Return the matplotlib colormap with the given name."""
    try:
        return mpl.colormaps[name]
    except:
        return mpl.cm.get_cmap(name)
def create_rose_plot(ax=None, *, vmin= None, vmax=None, log = False, cmap='turbo',
                     colorbar_show=False, colorbar_label=None, colorbar_fontsize=None,
                     xscale=1, yscale=1,
                     segment = None, rres=None,
                     **fig_kw):
    """
    Create a plot with a [rose projection](simple.plot.RoseAxes).

    The rose ax is a subclass of matplotlibs
    [polar ax](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes).

    Args:
        ax (): If no preexisting ax is given then a new figure with a single rose ax is created. If an existing
        ax is passed this ax will be deleted and replaced with a [RoseAxes][#RoseAxes].
        vmin (float): The lower limit of the colour map. If no value is given the minimum value is ``0`` (or ``1E-10`` if
        ``log=True``)
        vmax (float): The upper limit of the colour map. If no value is given then ``vmax`` is set to ``1`` and all bin
            default_weight are divided by the heaviest bin weight in each histogram.
        log (bool): Whether the color map scale is logarithmic or not.
        cmap (): The prefixes of the colormap to use. See,
                [matplotlib documentation][https://matplotlib.org/stable/users/explain/colors/colormaps.html]
                 for a list of available colormaps.
        colorbar_show (): Whether to add a colorbar to the right of the ax.
        colorbar_label (): The label given to the colorbar.
        colorbar_fontsize (): The fontsize of the colorbar label.
        xscale (): The scale of the x axis.
        yscale (): The scale of the y axis.
        segment (): Which segment of the rose diagram to show. Options are ``N``, ``E``, ``S``, ``W``, ``None``.
            If ``None`` the entire circle is shown.
        rres (): The resolution of lines drawn along the radius ``r``. The number of points in a line is calculated as
        ``r*rres+1`` (Min. 2).
        **fig_kw (): Additional figure keyword arguments passed to the ``pyplot.figure`` call. Only used when ``ax``
            is not given.

    Returns:
        RoseAxes : The new rose ax.
    """
    if ax is None:
        figure_kwargs = {'layout': 'constrained'}
        figure_kwargs.update(fig_kw)
        fig, ax = plt.subplots(subplot_kw={'projection': 'rose'}, **figure_kwargs)
    else:
        ax = get_axes(ax)
        fig = ax.get_figure()
        rows, cols, start, stop = ax.get_subplotspec().get_geometry()

        ax.remove()
        ax = fig.add_subplot(rows, cols, start + 1, projection='rose')

    if colorbar_label is None:
        if vmax is None:
            colorbar_label = f'Bin weight normalised to largest bin'
        else:
            colorbar_label = f'Bin weight'
    elif colorbar_label is False:
        colorbar_label = None

    ax.set_colorbar(vmin=vmin, vmax=vmax, log=log, cmap=cmap,
                    label=colorbar_label, show=colorbar_show, fontsize=colorbar_fontsize)
    ax.set_xyscale(xscale, yscale)

    if segment:
        ax.set_segment(segment)

    if rres:
        ax.set_rres(rres)

    return ax

class RoseAxes(mpl.projections.polar.PolarAxes):
    """
    A subclass of matplotlibs [Polar Axes](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes).

    Rose plots can be created using the [create_rose_plot](simple.plot.create_rose_plot) function or by
    specifying the projection ``'rose'`` using matplotlib functions.

    Only custom and reimplemented methods are described here. See matplotlibs documentation for more methods. Note
    however, that these method might not behave as the reimplemented version below. For example the matplotlib methods
    will not take into account the ``xscale`` and ``yscale``.

    **Note** that some features, like axlines, might require an updated version of matplotlib to work.
    """
    name = 'rose'

    def __init__(self, *args, **kwargs):
        self._xysegment = None
        self._yscale = 1
        self._xscale = 1
        self._rres = 720

        self._vrel, self._vmin, self._vmax = True, 0, 1
        self._norm = mpl.colors.Normalize(vmin=self._vmin, vmax=self._vmax)
        self._cmap = get_cmap('turbo')
        self._colorbar = None

        super().__init__(*args,
                         theta_offset=np.pi * 0.5, theta_direction=-1,
                         **kwargs)

        self.tick_params(axis='y', which='major', labelleft=False, labelright=False)
        self.tick_params(axis='y', which='minor')
        self.tick_params(axis='x', which='major', direction='out')
        self.margins(y = 0.1)


    def clear(self):
        """
        Clear the ax.
        """
        super().clear()

        self._last_hist_r = 0
        self._bar_color_cycle = itertools.cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])

        # Grid stuff
        self.grid(True, axis='y', which='minor')
        self.grid(True, axis='y', which='major', color='black')
        self.grid(False, axis='x', which='minor')
        self.grid(True, axis='x', which='major')


        self.set_rlim(rmin=0)
        self.set_rticks([], minor=True)
        self.set_rticks([], minor=False)

        # Segment
        self.set_xysegment(self._xysegment)
        #self.axes.set_yticklabels([])


    def set_colorbar(self, vmin=None, vmax=None, log=False, cmap='turbo',
                     label=None, fontsize=None, show=True, ax = None, clear=True):
        """
        Define the colorbar used for histograms.

        Currently, there is no way to delete any existing colorbars. Thus, everytime this function is called a new
        colorbar is created. Therefore, It's advisable to only call this method once. Note that it is always called
        by the [create_rose_plot](simple.plot.create_rose_plot) function.

        Args:
            vmin (float): The lower limit of the colour map. If no value is given the minimum value is ``0`` (or ``1E-10`` if
                ``log=True``)
            vmax (float): The upper limit of the colour map. If no value is given then ``vmax`` is set to ``1`` and all bin
                default_weight are divided by the heaviest bin weight in each histogram.
            log (bool): Whether the color map scale is logarithmic or not.
            cmap (): The prefixes of the colormap to use. See,
                [matplotlib documentation][https://matplotlib.org/stable/users/explain/colors/colormaps.html]
                for a list of available colormaps.
            label (): The label given to the colorbar.
            fontsize (): The fontsize of the colorbar label.
            show (): Whether to add a colorbar to the figure.
            ax (): The axis where the colorbar is drawn. If ``None`` it will be drawn on the right of the current axes.
            clear (): If ``True`` the current axes will be cleared.
        """
        self._vrel = True if vmax is None else False
        if log:
            self._vmin, self._vmax = vmin or 1E-10, vmax or 1
            self._norm = mpl.colors.LogNorm(vmin=self._vmin, vmax=self._vmax)
        else:
            self._vmin, self._vmax = vmin or 0, vmax or 1
            self._norm = mpl.colors.Normalize(vmin=self._vmin, vmax=self._vmax)

        self._cmap = get_cmap(cmap)
        if show:
            self._colorbar = self.get_figure().colorbar(mpl.cm.ScalarMappable(norm=self._norm, cmap=self._cmap),
                                                        ax=self, cax = ax, pad=0.1)
            self._colorbar.set_label(label, fontsize=fontsize)

        if clear:
            self.clear()

    def set_xyscale(self, xscale, yscale):
        """
        Set the scale of the *x* and *y* dimensions of the rose diagram.

        This can be used to distort the diagram to e.g. better show large or small slopes.

        **Note** Should not be confused with matplotlibs ``set_xscale`` and the ``set_yscale`` methods. They have
        are used to set the type of scale, e.g. log, linear etc., used for the different axis.

        Args:
            xscale (float): The scale of the *x* dimension of the rose diagram.
            yscale (float): The scale of the *y* dimension of the rose diagram.
        """
        # Not to be confused with set_xscale. This does something different.
        self._xscale = xscale
        self._yscale = yscale
        self.clear()

    def get_xyscale(self):
        """
        Return a tuple of the scale of the *x* and *y* dimensions of the rose diagram.
        """
        return (self._xscale, self._yscale)

    def set_xysegment(self, segment):
        """
        Define which segment of the rose diagram to show.

        Args:
            segment (): Options are ``N``, ``E``, ``S``, ``W``, ``None``.
                If ``None`` the entire circle is shown.
        """
        if segment is None:
            self.axes.set_thetagrids((0, 90, 180, 270),
                                     (self._yscale, self._xscale, self._yscale * -1, self._xscale * -1))
        elif type(segment) is not str:
            raise TypeError('segment must be a string')
        elif segment.upper() == 'N':
            self.axes.set_thetalim(-np.pi * 0.5, np.pi * 0.5)
            self.axes.set_thetagrids((-90, 0, 90), (-self._xscale, self._yscale, self._xscale))
        elif segment.upper() == 'S':
            self.axes.set_thetalim((np.pi * 0.5, np.pi * 1.5))
            self.axes.set_thetagrids((90, 180, 270), (-self._xscale, -self._yscale, self._xscale))
        elif segment.upper() == 'E':
            self.axes.set_thetalim(0, np.pi)
            self.axes.set_thetagrids((0, 90, 180), (self._yscale, self._xscale, -self._yscale))
        elif segment.upper() == 'W':
            self.axes.set_thetalim(np.pi, np.pi * 2)
            self.axes.set_thetagrids((180, 270, 360), (-self._yscale, -self._xscale, self._yscale))
        else:
            raise ValueError(f'Unknown segment: {segment}')
        self._xysegment = segment

    def _xy2rad(self, x, y):
        """
        Convert x, y coordinated to a theta value in relation to the *x* and *y* dimensions of the diagram.
        """
        return xy2rad(x, y, self._xscale, self._yscale)

    def set_rres(self, rres):
        """
        Set the resolution of lines drawn along the radius ``r``. The number of points in a line is calculated as
        ``r*rres+1`` (Min. 2).
        """
        self._rres = rres

    def get_rres(self):
        """
        Return the resolution of lines drawn along the radius ``r``.
        """
        return self._rres

    def _rplot(self, theta1, theta2, r, **kwargs):
        # Plot lines along the radius
        theta1, theta2, r = as0darray(theta1, theta2, r)

        if theta2 < theta1: theta1 -= np.pi * 2
        diff = (theta2 - theta1) / (np.pi * 2)
        nr = int(np.max([1, diff * self._rres * r])) + 1

        self.axes.plot(np.linspace(theta1, theta2, nr), np.full(nr, r), **kwargs)

    def _rfill(self, theta1, theta2, r1, r2, **kwargs):
        # Create a shaded segment.
        theta1, theta2, r1, r2 = as0darray(theta1, theta2, r1, r2)

        if theta2 < theta1: theta1 -= np.pi * 2
        diff = (theta2 - theta1) / (np.pi * 2)

        nr1 = int(np.max([1, diff * self._rres * r1])) + 1
        nr2 = int(np.max([1, diff * self._rres * r2])) + 1
        theta = np.append(np.linspace(theta1, theta2, nr1),
                          np.linspace(theta2, theta1, nr2))
        r = np.append(np.full(nr1, r1),
                      np.full(nr2, r2))

        self.fill(theta, r, **kwargs)

    def _rline(self, theta1, theta2, r):
        theta1, theta2, r = as0darray(theta1, theta2, r)

        if theta2 < theta1: theta1 -= np.pi * 2
        diff = (theta2 - theta1) / (np.pi * 2)

        nr = int(np.max([1, diff * self._rres * r])) + 1
        return np.linspace(theta1, theta2, nr), np.full(nr, r)


    #####################
    ### Point methods ###
    #####################
    def merrorbar(self, m, r=1, merr=None,
                  antipodal=None,
                  **kwargs):
        """
        Plot data points with errorbars.

        This is an adapted version of matplotlibs
        [errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html) method.

        **Note** it is currently not possible to add bar ends to the error bars.

        Args:
            m (float, (float, float)): Either a single array of floats representing a slope or a tuple of *x* and *y*
                coordinates from which a slope will be calculated.
            r (): The radius at which the data points will be drawn.
            merr (): The uncertainty of the slope.
            antipodal (): Whether the antipodal data points will be drawn. By default, ``antipodal=True`` when ``m`` is
                a slope and ``antipodal=False`` when ``m`` is *x,y* coordinates.
            **kwargs (): Additional keyword arguments passed to matplotlibs
            [errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html) method.
        """

        kwargs.setdefault('linestyle', '')
        kwargs.setdefault('marker', 'o')
        if type(m) is tuple and len(m) == 2:
            x, y = m
            if antipodal is None:
                antipodal = False
        else:
            x, y = 1, m
            if antipodal is None:
                antipodal = True

        x, y, r, merr = as1darray(x, y, r, merr)

        if merr is not None:
            # Makes errorbar show up in legend
            yerr = np.nan
        else:
            yerr = None

        kwargs['capsize'] = 0  # Because we cannot show these
        with warnings.catch_warnings():
            # Supresses warning that comes from having yerr as nan
            warnings.filterwarnings('ignore', message='All-NaN axis encountered', category=RuntimeWarning)
            data_line, caplines, barlinecols = self.errorbar(self._xy2rad(x, y), r, yerr=yerr, **kwargs)

        # print(len(barlinecols), barlinecols, barlinecols[0].get_colors(), barlinecols[0].get_linewidth())
        if merr is not None:
            colors = barlinecols[0].get_colors()
            if len(colors) == 1: colors = [colors[0]] * x.size

            linestyles = barlinecols[0].get_linestyles()
            if len(linestyles) == 1: linestyles = [linestyles[0]] * x.size

            linewidths = barlinecols[0].get_linewidths()
            if len(linewidths) == 1: linewidths = [linewidths[0]] * x.size

            zorder = barlinecols[0].get_zorder()

            for i in range(x.size):
                m = y[i] / x[i]
                self._rplot(self._xy2rad(x[i], (m + merr[i]) * x[i]), self._xy2rad(x[i], (m - merr[i]) * x[i]), r[i],
                            color=colors[i], linestyle=linestyles[i], linewidth=linewidths[i],
                            zorder=zorder, marker="")
        if antipodal:
            kwargs.pop('label', None)
            kwargs.pop('color', None)
            self.merrorbar((x * -1, y * -1), r, merr=merr, antipodal=False, color=data_line.get_color(), **kwargs)

    ####################
    ### Line methods ###
    ####################
    def _mline(self, m, r=1, merr=None,
               ecolor=None, elinestyle=":", elinewidth=None, ezorder=None,
               ealpha=0.5, efill=False, eline=True, axline=False,
               antipodal=None, **kwargs):
        # Does the heavy lifting for the axmline and mline methods.

        if type(m) is tuple and len(m) == 2:
            x, y = m
            if antipodal is None:
                antipodal = False
        else:
            x, y = 1, m
            if antipodal is None:
                antipodal = True

        if type(r) is tuple and len(r) == 2:
            rmin, rmax = r
        else:
            rmin, rmax = 0, r

        theta = self._xy2rad(x, y)[0]
        if axline:
            line = self.axvline(theta, rmin, rmax, **kwargs)
        else:
            line = self.plot([theta, theta], [rmin, rmax], **kwargs)[0]

        if merr is not None:
            if type(line) is list: line = line[0]
            ezorder = ezorder or line.get_zorder() - 0.001
            ecolor = ecolor or line.get_color()
            elinewidth = elinewidth or line.get_linewidth()

            m = y / x
            lowerlim = self._xy2rad(x, (m - merr) * x)
            upperlim = self._xy2rad(x, (m + merr) * x)

            # Do this first so it's beneath the lines.
            if efill:
                self._rfill(upperlim, lowerlim, rmin, rmax, color=ecolor, alpha=ealpha, zorder=ezorder)

            if eline:
                if axline:
                    self.axvline(lowerlim, rmin, rmax,
                                 color=ecolor, linestyle=elinestyle, linewidth=elinewidth, zorder=ezorder)
                    self.axvline(upperlim, rmin, rmax,
                                 color=ecolor, linestyle=elinestyle, linewidth=elinewidth, zorder=ezorder)
                else:
                    self.plot([lowerlim, lowerlim], [rmin, rmax],
                              color=ecolor, linestyle=elinestyle, linewidth=elinewidth, zorder=ezorder)
                    self.plot([upperlim, upperlim], [rmin, rmax],
                              color=ecolor, linestyle=elinestyle, linewidth=elinewidth, zorder=ezorder)

        if antipodal:
            kwargs.pop('label', None)
            kwargs.pop('label', None)
            kwargs['color'] = line.get_color()
            self._mline(m=(x * -1, y * -1), r=(rmin, rmax), merr=merr,
                        ecolor=ecolor, elinestyle=elinestyle, elinewidth=elinewidth,
                        ezorder=ezorder, ealpha=ealpha, efill=efill, eline=eline, axline=axline,
                        antipodal=False, **kwargs)

    def mline(self, m, r=1, merr=None, antipodal=None, *, eline=True, efill=False,
              ecolor=None, elinestyle=":", elinewidth=None, ezorder=None, ealpha=0.1,
              **kwargs):
        """
        Draw a line along a slope.

        Used matplotlibs [plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html) method to
        draw the line(s).

        Args:
            m (float, (float, float)): Either a single slope or a tuple of *x* and *y*
                coordinates from which a slope will be calculated.
            r (float, (float, float)): If a single value is given a line will be drawn between the ``0`` and ``r``.
                if a tuple of two values are given the line will be drawn between ``r[0]`` and ``r[1]``. Note these
                are absolute coordinates.
            merr (): The uncertainty of the slope.
            eline (): If ``True`` lines will also be drawn for the uncertainty of the slope.
            efill (): If ``True`` the area defined by the uncertainty of the slope will be shaded.
            ecolor (): The color used for the uncertainty lines and/or the shaded area.
            elinestyle (): The line style used for the uncertainty lines.
            elinewidth (): The line width used for the uncertainty lines.
            ezorder (): The z order width used for the uncertainty lines.
            ealpha (): The alpha value for the shaded area.
            antipodal (): Whether the antipodal data points will be drawn. By default, ``antipodal=True`` when ``m`` is
                a slope and ``antipodal=False`` when ``m`` is *x,y* coordinates.
            **kwargs (): Additional keyword arguments passed to matplotlibs
                [plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html) method.
        """

        kwargs.setdefault('linestyle', '-')
        return self._mline(m, r, merr,
                           ecolor=ecolor, elinestyle=elinestyle, elinewidth=elinewidth,
                           ezorder=ezorder, ealpha=ealpha, efill=efill, eline=eline,
                           antipodal=antipodal, axline=False, **kwargs)

    def axmline(self, m, r=1, merr=None, eline=True,
                ecolor=None, elinestyle=":", elinewidth=None, ezorder=None,
                antipodal=None, **kwargs):
        """
        Draw a line along a slope.

        Used matplotlibs [axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html) method
        to draw the line(s).

        Args:
            m (float, (float, float)): Either a single slope or a tuple of *x* and *y*
                coordinates from which a slope will be calculated.
            r (float, (float, float)): If a single value is given a line will be drawn between the ``0`` and ``r``.
                if a tuple of two values are given the line will be drawn between ``r[0]`` and ``r[1]``. Note these
                are relative coordinates.
            merr (): The uncertainty of the slope.
            eline (): If ``True`` lines will also be drawn for the uncertainty of the slope.
            ecolor (): The color used for the uncertainty lines.
            elinestyle (): The line style used for the uncertainty lines.
            elinewidth (): The line width used for the uncertainty lines.
            ezorder (): The z order width used for the uncertainty lines.
            antipodal (): Whether the antipodal data points will be drawn. By default, ``antipodal=True`` when ``m`` is
                a slope and ``antipodal=False`` when ``m`` is *x,y* coordinates.
            **kwargs (): Additional keyword arguments passed to matplotlibs
                [axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html) method.
        """

        return self._mline(m, r, merr,
                           ecolor=ecolor, elinestyle=elinestyle, elinewidth=elinewidth,
                           ezorder=ezorder, ealpha=0, eline=eline, efill=False,
                           antipodal=antipodal, axline=True, **kwargs)

    def axrline(self, r, tmin=0, tmax=1, **kwargs):
        """
        Plot a line along a given radius.

        Used matplotlibs [axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html) method
        to draw the line.

        Args:
            r (): The radius at which to draw the line.
            tmin (): The starting angle of the line. In relative coordinates.
            tmax (): The stopping angle of the line. In relative coordinates.
            **kwargs (): Additional keyword arguments passed to matplotlibs
                [axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html) method.

        Returns:

        """
        return self.axhline(r, tmin, tmax, **kwargs)

    def rtext(self, text, r, deg=0, rotation = None, **kwargs):
        deg = deg % 360

        if rotation is None:
            rotation = deg * -1
            if deg > 90 and deg < 270:
                rotation = (rotation + 180) % 360

        label_kw = {'text': text, 'xy': (deg2rad(deg), r),
                    'ha': 'center', 'va': 'center', 'rotation': rotation}
        label_kw.update(kwargs)
        self.annotate(**label_kw)

    ####################
    ### Hist Methods ###
    ####################
    def _mbins(self, m, r, weights, rwidth, rscale, rescale, antipodal, bins, update_rticks, minor_rticks):
        if type(m) is tuple and len(m) == 2:
            x, y = m
            if antipodal is None:
                antipodal = False
        else:
            x, y = 1, m
            if antipodal is None:
                antipodal = True

        x, y, weights = as1darray(x, y, weights)
        theta = self._xy2rad(x, y)
        if antipodal:
            theta = np.append(theta, self._xy2rad(x * -1, y * -1))
            weights = np.append(weights, weights)

        bin_weights, bin_edges = np.histogram(theta, bins=bins, range=(0, np.pi * 2), weights=weights, density=False)
        if self._vrel: bin_weights = bin_weights / np.max(bin_weights)

        if rscale:
            bin_heights = np.array([self._norm(bw, clip=True) for bw in bin_weights])
            if rescale: bin_heights = bin_heights / np.max(bin_heights)
            bin_heights = bin_heights * rwidth
        else:
            bin_heights = np.full(bin_weights.size, rwidth)

        if update_rticks:
            major_ticks = list(self.get_yticks(minor=False))
            if r not in major_ticks:
                major_ticks.append(r)
                self.set_yticks(major_ticks, minor=False)
            self.yaxis.set_view_interval(r, r+rwidth*1.15)

            minor_ticks = list(self.get_yticks(minor=True))
            update_minor = False
            for minor_r in list(np.linspace(r, r+rwidth, minor_rticks+1))[1:]:
                if minor_r not in minor_ticks:
                    minor_ticks.append(minor_r)
                    update_minor = True
            if update_minor:
                self.set_yticks(minor_ticks, minor=True)

        return bin_weights, bin_edges, bin_heights



    def mhist(self, m, r=None, weights=1, rwidth=0.9, rscale=True,
              rescale=True, antipodal=None, update_rticks=True, minor_rticks=2,
              bins=72, rtext = None, fill = True, outline=None, cmap = False, **kwargs):
        """
        Create a histogram of the given slopes.

        Args:
            m (float, (float, float)): Either a single array of floats representing a slope or a tuple of *x* and *y*
                coordinates from which a slope will be calculated.
            r (): The radius at which the histogram will be drawn. If 'None' it will be plotted ``1`` above the
                previous histogram, or at 1 if no histogram have been drawn.
            weights (): The weight assigned to each slope.
            rwidth (): The width of the histogram.
            rscale (): If ``True`` width of the individual bins will be scaled to their weight. Otherwise all bins
                will have the same width.
            rescale (): If ``True`` all bin widths will be scaled relative to the heaviest bin. Otherwise, they will
                be scaled to the color map.
            antipodal (): Whether the antipodal data points will be included in the histogram. By default,
            ``antipodal=True`` when ``m`` is a slope and ``antipodal=False`` when ``m`` is *x,y* coordinates.
            bins (): The number of even sized bin in the histogram.
            rtext (): A text label for the histogram in the plot. Created using the ``rtext`` method. Addtional keywords
                arguments can be passed using the prefix ``rtext_``.

        """
        kwargs = utils.KwargDict(kwargs)
        if r is None:
            r = self._last_hist_r + 1
        self._last_hist_r = r

        if outline is None:
            if fill and not cmap:
                outline=False
            else:
                outline=True

        color = kwargs.pop('color', None)
        if color is None:
            color = next(self._bar_color_cycle)

        rtext_kwargs = kwargs.extract(prefix='rtext')

        zorder= kwargs.pop('zorder', 1)
        fill_kwargs = kwargs.extract(prefix='fill', linestyle='', zorder=zorder)
        outline_kwargs = ukwargs.extract(prefix='outline',
                                         color=color,
                                         linestyle=kwargs.pop('linestyle', '-'),
                                         linewidth=kwargs.pop('linewidth', 1),
                                         zorder=zorder+0.001)
        baseline_kwargs = kwargs.extract(prefix='baseline', **outline_kwargs)

        bin_weights, bin_edges, bin_heights = self._mbins(m, r, weights, rwidth, rscale, rescale, antipodal, bins,
                                                          update_rticks, minor_rticks)
        label = kwargs.pop('label', None)
        if (fill and not cmap) or outline:
            label_fill_kwargs = fill_kwargs.copy()
            if outline:
                label_fill_kwargs['linestyle'] = outline_kwargs['linestyle']
                label_fill_kwargs['linewidth'] = outline_kwargs['linewidth']
                label_fill_kwargs['edgecolor'] = outline_kwargs['color']
            if (fill and not cmap):
                label_fill_kwargs['fill'] = True
            else:
                label_fill_kwargs['fill'] = False

            self.fill([np.nan, np.nan], facecolor=color, label = label, **label_fill_kwargs)
        elif (fill and cmap) and rtext is None:
            rtext = label

        if fill:
            for i in range(bin_weights.size):
                if cmap:
                    bin_color = self._cmap(self._norm(bin_weights[i]))
                else:
                    bin_color = color

                self._rfill(bin_edges[i], bin_edges[i + 1], r, r + bin_heights[i],
                            color=bin_color, **fill_kwargs)


        if outline:
            theta_, r_ = np.array([]), np.array([])
            for i in range(bin_weights.size):
                tr = self._rline(bin_edges[i], bin_edges[i + 1], r + bin_heights[i])
                theta_, r_ = np.append(theta_, tr[0]), np.append(r_, tr[1])
            theta_, r_ = np.append(theta_, [theta_[0]]), np.append(r_, [r_[0]])
            self.axes.plot(theta_, r_, **outline_kwargs)

            theta_, r_ = self._rline(bin_edges[0], bin_edges[-1], r)
            self.axes.plot(theta_, r_, **baseline_kwargs)

        #self.axrline(r, 0, np.pi*2, color='black', linewidth = 0.2)

        if rtext is not None:
            rtext_kwargs.setdefault('r', r + rwidth / 2)
            self.rtext(rtext, **rtext_kwargs)

mpl.projections.register_projection(RoseAxes)

################
### get data ###
################
@utils.set_default_kwargs()
def get_data(models, axis_names, *, where=None, latex_labels = True,
             key=None, default_attrname=None, unit=None, default_value = np.nan,
             key_in_label=None, numer_in_label=None, denom_in_label=None,
             model_in_label=None, unit_in_label=None, attrname_in_label=None, axis_name_in_label=None,
             label = True, prefix_label = None, suffix_label = None,
             mask = None, mask_na = True,
             kwargs = None):
    """
    Get one or more datasets from a group of models together with suitable labels.

    Each data point is a dictionary that contains a value for each of the axis given in *axis_names* plus a label
    describing the data point. The value for each axis is determined by the *key* argument. This argument has two
    possible components; the name of the attribute and the index, or key, to be applied this, or the
    *default_attrname*, attribute.

    The name of the attribute must start with a ``.`` followed by the path to the attribute relative to the Model
    object using successive ``.`` for nested attributes, e.g. ``.intnorm.eRi``.

    The index, or key, part of the *key* can either be an integer, a slice or a sequence of keys seperated by ``,``.
    The keys will be parsed into either [Isotope](simple.utils.Isotope), [Ratio](simple.utils.Ratio), or
    [Element](simple.utils.Element) strings. If a key is given it is assumed that the attribute contains an isotope
    key array. Therefore, Element strings will be replaced with all the isotopes of that element
    present in the attribute (Across all models) and Ratio strings will return the numerator value divided by the
    denominator value.

    If the attribute name is given in *key* then the index, or key, part must be enclosed in square brackets, e.g.
    ``.intnorm.eRi[105Pd]``. If the *default_attrname* should be used then *key* should only contain the index, or key.

    By the default the label for each data point only contains the information is not shared with all other data points.
    Information that is shared between all data points is instead included in the axis labels.

    Args:
        models (): A collection of models to plot. A subselection of these models can be made using the *where*
            argument.
        axis_names ():
        where (str): If given will be used to create a subselection of *models*. Any *kwargs* prefixed
            with ``where_`` will be supplied as keyword arguments. See
             [``ModelCollection.where``](simple.models.ModelCollection.where) for more details.
        latex_labels (bool): Whether to use the latex formatting in the labels, when available.
        key (str, int, slice): This can either be a valid index to the *default_attrname* array or the path, with
            or without a valid index, of a different attribute. Accepts either single universal value
            or a list of values, one for each axis (See below for details).
        default_attrname (): The name of the default attribute to use if *xkey* and *ykey* are indexes. By default,
            the default key array is used. Accepts either single universal value or a list of values, one for each
            axis (See below for details).
        unit (): The desired unit for the *xkey* and *ykey*. Different units for *xkey* and *ykey* can be specified
            by supplying a ``(<xkey_unit>, <ykey_unit>)`` sequence. Accepts either single universal value
            or a list of values, one for each axis (See below for details).
        default_value (): The value given to invalid indexes of arrays. Must have a shape compatible with the size
            of the indexed array. Accepts either single universal value
            or a list of values, one for each axis (See below for details).
        key_in_label (bool): Whether to include the key index in the label. Accepts either single universal value
            or a list of values, one for each axis (See below for details).
        numer_in_label (bool): Whether to include the numerator of a key index in the label. Accepts either single
            universal value or a list of values, one for each axis (See below for details).
        denom_in_label (bool): Whether to include the denominator of a key index in the label. Accepts either single
            universal value or a list of values, one for each axis (See below for details).
        model_in_label (bool): Whether to include the model name in the label. Accepts either single universal value
            or a list of values, one for each axis (See below for details).
        unit_in_label (bool): Whether to include the unit in the label. Accepts either single universal value
            or a list of values, one for each axis (See below for details).
        attrname_in_label (bool): Whether to include the attribute name in the label. By default
            the name is only included if it is different from the *default_attrname*. Accepts a single universal
            value or a list of values, one for each axis (See below for details).
        axis_name_in_label (bool): Whether to include the axis name in the label. Accepts either single universal value
            or a value for each axis (See below for details).
        label (str, bool, None): The label for individual datapoints. Accepts either a single universal value or
            a list of values, one per data point (See below for details).
        prefix_label (): Text to be added to the beginning of each data point label. Accepts either a single universal
            value or a list of values, one per data point (See below for details).
        suffix_label (): Text to be added at the end of each data point label. Accepts either a single universal
            value or a list of values, one per data point (See below for details).
        mask (str, int, slice): Can be used to apply a mask to the data which is plotted. See the
            ``get_mask`` function of the Model object. Accepts either a single universal
            value or a list of values, one per model (See below for details).
        mask_na (bool): If ``True`` masked values will be replaced by ``np.nan`` values. Only works if all arrays
            in a dataset have a float based datatype. Accepts either a single universal
            value or a list of values, one per model (See below for details).
        **kwargs:

    One per axis arguments:
        These arguments allow you to set a different value for each axis in *axis_names*. This can be
        either a single value used for all the axis or a sequence of values, one per axis.

        It is also possible to define the value for a specific axis by  including a keyword argument consiting
        of the axis name followed directly by the argument name. The value specified this way will take presidence over
        the value given by the argument itself. For example ``xkey=102Pd`` will set the *key* argument for
        the *x* axis to ``102Pd``.


    One per data point arguments:
        These arguments allow you to set a different value for each data point. The number of data points is
        equal to the number of models multiplied by the number of datasets generated. This can be
        either a single value used for all the axis or a sequence of values, one per data point.


    One per model arguments:
        These arguments allow you to set a different value for each model in *models*. This can be
        either a single value used for all the axis or a sequence of values, one per model.


    Returns:
        Tuple[dict, dict]: Two dictionaries containing:

            - A dictionary with the data points for each model, mapped to the model name

            - A dictionary containing labels for each axis, mapped to the axis name.

    Examples:
        Here is an example of how the return data can be used.
        ```
        model_datapoints, axis_labels = simple.get_data(models, 'x, y', xkey=..., ykey=...)

        # Set the axis labels
        plt.set_xlabel(axis_labels['x'])
        plt.set_ylabel(axis_labels['y'])

        # Iterate though the data and plot it
        for model_name, datapoints in model_datapoints.items():
            for dp in datapoints:
                plt.plot(dp['x'], dp['y'], label=dp['label'])
        ```

    """

    where_kwargs = kwargs.extract(prefix='where')
    models = get_models(models, where=where, where_kwargs=where_kwargs)

    if type(axis_names) is dict:
        axis_name_args = list(axis_names.keys())
        axis_key_args = list(axis_names.values())
    elif type(axis_names) is str:
        if ',' in axis_names:
            axis_name_args = list(n.strip() for n in axis_names.split(','))
        else:
            axis_name_args = list(n.strip() for n in axis_names.split())
        axis_key_args = None
    else:
        raise TypeError('``axis_name`` must be a string or a dict')

    lenargs = len(axis_name_args)
    lenmodels = len(models)

    def one_per_n(n, n_name, arg_name, arg_value):
        if isinstance(arg_value, str) or not isinstance(arg_value, Sequence):
            return [arg_value for i in range(n)]
        elif len(arg_value) == n:
            if type(arg_value) is list:
                return arg_value
            else:
                return list(arg_value)
        else:
            raise ValueError(f'Length of ``{arg_name}`` ({len(arg_value)}) must be equal to number of {n_name} ({n})')

    def one_per_arg(name, value):
        args = one_per_n(lenargs, 'axis', name, value)

        for i, axis in enumerate(axis_name_args):
            if (k:=f'{axis}{name}') in kwargs:
                args[i] = kwargs.pop(k)
            if (k:=f'{axis}{name}') in kwargs:
                args[i] = kwargs.pop(k)

        return args


    def parse_key_string(key, data_arrays):
        try:
            return utils.asisotopes(key), 'iso'
        except:
            pass

        try:
            return utils.asratios(key), 'rat'
        except:
            pass

        try:
            elements =  utils.aselements(key)
        except:
            raise ValueError(f'Unable to parse "{key}" into a sequence of valid Element, Isotope or Ratio string.')
        else:
            # Because the key list should be the same for all models we need to go through them all here
            # incase some have more or less isotopes in the specified data array
            all_isotopes = ()
            for element in elements:
                element_isotopes = []
                for data in data_arrays:
                    if not isinstance(data, (np.ndarray)) or data.dtype.fields is None:
                        raise ValueError(f'Data array "{attrname}" of model {model.name} is not a key array. '
                                         f'Cannot extract isotope keys.')

                    for iso in utils.get_isotopes_of_element(data.dtype.fields, element):
                        if iso not in element_isotopes:
                            element_isotopes.append(iso)
                all_isotopes += tuple(sorted(element_isotopes, key=lambda iso: float(iso.mass)))
            return all_isotopes, 'iso'

    def get_data_label(keylabels, keys, key_in_label, numer_in_label, denom_in_label):
        labels = []
        for key in keys:
            if type(key) is utils.Isotope:
                if key_in_label:
                    label = keylabels.get(key, f"!{key}")
                else:
                    label = ''
            elif key_in_label:
                if numer_in_label and denom_in_label:
                    label = f'{keylabels.get(key.numer, f"!{key.numer}")}/{keylabels.get(key.denom, f"!{key.denom}")} '
                elif numer_in_label:
                    label = keylabels.get(key.numer, f"!{key.numer}")
                elif denom_in_label:
                    label = keylabels.get(key.denom, f"!{key.denom}")
                else:
                    label = ''
            else:
                label = ''
            labels.append(label)
        return labels

    def get_data_index(data_array, index, mi, ai):
        try:
            return data_array[index]
        except ValueError as error:
            if isinstance(index, str):
                logger.warning(f'{models[mi]}.{attrname_a[ai]}: Missing field "{index}" replaced by the default value ({default_value})')
                return np.full(len(data_array), default_value_args[ai])
            else:
                raise error

    if axis_key_args is None:
        axis_key_args = one_per_arg('key', key)

    default_attrname_args = one_per_arg('default_attrname', default_attrname)
    desired_unit_args = one_per_arg('unit', unit)
    default_value_args = one_per_arg('default_value', default_value)
    key_in_label_args = one_per_arg('key_in_label', key_in_label)
    numer_in_label_args = one_per_arg('numer_in_label', numer_in_label)
    denom_in_label_args = one_per_arg('denom_in_label', denom_in_label)
    model_in_label_args = one_per_arg('model_in_label', model_in_label)
    unit_in_label_args = one_per_arg('unit_in_label', unit_in_label)
    attrname_in_label_args = one_per_arg('attrname_in_label', attrname_in_label)
    axis_name_in_label_args = one_per_arg('axis_name_in_label', axis_name_in_label)

    mask_args = one_per_n(lenmodels, 'models', 'mask', mask)
    mask_na_args = one_per_n(lenmodels, 'models', 'mask_na', mask_na)

    # _a -   [arg1, arg2, ...]
    # _am -  [(arg1_model1, arg1_model2, ...), (arg2_model1, arg2_model2, ...)]
    # _amk - [({arg1_model1_key1, arg1_model1_key2, ...}, {arg1_model2_key1, arg1_model2_key2, ...}), ...]
    attrname_a, keys_ak, keytype_a = [], [], []
    data_arrays_am, data_units_am = [], []
    data_label_am, data_keylabels_am = [], []
    for ai, arg in enumerate(axis_key_args):
        if type(arg) is not str:
            attrname = utils.parse_attrname(default_attrname_args[ai])
            key = arg
        else:
            if arg.startswith('.'):
                m = re.match(r'^([A-Za-z0-9_.]+)(?:\[(.*?)\])?$', arg)
                if m:
                    attrname = utils.parse_attrname(m.group(1))
                    key = m.group(2)
                    if attrname_in_label_args[ai] is None:
                        attrname_in_label_args[ai] = True
                else:
                    raise ValueError(f'Invalid arg: {key}')
            else:
                attrname = utils.parse_attrname(default_attrname_args[ai])
                key = arg

        if attrname_in_label_args[ai] is None and attrname is None:
            attrname_in_label_args[ai] = True

        attrname_a.append(attrname)

        # Here we get all the data arrays
        # For this we only need the attrname
        data_arrays_am.append([])
        data_units_am.append([])
        data_label_am.append([])
        data_keylabels_am.append([])
        for model in models:
            data, data_unit = model.get_array(attrname, desired_unit_args[ai])
            data_arrays_am[-1].append(data)
            data_units_am[-1].append(data_unit)

            attr_label, key_labels = model.get_array_labels(attrname, latex=latex_labels)
            data_label_am[-1].append(attr_label)
            data_keylabels_am[-1].append(key_labels)


        # Parse the key
        # Is the key is an element symbol it will extract all isotopes of that element from the data
        # Hence why we need to get the data arrays before this step
        if type(key) is str:
            # Check if key is an integer index or slice
            m = re.match(r'^\s*(-?\d+)\s*$|^\s*(-?\d*)\s*:\s*(-?\d*)\s*(?::\s*(-?\d*))?\s*$', key)
            if m:
                if m.group(1):
                    key = int(m.group(1))
                else:  # Slice
                    key = slice(int(m.group(2)) if m.group(2) is not None else None,
                                int(m.group(3)) if m.group(3) is not None else None,
                                int(m.group(4)) if m.group(4) is not None else None)
                key = (key,)
                keytype = 'index'

            else:
                key, keytype = parse_key_string(key, data_arrays_am[-1])
        elif type(key) is int or type(key) is slice:
            key = (key,)
            keytype = 'index'
        elif key is None:
            key = (key, )
            keytype = 'none'
        else:
            key, keytype = parse_key_string(key, data_arrays_am[-1])

        keys_ak.append(key)
        keytype_a.append(keytype)

    # Make sure the size of the keys is the same for all args
    size = {len(k) for k in keys_ak}
    size.discard(1)
    if len(size) > 1:
        raise ValueError(f'Length of indexes for not compatible {[len(k) for k in attrname_a]}')
    elif len(size) == 1:
        lenkeys = size.pop()
    else:
        lenkeys = 1

    for ai in range(lenargs):
        if len(keys_ak[ai]) != lenkeys:
            # current size can only be 1. Repeat until it is the correct length
            keys_ak[ai] = [keys_ak[ai][0] for i in range(lenkeys)]

    axis_label_args = [kwargs.pop(f'{name}label', True) for name in axis_name_args]
    axis_prefix_label_args = [kwargs.pop(f'{name}prefix_label', '') for name in axis_name_args]
    axis_suffix_label_args = [kwargs.pop(f'{name}suffix_label', '') for name in axis_name_args]
    label_args = one_per_n(lenmodels * lenkeys, 'datapoints', 'label', label)
    prefix_label_args = one_per_n(lenmodels * lenkeys, 'datapoints', 'prefix_label', prefix_label)
    suffix_label_args = one_per_n(lenmodels * lenkeys, 'datapoints', 'suffix_label', suffix_label)

    result_data = {}
    result_axis_label = {}
    data_labels_amk = []

    # Get the arg label which can be used as an axis label
    # Get the data point label for each arg. These are all combined later
    # Model name is not added. It will be added once the individual arg labels have been joined
    for ai in range(lenargs):
        keys = keys_ak[ai]
        keytype = keytype_a[ai]

        # Find common keys that can go into the arg label
        if keytype == 'iso':
            unique_keylabels = set()
            for mi, keylabels in enumerate(data_keylabels_am[ai]):
                if keylabels is None:
                    raise ValueError(f"Data array '{attrname_a[ai]}' of model '{models[mi].name}' is not a key array.")
                unique_keylabels = {*unique_keylabels, *(keylabels.get(k, None) for k in keys)}

            unique_keylabels.discard(None)
            if len(unique_keylabels) == 1: # Same label for all data points
                arg_label = unique_keylabels.pop()
                if key_in_label_args[ai] is None:
                    key_in_label_args[ai] = False
                if axis_name_in_label_args[ai] is None:
                    axis_name_in_label_args[ai] = False
            else:
                arg_label = f"<{axis_name_args[ai]}>"
                if key_in_label_args[ai] is None:
                    key_in_label_args[ai] = True
                if axis_name_in_label_args[ai] is None:
                    axis_name_in_label_args[ai] = True

        elif keytype == 'rat':
            unique_n_keylabels = {}
            unique_d_keylabels = {}
            for keylabels in data_keylabels_am[ai]:
                if keylabels is None:
                    raise ValueError(f"Data array '{attrname[ai]}' of model '{models[ai].name}' is not a key array.")

                unique_n_keylabels = {*unique_n_keylabels, *(keylabels.get(k.numer, None) for k in keys)}
                unique_d_keylabels = {*unique_d_keylabels, *(keylabels.get(k.denom, None) for k in keys)}

            unique_n_keylabels.discard(None)
            unique_d_keylabels.discard(None)

            if key_in_label_args[ai] is not None:
                if numer_in_label_args[ai] is None:
                    numer_in_label_args[ai] = key_in_label_args[ai]
                if denom_in_label_args[ai] is None:
                    denom_in_label_args[ai] = key_in_label_args[ai]

            if len(unique_n_keylabels) == 1 and len(unique_d_keylabels) == 1:
                arg_label = f"{unique_n_keylabels.pop()} / {unique_d_keylabels.pop()}"
                if key_in_label_args[ai] is None:
                    key_in_label_args[ai] = False
                if numer_in_label_args[ai] is None:
                    numer_in_label_args[ai] = False
                if denom_in_label_args[ai] is None:
                    denom_in_label_args[ai] = False
                if axis_name_in_label_args[ai] is None:
                    axis_name_in_label_args[ai] = False
            elif len(unique_n_keylabels) == 1:
                arg_label = f'{unique_n_keylabels.pop()} / <{axis_name_args[ai]}>'
                if key_in_label_args[ai] is None:
                    key_in_label_args[ai] = True
                if numer_in_label_args[ai] is None:
                    numer_in_label_args[ai] = False
                if denom_in_label_args[ai] is None:
                    denom_in_label_args[ai] = True
                if axis_name_in_label_args[ai] is None:
                    axis_name_in_label_args[ai] = True
            elif len(unique_d_keylabels) == 1:
                arg_label = f"<{axis_name_args[ai]}> / {unique_d_keylabels.pop()}"
                if key_in_label_args[ai] is None:
                    key_in_label_args[ai] = True
                if numer_in_label_args[ai] is None:
                    numer_in_label_args[ai] = True
                if denom_in_label_args[ai] is None:
                    denom_in_label_args[ai] = False
                if axis_name_in_label_args[ai] is None:
                    axis_name_in_label_args[ai] = True
            else:
                arg_label = f"<{axis_name_args[ai]}>"
                if key_in_label_args[ai] is None:
                    key_in_label_args[ai] = True
                if numer_in_label_args[ai] is None:
                    numer_in_label_args[ai] = True
                if denom_in_label_args[ai] is None:
                    denom_in_label_args[ai] = True
                if axis_name_in_label_args[ai] is None:
                    axis_name_in_label_args[ai] = True

        else:
            arg_label = ''

            # Neither are possible so just set to False
            key_in_label_args[ai] = False
            axis_name_in_label_args[ai] = False

        # Create labels for each key
        data_labels_amk.append([])
        if keytype == 'iso' or keytype == 'rat':
            for keylabels in data_keylabels_am[ai]:
                data_labels_amk[-1].append(get_data_label(keylabels, keys,
                                                          key_in_label_args[ai], numer_in_label_args[ai], denom_in_label_args[ai]))
                if attrname_in_label_args[ai] is None:
                    attrname_in_label_args[ai] = False

        else:
            # No keys so just creates an empty label
            data_labels_amk[-1].extend([['' for i in range(lenkeys)] for j in range(lenmodels)])
            if attrname_in_label_args[ai] is None:
                attrname_in_label_args[ai] = True

        # Add the unit either to arg label if common across all models or to each key label
        # [unit] added to the end of the string
        if unit_in_label_args[ai] is not False:
            unique_data_units = {*data_units_am[ai]}
            unique_data_units.discard(None)
            if len(unique_data_units) == 1:
                arg_label = f'{arg_label} [{unique_data_units.pop()}]'
            elif len(unique_data_units) > 1:
                for mi, arg_data_labels_k in enumerate(data_labels_amk[-1]):
                    for ki, key in enumerate(arg_data_labels_k):
                        if data_units_am[ai][mi] is not None:
                            data_labels_amk[-1][mi][ki] = f'{key} [{data_units_am[ai][mi]}]'.strip()

        # Add the attrname either to arg label if common across all models or to each key label
        # arrname added to the start of the string
        if attrname_in_label_args[ai]:
            unique_data_label = {*data_label_am[ai]}
            unique_data_label.discard(None)
            if len(unique_data_label) == 1:
                if arg_label == '':
                    arg_label = unique_data_label.pop().strip()
                else:
                    arg_label = f'{unique_data_label.pop()} | {arg_label}'.strip()
            elif len(unique_data_label) > 1:
                for mi, arg_data_labels_k in enumerate(data_labels_amk[-1]):
                    for ki, key in enumerate(arg_data_labels_k):
                        if data_label_am[ai][mi] is not None:
                            if key == '':
                                data_labels_amk[-1][mi][ki] = data_label_am[ai][mi].strip()
                            else:
                                data_labels_amk[-1][mi][ki] = f'{data_label_am[ai][mi]} | {key}'.strip()

        axis_label_arg = axis_label_args[ai]
        if axis_label_arg is True:
            prefix = axis_prefix_label_args[ai]
            suffix = axis_suffix_label_args[ai]
            if prefix:
                arg_label = f"{prefix}{arg_label}"
            if suffix:
                arg_label = f"{arg_label}{suffix}"

            result_axis_label[axis_name_args[ai]] = arg_label or None
        else:
            result_axis_label[axis_name_args[ai]] = axis_label_arg or None

    has_labels = False
    for mi in range(lenmodels):
        results = []
        for ki in range(lenkeys):
            results.append({})

            label = ''
            for ai in range(lenargs):
                data_array = data_arrays_am[ai][mi]
                keytype = keytype_a[ai]

                if keytype == 'rat':
                    key = keys_ak[ai][ki]
                    n = get_data_index(data_array, key.numer, mi, ai)
                    d = get_data_index(data_array, key.denom, mi, ai)
                    data = n/d

                elif keytype == 'iso' or keytype == 'index':
                    key = keys_ak[ai][ki]
                    data = get_data_index(data_array, key, mi, ai)
                else: # keytype == 'none'
                    data = data_array

                results[-1][axis_name_args[ai]] = data

                data_label = data_labels_amk[ai][mi][ki].strip()
                if data_label != '':
                    if axis_name_in_label_args[ai]:
                        label += f"<{axis_name_args[ai]}: {data_label}>"
                    else:
                        label += data_label

            if mask_args[mi] is not None:
                imask = models[mi].get_mask(mask, **results[-1])
                if mask_na_args[mi] and False not in (np.issubdtype(v.dtype, np.floating) for v in results[-1].values()):
                    for k, v in results[-1].items():
                        v = v.copy()
                        v[np.logical_not(imask)] = np.nan
                        results[-1][k] = v
                else:
                    for k, v in results[-1].items():
                        results[-1][k] = v[imask]

            label_arg = label_args[(mi * lenkeys) + ki]
            if label_arg is True:
                prefix = prefix_label_args[mi * lenkeys + ki]
                suffix = suffix_label_args[mi * lenkeys + ki]

                if model_in_label_args[ai] or (model_in_label_args[ai] is None and lenmodels > 1):
                    if label == '':
                        label = models[mi].name
                    else:
                        label = f'{label} ({models[mi].name})'.strip()
                if type(prefix) is str:
                    label = f"{prefix}{label}"
                if type(suffix) is str:
                    label = f"{label}{suffix}"

                results[-1]['label'] = label.strip() or None
            else:
                results[-1]['label'] = label_arg or None
            if results[-1]['label']:
                has_labels = True

        result_data[models[mi]] = tuple(results)

    if has_labels and kwargs.get('legend', False) is None:
        kwargs['legend'] = True

    return result_data, result_axis_label

@utils.set_default_kwargs()
def add_weights(modeldata, axis, weights=1, *,
                sum_weights=True, norm_weights=True,
                default_attrname=None, unit=None, default_value=0,
                mask=None, mask_na=True, axisname='w'):
    """
    Add weights to the specified axis of each datapoint in the modeldata dictionary.

    This function appends a new array of weights (under `axisname`) to each datapoint
    in `modeldata`. The weights can be a constant or a string referring to data to be individually
    retrieved from each model. Optionally, the weights can be summed,
    normalized, and masked for missing data.

    The 'mask' and 'mask_na' arguments should be the same as those used to generate `modeldata` to ensure
    consistent results.

    Args:
        modeldata (dict): The data dictionary returned from `get_data`. It should be a
            dict of models, each containing a list of datapoint dictionaries.
        axis (str): The axis in the datapoints that the weights correspond to (e.g., 'x', 'y').
        weights (int, float, str): The weights to add. Can be:
            - A scalar to apply uniformly,
            - A string key that will be used to retrieve data from each model individually.
        sum_weights (bool): If True and `weights` is a string consisting of multiple keys, the values for the different
            keys are summed together and used for each datapoint for a given model. Default is True.
        norm_weights (bool): If True, normalise weights along the specified axis. Default is True.
        default_attrname (str or None): Attribute name to use when fetching weights if not included
            in labels. Optional.
        unit (str or None): Unit to assign to the fetched weight values. Optional.
        default_value (float): Default value to assign if weights are missing. Default is 0.
        mask (str or None): Optional mask to apply to the data when computing or assigning weights.
        mask_na (bool): If True, mask values will be replaced with NaNs. If False, masked values are omitted.
        axisname (str): The name under which the weight data will be stored in each datapoint. Default is 'w'.

    Returns:
        dict: The modified `modeldata`, with weight arrays added to each datapoint.

    Raises:
        ValueError: If the number of weight arrays does not match the number of datapoints
            and they cannot be broadcast.
    """

    # Remove any previous weights
    for model in modeldata:
        for dp in modeldata[model]:
            dp.pop(axisname, None)

    models = list(modeldata.keys())
    if type(weights) is str:
        modeldata_w, axis_labels_w = get_data(models, {'w': weights},
                                              mask=mask, mask_na=mask_na,
                                              default_attrname=default_attrname, unit=unit,
                                              default_value=default_value,
                                              attrname_in_label=True, model_in_label=False, axis_name_in_label=False,
                                              latex_labels=False)

        if sum_weights:
            for model, datapoints_w in modeldata_w.items():
                if len(datapoints_w) > 1:
                    labels = [dw.get('label', 'Missing label') for dw in datapoints_w]
                    logger.info(
                        f'{model}: Calculating weights by adding together: {axis_labels_w["w"]} <w: {", ".join(labels)}>')
                    modeldata_w[model] = [{axisname: functools.reduce(np.add, [dw['w'] for dw in datapoints_w])}]

    else:
        modeldata_w = {}
        for model in models:
            datapoints_xy = modeldata[model]
            if mask:
                m = model.get_mask(mask)
                if mask_na:
                    modeldata_w[model] = [{axisname: np.full(m.shape, weights, dtype=np.float64)}]
                    modeldata_w[model][0][axisname][np.logical_not(m)] = np.nan
                else:
                    modeldata_w[model] = [{axisname: np.full(np.count_nonzero(m), weights, dtype=np.float64)}]
            else:
                modeldata_w[model] = [{axisname: np.full_like(dp[axis], weights, dtype=np.float64)} for dp in datapoints_xy]

    for model, datapoints in modeldata.items():
        datapoints_w = modeldata_w[model]

        if len(datapoints_w) == 1 and len(datapoints) > 1:
            for datapoint in datapoints:
                datapoint[axisname] = datapoints_w[0][axisname].copy()
        elif len(datapoints_w) == len(datapoints):
            for i, datapoint in enumerate(datapoints):
                datapoint[axisname] = datapoints_w[i][axisname]
        else:
            raise ValueError(f'Size of weights data incompatible with size of {axis} data')

    if norm_weights:
        _norm_weights(modeldata, axisname)

    return modeldata

def _norm_weights(modeldata, axisname):
    logger.info(
        f'Normalising weights so that the sum of all weights is equal to 1.')
    for model, datapoints in modeldata.items():
        for datapoint in datapoints:
            weights = datapoint[axisname]
            sum = np.nansum(weights)
            if sum > 0: datapoint[axisname] = weights / sum

@utils.set_default_kwargs()
def _make_table(models, axis_names, kwargs=None):
    model_datapoints, axis_labels = simple.get_data(models, axis_names, **kwargs)
    pass

################
### xy plots ###
################
@utils.set_default_kwargs()
def create_legend(ax, outside = False, outside_margin=0.01, kwargs=None):
    """
    Add a legend to a plot.

    Args:
        ax (): The working axes. Accepted values are any matplotlib Axes object or plt instance.
        outside (bool): If ``True`` the legend will be drawn just outside the upper left corner of the plot. This will
            overwrite any ``loc`` and ``bbox_to_anchor`` arguments in ``kwargs``.
        outside_margin (): Margin between the plot and the legend. Relative to the width of the plot.
        **kwargs (): Any valid argument for matplotlibs
            [``legend``](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html) function.
    """
    ax = get_axes(ax)

    if outside:
        kwargs['loc'] = 'upper left'
        kwargs['bbox_to_anchor'] = (1+outside_margin, 1)

    ax.legend(**kwargs)

def update_axes(ax, kwargs, *, delay=None, update_ax = True, update_fig = True, delay_all=False):
    """
    Updates the axes and figure objects.

    Keywords beginning with ``ax_<name>``, ``xax_<name>``, ``yax_<name>`` and ``fig_<name>`` will be stripped
    from kwargs. These will then be used to call the ``set_<name>`` or ``<name>`` method of the axes, axis or
    figure object.

    If the value mapped to the above arguments is:
    - A boolean it is used to determine whether to call the method. The boolean itself will not be passed to
        the method. To pass a boolean to a method place it in a tuple, e.g. ``(True, )``.
    - A tuple then the contents of the tuple is unpacked as arguments for the method call.
    - A dictionary then the contents of the dictionary is unpacked as keyword arguments for the method call.
    - Any other value will be passed as the first argument to the method call.

    Additional keyword arguments can be passed to methods by mapping e.g. ``<ax|xax|yax|fig>_kw_<name>_<keyword>``
    kwargs to the value. These additional keyword arguments are only used if the
    ``<ax|xax|yax|fig>_<name>`` kwargs exists. Note however that they are always stripped from ``kwargs``.

    It is possible to delay calling certain method by adding ``<ax|xax|yax|fig>_<name>`` to ``*delay``. Keywords
    associated with these method will then be included in the returned dictionary. This dictionary can be passed back
    to the function at a later time. To delay all calls but remove the relevant kwargs from *kwargs* use
    ``delay_all=True``.

    Returns
        dict: A dictionary containing the delayed method calls.
    """

    ax = get_axes(ax)
    axes_meth = kwargs.extract(prefix='ax')
    axes_kw = axes_meth.extract(prefix='kw')

    xaxes_meth = kwargs.extract(prefix='xax')
    xaxes_kw = axes_meth.extract(prefix='kw')

    yaxes_meth = kwargs.extract(prefix='yax')
    yaxes_kw = axes_meth.extract(prefix='kw')

    figure_meth = kwargs.extract(prefix='fig')
    figure_kw = figure_meth.extract(prefix='kw')

    # Special cases
    if 'size' in figure_meth: figure_meth.setdefault('size_inches', figure_meth.pop('size'))

    if delay is None:
        delay = []
    elif type(delay) is str:
        delay = [delay]
    delayed_kwargs = {}

    def update(obj, name, meth_kwargs, kw_kwargs):
        for var, arg in meth_kwargs.items():
            var_kwargs = kwargs.extract(prefix=var)
            try:
                method = getattr(obj, f'set_{var}')
            except:
                try:
                    method = getattr(obj, var)
                except:
                    raise AttributeError(f'The {name} object has no method called ``set_{var}`` or ``{var}``')

            if f'{name}_{var}' in delay or delay_all:
                delayed_kwargs[f'{name}_{var}'] = arg
                delayed_kwargs.update({f'{name}_kw_{var}_{k}': v for k,v in var_kwargs.items()})
                continue

            elif arg is False:
                continue
            elif arg is True:
                arg = ()
            elif type(arg) is dict:
                var_kwargs.update(arg)
                arg = ()
            elif type(arg) is not tuple:
                arg = (arg, )

            method(*arg, **var_kwargs)

    if update_ax:
        update(ax, 'ax', axes_meth, axes_kw)
        if xaxes_meth:
            update(ax.xaxis, 'xax', xaxes_meth, xaxes_kw)
        if yaxes_meth:
            update(ax.yaxis, 'yax', yaxes_meth, yaxes_kw)

    if update_fig:
        update(ax.get_figure(), 'fig', figure_meth, figure_kw)

    return delayed_kwargs


def _axline(direction, ax, v, verr, lim, lim_coord, kwargs):
    fill_kwargs = kwargs.extract(prefix='fill')
    ax = get_axes(ax)

    if lim_coord == 'data' and lim is not None:
        if direction == 'h':
            if lim is None: lim = ax.get_xlim()
            ax.hline(v, *lim, **kwargs)
        elif direction == 'v':
            if lim is None: lim = ax.get_ylim()
            ax.vline(v, *lim, **kwargs)

    if lim_coord == 'axis':
        if lim is None: lim == (0, 1)

        if verr is not None:
            pass


        if direction == 'h':
            ax.axhline(v, *lim, **kwargs)
        elif direction == 'v':
            ax.axvline(v, *lim, **kwargs)



def axhline(ax, y, yerr = None, lim = None, lim_coord='axes', **kwargs):


    pass


@utils.add_shortcut('abundance', default_attrname ='abundance', unit=None)
@utils.add_shortcut('stdnorm', default_attrname ='stdnorm.Ri', unit=None)
@utils.add_shortcut('intnorm', default_attrname='intnorm.eRi', unit=None)
@utils.set_default_kwargs(
    linestyle=False, color=True, marker=True,
    fixed_model_linestyle = None, fixed_model_color = None, fixed_model_marker = None,
    ax_kw_xlabel_fontsize=15,
    ax_kw_ylabel_fontsize=15,
    markersize=4,
    legend_outside=True,
    ax_tick_params=dict(axis='both', left=True, right=True, top=True),
    fig_size=(7,6.5),
    )
def plot(models, xkey, ykey, *,
         default_attrname=None, unit=None,
         where=None, mask = None, mask_na = True, ax = None,
         legend = None, update_ax = True, update_fig = True,
         hist=False, hist_size=0.3, hist_pad=0.05, kwargs=None):
    """
    Plot *xkey* against *ykey* for each model in *models*.

    This function retrieves data using [`get_data`](simple.get_data) and plots it using matplotlib. It supports
    optional filtering, masking, and per-model or per-dataset styling. Additional arguments can be passed using
    keyword prefixes to control axes, figure appearance, legends, and more.

    This function is split into two stages: [`plot_get_data`](simple.plotting.plot_get_data) and
    [`plot_draw`](simple.plotting.plot_draw), which can be used independently.

    Args:
        models (ModelCollection): A collection of models to plot. A subset can be selected using the *where* argument.
        xkey, ykey (str, int, or slice): Keys or indices used to retrieve the x and y data arrays. These may refer to
            array indices (relative to *default_attrname*) or full attribute paths.
            See [`get_data`](simple.get_data) for more.
        default_attrname (str): Name of the default attribute used when *xkey* or *ykey* is an index.
        unit (str or tuple): Desired unit(s) for the x and y axes. Use a tuple `(xunit, yunit)` for different units.
        where (str): Filter expression to select a subset of *models*. Any *kwargs* prefixed with `where_`
            are passed to the model filtering function.
            See [`ModelCollection.where`](simple.models.ModelCollection.where).
        mask (str, int, or slice): Optional mask to apply to the data. See the `get_mask` method on model instances.
        mask_na (bool): If True, masked values are replaced with `np.nan`. Only applies if *xkey* and *ykey* are
            float-based.
        ax (matplotlib.axes.Axes or None): The axes to plot on. If None, defaults to `plt.gca()`.
        legend (bool): Whether to add a legend. If None, a legend is shown if at least one datapoint has a label.
        update_ax, update_fig (bool): Whether to apply `ax_` and `fig_` keyword argument updates using
            [`update_axes`](simple.plotting.update_axes).
        hist (bool): Whether to show marginal histograms along the axes.
        hist_size (float): Relative size of the histogram axes.
        hist_pad (float): Padding between the main plot and histogram axes.
        kwargs (dict, optional): A dictionary of keyword arguments. This provides an explicit way to pass additional
            options and overrides any conflicting values passed via `**kwargs_`.
        **kwargs_ (): Additional keyword arguments passed directly to the function. These are merged into *kwargs* unless
            a key already exists in *kwargs*, in which case the value in *kwargs* takes precedence.
            kwargs (dict): Additional keyword arguments. These may include:
        kwargs (dict or KwargDict, optional): A dictionary of keyword arguments that may be modified internally.
            Any keys in *kwargs* that match parameters in the function's signature are automatically passed to those
            parameters. If a key exists in both *kwargs* and ***kwargs*, the value in *kwargs* takes precedence.
        **kwargs (): Additional keyword arguments passed directly to the function. These are merged into *kwargs*.
            Possible keyword arguments are:

            - Parameters passed to [`simple.get_data`](simple.get_data)
            - Matplotlib `plot()` parameters (e.g., `color`, `linestyle`, `marker`)
            - Prefix-based controls (e.g., `ax_xlabel`, `legend_outside`, `fig_size`)

    Iterable plot arguments:
        The following matplotlib arguments support iterable or preset behaviour:

        - `color`: Can be a list of colours, `True` for defaults, or `False` to use black.
        - `linestyle`: Can be a list of styles, `True` for defaults, or `False` to disable lines.
        - `marker`: Can be a list of markers, `True` for defaults, or `False` to disable markers.

        These are assigned per-model or per-dataset depending on the context:

        - If multiple models are plotted, all datasets for a model share the same *color*.
        - If one model has multiple datasets, each gets a different *color*.
        - *linestyle* and *marker* behave similarly, controlled by:
            - `fixed_model_color`
            - `fixed_model_linestyle`
            - `fixed_model_marker`

    Axis and data labels:
        Axis labels are automatically inferred based on shared and unique elements in the data. You can override them
        using `ax_xlabel` and `ax_ylabel` in *kwargs*. Datapoint labels can be overridden with a list of labels
        (one per line in the legend).

    Shortcuts and default values:
        This function includes shortcut variants with predefined default values:

        - `plot.intnorm`: sets `default_attrname="intnorm.eRi"` and `unit=None`
        - `plot.stdnorm`: sets `default_attrname="stdnorm.Ri"` and `unit=None`
        - `plot.abundance`: sets `default_attrname="abundance"` and `unit=None`

        Default argument values can also be updated through `plot.update_kwargs()`. Values defined in the function
        signature are used only if not overridden there. You can retrieve the default arguments using `plot.kwargs`

    Returns:
        matplotlib.axes.Axes: The axes object used for plotting.
    """
    modeldata, axis_labels = plot_get_data.raw(models, xkey, ykey,
                                           default_attrname=default_attrname, unit=unit,
                                           where=where, mask=mask, mask_na=mask_na,
                                           kwargs=kwargs)
    return plot_draw.raw(modeldata, axis_labels, ax=ax, legend=legend,
                     update_ax=update_ax, update_fig=update_fig,
                     hist=hist, hist_size=hist_size, hist_pad=hist_pad,
                     kwargs=kwargs)

@utils.set_default_kwargs(inherits=plot, match_signature=True)
def plot_get_data(models, xkey, ykey, *, default_attrname=None, unit=None,
                  where=None, mask = None, mask_na = True,
                  kwargs=None):
    """
    Retrieve model data and axis labels for plotting.

    This function performs the data preparation step of [`plot`](simple.plotting.plot).

    Args:
        See [`plot`](simple.plotting.plot) for a complete description of arguments.

    Returns:
        tuple:
            - modeldata (dict): Structured data for plotting.
            - axis_labels (dict): Suggested axis labels.
    """
    modeldata, axis_labels = get_data(models, {'x': xkey, 'y': ykey},
                                      where=where,
                                      default_attrname=default_attrname, unit=unit,
                                      mask=mask, mask_na=mask_na,
                                      kwargs=kwargs)

    func_weights = kwargs.pop('_SIMPLE_add_weights', add_weights)
    weights_kwargs = kwargs.extract('weights', 'sum_weights', 'norm_weights', prefix='weights')
    if hist or kwargs.get('xhist', False) or kwargs.get('yhist', False):
        func_weights(modeldata, axis, mask=mask, mask_na=mask_na, **weights_kwargs)

    return modeldata, axis_labels


@utils.set_default_kwargs(inherits=plot, match_signature=True)
def plot_draw(modeldata, axis_labels, *, ax=None, legend=None,
              update_ax=True, update_fig=True,
              hist=False, hist_size=0.3, hist_pad=0.05, kwargs=None):
    """
    Render the data using matplotlib.

    This function handles the styling, axes setup, and drawing logic of [`plot`](simple.plotting.plot)..

    Args:
        See [`plot`](simple.plotting.plot) for a complete description of arguments.

    Returns:
        matplotlib Axes: The axes on which the data was plotted.
    """
    ax = get_axes(ax)  # We are working on the axes object proper

    # Get the linestyle, color and marker for each thing to be plotted.
    linestyles, colors, markers = parse_lscm(kwargs.extract(('linestyle', True), ('color', True), ('marker', False)))
    fixed_model_linestyle = kwargs.pop('fixed_model_linestyle', None)
    fixed_model_color = kwargs.pop('fixed_model_color', None)
    fixed_model_marker = kwargs.pop('fixed_model_marker', None)

    # Extract the legend arguments
    legend_kwargs = kwargs.extract(prefix='legend')

    # Extract the hist arguments
    xhist = kwargs.pop('xhist', hist)
    yhist = kwargs.pop('yhist', hist)
    hist_kwargs = kwargs.extract(prefix='hist',
                                 legend=False, fig_size=False,
                                 default_attrname=default_attrname, unit=unit, mask=mask,
                                 linestyle=linestyles, color=colors,
                                 fixed_model_linestyle=fixed_model_linestyle, fixed_model_color=fixed_model_color,)
    xhist_kwargs = kwargs.extract(prefix='xhist', size=hist_size, pad = hist_pad,
                                  ax_xlabel=None, **hist_kwargs)
    yhist_kwargs = kwargs.extract(prefix='yhist', size=hist_size, pad = hist_pad,
                                  ax_ylabel=None, flip=True, **hist_kwargs)

    # Update the axes/figure
    kwargs.setdefault('ax_xlabel', axis_labels['x'])
    kwargs.setdefault('ax_ylabel', axis_labels['y'])
    delayed_kwargs = update_axes(ax, kwargs, delay='ax_legend', update_ax=update_ax, update_fig=update_fig)

    # Extract in case any are left behind.
    simple_kwargs = kwargs.extract(prefix='_SIMPLE')

    mfc = kwargs.pop('markerfacecolor', None)

    for mi, (model, datapoints) in enumerate(modeldata.items()):
        for di, datapoint in enumerate(datapoints):
            if fixed_model_linestyle or (fixed_model_linestyle is None and len(datapoints) == 1):
                ls = linestyles[mi]
            else:
                ls = linestyles[di]
            if fixed_model_color is True or (fixed_model_color is None and len(modeldata) > 1):
                c = colors[mi]
            else:
                c = colors[di]
            if fixed_model_marker is True or (fixed_model_marker is None and len(datapoints) == 1):
                m = markers[mi]
            else:
                m = markers[di]

            ax.plot(datapoint['x'], datapoint['y'],
                    label = datapoint.get('label', None),
                    color=c, ls=ls, marker=m,
                    markerfacecolor=mfc or c,
                    **kwargs)

    # Create the hist plots
    if xhist:
        if xhist_kwargs.get('ax', None) is None:
            ax_histx = getattr(ax, '_SIMPLE_ax_histx', None)
            if ax_histx is None:
                ax_histx = ax.inset_axes([0, 1 + xhist_kwargs.pop('pad'), 1, xhist_kwargs.pop('size')], sharex=ax)
                setattr(ax, '_SIMPLE_ax_histx', ax_histx)
            xhist_kwargs['ax'] = ax_histx

        xhist_kwargs.setdefault('range', ax.get_xlim())
        xhist_kwargs.setdefault('xax_visible', (False,))
        hist_draw(modeldata, axis_labels, 'x', **xhist_kwargs)

    if yhist:
        if xhist_kwargs.get('ax', None) is None:
            legend_kwargs['outside_margin'] = (legend_kwargs.get('outside_margin', 0.01)
                                               + yhist_kwargs['pad'] + yhist_kwargs['size'])
            ax_histy = getattr(ax, '_SIMPLE_ax_histy', None)
            if ax_histy is None:
                ax_histy = ax.inset_axes([1 + yhist_kwargs.pop('pad'), 0, yhist_kwargs.pop('size'), 1], sharey=ax)
                setattr(ax, '_SIMPLE_ax_histy', ax_histy)
            yhist_kwargs['ax'] = ax_histy

        yhist_kwargs.setdefault('yax_visible', (False,))
        yhist_kwargs.setdefault('range', ax.get_ylim())
        hist_draw(modeldata, axis_labels, 'y', **yhist_kwargs)

    # Create legend and process any delayed axes/figure arguments
    update_axes(ax, delayed_kwargs, update_ax=update_ax, update_fig=update_fig)
    if legend:
        create_legend(ax, **legend_kwargs)

    return ax

@utils.add_shortcut('abundance', default_attrname ='abundance', unit=None)
@utils.add_shortcut('stdnorm', default_attrname ='stdnorm.Ri', unit=None)
@utils.add_shortcut('intnorm', default_attrname='intnorm.eRi', unit=None)
@utils.set_default_kwargs(
    linestyle=True, color=True,
    fixed_model_linestyle = None, fixed_model_color = None,
    ax_kw_xlabel_fontsize=15,
    ax_kw_ylabel_fontsize=15,
    legend_outside=True,
    ax_tick_params=dict(axis='both', left=True, right=True, top=True),
    fig_size=(7,6.5),
    )
def hist(models, key, weights=1, axis='x', *,
         sum_weights=True, norm_weights=True,
         bins = 20, filled=None,
         default_attrname=None, unit=None,
         weights_default_attrname = None, weights_unit=None, weights_default_value=0,
         where=None, mask=None, ax=None,
         legend=None, update_ax=True, update_fig=True,
         kwargs=None):
    """
    Make a histogram of *key*, on *axis*, for each model in *models*.

    This function retrieves data using [`get_data`](simple.get_data) and plots it using matplotlib. It supports
    optional filtering, masking, and per-model or per-dataset styling. Additional arguments can be passed using
    keyword prefixes to control axes, figure appearance, legends, and more.

    This function is split into two stages: [`hist_get_data`](simple.plotting.hist_get_data) and
    [`hist_draw`](simple.plotting.hist_draw), which can be used independently.

    Args:
        models (ModelCollection): A collection of models to plot. A subset can be selected using the *where* argument.
        key (str, int, or slice): Keys or indices used to retrieve the data array. These may refer to
            array indices (relative to *default_attrname*) or full attribute paths.
            See [`get_data`](simple.get_data) for more.
        default_attrname (str): Name of the default attribute used when *xkey* or *ykey* is an index.
        unit (str or tuple): Desired unit(s) for the x and y axes. Use a tuple `(xunit, yunit)` for different units.
        where (str): Filter expression to select a subset of *models*. Any *kwargs* prefixed with `where_`
            are passed to the model filtering function.
            See [`ModelCollection.where`](simple.models.ModelCollection.where).
        mask (str, int, or slice): Optional mask to apply to the data. See the `get_mask` method on model instances.
        mask_na (bool): If True, masked values are replaced with `np.nan`. Only applies if *xkey* and *ykey* are
            float-based.
        ax (matplotlib.axes.Axes or None): The axes to plot on. If None, defaults to `plt.gca()`.
        legend (bool): Whether to add a legend. If None, a legend is shown if at least one datapoint has a label.
        update_ax, update_fig (bool): Whether to apply `ax_` and `fig_` keyword argument updates using
            [`update_axes`](simple.plotting.update_axes).
        hist (bool): Whether to show marginal histograms along the axes.
        hist_size (float): Relative size of the histogram axes.
        hist_pad (float): Padding between the main plot and histogram axes.
        kwargs (dict, optional): A dictionary of keyword arguments. This provides an explicit way to pass additional
            options and overrides any conflicting values passed via `**kwargs_`.
        **kwargs_ (): Additional keyword arguments passed directly to the function. These are merged into *kwargs* unless
            a key already exists in *kwargs*, in which case the value in *kwargs* takes precedence.
            kwargs (dict): Additional keyword arguments. These may include:
        kwargs (dict or KwargDict, optional): A dictionary of keyword arguments that may be modified internally.
            Any keys in *kwargs* that match parameters in the function's signature are automatically passed to those
            parameters. If a key exists in both *kwargs* and ***kwargs*, the value in *kwargs* takes precedence.
        **kwargs (): Additional keyword arguments passed directly to the function. These are merged into *kwargs*.
            Possible keyword arguments are:

            - Parameters passed to [`simple.get_data`](simple.get_data)
            - Matplotlib `plot()` parameters (e.g., `color`, `linestyle`, `marker`)
            - Prefix-based controls (e.g., `ax_xlabel`, `legend_outside`, `fig_size`)

    Iterable plot arguments:
        The following matplotlib arguments support iterable or preset behaviour:

        - `color`: Can be a list of colours, `True` for defaults, or `False` to use black.
        - `linestyle`: Can be a list of styles, `True` for defaults, or `False` to disable lines.
        - `marker`: Can be a list of markers, `True` for defaults, or `False` to disable markers.

        These are assigned per-model or per-dataset depending on the context:

        - If multiple models are plotted, all datasets for a model share the same *color*.
        - If one model has multiple datasets, each gets a different *color*.
        - *linestyle* and *marker* behave similarly, controlled by:
            - `fixed_model_color`
            - `fixed_model_linestyle`
            - `fixed_model_marker`

    Axis and data labels:
        Axis labels are automatically inferred based on shared and unique elements in the data. You can override them
        using `ax_xlabel` and `ax_ylabel` in *kwargs*. Datapoint labels can be overridden with a list of labels
        (one per line in the legend).

    Shortcuts and default values:
        This function includes shortcut variants with predefined default values:

        - `plot.intnorm`: sets `default_attrname="intnorm.eRi"` and `unit=None`
        - `plot.stdnorm`: sets `default_attrname="stdnorm.Ri"` and `unit=None`
        - `plot.abundance`: sets `default_attrname="abundance"` and `unit=None`

        Default argument values can also be updated through `plot.update_kwargs()`. Values defined in the function
        signature are used only if not overridden there. You can retrieve the default arguments using `plot.kwargs`

    Returns:
        matplotlib.axes.Axes: The axes object used for plotting.
    """

    modeldata, axis_labels, axis = hist_get_data.raw(models, key, weights, axis,
                                                 sum_weights=sum_weights, norm_weights=norm_weights,
                                                 default_attrname=default_attrname, unit=unit,
                                                 weights_default_attrname=weights_default_attrname,
                                                 weights_unit=weights_unit, weights_default_value=weights_default_value,
                                                 where=where, mask=mask, kwargs=kwargs)


    return hist_draw.raw(modeldata, axis_labels, axis, bins=bins, filled=filled,
                     legend=legend, update_ax=update_ax, update_fig=update_fig,
                     ax=ax, kwargs=kwargs)

@utils.add_shortcut('abundance', default_attrname ='abundance', unit=None)
@utils.add_shortcut('stdnorm', default_attrname ='stdnorm.Ri', unit=None)
@utils.add_shortcut('intnorm', default_attrname='intnorm.eRi', unit=None)
@utils.set_default_kwargs(inherits=hist, match_signature=True)
def hist_get_data(models, key, weights=1, axis='x', *,
                  sum_weights=True, norm_weights=True,
                  default_attrname=None, unit=None,
                  weights_default_attrname=None, weights_unit=None, weights_default_value=0,
                  where=None, mask=None,
                  kwargs=None):
    if axis not in ['x', 'y']:
        raise ValueError('Axis must be either x or y')

    modeldata, axis_labels = get_data(models, {axis: key},
                                      where=where,
                                      default_attrname=default_attrname, unit=unit,
                                      mask=mask, mask_na=False, kwargs=kwargs)

    func_weights = kwargs.pop('_SIMPLE_add_weights', add_weights)
    func_weights(modeldata, axis,
                 weights=weights, sum_weights=sum_weights, norm_weights=norm_weights,
                 default_attrname=weights_default_attrname, unit=weights_unit,
                 default_value=weights_default_value, mask=mask, mask_na=False)


@utils.set_default_kwargs(inherits=hist, match_signature=True)
def hist_draw(modeldata, axis_labels, axis, *, flip=False, bins=20, filled=None,
              ax=None, legend=None, update_ax=True, update_fig=True,
              kwargs=None):
    ax = get_axes(ax)  # We are working on the axes object proper

    # Get the linestyle, color and marker for each thing to be plotted.
    linestyles, colors, markers = parse_lscm(kwargs.extract(('linestyle', True), ('color', True), ('marker', False)))
    fixed_model_linestyle = kwargs.pop('fixed_model_linestyle', None)
    fixed_model_color = kwargs.pop('fixed_model_color', None)
    fixed_model_marker = kwargs.pop('fixed_model_marker', None)

    legend_kwargs = kwargs.extract(prefix='legend')

    if filled is None:
        if len(models) > 1 or (len(models) > 0 and len(next(iter(modeldata.values()))) > 1):
            filled = False
        else:
            filled = True

    if filled is True:
        kwargs.setdefault('histtype', 'stepfilled')
    else:
        kwargs.setdefault('histtype', 'step')

    if flip:
        kwargs.setdefault('orientation', 'horizontal')
        kwargs.setdefault('ax_ylabel', axis_labels['y'])
    else:
        kwargs.setdefault('orientation', 'vertical')
        kwargs.setdefault('ax_xlabel', axis_labels['x'])

    delayed_kwargs = update_axes(ax, kwargs, delay='ax_legend', update_ax=update_ax, update_fig=update_fig)
    simple_kwargs = kwargs.extract(prefix='_SIMPLE')

    has_labels = False
    if bins is not None:
        for mi, (model, datapoints) in enumerate(modeldata.items()):
            for di, datapoint in enumerate(datapoints):
                if fixed_model_linestyle or (fixed_model_linestyle is None and len(datapoints) == 1):
                    ls = linestyles[mi]
                else:
                    ls = linestyles[di]
                if fixed_model_color is True or (fixed_model_color is None and len(modeldata) > 1):
                    c = colors[mi]
                else:
                    c = colors[di]

                if not has_labels and datapoint.get('label', None):
                    has_labels = True

                ax.hist(datapoint[axis], bins=bins, weights=datapoint['w'],
                        label=datapoint.get('label', None),
                        color=c, ls=ls,
                        **kwargs)

    update_axes(ax, delayed_kwargs, update_ax=update_ax, update_fig=update_fig)
    if legend or (legend is None and has_labels):
        create_legend(ax, **legend_kwargs)

    return ax

@utils.add_shortcut('abundance', default_attrname ='abundance', unit=None)
@utils.add_shortcut('stdnorm', default_attrname ='stdnorm.Ri', unit=None)
@utils.add_shortcut('intnorm', default_attrname='intnorm.eRi', unit=None)
@utils.set_default_kwargs(
    linestyle=True, color=True,
    fixed_model_linestyle = None, fixed_model_color = None,
    ax_kw_xlabel_fontsize=15,
    ax_kw_ylabel_fontsize=15,
    markersize=4,
    legend_outside=True,
    ax_tick_params=dict(axis='both', left=True, right=True, top=True),
    fig_size=(7,6.5),
    arrow_linewidth=0, arrow_length_includes_head=True, arrow_head_width=0.05,
    arrow_zorder=3
    )
def slope(models, xkey, ykey, xycoord=(0, 0), *,
          arrow=True, arrow_position=0.9,
          default_attrname=None, unit=None,
          where=None, mask = None, mask_na = True, ax = None,
          legend = None, update_ax = True, update_fig = True,
          kwargs=None):
    """
    Plot the slope of *ykey* / *xkey* for each model in `*models*.

    It is possible to plot multiple datasets if *xkey* and/or *ykey* is a list of multiple keys for a isotope key
    array. If only one of the arguments is a list then the second argument will be reused for each dataset. If a key
    is not present in an array then a default value is used. See [``get_data``](simple.get_data) for more details.

    The data to be plotted is retrieved using the [``get_data``](simple.get_data) function. All arguments available
    for that function not included in the argument list here can be given as one of the *kwargs* to this function.

    The data will be plotted using matplotlib's ``axline`` function. Additional arguments to this function can be
    passed as one of the *kwargs* to this function. Some arguments have enhanced behaviour detailed in a
    section below.

    Args:
        models (): A collection of models to plot. A subselection of these models can be made using the *where*
            argument.
        xkey, ykey (str, int, slice): This can either be a valid index to the *default_attrname* array or the path, with
            or without a valid index, of a different attribute. See [``get_data``](simple.get_data) for more details.
        default_attrname (str): The name of the default attribute to use if *xkey* and *ykey* are indexes.
        unit (str): The desired unit for the *xkey* and *ykey*. Different units for *xkey* and *ykey* can be specified
            by supplying a ``(<xkey_unit>, <ykey_unit>)`` sequence.
        where (str): If given will be used to create a subselection of *models*. Any *kwargs* prefixed
            with ``where_`` will be supplied as keyword arguments. See
             [``ModelCollection.where``](simple.models.ModelCollection.where) for more details.
        mask (str, int, slice): Can be used to apply a mask to the data which is plotted. See the ``get_mask`` function of the Model
            object.
        mask_na (bool): If ``True`` masked values will be replaced by ``np.nan`` values. Only works if both *xkey* and
            *ykey* have a float based datatype.
        ax (): The axes where the data is plotted. Accepted values are any matplotlib Axes object or plt instance.
            Defaults to ``plt.gca()``.
        legend (bool): Whether to create a legend. By default, a legend will be created if one or more datapoints have
            a valid label.
        update_ax, update_fig (bool): Whether to update the axes and figure objects using kwargs that have the prefix
            ``ax_`` and ``fig_``. See [``simple.plotting.update_axes``](simple.plotting.update_axes) for more details.
        **kwargs ():
            Valid keyword arguments are those using one of the prefixes define by other arguments, any argument
            for the [``simple.get_data``](simple.get_data) function, or any valid keyword argument for
            matplotlib's ``plot`` function.

    Data and axis labels:
        Labels for each axis and individual datapoints will be automatically generated. By default, the axis labels
        will contain the information common to all datasets while the label for the individual datapoints will contain
        only the unique information. You can override the axis labels by passing ``ax_xlabel`` and ``ax_ylabel`` as
        one of the *kwargs*. You can also override the datapoint labels by passing a list of labels, one each
        for each datapoint in the legend. See [``get_data``](simple.get_data) for more details on customising the
        labels.


    Iterable plot arguments:
        The following arguments for matplotlibs ``plot`` function have enhanced behaviour that allows them to be
        iterated through when plotting different models and/or datasets.

        - ``linestyle`` Can be a list of linestyles that will be iterated through. If ``True`` simple's predefined
        list of linestyles is used. If ``False`` no lines will be shown.

        - ``color`` Can be a list of colors that will be iterated through. If ``True`` simple's predefined
        list of colors is used. If ``False`` the colour defaults to black.

        There are two ways these values can be iterated through. Either all the datapoints of a given model gets the
        same value or each set of datapoints across the different models gets the same value. By default, if there are
        multiple models then all the datasets for each model will have the same *color*. If there is only one model
        then the color will be different for the different datasets. If there are multiple datasets then each dataset
        across the different models will have the same *linestyle* and *marker*. If there is only one dataset then
        *linestyle* and *marker* will be different for each model.

        This behaviour can be changed by passing ``fixed_model_linestyle``, ``fixed_model_color``
        and ``fixed_model_marker`` keyword arguments set to either ``True`` or ``False`` If ``True`` each model will
        have the same value. If ``False`` each dataset across the different models will have the same value.

    Default kwargs and shortcuts:
        The default values for arguments can be updated by changing the  ``plot.kwargs`` dictionary. Any
        argument not defined in the function description will be included in *kwargs*. Default values given in the
        function definition will be used only if a default value does not exist in ``plot.kwargs``.
        Additionally, one or more shortcuts with additional/different default values are attached to this function.
        The following shortcuts exist for this function:

        - ``plotm.intnorm`` Default values to plot internally normalised data. This sets *default_attrname* to
            ``intnorm`` and the ``default_unit`` to ``None``.

        - ``plotm.stdnorm`` Default values to plot the basic ratio normalised data. This sets
                *default_attrname* to ``stdnorm`` and the ``default_unit`` to ``None``.

    Returns:
        The axes where the data was plotted.
    """

    modeldata, axis_labels = slope_get_data.raw(models, xkey, ykey,
                                                default_attrname=default_attrname, unit=unit,
                                                where=where, mask=mask, mask_na=mask_na,
                                                kwargs=kwargs)
    return slope_draw.raw(modeldata, axis_labels, xycoord=xycoord,
                   arrow=arrow, arrow_position=arrow_position,
                   ax=ax,
                   legend=legend, update_ax=update_ax, update_fig=update_fig,
                   kwargs=kwargs)

@utils.set_default_kwargs(inherits=slope, match_signature=True)
def slope_get_data(models, xkey, ykey, *,
                   default_attrname=None, unit=None,
                   where=None, mask=None, mask_na=True,
                   kwargs=None):
    modeldata, axis_labels = get_data(models, {'x': xkey, 'y': ykey},
                                      where=where,
                                      default_attrname=default_attrname, unit=unit,
                                      mask=mask, mask_na=mask_na,
                                      kwargs=kwargs)
    return modeldata, axis_labels




@utils.set_default_kwargs(inherits=slope, match_signature=True)
def slope_draw(modeldata, axis_labels, xycoord=(0,0), *,
             arrow=True, arrow_position=0.9,
             legend=None, update_ax=True, update_fig=True,
             kwargs=None):
    ax = get_axes(ax)  # We are working on the axes object proper

    # Get the linestyle, color and marker for each thing to be plotted.
    linestyles, colors, markers = parse_lscm(kwargs.extract(('linestyle', True), ('color', True), ('marker', False)))
    fixed_model_linestyle = kwargs.pop('fixed_model_linestyle', None)
    fixed_model_color = kwargs.pop('fixed_model_color', None)
    fixed_model_marker = kwargs.pop('fixed_model_marker', None)

    legend_kwargs = kwargs.extract(prefix='legend')
    arrow_kwargs = kwargs.extract(prefix='arrow')

    kwargs.setdefault('ax_xlabel', axis_labels['x'])
    kwargs.setdefault('ax_ylabel', axis_labels['y'])
    delayed_kwargs = update_axes(ax, kwargs, delay='ax_legend', update_ax=update_ax, update_fig=update_fig)
    simple_kwargs = kwargs.extract(prefix='_SIMPLE')

    has_labels = False
    for mi, (model, datapoints) in enumerate(modeldata.items()):
        for di, datapoint in enumerate(datapoints):
            if fixed_model_linestyle or (fixed_model_linestyle is None and len(datapoints) == 1):
                ls = linestyles[mi]
            else:
                ls = linestyles[di]
            if fixed_model_color is True or (fixed_model_color is None and len(modeldata) > 1):
                c = colors[mi]
            else:
                c = colors[di]

            if not has_labels and datapoint.get('label', None):
                has_labels = True

            label = datapoint.get('label', None)
            for i in range(len(datapoint['x'])):
                x, y = datapoint['x'][i], datapoint['y'][i]
                slope = y / x
                ax.axline(xycoord, slope=slope, label=label,
                          color = c, ls=ls, **kwargs)
                label = None

                if arrow:
                    if np.abs(slope) > 1:
                        y_arrow = np.array([arrow_position, arrow_position + 0.01]) * (-1 if y < 0 else 1)
                        x_arrow = 1 / slope * y_arrow
                    else:
                        x_arrow = np.array([arrow_position, arrow_position + 0.01]) * (-1 if x < 0 else 1)
                        y_arrow = slope * x_arrow

                    ax.arrow(x_arrow[0], y_arrow[1], x_arrow[1] - x_arrow[0], y_arrow[1] - y_arrow[0],
                            facecolor=c, **arrow_kwargs)

    update_axes(ax, delayed_kwargs, update_ax=update_ax, update_fig=update_fig)
    if legend or (legend is None and has_labels):
        create_legend(ax, **legend_kwargs)

    return ax

##################
### rose plots ###
################

@utils.add_shortcut('abundance', default_attrname ='abundance', unit=None)
@utils.add_shortcut('stdnorm', default_attrname ='stdnorm.Ri', unit=None)
@utils.add_shortcut('intnorm', default_attrname='intnorm.eRi', unit=None)
@utils.set_default_kwargs(
    ax_kw_ylabel_labelpad=20,
    legend_outside=True,)
def rose_hist(models, xkey, ykey, r=None, weights=1, *,
              default_attrname = None, unit=None,
              weights_default_attrname = None, weights_unit=None, weights_default_value=0,
              sum_weights=True, norm_weights=True,
              mask = None, ax = None, where=None,
              legend=None, update_ax = True, update_fig = True,
              kwargs=None):
    """
    Histogram plot on a rose diagram.
    """
    modeldata, axis_labels = rose_hist_get_data.raw(models, xkey, ykey, weights,
                                                    default_attrname=default_attrname, unit=unit,
                                                    weights_default_attrname=weights_default_attrname,
                                                    weights_unit=weights_unit,
                                                    weights_default_value=weights_default_value,
                                                    sum_weights=sum_weights, norm_weights=norm_weights,
                                                    mask=mask, where=where, kwargs=kwargs)
    return rose_hist_draw.raw(modeldata, axis_labels, r=r,
                              ax=ax, legend=legend, update_ax=update_ax, update_fig=update_fig,
                              kwargs=kwargs)

@utils.set_default_kwargs(inherits=rose_hist, match_signature=True)
def rose_hist_get_data(models, xkey, ykey, weights=1, *,
                        default_attrname =None, unit = None,
                        weights_default_attrname = None, weights_unit = None, weights_default_value = 0,
                        sum_weights = True, norm_weights = True,
                        mask = None, where = None,
                        kwargs=None):
    modeldata, axis_labels = get_data(models, {'x': xkey, 'y': ykey},
                                      where=where,
                                      default_attrname=default_attrname, unit=unit,
                                      mask=mask, mask_na=False,
                                      kwargs=None)

    func_weights = kwargs.pop('_SIMPLE_add_weights', add_weights)
    func_weights(modeldata, 'x',
                 weights=weights, sum_weights=sum_weights, norm_weights=norm_weights,
                 default_attrname=weights_default_attrname, unit=weights_unit,
                 default_value=weights_default_value, mask=mask, mask_na=False)

    return modeldata, axis_labels



@utils.set_default_kwargs(inherits=rose_hist, match_signature=True)
def rose_hist_draw(modeldata, axis_labels, r=None, *,
                   ax = None, legend=None, update_ax = True, update_fig = True,
                   kwargs=None):
    ax = get_axes(ax)
    rose_kwargs = kwargs.extract(prefix='rose')
    if ax.name != 'rose':
        ax = create_rose_plot(ax, **rose_kwargs)

    if not isinstance(r, Sequence):
        r = [r for i in range(len(modeldata))]
    elif len(r) != len(modeldata):
        raise ValueError(f'Size of r must match size of models ({len(r)}!={len(modeldata)})')


    legend_kwargs = kwargs.extract(prefix='legend')
    delayed_kwargs = update_axes(ax, kwargs, delay='ax_legend', update_ax=update_ax, update_fig=update_fig)
    simple_kwargs = kwargs.extract(prefix='_SIMPLE')

    kwargs.setdefault('ax_xlabel', axis_labels['x'])
    kwargs.setdefault('ax_ylabel', axis_labels['y'])

    has_labels = False
    for mi, (model, datapoints) in enumerate(modeldata.items()):
        for di, datapoint in enumerate(datapoints):
            if not has_labels and datapoint.get('label', None):
                has_labels = True
            ax.mhist((datapoint['x'], datapoint['y']), r=r[mi], weights=datapoint['w'],
                     label=datapoint.get('label', None), **kwargs)

    update_axes(ax, delayed_kwargs, update_ax=update_ax, update_fig=update_fig)
    if legend or (legend is None and has_labels):
        if ax._colorbar is not None:
            legend_kwargs.setdefault('outside_margin', 0.35)
        create_legend(ax, **legend_kwargs)

    return ax

########################
### Depricated stuff ###
########################

@utils.deprecation_warning('``plot_intnorm`` has been deprecated: Use ``plot.intnorm`` instead')
def plot_intnorm(*args, **kwargs):
    return plot.intnorm(*args, **kwargs)

@utils.deprecation_warning('``plot_abundance`` has been deprecated: Use ``plot.stdnorm`` instead')
def plot_simplenorm(*args, **kwargs):
    return plot.stdnorm(*args, **kwargs)

@utils.deprecation_warning('``mhist`` has been deprecated: Use ``plot.rose_hist`` instead')
def mhist(*args, **kwargs):
    kwargs.setdefault('rose_colorbar_show', True)
    kwargs.setdefault('cmap', True)
    return rose_hist(*args, **kwargs)

# TODO No longer used. Delete when new code has been tests.
def __prep_hist(models, key, weights,
               sum_weights, norm_weights, flip, filled,
               default_attrname, unit, weights_default_attrname, weights_unit, weights_default_value,
               mask, label_kwargs, kwargs):
    if flip:
        axis = 'y'
    else:
        axis = 'x'

    modeldata, axis_labels = get_data(models, {axis: key},
                                      default_attrname=default_attrname, unit=unit,
                                      mask=mask, mask_na=False, _kwargs=kwargs, **label_kwargs)

    func_weights = kwargs.pop('_SIMPLE_add_weights', add_weights)
    func_weights(modeldata, axis,
                 weights=weights, sum_weights=sum_weights, norm_weights=norm_weights,
                 default_attrname=weights_default_attrname, unit=weights_unit,
                 default_value=weights_default_value, mask=mask, mask_na=False)

    if filled is None:
        if len(models) > 1 or (len(models) > 0 and len(next(iter(modeldata.values()))) > 1):
            filled = False
        else:
            filled = True

    if filled is True:
        kwargs.setdefault('histtype', 'stepfilled')
    else:
        kwargs.setdefault('histtype', 'step')

    if flip:
        kwargs.setdefault('orientation', 'horizontal')
        kwargs.setdefault('ax_ylabel', axis_labels['y'])
    else:
        kwargs.setdefault('orientation', 'vertical')
        kwargs.setdefault('ax_xlabel', axis_labels['x'])

    return modeldata, axis, filled

def __rose_prep(models, xkey, ykey, r, weights, *,
               default_attrname=None, unit=None, sum_weights=True, norm_weights=True,
               weights_default_attrname=None, weights_unit=None, weights_default_value=0,
               mask=None, ax=None, where=None, where_kwargs={},
               **kwargs):
    ax = get_axes(ax)
    rose_kwargs = utils.extract_kwargs(kwargs, prefix='rose')
    if ax.name != 'rose':
        ax = create_rose_plot(ax, **rose_kwargs)

    where_kwargs.update(utils.extract_kwargs(kwargs, prefix='where'))
    models = get_models(models, where=where, where_kwargs=where_kwargs)

    label_kwargs = utils.extract_kwargs(kwargs, 'label', 'prefix_label', 'suffix_label',
                                        'key_in_label', 'numer_in_label', 'denom_in_label',
                                        'model_in_label', 'unit_in_label', 'attrname_in_label')

    modeldata, axis_labels = get_data(models, {'x': xkey, 'y': ykey},
                                         default_attrname=default_attrname, unit=unit,
                                         mask=mask, mask_na=False, _kwargs=kwargs, **label_kwargs)

    kwargs.setdefault('ax_xlabel', axis_labels['x'])
    kwargs.setdefault('ax_ylabel', axis_labels['y'])

    func_weights = kwargs.pop('_SIMPLE_add_weights', add_weights)
    func_weights(modeldata, 'x',
                 weights=weights, sum_weights=sum_weights, norm_weights=norm_weights,
                 default_attrname=weights_default_attrname, unit=weights_unit,
                 default_value=weights_default_value, mask=mask, mask_na=False)

    if not isinstance(r, Sequence):
        r = [r for i in range(len(modeldata))]
    elif len(r) != len(modeldata):
        raise ValueError(f'Size of r must match size of models ({len(r)}!={len(modeldata)})')

    return ax, models, r, modeldata, kwargs

def __plot_prep(models, ax, where, kwargs):
    ax = get_axes(ax)  # We are working on the axes object proper

    # Get the linestyle, color and marker for each thing to be plotted.
    linestyles, colors, markers = parse_lscm(kwargs.extract(('linestyle', True), ('color', True), ('marker', False)))
    fixed_model_linestyle = kwargs.pop('fixed_model_linestyle', None)
    fixed_model_color = kwargs.pop('fixed_model_color', None)
    fixed_model_marker = kwargs.pop('fixed_model_marker', None)

    legend_kwargs = utils.extract_kwargs(kwargs, prefix='legend')

    # If there is only one model it is set as the title to make the legend shorter
    model_in_label = label_kwargs.pop('model_in_label', None)
    if len(models) == 1 and model_in_label is None:
        label_kwargs['model_in_label'] = False
        legend_kwargs.setdefault('title', models[0].name)
    else:
        label_kwargs['model_in_label'] = model_in_label

    return (ax, models,
            linestyles, colors, markers,
            fixed_model_linestyle, fixed_model_color, fixed_model_marker,
            legend_kwargs, label_kwargs)
