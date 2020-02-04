#! /usr/bin/python

#
# Description:This will read in the array data file that contains all the leave histogram information
# ================================================================
# Time-stamp: "2019-04-22 16:55:25 trottar"
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
# np.set_printoptions(threshold=sys.maxsize)


class pyPlot:
    def __init__(self,rootName,tree1,T1_arrkey,T1_arrhist):
        self.rootName = rootName
        self.tree1 = tree1
        self.T1_arrkey = T1_arrkey
        self.T1_arrhist = T1_arrhist
        
    def progressBar(self,value, endvalue, bar_length):

        percent = float(value) / endvalue
        arrow = '=' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))
        
        sys.stdout.write(" \r[{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()
        
    # Retrieves the array data file and creates new leaves from this
    def pullArray(self):
        
        data = np.load("%s.npz" % self.rootName)
        
        T1 = data[self.T1_arrkey]
        T1_hist = data[self.T1_arrhist]
        
        return[T1,T1_hist]

    # Creates a dictionary that stores leaf names with the corresponding array
    def dictionary(self):
            
        [T1,T1_hist] = self.pullArray()
        
        T1_leafdict = dict(zip(T1, T1_hist))
        
        return[T1_leafdict]
        
    # A quick way to look up a leaf name for its array
    def lookup(self,key):
        
        [T1_leafdict] = self.dictionary()
        
        T_leafFound = T1_leafdict.get(key,"Leaf name not found")
        
        if (T_leafFound == "Leaf name not found"):
            print("ERROR: %s not found" % key)
            sys.exit()
                
        return[T_leafFound]
            
    # Recreates the histograms of the root file
    def recreateLeaves(self):
            
        [T1_leafdict] = self.dictionary()
                
        binwidth = 1.0
    
        i=1
        print("Looing at TTree %s" % self.tree1)
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

        print("\nTTree %s completed" % self.tree1)
    
    def setbin(self,plot,numbin,xmin=None,xmax=None):
        
        if (xmin or xmax):
            leaf = self.fixBin(plot,plot,xmin,xmax)[0]
        else:
            leaf = plot
            
        binwidth = (abs(leaf).max()-abs(leaf).min())/numbin
        
        bins = np.arange(min(leaf), max(leaf) + binwidth, binwidth)

        return [bins]

    def fixBin(self,cut,plot,low,high):
    
        [T1_leafdict] = self.dictionary()
            
        arrCut = cut
        arrPlot = plot
        
        arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]

        return [arrPlot]
    
class pyCut:
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

    # def densityPlot(self,x,y,title,xlabel,ylabel,binx,biny,xmin=None,xmax=None,ymin=None,ymax=None,cuts=None,figure=None,sub=None):

    #     if cuts:
    #         xcut  = self.applyCuts(x,cuts)[0]
    #         ycut = self.applyCuts(y,cuts)[0]
    #     else:
    #         xcut = x
    #         ycut = y
    #     if sub or figure:
    #         ax = figure.add_subplot(sub)
    #     else:
    #         fig, ax = plt.subplots(tight_layout=True,figsize=(11.69,8.27))
    #     if (xmin or xmax or ymin or ymax):
    #         hist = ax.hist2d(xcut, ycut,bins=(p.setbin(x,binx,xmin,xmax)[0],p.setbin(y,biny,ymin,ymax)[0]), norm=colors.LogNorm())
    #     else:
    #         hist = ax.hist2d(xcut, ycut,bins=(p.setbin(x,binx)[0],p.setbin(y,biny)[0]), norm=colors.LogNorm())
    #     plt.title(title)
    #     plt.xlabel(xlabel)
    #     plt.ylabel(ylabel)

    # def polarPlot(self,theta,r,title,thetalabel,rlabel,bintheta,binr,thetamin=None,thetamax=None,rmin=None,rmax=None,cuts=None,figure=None,sub=None):

    #     if cuts:
    #         thetacut  = self.applyCuts(theta,cuts)[0]
    #         rcut = self.applyCuts(r,cuts)[0]
    #     else:
    #         thetacut = theta
    #         rcut = r
    #     xy = np.vstack([thetacut, rcut])
    #     z = stats.gaussian_kde(xy)(xy)
    #     idx = z.argsort()
    #     x, y, z = np.array(thetacut)[idx], np.array(rcut)[idx], z[idx]
    #     if sub or figure:
    #         ax = figure.add_subplot(sub,polar=True)
    #     else:
    #         ax = plt.subplot(111,polar=True)
    #     if (thetamin or thetamax or rmin or rmax):
    #         hist = ax.scatter(thetacut, rcut, c=z, edgecolor='', alpha = 0.75)
    #     else:
    #         hist = ax.scatter(thetacut, rcut, c=z, edgecolor='', alpha = 0.75)
    #     ax.grid(True)
    #     plt.title(title)
    #     plt.xlabel(thetalabel)
    #     plt.ylabel(rlabel)
    #     # plt.colorbar()    