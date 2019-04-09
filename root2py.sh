#! /bin/bash

#
# Description:This script will convert a root file to a data file (*.npz) filled with arrays for each leaf histogram.
# It will then create a new script for plotting these histograms in python
# Note: This is for one tree at a time so will need to repeat for each. May change this in the future.
# ================================================================
# Time-stamp: "2019-04-08 16:07:44 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

ROOTFILE=$1
TTREE1=$2
DIR=$PWD

ROOTNAME=$(echo $ROOTFILE | sed 's/.....$//')

python $HOME/bin/rootPy.py $ROOTNAME $TTREE1

mv $HOME/bin/${ROOTNAME}.npz $DIR

NEWPY="$DIR/${ROOTNAME}_pyPlot.py"

echo "#! /usr/bin/python" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "#" >> ${NEWPY}
echo "# Description:This will read in the array data file that contains all the leave histogram information" >> ${NEWPY}
echo "# ================================================================" >> ${NEWPY}
echo "# Time-stamp: "2019-04-08 08:07:33 trottar"" >> ${NEWPY}
echo "# ================================================================" >> ${NEWPY}
echo "#" >> ${NEWPY}
echo "# Author:  Richard L. Trotta III <trotta@cua.edu>" >> ${NEWPY}
echo "#" >> ${NEWPY}
echo "# Copyright (c) trottar" >> ${NEWPY}
echo "#" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "import logging" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "# Gets rid of matplot logging DEBUG messages" >> ${NEWPY}
echo "plt_logger = logging.getLogger('matplotlib')" >> ${NEWPY}
echo "plt_logger.setLevel(logging.WARNING)" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText, TTreeReader, TTreeReaderValue" >> ${NEWPY}
echo "from ROOT import gROOT" >> ${NEWPY}
echo "from rootpy.interactive import wait" >> ${NEWPY}
echo "import matplotlib.pyplot as plt" >> ${NEWPY}
echo "from matplotlib import interactive" >> ${NEWPY}
echo "import numpy as np" >> ${NEWPY}
echo "import sys" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "rootName =  \"${ROOTNAME}\"" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "tree1 = \"${TTREE1}\"" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "T1_arrkey =  \"leafName1\"" >> ${NEWPY}
echo "T1_arrhist = \"histData1\"" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "# Retrieves the array data file and creates new leaves from this" >> ${NEWPY}
echo "def pullArray():" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "    data = np.load(\"%s.npz\" % rootName)" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    T1 = data[T1_arrkey]" >> ${NEWPY}
echo "    T1_hist = data[T1_arrhist]" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    return[T1,T1_hist]" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "# Creates a dictionary that stores leaf names with the corresponding array" >> ${NEWPY}
echo "def dictionary():" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    [T1,T1_hist] = pullArray()" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "    T1_leafdict = dict(zip(T1, T1_hist))" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    return[T1_leafdict]" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "# A quick way to look up a leaf name for its array" >> ${NEWPY}
echo "def lookup(key):" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    [T1_leafdict] = dictionary()" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "    T_leafFound = T1_leafdict.get(key,\"Leaf name not found\")" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    return[T_leafFound]" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "# Recreates the histograms of the root file" >> ${NEWPY}
echo "def recreateLeaves():" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    [T1_leafdict] = dictionary()" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    binwidth = 1.0" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "    i=1" >> ${NEWPY}
echo "    print(\"Looing at TTree %s\" % tree1)" >> ${NEWPY}
echo "    print(\"Enter n to see next plot and q to exit program\n\")" >> ${NEWPY}
echo "    for key,arr in T1_leafdict.items():" >> ${NEWPY}
echo "        # print key, "->", arr)" >> ${NEWPY}
echo "        if (np.all(arr == 0.)):" >> ${NEWPY}
echo "            print(\"Histogram %s: Empty array\" % key)" >> ${NEWPY}
echo "        elif ( 2. > len(arr)) :" >> ${NEWPY}
echo "            print(\"Histogram %s: Only one element\" % key)" >> ${NEWPY}
echo "        else:" >> ${NEWPY}
echo "            binwidth = (abs(arr).max())/100" >> ${NEWPY}
echo "            plt.figure()" >> ${NEWPY}
echo "            plt.hist(arr,bins=np.arange(min(arr), max(arr) + binwidth, binwidth),histtype='step', stacked=True, fill=False )" >> ${NEWPY}
echo "            plt.title(key, fontsize =16)" >> ${NEWPY}
echo "            foutname = 'fig_'+key+'.png'" >> ${NEWPY}
echo "            i+=1" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    print(\"\nTTree %s completed\" % tree1)" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "def cut(cut,plot,low,high):" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    [T1,T1_hist] = pullArray()" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "    [T1_leafdict] = dictionary()" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    arrCut = T1_leafdict[cut]" >> ${NEWPY}
echo "    arrPlot = T1_leafdict[plot]" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "    arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    return[arrPlot]" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "def cutRecursive(lastCut,newcut,plot,low,high):" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    [T1,T1_hist] = pullArray()" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "    [T1_leafdict] = dictionary()" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    arrLast = lastCut" >> ${NEWPY}
echo "    arrCut = T1_leafdict[newcut]" >> ${NEWPY}
echo "    arrPlot = T1_leafdict[plot]" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "    arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    arrNew = np.intersect1d(arrLast,arrPlot)" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    return[arrNew]    " >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "def densityPlot(x,y,title):" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    fig, ax = plt.subplots(tight_layout=True)" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "    hist = ax.hist2d(x, y,bins=40, norm=colors.LogNorm())" >> ${NEWPY}
echo "    plt.title(title, fontsize =16)" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "        " >> ${NEWPY}
echo "# Can call arrays to create your own plots" >> ${NEWPY}
echo "def customPlots():" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    [T1_leafdict] = dictionary()" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "def main() :" >> ${NEWPY}
echo "" >> ${NEWPY}
echo "    customPlots()" >> ${NEWPY}
echo "    # recreateLeaves()" >> ${NEWPY}
echo "    plt.show()" >> ${NEWPY}
echo "    " >> ${NEWPY}
echo "if __name__=='__main__': main()" >> ${NEWPY}
