#! /usr/bin/python

#
# Description:This will read in the array data file that contains all the leave histogram information
# ================================================================
# Time-stamp: "2019-04-11 16:14:07 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

from __future__ import division
import logging

# Gets rid of matplot logging DEBUG messages
plt_logger = logging.getLogger('matplotlib')
plt_logger.setLevel(logging.WARNING)

import matplotlib.pyplot as plt
from matplotlib import interactive
from matplotlib import colors
import numpy as np
import math
import sys

rootName =  sys.argv[1]

tree1 = sys.argv[2]

T1_arrkey =  "leafName"
T1_arrhist = "histData"

# Retrieves the array data file and creates new leaves from this
def pullArray():
    
    data = np.load("%s.npz" % rootName)

    T1 = data[T1_arrkey]
    T1_hist = data[T1_arrhist]

    return[T1,T1_hist]

# Creates a dictionary that stores leaf names with the corresponding array
def dictionary():

    [T1,T1_hist] = pullArray()
    
    T1_leafdict = dict(zip(T1, T1_hist))

    return[T1_leafdict]

# A quick way to look up a leaf name for its array
def lookup(key):

    [T1_leafdict] = dictionary()
    
    T_leafFound = T1_leafdict.get(key,"Leaf name not found")

    return[T_leafFound]

# Recreates the histograms of the root file
def recreateLeaves():

    [T1_leafdict] = dictionary()

    binwidth = 1.0
    
    i=1
    print("Looing at TTree %s" % tree1)
    print("Enter n to see next plot and q to exit program\n")
    for key,arr in T1_leafdict.items():
        # print key, -
        if (np.all(arr == 0.)):
            print("Histogram %s: Empty array" % key)
        elif ( 2. > len(arr)) :
            print("Histogram %s: Only one element" % key)
        else:
            binwidth = (abs(arr).max())/100
            plt.figure()
            plt.hist(arr,bins=np.arange(min(arr), max(arr) + binwidth, binwidth),histtype='step', stacked=True, fill=False )
            plt.title(key, fontsize =16)
            foutname = 'fig_'+key+'.png'
            i+=1

    print("\nTTree %s completed" % tree1)

def cut(cut,plot,low,high):
    
    [T1_leafdict] = dictionary()

    arrCut = T1_leafdict[cut]
    arrPlot = T1_leafdict[plot]
    
    arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]

    return[arrPlot]

def cutRecursive(lastCut,newcut,plot,low,high):
    
    [T1_leafdict] = dictionary()

    arrLast = lastCut
    arrCut = T1_leafdict[newcut]
    arrPlot = T1_leafdict[plot]
    
    arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]

    arrNew = np.intersect1d(arrLast,arrPlot)

    return[arrNew]

# Wider the binsize the fewer bins
def setbin(leaf,binsize):

    binwidth = (abs(leaf).max()-abs(leaf).min())/binsize
    
    bins = np.arange(min(leaf), max(leaf) + binwidth, binwidth)

    return[bins]
    
def densityPlot(x,y,title,xlabel,ylabel,binx,biny):

    fig, ax = plt.subplots(tight_layout=True)
    hist = ax.hist2d(x, y,bins=(setbin(x,binx)[0],setbin(y,biny)[0]), norm=colors.LogNorm())
    plt.title(title, fontsize =16)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
# Can call arrays to create your own plots
def customPlots():
    
def main() :

    customPlots()
    # recreateLeaves()
    plt.show()
    
if __name__=='__main__': main()
