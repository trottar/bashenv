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

import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
from scipy.integrate import simps
from matplotlib import interactive
from matplotlib import colors
from sys import path
import time,math,sys
# np.set_printoptions(threshold=sys.maxsize)

# My class function
# sys.path.insert(0,'python')
sys.path.insert(0,'.')
from test_rootPy import pyPlot,pyCut

# rootName =  "KaonLT_coin_replay_production_8005_-1"
rootName =  "KaonLT_coin_replay_production_8010_-1"
# rootName = "chain_8005-8010"

tree1 = "T"

T1_arrkey =  "leafName"
T1_arrhist = "histData"

pdf = matplotlib.backends.backend_pdf.PdfPages("%s.pdf" % rootName)

b = pyPlot(rootName,tree1,T1_arrkey,T1_arrhist)

# Define phyisics data
CTime_eKCoinTime_ROC1  = b.lookup("CTime.eKCoinTime_ROC1")[0] - 43
CTime_ePiCoinTime_ROC1 = b.lookup("CTime.ePiCoinTime_ROC1")[0]
CTime_epCoinTime_ROC1  = b.lookup("CTime.epCoinTime_ROC1")[0]
P_gtr_beta             = b.lookup("P.gtr.beta")[0]
P_gtr_th               = b.lookup("P.gtr.th")[0]
P_gtr_ph               = b.lookup("P.gtr.ph")[0]
H_gtr_beta             = b.lookup("H.gtr.beta")[0]
H_gtr_th               = b.lookup("H.gtr.th")[0]
H_gtr_ph               = b.lookup("H.gtr.ph")[0]
H_cal_etotnorm         = b.lookup("H.cal.etotnorm")[0] 
H_cer_npeSum           = b.lookup("H.cer.npeSum")[0]
P_cal_etotnorm         = b.lookup("P.cal.etotnorm")[0]
P_aero_npeSum          = b.lookup("P.aero.npeSum")[0]
P_hgcer_npeSum         = b.lookup("P.hgcer.npeSum")[0]
H_gtr_dp               = b.lookup("H.gtr.dp")[0]
P_gtr_dp               = b.lookup("P.gtr.dp")[0]
P_gtr_p                = b.lookup("P.gtr.p")[0]
Q2                     = b.lookup("H.kin.primary.Q2")[0]
W                      = b.lookup("H.kin.primary.W")[0]
epsilon                = b.lookup("H.kin.primary.epsilon")[0]
ph_q                   = b.lookup("P.kin.secondary.ph_xq")[0]
emiss                  = b.lookup("P.kin.secondary.emiss")[0]
pmiss                  = b.lookup("P.kin.secondary.pmiss")[0]
MandelT                = b.lookup("P.kin.secondary.MandelT")[0]
fEvtType               = b.lookup("fEvtHdr.fEvtType")[0]
pEDTM                  = b.lookup("T.coin.pEDTM_tdcTime")[0]
        
missMass               = np.sqrt((emiss*emiss) - (pmiss*pmiss))

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

c = pyCut(cutDict)

def selectCut():
    
    cuts1 = ["H_cal_etotnorm", "H_cer_npeSum", "P_cal_etotnorm", "H_gtr_dp", "P_gtr_dp", "P_gtr_th", "P_gtr_ph", "H_gtr_th", "H_gtr_ph", "P_aero_npeSum", "P_hgcer_npeSum"]
    
    cuts2 = ["H_cal_etotnorm", "H_cer_npeSum", "P_cal_etotnorm", "H_gtr_dp", "P_gtr_dp", "P_gtr_th", "P_gtr_ph", "H_gtr_th", "H_gtr_ph", "P_aero_npeSum", "P_hgcer_npeSum","P_gtr_beta"]

    cuts3 = ["H_cal_etotnorm", "H_cer_npeSum", "P_cal_etotnorm", "H_gtr_dp", "P_gtr_dp", "P_gtr_th", "P_gtr_ph", "H_gtr_th", "H_gtr_ph", "P_aero_npeSum", "P_hgcer_npeSum","P_gtr_beta","CTime_eKCoinTime_ROC1"]

    cuts4 = ["H_cal_etotnorm", "H_cer_npeSum", "P_cal_etotnorm", "H_gtr_dp", "P_gtr_dp", "P_gtr_th", "P_gtr_ph", "H_gtr_th", "H_gtr_ph", "P_aero_npeSum", "P_hgcer_npeSum","P_gtr_beta","CTime_eKCoinTime_ROC1-KaonCut"]

    return[cuts1,cuts2,cuts3,cuts4]

