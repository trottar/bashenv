#! /usr/bin/python

#
# Description:This will read in the array data file that contains all the leave histogram information
# ================================================================
# Time-stamp: "2019-04-08 17:16:11 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

import logging

# Gets rid of matplot logging DEBUG messages
plt_logger = logging.getLogger('matplotlib')
plt_logger.setLevel(logging.WARNING)

import matplotlib.pyplot as plt
from matplotlib import interactive
import numpy as np
import sys

rootName =  sys.argv[1]

tree1 = sys.argv[2]

T1_arrkey =  "leafName1"
T1_arrhist = "histData1"

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
        # print key, "->", arr)
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

    [T1,T1_hist] = pullArray()
    
    [T1_leafdict] = dictionary()

    arrCut = T1_leafdict[cut]
    arrPlot = T1_leafdict[plot]
    
    arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]

    return[arrPlot]

def cutRecursive(lastCut,newcut,plot,low,high):

    [T1,T1_hist] = pullArray()
    
    [T1_leafdict] = dictionary()

    arrLast = lastCut
    arrCut = T1_leafdict[newcut]
    arrPlot = T1_leafdict[plot]
    
    arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]

    arrNew = np.intersect1d(arrLast,arrPlot)

    return[arrNew]    
    
def densityPlot(x,y,title):

    fig, ax = plt.subplots(tight_layout=True)
    
    hist = ax.hist2d(x, y,bins=40, norm=colors.LogNorm())
    plt.title(title, fontsize =16)
    
        
# Can call arrays to create your own plots
def customPlots():

    [T1_leafdict] = dictionary()
    
    
def main() :

    customPlots()
    # recreateLeaves()
    plt.show()
    
if __name__=='__main__': main()
