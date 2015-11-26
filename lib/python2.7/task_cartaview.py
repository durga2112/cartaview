import sys
import os
import inspect
import string
import time
from taskinit import *
import viewertool
import carta.cartavis as cartavis
###
### if numpy is not available, make float64 and ndarray redundant checks...
###
try:
    from numpy import float64 as float64
    from numpy import ndarray as ndarray
except:
    float64 = float
    ndarray = list

class __cartaview_class(object):
    "cartaview() task with local state for created viewer tool"

    def __init__( self ):
        self.local_vi = None
        self.local_ving = None
        self.__dirstack = [ ]
        self.__colorwedge_queue = [ ]

    def __call__(self, executable, configFile, port, htmlFile,
                 imageFile):
        """ Old parameters:
               infile=None,displaytype=None,channel=None,zoom=None,outfile=None,
               outscale=None,outdpi=None,outformat=None,outlandscape=None,gui=None
        The cartaview task will display images in raster, contour, vector or
        marker form.  Images can be blinked, and movies are available
        for spectral-line image cubes.  For measurement sets, many
        display and editing options are available.

        examples of usage:

        cartaview
        cartaview "myimage.im"
        cartaview "myrestorefile.rstr"
        
        cartaview "myimage.im", "contour"

        cartaview "'myimage1.im' - 2 * 'myimage2.im'", "lel"
    
        Executing cartaview( ) will bring up a display panel
        window, which can be resized.  If no data file was specified,
        a Load Data window will also appear.  Click on the desired data
        file and choose the display type; the rendered data should appear
        on the display panel.

        A Data Display Options window will also appear.  It has drop-down
        subsections for related options, most of which are self-explanatory.
      
        The state of the cartaview task -- loaded data and related display
        options -- can be saved in a 'restore' file for later use.
        You can provide the restore filename on the command line or
        select it from the Load Data window.

        See the cookbook for more details on using the cartaview task.
    
        Keyword arguments:
        infile -- Name of file to visualize
            default: ''
            example: infile='ngc5921.image'
            If no infile is specified the Load Data window
            will appear for selecting data.
        displaytype -- (optional): method of rendering data
            visually (raster, contour, vector or marker).  
            You can also set this parameter to 'lel' and
            provide an lel expression for infile (advanced).
            default: 'raster'
            example: displaytype='contour'

        Note: the filetype parameter is optional; typing of
                data files is now inferred.
                example:  cartaview infile='my.im'
            implies:  cartaview infile='my.im', filetype='raster'
        the filetype is still used to load contours, etc.


        """
        a=inspect.stack()
        stacklevel=0
        for k in range(len(a)):
            if a[k][1] == "<string>" or (string.find(a[k][1], 'ipython console') > 0 or string.find(a[k][1],"casapy.py") > 0):
                stacklevel=k

        myf=sys._getframe(stacklevel).f_globals

        casalog.origin('cartaview')

        v = cartavis.Cartavis(executable, configFile, int(port), htmlFile,
                              imageFile)
        return v

cartaview = __cartaview_class( )
