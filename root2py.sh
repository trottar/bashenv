#! /bin/bash

#
# Description:This script will convert a root file to a data file (*.npy) filled with arrays for each leaf histogram.
# It will then create a new script for plotting these histograms in python.
# Note:This will need to be run for each tree.
# ================================================================
# Time-stamp: "2019-04-08 08:09:07 trottar"
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

mv $HOME/bin/${ROOTNAME}.npy $DIR

NEWPY="$DIR/${ROOTNAME}_pyPlot.py"

echo "#! /usr/bin/python"
echo ""
echo "#"
echo "# Description:This will read in the array data file that contains all the leave histogram information"
echo "# ================================================================"
echo "# Time-stamp: "2019-04-08 08:07:33 trottar""
echo "# ================================================================"
echo "#"
echo "# Author:  Richard L. Trotta III <trotta@cua.edu>"
echo "#"
echo "# Copyright (c) trottar"
echo "#"
echo ""
echo "import logging"
echo ""
echo "# Gets rid of matplot logging DEBUG messages"
echo "plt_logger = logging.getLogger('matplotlib')"
echo "plt_logger.setLevel(logging.WARNING)"
echo ""
echo "from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText, TTreeReader, TTreeReaderValue"
echo "from ROOT import gROOT"
echo "from rootpy.interactive import wait"
echo "import matplotlib.pyplot as plt"
echo "from matplotlib import interactive"
echo "import numpy as np"
echo "import sys"
echo ""
echo "rootName =  sys.argv[1]"
echo ""
echo "tree1 = sys.argv[2]"
echo ""
echo "T1_arrkey =  "leafName1""
echo "T1_arrhist = "histData1""
echo ""
echo "# Retrieves the array data file and creates new leaves from this"
echo "def pullArray():"
echo "    "
echo "    data = np.load("%s.npz" % rootName)"
echo ""
echo "    T1 = data[T1_arrkey]"
echo "    T1_hist = data[T1_arrhist]"
echo ""
echo "    return[T1,T1_hist]"
echo ""
echo "# Creates a dictionary that stores leaf names with the corresponding array"
echo "def dictionary():"
echo ""
echo "    [T1,T1_hist] = pullArray()"
echo "    "
echo "    T1_leafdict = dict(zip(T1, T1_hist))"
echo ""
echo "    return[T1_leafdict]"
echo ""
echo "# A quick way to look up a leaf name for its array"
echo "def lookup(key):"
echo ""
echo "    [T1_leafdict] = dictionary()"
echo "    "
echo "    T_leafFound = T1_leafdict.get(key,"Leaf name not found")"
echo ""
echo "    return[T_leafFound]"
echo ""
echo "# Recreates the histograms of the root file"
echo "def recreateLeaves():"
echo ""
echo "    [T1_leafdict] = dictionary()"
echo ""
echo "    binwidth = 1.0"
echo "    "
echo "    i=1"
echo "    print("Looing at TTree %s" % tree1)"
echo "    print("Enter n to see next plot and q to exit program\n")"
echo "    for key,arr in T1_leafdict.items():"
echo "        # print key, "->", arr)"
echo "        if (np.all(arr == 0.)):"
echo "            print("Histogram %s: Empty array" % key)"
echo "        elif ( 2. > len(arr)) :"
echo "            print("Histogram %s: Only one element" % key)"
echo "        else:"
echo "            binwidth = (abs(arr).max())/100"
echo "            plt.figure()"
echo "            plt.hist(arr,bins=np.arange(min(arr), max(arr) + binwidth, binwidth),histtype='step', stacked=True, fill=False )"
echo "            plt.title(key, fontsize =16)"
echo "            foutname = 'fig_'+key+'.png'"
echo "            i+=1"
echo ""
echo "    print("\nTTree %s completed" % tree1)"
echo ""
echo "def cut(cut,plot,low,high):"
echo ""
echo "    [T1,T1_hist] = pullArray()"
echo "    "
echo "    [T1_leafdict] = dictionary()"
echo ""
echo "    arrCut = T1_leafdict[cut]"
echo "    arrPlot = T1_leafdict[plot]"
echo "    "
echo "    arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]"
echo ""
echo "    return[arrPlot]"
echo ""
echo "def cutRecursive(lastCut,newcut,plot,low,high):"
echo ""
echo "    [T1,T1_hist] = pullArray()"
echo "    "
echo "    [T1_leafdict] = dictionary()"
echo ""
echo "    arrLast = lastCut"
echo "    arrCut = T1_leafdict[newcut]"
echo "    arrPlot = T1_leafdict[plot]"
echo "    "
echo "    arrPlot = arrPlot[(arrCut > low) & (arrCut < high)]"
echo ""
echo "    arrNew = np.intersect1d(arrLast,arrPlot)"
echo ""
echo "    return[arrNew]    "
echo "    "
echo "def densityPlot(x,y,title):"
echo ""
echo "    fig, ax = plt.subplots(tight_layout=True)"
echo "    "
echo "    hist = ax.hist2d(x, y,bins=40, norm=colors.LogNorm())"
echo "    plt.title(title, fontsize =16)"
echo "    "
echo "        "
echo "# Can call arrays to create your own plots"
echo "def customPlots():"
echo ""
echo "    [T1_leafdict] = dictionary()"
echo "    "
echo "    "
echo "def main() :"
echo ""
echo "    customPlots()"
echo "    # recreateLeaves()"
echo "    plt.show()"
echo "    "
echo "if __name__=='__main__': main()"