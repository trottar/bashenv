#! /usr/bin/python

#
# Description: Script to quickly convert ROOT leaf histograms into python matplotlib, just need to
# include...
'''

# My class function
sys.path.insert(0,'/home/trottar/bin/python/')
from root2numpy import pyPlot

rootName = "Path/to/root/file"
treeName = <NameofTree>
leafName =  {"<HistoVarName>": "<LeafName>",
}

print leafName
p = pyPlot(rootName,tree1,leafName)

rootName =  p.newDict()
locals().update(rootName)

'''
# ================================================================
# Time-stamp: "2020-01-30 15:39:49 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

from __future__ import division
import logging
import uproot as up
import numpy as np
import time, math, sys, time, os
    
class pyDict(dict):
    
    def __init__(self,inputROOT,inputTree,inputLeaf):
        self.inputROOT = inputROOT
        self.inputTree = inputTree
        self.inputLeaf = inputLeaf
        
        start = time. time()
        
        # Opens root file and gets tree info
        print "Looking at root file:", inputROOT
        print "\nLooking at leaf", inputLeaf.values(), "in tree", inputTree
        rfile = up.open(inputROOT)
        Tree = rfile[inputTree]
    
        print("\nConverting root file to numpy arrays...\n")
    
        '''

        Convert a TTree in a ROOT file into a NumPy structured array
        T1_array = Tree.arrays(["T.coin.*", "CTime.*","P.*","H.*"])
        T1_array = Tree.arrays(["T.coin.*"])
        
        Below are all the leaves needed to set the reference times for each detector

        '''
        
        leafName = Tree.arrays(list(inputLeaf.values()))
        
        histName = list(inputLeaf.keys())

        leafName = leafName.items()

        i=0
        for key,value in inputLeaf.items():
            # Check if float (i.e. histogram)
            if type(leafName[i][1][0]) is np.dtype('>f8').type or np.dtype('>f8').type: 
                inputLeaf[key] = leafName[i][1]
                print inputLeaf[key]
            i+=1

        # Redefine dictionary, replacing leaf names with histogram values
        self._newDict = inputLeaf

        end = time. time()
        print("\nTime to pull root file: %0.1f seconds" % (end-start))
        
    def newDict(self):
        return self._newDict
        
class pyPlot(pyDict):

    def progressBar(self,value, endvalue, bar_length):

        percent = float(value) / endvalue
        arrow = '=' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))
        
        sys.stdout.write(" \r[{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()
                
    def setbin(self,plot,numbin,xmin=None,xmax=None):
        
        if (xmin or xmax):
            leaf = self.fixBin(plot,plot,xmin,xmax)
        else:
            leaf = plot
            
        binwidth = (abs(leaf).max()-abs(leaf).min())/numbin
        
        bins = np.arange(min(leaf), max(leaf) + binwidth, binwidth)

        return bins

    def fixBin(self,cut,plot,low,high):
            
        arrCut = cut
        arrPlot = plot
        
        arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]

        return arrPlot
        
    def cut(self,key):
            
        return[self.cutDict.get(key,"Leaf name not found")]

    def applyCuts(self,leaf,cuts=None):
        
        if cuts:
            tmp = leaf
            applycut = 'tmp['
            i=0
            while i < (len(cuts)-1):
                applycut += 'self.cut("%s") & ' % cuts[i]
                i+=1
            applycut += 'self.cut("%s")]' % cuts[len(cuts)-1]
            tmp = eval(applycut)
        else:
            print 'No cuts applied to %s' % leaf
            tmp = leaf
        
        return tmp
    
    def densityPlot(self,x,y,title,xlabel,ylabel,binx,biny,pyMisc,
                    xmin=None,xmax=None,ymin=None,ymax=None,cuts=None,figure=None,ax=None,layered=True):
        if cuts:
            xcut  = self.applyCuts(x,cuts)
            ycut = self.applyCuts(y,cuts)
        else:
            xcut = x
            ycut = y
        if ax or figure:
            print ""
        else:
            fig, ax = plt.subplots(tight_layout=True,figsize=(11.69,8.27))
        if (xmin or xmax or ymin or ymax):
            # norm=colors.LogNorm() makes colorbar normed and logarithmic
            hist = ax.hist2d(xcut, ycut,bins=(pyMisc.setbin(x,binx,xmin,xmax),pyMisc.setbin(y,biny,ymin,ymax)), norm=colors.LogNorm())
        else:
            # norm=colors.LogNorm() makes colorbar normed and logarithmic
            hist = ax.hist2d(xcut, ycut,bins=(pyMisc.setbin(x,binx),pyMisc.setbin(y,biny)), norm=colors.LogNorm())
        if layered is True :
            plt.colorbar(hist[3], ax=ax, spacing='proportional', label='Number of Events')

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        inputVal = [x,y]
        
        if (xmin or xmax or ymin or ymax):
            binVal = [pyMisc.setbin(x,binx,xmin,xmax),pyMisc.setbin(y,biny,ymin,ymax)]
        else:
            binVal = [pyMisc.setbin(x,binx),pyMisc.setbin(y,biny)]
        return binVal


    def polarPlot(self,theta,r,title,thetalabel,rlabel,bintheta,binr,pyMisc,
                  thetamin=None,thetamax=None,rmin=None,rmax=None,cuts=None,figure=None,ax=None):

        if cuts:
            thetacut  = self.applyCuts(theta,cuts)
            rcut = self.applyCuts(r,cuts)
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