def densityPlot(x,y,title,xlabel,ylabel,binx,biny,xmin=None,xmax=None,ymin=None,ymax=None,cuts=None,figure=None,sub=None):

    if cuts:
        xcut  = c.applyCuts(x,cuts)[0]
        ycut = c.applyCuts(y,cuts)[0]
    else:
        xcut = x
        ycut = y
    if sub or figure:
        ax = figure.add_subplot(sub)
    else:
        fig, ax = plt.subplots(tight_layout=True,figsize=(11.69,8.27))
    if (xmin or xmax or ymin or ymax):
        hist = ax.hist2d(xcut, ycut,bins=(b.setbin(x,binx,xmin,xmax)[0],b.setbin(y,biny,ymin,ymax)[0]), norm=colors.LogNorm())
    else:
        hist = ax.hist2d(xcut, ycut,bins=(b.setbin(x,binx)[0],b.setbin(y,biny)[0]), norm=colors.LogNorm())
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def polarPlot(theta,r,title,thetalabel,rlabel,bintheta,binr,thetamin=None,thetamax=None,rmin=None,rmax=None,cuts=None,figure=None,sub=None):

    if cuts:
        thetacut  = c.applyCuts(theta,cuts)[0]
        rcut = c.applyCuts(r,cuts)[0]
    else:
        thetacut = theta
        rcut = r
    xy = np.vstack([thetacut, rcut])
    z = stats.gaussian_kde(xy)(xy)
    idx = z.argsort()
    x, y, z = np.array(thetacut)[idx], np.array(rcut)[idx], z[idx]
    if sub or figure:
        ax = figure.add_subplot(sub,polar=True)
    else:
        ax = plt.subplot(111,polar=True)
    if (thetamin or thetamax or rmin or rmax):
        hist = ax.scatter(thetacut, rcut, c=z, edgecolor='', alpha = 0.75)
    else:
        hist = ax.scatter(thetacut, rcut, c=z, edgecolor='', alpha = 0.75)
    ax.grid(True)
    plt.title(title)
    plt.xlabel(thetalabel)
    plt.ylabel(rlabel)
    # plt.colorbar()

