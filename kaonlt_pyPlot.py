#! /usr/bin/python

#
# Description:This will read in the array data file that contains all the leave histogram information
# ================================================================
# Time-stamp: 2019-04-08 08:07:33 trottar
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

from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText, TTreeReader, TTreeReaderValue
from ROOT import gROOT
from rootpy.interactive import wait
import matplotlib.pyplot as plt
from matplotlib import interactive
from matplotlib import colors
import time
import math
import sys
# np.set_printoptions(threshold=sys.maxsize)

# rootName =  "KaonLT_coin_replay_production_8005_-1"
rootName =  "KaonLT_coin_replay_production_8010_-1"
# rootName = "chain_8005-8010"

tree1 = "T"

T1_arrkey =  "leafName"
T1_arrhist = "histData"


def progressBar(value, endvalue, bar_length):

        percent = float(value) / endvalue
        arrow = '=' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write(" \r[{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()

# Retrieves the array data file and creates new leaves from this
def pullArray():

    data = np.load("%s.npz" % rootName)

    T1 = data[T1_arrkey]
    T1_hist = data[T1_arrhist]

    return[T1,T1_hist]

# Creates a dictionary that stores leaf names with the corresponding array
def dictionary():

    [T1,T1_hist] = pullArray()
    
    # print("Gathering data and removing non-physics...")
    # for i in range(0,len(T1_hist)):
    #     progressBar(i,len(T1_hist),50)
    #     for j  in range(0,len(T1_hist[i])):
    #         if (T1_hist[i][j] < 1e36):
    #             T1_leafdict = dict(zip(T1, T1_hist))
    T1_leafdict = dict(zip(T1, T1_hist))
    
    return[T1_leafdict]

# A quick way to look up a leaf name for its array
def lookup(key):

    [T1_leafdict] = dictionary()
    
    T_leafFound = T1_leafdict.get(key,"Leaf name not found")

    if (T_leafFound == "Leaf name not found"):
        print("ERROR: %s not found" % key)
        sys.exit()

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

    arrCut = cut
    arrPlot = plot
    
    arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]

    return[arrPlot]

def cutRecursive(lastCut,newcut,plot,low,high):
    
    [T1_leafdict] = dictionary()

    arrLast = lastCut
    arrCut = newcut
    arrPlot = plot
    
    arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]

    arrNew = np.intersect1d(arrLast,arrPlot)

    return[arrNew]
    
def densityPlot(x,y,title,xlabel,ylabel,binx,biny,xmin=None,xmax=None,ymin=None,ymax=None):

    fig, ax = plt.subplots(tight_layout=True)
    if (xmin or xmax or ymin or ymax):
        hist = ax.hist2d(x, y,bins=(setbin(x,binx,xmin,xmax)[0],setbin(y,biny,ymin,ymax)[0]), norm=colors.LogNorm())
    else:
        hist = ax.hist2d(x, y,bins=(setbin(x,binx)[0],setbin(y,biny)[0]), norm=colors.LogNorm())
    plt.title(title, fontsize =16)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

# Wider the binsize the fewer bins
def setbin(plot,binsize,xmin=None,xmax=None):
    
    if (xmin or xmax):
        leaf = cut(plot,plot,xmin,xmax)[0]
    else:
        leaf = plot
        
    binwidth = (abs(leaf).max()-abs(leaf).min())/binsize
    
    bins = np.arange(min(leaf), max(leaf) + binwidth, binwidth)

    return[bins]

# Define phyisics data
CTime_eKCoinTime_ROC1  = lookup("CTime.eKCoinTime_ROC1")[0]
CTime_ePiCoinTime_ROC1 = lookup("CTime.ePiCoinTime_ROC1")[0]
CTime_epCoinTime_ROC1  = lookup("CTime.epCoinTime_ROC1")[0]
P_gtr_beta             = lookup("P.gtr.beta")[0]
P_gtr_th               = lookup("P.gtr.th")[0]
P_gtr_ph               = lookup("P.gtr.ph")[0]
H_gtr_beta             = lookup("H.gtr.beta")[0]
H_gtr_th               = lookup("H.gtr.th")[0]
H_gtr_ph               = lookup("H.gtr.ph")[0]
H_cal_etotnorm         = lookup("H.cal.etotnorm")[0] 
H_cer_npeSum           = lookup("H.cer.npeSum")[0]
P_cal_etotnorm         = lookup("P.cal.etotnorm")[0]
P_aero_npeSum          = lookup("P.aero.npeSum")[0]
P_hgcer_npeSum         = lookup("P.hgcer.npeSum")[0]
H_gtr_dp               = lookup("H.gtr.dp")[0]
P_gtr_dp               = lookup("P.gtr.dp")[0]
P_gtr_p                = lookup("P.gtr.p")[0]
Q2                     = lookup("H.kin.primary.Q2")[0]
W                      = lookup("H.kin.primary.W")[0]
epsilon                = lookup("H.kin.primary.epsilon")[0]
ph_q                   = lookup("P.kin.secondary.ph_xq")[0]
emiss                  = lookup("P.kin.secondary.emiss")[0]
pmiss                  = lookup("P.kin.secondary.pmiss")[0]
MandelT                = lookup("P.kin.secondary.MandelT")[0]
fEvtType               = lookup("fEvtHdr.fEvtType")[0]
pEDTM                  = lookup("T.coin.pEDTM_tdcTime")[0]
missMass               = np.square((emiss*emiss)-(pmiss*pmiss))

# Can call arrays to create your own plots
def customPlots():

    densityPlot(P_aero_npeSum,P_hgcer_npeSum,'HGCER vs AERO','AERO (npe)','HGCER (npe)',100,100,0.,25.,0.,10.)
    
    densityPlot(Q2,W,'Q2 vs W','W','Q2',100,100,0.,7.,0.,4.)

    densityPlot(CTime_eKCoinTime_ROC1-43,missMass, 'Missing Mass vs Coin Time','Coin Time (ns)','Missing Mass (GeV)',100,100,-10.,10.,0.,2.)
    
    f, ax = plt.subplots()
    coinhist = ax.hist(CTime_eKCoinTime_ROC1,bins=setbin(CTime_eKCoinTime_ROC1,100,-10.,10.)[0],histtype='step', stacked=True, fill=False )
    plt.title("CTime_eKCoinTime_ROC1", fontsize =16)
    plt.yscale('log')
    
    f, ax = plt.subplots()
    mmhist = ax.hist(missMass,bins=setbin(missMass,200,0,2)[0],histtype='step', stacked=True, fill=False )
    plt.title("missMass", fontsize =16)
    
def main() :

    customPlots()
    # recreateLeaves()
    plt.show()
    
if __name__=='__main__': main()
