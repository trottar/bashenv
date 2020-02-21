#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2020-02-13 15:02:32 trottar"
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
import uproot as up
from sys import path
import time,math,sys
# np.set_printoptions(threshold=sys.maxsize)

# My class function
sys.path.insert(0,'/home/trottar/bin/python/root2py/')
from root2py import pyPlot, pyBin

rootName = sys.argv[1]
treeName = sys.argv[2]
inputLeaf = sys.argv[3]

tree = up.open(rootName)[treeName]

hist_var = tree.array(inputLeaf)

b = pyBin()

def plotHist():
    
    plt.style.use('default')
    f,ax = plt.subplots(tight_layout=True,figsize=(11.69,8.27));
    histplot = ax.hist(hist_var,bins=b.setbin(hist_var,200,-20,20))
    plt.xlabel(inputLeaf)
    plt.ylabel('Events')
    plt.title(inputLeaf, fontsize =20)

def main() :

    plotHist()
    plt.show()
    
if __name__=='__main__': main()