def kaonPlots():

    [cuts1,cuts2,cuts3,cuts4] = selectCut()
    
    f = plt.figure(figsize=(11.69,8.27))
    # f.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.7, wspace=0.3, hspace=0.3)
    ax = f.add_subplot(221)
    hemiss = ax.hist(emiss,bins=b.setbin(emiss,200,0.,2.0)[0],histtype='step', alpha=0.5, stacked=True, fill=True )
    plt.title("emiss", fontsize =16)
    ax = f.add_subplot(222)
    hpmiss = ax.hist(pmiss,bins=b.setbin(pmiss,200,0.,2.0)[0],histtype='step',  alpha=0.5, stacked=True, fill=True )
    plt.title("pmiss", fontsize =16)
    ax = f.add_subplot(223)    
    h1mmissK = ax.hist(missMass,bins=b.setbin(missMass,200,.8,1.8)[0],histtype='step',  alpha=0.5, stacked=True, fill=True )
    plt.title("missMassK", fontsize =16)
    ax = f.add_subplot(224)    
    hp = ax.hist(P_gtr_p,bins=b.setbin(P_gtr_p,200,0.,10.)[0],histtype='step',  alpha=0.5, stacked=True, fill=True )
    plt.title("P_gtr_p", fontsize =16)
    
    ################### cut 1

    h2ROC1_Coin_Beta_noID_kaon = densityPlot(CTime_eKCoinTime_ROC1, P_gtr_beta, 'Beta vs Coin Time','Coin Time (ns)', '$beta$', 100, 200, -40., 40., 0., 2., cuts1)

    ################### cut 2

    h1missKcut_CT = densityPlot(CTime_eKCoinTime_ROC1, missMass, 'Missing Mass vs Coin Time','Coin Time (ns)','Missing Mass (GeV)', 200, 100, -10., 10., 0., 2.0, cuts2)
    
    ################### cut 3

    f = plt.figure(figsize=(11.69,8.27))
    f.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.35, hspace=0.35)
    h2ROC1_Coin_Beta_kaon = densityPlot(CTime_eKCoinTime_ROC1, P_gtr_beta, 'Beta vs Coin Time','Coin Time (ns)', '$beta$',200,200,-10.,10.,0.,2., cuts3, figure=f, sub=221)
    h2SHMSK_kaon_cut = densityPlot(P_aero_npeSum, P_hgcer_npeSum, 'HGCER vs AERO','AERO (npe)','HGCER (npe)',200,200,0.,25.,0.,10., cuts3, figure=f, sub=222)
    h2SHMSK_pion_cut = densityPlot(P_cal_etotnorm, P_hgcer_npeSum, 'HGCER vs CAL','CAL (npe)','HGCER (npe)',200,200,0.,2.,0.,30., cuts3, figure=f, sub=223)
    hemiss_aero_cut = densityPlot(CTime_eKCoinTime_ROC1, P_aero_npeSum, 'AERO vs Coin Time','Coin Time (npe)','AERO (npe)',200,200,-10,10,0.,25., cuts3, figure=f, sub=224)

    f = plt.figure(figsize=(11.69,8.27))
    f.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.35, hspace=0.35)
    ax = f.add_subplot(224)
    h1mmissK_cut = ax.hist(c.applyCuts(missMass,cuts3)[0],bins=b.setbin(missMass,200,0.,2.0)[0], histtype='step',  alpha=0.5, stacked=True, fill=True )
    plt.title("missMassK_cut", fontsize =16)    
    h2WvsQ2 = densityPlot(Q2, W, 'Q2 vs W','W','Q2',200,200,0.,7.,0.,4., cuts3, figure=f, sub=221)
    h2tvsph_q = polarPlot(ph_q, -MandelT, '','','',200,200,-3.14,3.14,0.,1., cuts3, figure=f, sub=223)
    ax = f.add_subplot(222)
    h1epsilon = ax.hist(c.applyCuts(epsilon,cuts3)[0],bins=b.setbin(epsilon,100,0.,1.)[0],histtype='step',  alpha=0.5, stacked=True, fill=True )
    plt.title("Epsilon", fontsize =16)

    
    ################### cut 4

    
    f = plt.figure(figsize=(11.69,8.27))
    f.tight_layout()
    ax = f.add_subplot(121)
    h1mmissK_rand = ax.hist(c.applyCuts(missMass,cuts4)[0],bins=b.setbin(missMass,200,0.,2.)[0],histtype='step',  alpha=0.5, stacked=True, fill=True )
    plt.title("missMassK_rand", fontsize =16)
    ax = f.add_subplot(122)
    h1mmissK_remove = ax.hist(c.applyCuts(missMass,cuts4)[0],bins=b.setbin(missMass,200,0.,2.)[0],histtype='step',  alpha=0.5, stacked=True, fill=True )
    plt.title("missMassK_remove", fontsize =16)

# Gaussian with linear background fit
def gauss_fit(x, constant, A, B, mean, sigma):

    return (constant*np.exp(-0.5*((x-mean)/sigma)*((x-mean)/sigma)) + A + B*x)

