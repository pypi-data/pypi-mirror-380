#Various routines for plotting remix output data
#Generally dependant on basemap

# Standard modules

# Third-party modules
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.pyplot as plt
import h5py

# Kaipy modules
import kaipy.kaiViz as kv
import cartopy.crs as ccrs
import cartopy.feature as cfeature

r2deg = 180.0/np.pi
pType = 'npstere'
#pType = 'npaeqd'
#pType = 'nplaea'
cMax = 2.0 #Max current density

dfs = "medium"
fcMap = "bwr" #Colormap for current

#Potential plots
pMax = 60.0 #Max potential [kV]
doAPC = True #Do solid/dash for potential contours
dpC = 5.0 #Spacing [kV] for potential contours
#pMap = "PRGn"
pMax = 35.0 #Max potential [kV]
apMap = "bone" #Absolute value of potential map
pMap = apMap

NumP = 10
pVals = np.linspace(-pMax,pMax,NumP)
cLW = 0.5
cAl = 0.5 #Contour alpha

lon0 = -90
R0 = 6.5/6.38

dLon = 45.0 #Degree spacing for longitude
dLat = 10.0 #Degree spacing for latitude

AxEC = 'silver'
gC = 'dimgrey'

gDash = [1,0]
gLW = 0.125

#Adds inset figure to axis using data from fmix
#dxy = [width%,height%]
def CMIPic(nLat, nLon, llBC, P, C, AxM=None, doNorth=True, loc="upper left", dxy=[20, 20]):
    """
    Generate a map plot using Cartopy and plot data on it.

    Args:
        nLat (int): Number of latitude lines.
        nLon (int): Number of longitude lines.
        llBC (float): Bounding latitude for the map.
        P (numpy.ndarray): Data to be plotted as contours.
        C (numpy.ndarray): Data to be plotted as pcolormesh.
        AxM (matplotlib.axes.Axes, optional): The axes to add the inset figure to. If not provided, the current axes will be used.
        doNorth (bool, optional): Flag indicating whether the map is in the northern hemisphere. Default is True.
        loc (str, optional): Location of the inset figure. Default is "upper left".
        dxy (list, optional): Width and height of the inset figure as a percentage of the parent axes. Default is [20, 20].
    """
    if doNorth:
        tStr = "North"
        projection = ccrs.NorthPolarStereo()
    else:
        tStr = "South"
        projection = ccrs.SouthPolarStereo()

    vC = kv.genNorm(cMax)
    vP = kv.genNorm(pMax)

    # Add inset figure to the passed axis
    wStr = "%f%%" % (dxy[0])
    hStr = "%f%%" % (dxy[1])

    if AxM is None:
        AxM = plt.gca()

    Ax = inset_axes(AxM, width=wStr, height=hStr, loc=loc)

    for spine in Ax.spines.values():
        spine.set_edgecolor(AxEC)
    Ax.patch.set_alpha(0)
    if doNorth:
        Ax.set_xlabel(tStr, fontsize=dfs, color=AxEC)
    else:
        Ax.set_title(tStr, fontsize=dfs, color=AxEC)

    # Set up the Cartopy map
    Ax = plt.axes(projection=projection)
    Ax.set_extent([-180, 180, llBC, 90] if doNorth else [-180, 180, -90, llBC], crs=ccrs.PlateCarree())

    # Add features
    Ax.add_feature(cfeature.COASTLINE, edgecolor=gC, linewidth=gLW)
    Ax.add_feature(cfeature.BORDERS, edgecolor=gC, linewidth=gLW)

    # Latitude and longitude gridlines
    gl = Ax.gridlines(draw_labels=False, linewidth=gLW, color=gC, alpha=0.5, linestyle='--')
    gl.xlocator = plt.MultipleLocator(dLon)
    gl.ylocator = plt.MultipleLocator(dLat)

    # Create meshgrid for data
    Lat0 = np.linspace(90, llBC, nLat + 0) if doNorth else np.linspace(-90, llBC, nLat + 0)
    Lat1 = np.linspace(90, llBC, nLat + 1) if doNorth else np.linspace(-90, llBC, nLat + 1)
    Lon0 = np.linspace(0, 360, nLon + 0)
    Lon1 = np.linspace(0, 360, nLon + 1)
    LonC, LatC = np.meshgrid(Lon0, Lat0)
    LonI, LatI = np.meshgrid(Lon1, Lat1)

    # Plot data
    mesh = Ax.pcolormesh(LonI, LatI, C, transform=ccrs.PlateCarree(), norm=vC, cmap=fcMap)

    # Plot potential contours
    if doAPC:
        # Positive contours
        vAPp = kv.genNorm(0, pMax)
        pVals = np.arange(dpC, pMax, dpC)
        if P.max() > dpC:
            Ax.contour(LonC, LatC, P, pVals, transform=ccrs.PlateCarree(), norm=vAPp, cmap=apMap, alpha=cAl, linewidths=cLW, linestyles='solid')
        # Negative contours
        vAPm = kv.genNorm(-pMax, 0)
        apMapm = apMap + "_r"
        pVals = -pVals[::-1]
        if P.min() < -dpC:
            Ax.contour(LonC, LatC, P, pVals, transform=ccrs.PlateCarree(), norm=vAPm, cmap=apMapm, alpha=cAl, linewidths=cLW, linestyles='dashed')
    else:
        Ax.contour(LonC, LatC, P, pVals, transform=ccrs.PlateCarree(), norm=vP, cmap=pMap, alpha=cAl, linewidths=cLW)

def AddPotCB(Ax, Lab="Potential [kV]", Ntk=7):
    """
    Add a potential colorbar to the given axis.

    Args:
        Ax (matplotlib.axes.Axes): The axis to add the colorbar to.
        Lab (str, optional): The label for the colorbar. Default is "Potential [kV]".
        Ntk (int, optional): The number of ticks on the colorbar. Default is 7.
    """
    if (doAPC):
        vP = kv.genNorm(0, pMax)
        cm = apMap
    else:
        vP = kv.genNorm(-pMax, pMax)
        cm = pMap
    kv.genCB(Ax, vP, Lab, cM=cm, Ntk=Ntk)


def AddCBs(Ax1, Ax2, Lab1="Potential [kV]", Lab2="FAC", Ntk1=7, Ntk2=5, doFlip=True):
    """
    Add colorbars to the given axes.

    Args:
        Ax1 (matplotlib.axes.Axes): The first axes object to add the colorbar to.
        Ax2 (matplotlib.axes.Axes): The second axes object to add the colorbar to.
        Lab1 (str, optional): The label for the colorbar on Ax1. Default is "Potential [kV]".
        Lab2 (str, optional): The label for the colorbar on Ax2. Default is "FAC".
        Ntk1 (int, optional): The number of ticks for the colorbar on Ax1. Default is 7.
        Ntk2 (int, optional): The number of ticks for the colorbar on Ax2. Default is 5.
        doFlip (bool, optional): Whether to flip the colorbar on Ax2. Default is True.
    """
    if (doAPC):
        vP = kv.genNorm(0, pMax)
        cm = apMap
    else:
        vP = kv.genNorm(-pMax, pMax)
        cm = pMap
    kv.genCB(Ax1, vP, Lab1, cM=cm, Ntk=Ntk1)
    kv.genCB(Ax2, kv.genNorm(cMax), Lab2, fcMap, Ntk=Ntk2)
    if (doFlip):
        Ax2.xaxis.tick_top()
        Ax2.xaxis.set_label_position('top')

