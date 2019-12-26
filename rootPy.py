#! /usr/bin/python

#
# Description:This will read in the array data file that contains all the leave histogram information
# ================================================================
# Time-stamp: "2019-08-14 21:10:09 trottar"
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

# Suppresses unwanted numpy warning
import warnings
import numpy as np
warnings.simplefilter(action='ignore', category=FutureWarning)

import matplotlib.pyplot as plt
from matplotlib import interactive
from matplotlib import colors
import time, math, sys

# garbage collector
import gc
gc.collect()

class pyDict(dict):
    
    def __init__(self,rootName,tree1,T1_arrkey,T1_arrhist):
        self.rootName = rootName
        self.tree1 = tree1
        self.T1_arrkey = T1_arrkey
        self.T1_arrhist = T1_arrhist
        # Retrieves the array data file and creates new leaves from this
        data = np.load("%s.npz" % self.rootName)        
        T1 = data[self.T1_arrkey]
        T1_hist = data[self.T1_arrhist]
        data.close()
        # Creates a dictionary that stores leaf names with the corresponding array
        self.T1_leafdict = dict(zip(T1, T1_hist))
        
class pyMisc(pyDict):

    def progressBar(self,value, endvalue, bar_length):

        percent = float(value) / endvalue
        arrow = '=' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))
        
        sys.stdout.write(" \r[{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()
        
    # A quick way to look up a leaf name for its array
    def lookup(self,key):

        T_leafFound = self.T1_leafdict.get(key,"Leaf name not found")
        
        if (T_leafFound == "Leaf name not found"):
            print("ERROR: %s not found" % key)
            sys.exit()
        
        return[T_leafFound]
                
    def setbin(self,plot,numbin,xmin=None,xmax=None):
        
        if (xmin or xmax):
            leaf = self.fixBin(plot,plot,xmin,xmax)[0]
        else:
            leaf = plot
            
        binwidth = (abs(leaf).max()-abs(leaf).min())/numbin
        
        bins = np.arange(min(leaf), max(leaf) + binwidth, binwidth)

        return [bins]

    def fixBin(self,cut,plot,low,high):
            
        arrCut = cut
        arrPlot = plot
        
        arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]

        return [arrPlot]
    
class pyPlot(pyDict):
    
    def __init__(self, cutDict):
        self.cutDict = cutDict
        
    def cut(self,key):
            
        return[self.cutDict.get(key,"Leaf name not found")]

    def applyCuts(self,leaf,cuts=None):
        
        if cuts:
            tmp = leaf
            applycut = 'tmp['
            i=0
            while i < (len(cuts)-1):
                applycut += 'self.cut("%s")[0] & ' % cuts[i]
                i+=1
            applycut += 'self.cut("%s")[0]]' % cuts[len(cuts)-1]
            tmp = eval(applycut)
        else:
            print 'No cuts applied to %s' % leaf
            tmp = leaf
        
        return [tmp]

        # Recreates the histograms of the root file
    def recreateLeaves(self):
                
        binwidth = 1.0
    
        i=1
        print("Looing at TTree %s" % self.tree1)
        print("Enter n to see next plot and q to exit program\n")
        # for key,arr in self.T1_leafdict.dictionary().items():
        for key,arr in self.T1_leafdict.items():
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

        print("\nTTree %s completed" % self.tree1)

    def densityPlot(self,x,y,title,xlabel,ylabel,binx,biny,pyMisc,
                    xmin=None,xmax=None,ymin=None,ymax=None,cuts=None,figure=None,ax=None,layered=True):
        if cuts:
            xcut  = self.applyCuts(x,cuts)[0]
            ycut = self.applyCuts(y,cuts)[0]
        else:
            xcut = x
            ycut = y
        if ax or figure:
            print ""
        else:
            fig, ax = plt.subplots(tight_layout=True,figsize=(11.69,8.27))
        if (xmin or xmax or ymin or ymax):
            # norm=colors.LogNorm() makes colorbar normed and logarithmic
            hist = ax.hist2d(xcut, ycut,bins=(pyMisc.setbin(x,binx,xmin,xmax)[0],pyMisc.setbin(y,biny,ymin,ymax)[0]), norm=colors.LogNorm())
        else:
            # norm=colors.LogNorm() makes colorbar normed and logarithmic
            hist = ax.hist2d(xcut, ycut,bins=(pyMisc.setbin(x,binx)[0],pyMisc.setbin(y,biny)[0]), norm=colors.LogNorm())
        if layered is True :
            plt.colorbar(hist[3], ax=ax, spacing='proportional', label='Number of Events')

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        inputVal = [x,y]
        
        if (xmin or xmax or ymin or ymax):
            binVal = [pyMisc.setbin(x,binx,xmin,xmax)[0],pyMisc.setbin(y,biny,ymin,ymax)[0]]
        else:
            binVal = [pyMisc.setbin(x,binx)[0],pyMisc.setbin(y,biny)[0]]
        return binVal


    def polarPlot(self,theta,r,title,thetalabel,rlabel,bintheta,binr,pyMisc,
                  thetamin=None,thetamax=None,rmin=None,rmax=None,cuts=None,figure=None,ax=None):

        if cuts:
            thetacut  = self.applyCuts(theta,cuts)[0]
            rcut = self.applyCuts(r,cuts)[0]
        else:
            thetacut = theta
            rcut = r
        xy = np.vstack([thetacut, rcut])
        z = stats.gaussian_kde(xy)(xy)
        idx = z.argsort()
        x, y, z = np.array(thetacut)[idx], np.array(rcut)[idx], z[idx]
        if ax or figure:
            # ax = figure.add_subplot(sub,polar=True)
            print ""
        else:
            fig,ax = plt.subplot(111,polar=True)
        if (thetamin or thetamax or rmin or rmax):
            hist = ax.scatter(thetacut, rcut, c=z, edgecolor='', alpha = 0.75)
        else:
            hist = ax.scatter(thetacut, rcut, c=z, edgecolor='', alpha = 0.75)
        ax.grid(True)
        plt.title(title)
        plt.xlabel(thetalabel)
        plt.ylabel(rlabel)
        # plt.colorbar()    
