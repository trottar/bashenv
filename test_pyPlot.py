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

# My class function
from test_rootPy import pyPlot
p = pyPlot(rootName,tree1,T1_arrkey,T1_arrhist)

def cut(key):

    # arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]
    # To call item, cutDict.get(key,"Leaf name not found")
    cutDict = {
        "H_cal_etotnorm" : (H_cal_etotnorm > 0.7),
        "H_cer_npeSum" : (H_cer_npeSum > 1.5),
        "P_cal_etotnorm" : (P_cal_etotnorm < 0.6),
        "H_gtr_dp" : (abs(H_gtr_dp) < 10.0),
        "P_gtr_dp" : (P_gtr_dp < 20.0) | (P_gtr_dp > -10.0),
        "P_gtr_th" : (abs(P_gtr_th) < 0.040),
        "P_gtr_ph" : (abs(P_gtr_ph) < 0.024),
        "H_gtr_th" : (abs(H_gtr_th) < 0.080),
        "H_gtr_ph" : (abs(H_gtr_ph) < 0.035),
        "P_aero_npeSum" : (P_aero_npeSum > 1.5),
        "P_hgcer_npeSum" : (P_hgcer_npeSum < 1.5),
        "P_gtr_beta" : (abs(P_gtr_beta-1.00) < 0.1),
        # "CTime_eKCoinTime_ROC1" : (CTime_eKCoinTime_ROC1 > -1.) & (CTime_eKCoinTime_ROC1 < 1.),
        "CTime_eKCoinTime_ROC1" : (CTime_eKCoinTime_ROC1 > -0.5) & (CTime_eKCoinTime_ROC1 < 1.5),
        "CTime_eKCoinTime_ROC1-KaonCut" : (CTime_eKCoinTime_ROC1 > -21.0) & (CTime_eKCoinTime_ROC1 < -9.0),
        "P_gtr_p" : (P_gtr_p < 100)
    }
    
    return[cutDict.get(key,"Leaf name not found")]

def applyCuts(leaf,cuts=None):

    if cuts:
        tmp = leaf
        tmp = eval(p.applyCuts(leaf,cuts)[0])
    else:
        tmp = leaf
    
    return[tmp]
    

def selectCut():
    
    cuts1 = ["H_cal_etotnorm", "H_cer_npeSum", "P_cal_etotnorm", "H_gtr_dp", "P_gtr_dp", "P_gtr_th", "P_gtr_ph", "H_gtr_th", "H_gtr_ph", "P_aero_npeSum", "P_hgcer_npeSum"]
    
    cuts2 = ["H_cal_etotnorm", "H_cer_npeSum", "P_cal_etotnorm", "H_gtr_dp", "P_gtr_dp", "P_gtr_th", "P_gtr_ph", "H_gtr_th", "H_gtr_ph", "P_aero_npeSum", "P_hgcer_npeSum","P_gtr_beta"]

    cuts3 = ["H_cal_etotnorm", "H_cer_npeSum", "P_cal_etotnorm", "H_gtr_dp", "P_gtr_dp", "P_gtr_th", "P_gtr_ph", "H_gtr_th", "H_gtr_ph", "P_aero_npeSum", "P_hgcer_npeSum","P_gtr_beta","CTime_eKCoinTime_ROC1"]

    cuts4 = ["H_cal_etotnorm", "H_cer_npeSum", "P_cal_etotnorm", "H_gtr_dp", "P_gtr_dp", "P_gtr_th", "P_gtr_ph", "H_gtr_th", "H_gtr_ph", "P_aero_npeSum", "P_hgcer_npeSum","P_gtr_beta","CTime_eKCoinTime_ROC1-KaonCut"]

    return[cuts1,cuts2,cuts3,cuts4]