def fit_hist(hist,constant,A,B,mean,sigma):

    # Return num evenly spaced numbers over a specified interval [start, stop].
    # bins = np.linspace(start=0., stop=2., num=21)
    bins = np.linspace(A[1],B[1], num=(B[1]-A[1])*10+1)
    binscenterstmp = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
    
    hist = np.nan_to_num(hist)
    binscenterstmp = np.nan_to_num(binscenterstmp)

    binscenters = np.zeros_like(hist)
    binscenters[np.indices(binscenterstmp.shape)] = binscenterstmp

    # p0 = [constant, A, B, mean, sigma], initial guesses for parameters (bounded by bounds=((lower),(upper))).
    # np.inf is a not bounded parameter    
    p0 = [constant[1],A[1],B[1],mean[1],sigma[1]]
    bounds = ((constant[0],A[0],B[0],mean[0],sigma[0]),(constant[2],A[2],B[2],mean[2],sigma[2]))
    
    # Use non-linear least squares to fit a function to data.
    popt, pcov = curve_fit(gauss_fit, xdata=binscenters, ydata=hist, p0=p0,bounds=bounds)
    # print(popt)

    xspace = np.linspace(A[1],B[1], len(hist)+1)


     # ag,bg,cg = stats.gamma.fit(hist)  
    # fit = stats.gamma.pdf(xspace, ag, bg,cg) 
    fit = gauss_fit(xspace, *popt)

    return fit

def plot_fit(hist,fit,xmin,xmax,figure,sub,color=None):

    xspace = np.linspace(xmin,xmax, len(hist)+1)
    
    ax = figure.add_subplot(sub)
    if color:
        y = ax.plot(xspace, fit, color=color, linewidth=1.5)
    else:
        y = ax.plot(xspace, fit, color='darkorange', linewidth=1.5)

def integrate_fit(hist,fit,xmin,xmax,constant):

    xspace = np.linspace(xmin, xmax, len(hist)+1)
    
    # Simpson's rule integration
    # area = simps(fit,xspace)*constant
    area = simps(fit,xspace)*200
    # area = simps(fit,hist)

    return area

def kaonSelection():
    
    [cuts1,cuts2,cuts3,cuts4] = selectCut()

    # scale = 1./12.
    scale = 1./3.

    h1mmissK = missMass

    h1mmissK_cut = c.applyCuts(missMass,cuts1)[0]
    
    h1mmissK_randScale = c.applyCuts(missMass,cuts4)[0]*scale

    # Make the two arrays the same shape by filling the rest of array with zeros
    h1mmissK_rand = np.zeros_like(h1mmissK_cut)
    h1mmissK_rand[np.indices(h1mmissK_randScale.shape)] = h1mmissK_randScale
    
    h1mmissK_remove = h1mmissK_cut - h1mmissK_rand

    # Lambda fit
    # parameter  = [lowbound,input,upbound]
    constant = [0,60,5000]
    A = [0.,1.09,1.09]
    B = [1.15,1.15,2.0]
    mean = [1.11,1.12,1.13]
    sigma = [0.001,0.004,0.01]

    fitLambda = fit_hist(h1mmissK_remove,constant,A,B,mean,sigma)

    # Sigma fit
    # parameter  = [lowbound,input,upbound]
    constant2 = [0,20,5000]
    A2 = [0.,1.165,1.165]
    B2 = [1.225,1.225,2.0]
    mean2 = [1.185,1.195,1.205]
    sigma2 = [0.001,0.002,0.01]

    fitSig = fit_hist(h1mmissK_remove,constant2,A2,B2,mean2,sigma2)

    areaLambda = integrate_fit(h1mmissK_remove,fitLambda,A[1],B[1],constant[1])
    areaSig = integrate_fit(h1mmissK_remove,fitSig,A2[1],B2[1],constant2[1])
    
    f, ax = plt.subplots(tight_layout=True,figsize=(11.69,8.27))
    plot_fit(h1mmissK_remove,fitLambda,A[1],B[1],f,ax)
    plot_fit(h1mmissK_remove,fitSig,A2[1],B2[1],f,ax,'green')
    plot = ax.hist(h1mmissK_remove,bins=b.setbin(missMass,200,0.8,1.8)[0],histtype='step',  alpha=0.5, stacked=True, fill=True )
    plt.title("missMassK_remove")
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, 'Lambdas = %0.f \n Sigmas = %0.f' % (areaLambda,areaSig), transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)
    plt.axvline(x=1.115,color='red')
    plt.axvline(x=1.189,color='pink')
    plt.xlim(0.8,1.4)
    
    for f in xrange(1, plt.figure().number):
        pdf.savefig(f)
    pdf.close()
    
def main() :

    kaonPlots()
    kaonSelection()
    # recreateLeaves()
    plt.show()
    
if __name__=='__main__': main()