def densityPlot(x,y,title,xlabel,ylabel,binx,biny,xmin=None,xmax=None,ymin=None,ymax=None,cuts=None):

    if cuts:
        xcut  = applyCuts(x,cuts)[0]
        ycut = applyCuts(y,cuts)[0]
    else:
        xcut = x
        ycut = y
        
    fig, ax = plt.subplots(tight_layout=True)
    if (xmin or xmax or ymin or ymax):
        hist = ax.hist2d(xcut, ycut,bins=(p.setbin(x,binx,xmin,xmax)[0],p.setbin(y,biny,ymin,ymax)[0]), norm=colors.LogNorm())
    else:
        hist = ax.hist2d(xcut, ycut,bins=(p.setbin(x,binx)[0],p.setbin(y,biny)[0]), norm=colors.LogNorm())
    plt.title(title, fontsize =16)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

# Define phyisics data
CTime_eKCoinTime_ROC1  = p.lookup("CTime.eKCoinTime_ROC1")[0] - 43
CTime_ePiCoinTime_ROC1 = p.lookup("CTime.ePiCoinTime_ROC1")[0]
CTime_epCoinTime_ROC1  = p.lookup("CTime.epCoinTime_ROC1")[0]
P_gtr_beta             = p.lookup("P.gtr.beta")[0]
P_gtr_th               = p.lookup("P.gtr.th")[0]
P_gtr_ph               = p.lookup("P.gtr.ph")[0]
H_gtr_beta             = p.lookup("H.gtr.beta")[0]
H_gtr_th               = p.lookup("H.gtr.th")[0]
H_gtr_ph               = p.lookup("H.gtr.ph")[0]
H_cal_etotnorm         = p.lookup("H.cal.etotnorm")[0] 
H_cer_npeSum           = p.lookup("H.cer.npeSum")[0]
P_cal_etotnorm         = p.lookup("P.cal.etotnorm")[0]
P_aero_npeSum          = p.lookup("P.aero.npeSum")[0]
P_hgcer_npeSum         = p.lookup("P.hgcer.npeSum")[0]
H_gtr_dp               = p.lookup("H.gtr.dp")[0]
P_gtr_dp               = p.lookup("P.gtr.dp")[0]
P_gtr_p                = p.lookup("P.gtr.p")[0]
Q2                     = p.lookup("H.kin.primary.Q2")[0]
W                      = p.lookup("H.kin.primary.W")[0]
epsilon                = p.lookup("H.kin.primary.epsilon")[0]
ph_q                   = p.lookup("P.kin.secondary.ph_xq")[0]
emiss                  = p.lookup("P.kin.secondary.emiss")[0]
pmiss                  = p.lookup("P.kin.secondary.pmiss")[0]
MandelT                = p.lookup("P.kin.secondary.MandelT")[0]
fEvtType               = p.lookup("fEvtHdr.fEvtType")[0]
pEDTM                  = p.lookup("T.coin.pEDTM_tdcTime")[0]
missMass               = np.square((emiss*emiss) - (pmiss*pmiss))
# missMass               = np.square(((emiss*emiss) + np.square((0.13957018*0.13957018) + (P_gtr_p*P_gtr_p)) - np.square((0.493677*0.493677) + (P_gtr_p*P_gtr_p)) - (pmiss*pmiss)))
# missMass               = np.square(((emiss*emiss) + np.square((0.13957018*0.13957018) + (P_gtr_p*P_gtr_p)) - np.square((0.493677*0.493677) + (P_gtr_p*P_gtr_p)) - (pmiss*pmiss)), dtype=np.float128)

def kaonPlots():

    [cuts1,cuts2,cuts3,cuts4] = selectCut()

    # arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]
    
    f, ax = plt.subplots()
    hemiss = ax.hist(emiss,bins=p.setbin(emiss,200,0.,2.0)[0],histtype='step', stacked=True, fill=False )
    plt.title("emiss", fontsize =16)

    f, ax = plt.subplots()
    hpmiss = ax.hist(pmiss,bins=p.setbin(pmiss,200,0.,2.0)[0],histtype='step', stacked=True, fill=False )
    plt.title("pmiss", fontsize =16)
    
    # Plots
    f, ax = plt.subplots()
    h1mmissK = ax.hist(missMass,bins=p.setbin(missMass,200,0.002,2.0)[0],histtype='step', stacked=True, fill=False )
    plt.title("missMassK", fontsize =16)
    
    ################### cut 1

    h2ROC1_Coin_Beta_noID_kaon = densityPlot(CTime_eKCoinTime_ROC1, P_gtr_beta, 'Beta vs Coin Time','Coin Time (ns)', '$beta$', 200, 200, -40., 40., 0., 2., cuts1)

    ################### cut 2

    h1missKcut_CT = densityPlot(CTime_eKCoinTime_ROC1, missMass, 'Missing Mass vs Coin Time','Coin Time (ns)','Missing Mass (GeV)', 200, 200, -10., 10., 0., 2.0, cuts2)
    
    ################### cut 3

    h2ROC1_Coin_Beta_kaon = densityPlot(CTime_eKCoinTime_ROC1, P_gtr_beta, 'Beta vs Coin Time','Coin Time (ns)', '$beta$',200,200,-40.,40.,0.,2., cuts3)
    
    h2SHMSK_kaon_cut = densityPlot(P_aero_npeSum, P_hgcer_npeSum, 'HGCER vs AERO','AERO (npe)','HGCER (npe)',200,200,0.,25.,0.,10., cuts3)

    h2SHMSK_pion_cut = densityPlot(P_cal_etotnorm, P_hgcer_npeSum, 'HGCER vs CAL','CAL (npe)','HGCER (npe)',200,200,0.,2.,0.,30., cuts3)

    f, ax = plt.subplots()
    h1mmissK_cut = ax.hist(applyCuts(missMass,cuts3)[0],bins=p.setbin(missMass,200,0.,2.0)[0],histtype='step', stacked=True, fill=False )
    plt.title("missMassK_cut", fontsize =16)
    
    h2WvsQ2 = densityPlot(Q2, W, 'Q2 vs W','W','Q2',200,200,0.,7.,0.,4., cuts3)

    h2tvsph_q = densityPlot(ph_q, -MandelT, 'Phi t plot','','',200,200,-3.14,3.14,0.,1., cuts3)

    f, ax = plt.subplots()
    h1epsilon = ax.hist(applyCuts(epsilon,cuts3)[0],bins=p.setbin(epsilon,100,0.,1.)[0],histtype='step', stacked=True, fill=False )
    plt.title("Epsilon", fontsize =16)
    
    ################### cut 4

    f, ax = plt.subplots()
    h1mmissK_rand = ax.hist(applyCuts(missMass,cuts4)[0],bins=p.setbin(missMass,200,0.,2.)[0],histtype='step', stacked=True, fill=False )
    plt.title("missMassK_rand", fontsize =16)
    
    f, ax = plt.subplots()
    h1mmissK_remove = ax.hist(applyCuts(missMass,cuts4)[0],bins=p.setbin(missMass,200,0.,2.)[0],histtype='step', stacked=True, fill=False )
    plt.title("missMassK_remove", fontsize =16)

def kaonSelection():
    
    [cuts1,cuts2,cuts3,cuts4] = selectCut()

    scale = 1./12.

    h1mmissK = missMass

    h1mmissK_cut = applyCuts(missMass,cuts1)[0]
    
    h1mmissK_randScale = applyCuts(missMass,cuts4)[0]*scale

    # Make the two arrays the same shape by filling the rest of array with zeros
    h1mmissK_rand = np.zeros_like(h1mmissK_cut)
    h1mmissK_rand[np.indices(h1mmissK_randScale.shape)] = h1mmissK_randScale
    
    h1mmissK_remove = h1mmissK_cut - h1mmissK_rand

    f, ax = plt.subplots()
    # ax.hist(h1mmissK_remove,bins=p.setbin(missMass,200,0.,2.0)[0],histtype='step', stacked=True, fill=False )
    ax.hist(h1mmissK_cut,bins=p.setbin(missMass,200,0.,2.0)[0],histtype='step', stacked=True, fill=False )
    plt.title("missMassK_remove", fontsize =16)
    plt.xlim(0,1.4)
    
def main() :

    kaonPlots()
    kaonSelection()
    # recreateLeaves()
    plt.show()
    
if __name__=='__main__': main()
