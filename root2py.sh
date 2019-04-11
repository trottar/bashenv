#! /bin/bash

#
# Description:This script will convert a root file to a data file (*.npz) filled with arrays for each leaf histogram.
# It will then create a new script for plotting these histograms in python
# Note: This is for one tree at a time so will need to repeat for each. May change this in the future.
# ================================================================
# Time-stamp: "2019-04-11 16:14:49 trottar"
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

cr=`echo $'\n(Please answer yes or no).'`
cr=${cr%.}

while true; do
    read -p "Would you like to convert root to data file (*.npz)? $cr " yn
    case $yn in
        [Yy]* )
	    python $HOME/bin/rootPy.py $ROOTNAME $TTREE1
	    break;;
        [Nn]* ) break;;
	* ) echo "Please answer yes or no.";;
    esac
done
# mv $HOME/bin/${ROOTNAME}.npz $DIR

NEWPY="$DIR/${ROOTNAME}_pyPlot.py"

NEWPYCHAIN="$DIR/${ROOTNAME}_pyChain.py"

while true; do
    read -p "Would you like to create a plot script? (Please answer yes or no) " yn
    case $yn in
        [Yy]* )
	    rm ${NEWPY}	    
	    echo "#! /usr/bin/python" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "#" >> ${NEWPY}
	    echo "# Description:This will read in the array data file that contains all the leave histogram information" >> ${NEWPY}
	    echo "# ================================================================" >> ${NEWPY}
	    echo "# Time-stamp: "2019-04-09 01:52:08 trottar"" >> ${NEWPY}
	    echo "# ================================================================" >> ${NEWPY}
	    echo "#" >> ${NEWPY}
	    echo "# Author:  Richard L. Trotta III <trotta@cua.edu>" >> ${NEWPY}
	    echo "#" >> ${NEWPY}
	    echo "# Copyright (c) trottar" >> ${NEWPY}
	    echo "#" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "from __future__ import division	    " >> ${NEWPY}
	    echo "import logging" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "# Gets rid of matplot logging DEBUG messages" >> ${NEWPY}
	    echo "plt_logger = logging.getLogger('matplotlib')" >> ${NEWPY}
	    echo "plt_logger.setLevel(logging.WARNING)" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "import matplotlib.pyplot as plt" >> ${NEWPY}
	    echo "from matplotlib import interactive" >> ${NEWPY}
	    echo "import numpy as np" >> ${NEWPY}
	    echo "import sys" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "rootName =  sys.argv[1]" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "tree1 = sys.argv[2]" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "T1_arrkey =  \"leafName\"" >> ${NEWPY}
	    echo "T1_arrhist = \"histData\"" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "# Retrieves the array data file and creates new leaves from this" >> ${NEWPY}
	    echo "def pullArray():" >> ${NEWPY}
	    echo "    " >> ${NEWPY}
	    echo "    print(\"\n\nUploading chained data file, this may take a few minutes.\")    " >> ${NEWPY}
	    echo "    data = np.load("%s.npz" % rootName)" >> ${NEWPY}
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
	    echo "    T_leafFound = T1_leafdict.get(key,"Leaf name not found")" >> ${NEWPY}
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
	    echo "        # print key, -" >> ${NEWPY}
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
	    echo "def setbin(leaf,binsize):" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "    binwidth = (abs(leaf).max()-abs(leaf).min())/binsize" >> ${NEWPY}
	    echo "    " >> ${NEWPY}
	    echo "    bins = np.arange(min(leaf), max(leaf) + binwidth, binwidth)" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "    return[bins]" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "def densityPlot(x,y,title,xlabel,ylabel,binx,biny):" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "    fig, ax = plt.subplots(tight_layout=True)" >> ${NEWPY}
	    echo "    hist = ax.hist2d(x, y,bins=(setbin(x,binx)[0],setbin(y,biny)[0]), norm=colors.LogNorm())" >> ${NEWPY}
	    echo "    plt.title(title, fontsize =16)" >> ${NEWPY}
	    echo "    plt.xlabel(xlabel)" >> ${NEWPY}
	    echo "    plt.ylabel(ylabel)" >> ${NEWPY}
	    echo "    " >> ${NEWPY}
	    echo "# Can call arrays to create your own plots" >> ${NEWPY}
	    echo "def customPlots():" >> ${NEWPY}
	    echo "    " >> ${NEWPY}
	    echo "def main() :" >> ${NEWPY}
	    echo "" >> ${NEWPY}
	    echo "    customPlots()" >> ${NEWPY}
	    echo "    # recreateLeaves()" >> ${NEWPY}
	    echo "    plt.show()" >> ${NEWPY}
	    echo "    " >> ${NEWPY}
	    echo "if __name__=='__main__': main()" >> ${NEWPY}
	    
	    break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done
while true; do
    read -p "Would you like to chain a few runs? (Please answer yes or no) " yn
    case $yn in
        [Yy]* )
	    read -p "How many runs would you like to analyze? " numRuns
	    i=0
	    while (("$i" < "$numRuns"))
	    do
		read -p "Please enter run $i " ID
		run[$i]=$ID
		i=$(( i + 1 ))		
	    done
	    rm ${NEWPYCHAIN}
	    echo "#! /usr/bin/python" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "#" >> ${NEWPYCHAIN}
	    echo "# Description:Chain a series of ROOT2PY data file (*.npz) into one data file for future use " >> ${NEWPYCHAIN}
	    echo "# ================================================================" >> ${NEWPYCHAIN}
	    echo "# Time-stamp: "2019-04-10 21:14:43 trottar"" >> ${NEWPYCHAIN}
	    echo "# ================================================================" >> ${NEWPYCHAIN}
	    echo "#" >> ${NEWPYCHAIN}
	    echo "# Author:  Richard L. Trotta III <trotta@cua.edu>" >> ${NEWPYCHAIN}
	    echo "#" >> ${NEWPYCHAIN}
	    echo "# Copyright (c) trottar" >> ${NEWPYCHAIN}
	    echo "#" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "import numpy as np" >> ${NEWPYCHAIN}
	    echo "import sys" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "numDatFiles = ${numRuns}" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "chainName = \"chain_8005-8010\"" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "T1_arrkey =  \"leafName\"" >> ${NEWPYCHAIN}
	    echo "T1_arrhist = \"histData\"" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "def progressBar(value, endvalue, bar_length):" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "        percent = float(value) / endvalue" >> ${NEWPYCHAIN}
	    echo "        arrow = '=' * int(round(percent * bar_length)-1) + '>'" >> ${NEWPYCHAIN}
	    echo "        spaces = ' ' * (bar_length - len(arrow))" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "        sys.stdout.write(\" \r[{0}] {1}%\".format(arrow + spaces, int(round(percent * 100))))" >> ${NEWPYCHAIN}
	    echo "        sys.stdout.flush()" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "# Retrieves the array data file and creates new leaves from this" >> ${NEWPYCHAIN}
	    echo "def pullArray():" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    rootDict = {" >> ${NEWPYCHAIN}
	    i=0
	    while (("$i" < "$numRuns"))
	    do
		echo "         $i...${run[$i]}"
		echo "         $i : \"${DIR}/${run[$i]}\"," >> ${NEWPYCHAIN}
		i=$(( i + 1 ))
	    done	    
	    echo "    }" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    dictT1 = {}" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    dictT1_hist = {}" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    j=0" >> ${NEWPYCHAIN}
	    echo "    print(\"Gathering data files...\")" >> ${NEWPYCHAIN}
	    echo "    for i in range(0,numDatFiles):" >> ${NEWPYCHAIN}
	    echo "        progressBar(j,numDatFiles, 50)" >> ${NEWPYCHAIN}
	    echo "        rootName = rootDict[i]" >> ${NEWPYCHAIN}
	    echo "        data = np.load(\"%s.npz\" % rootName)" >> ${NEWPYCHAIN}
	    echo "        " >> ${NEWPYCHAIN}
	    echo "        dictT1[\"T1_%i\" % i] = data[T1_arrkey]" >> ${NEWPYCHAIN}
	    echo "        dictT1_hist[\"T1__hist_%i\" % i] = data[T1_arrhist]" >> ${NEWPYCHAIN}
	    echo "        j+=1" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    return[dictT1,dictT1_hist]" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "# Creates a dictionary that stores leaf names with the corresponding array" >> ${NEWPYCHAIN}
	    echo "def mergeKeys():" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    [dictT1,dictT1_hist] = pullArray()" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    T1_leafdicttmp = np.array([])" >> ${NEWPYCHAIN}
	    echo "    " >> ${NEWPYCHAIN}
	    echo "    for i in range(0,numDatFiles):" >> ${NEWPYCHAIN}
	    echo "        T1_leafdicttmp = np.append(T1_leafdicttmp, dict(zip(dictT1.get(\"T1_%i\" % i, \"Leaf not found\"),dictT1_hist.get(\"T1__hist_%i\" % i, \"Leaf not found\"))))" >> ${NEWPYCHAIN}
	    echo "        T1_leafdictmerge = [dict(zip(dictT1.get(\"T1_%i\" % i, \"Leaf not found\"), dictT1_hist.get(\"T1__hist_%i\" % i, \"Leaf not found\"))), dict(zip(dictT1.get(\"T1_%i\" % i, \"Leaf not found\"), dictT1_hist.get(\"T1__hist_%i\" % i, \"Leaf not found\")))]" >> ${NEWPYCHAIN}
	    echo "        T1_leafdictnew = {}" >> ${NEWPYCHAIN}
	    echo "        for k in dict(zip(dictT1.get(\"T1_%i\" % i, \"Leaf not found\"), dictT1_hist.get(\"T1__hist_%i\" % i, \"Leaf not found\"))).iterkeys():" >> ${NEWPYCHAIN}
	    echo "                  T1_leafdictnew[k] = tuple(T1_leafdictnew[k] for T1_leafdictnew in T1_leafdictmerge)" >> ${NEWPYCHAIN}
	    echo "    " >> ${NEWPYCHAIN}
	    echo "    return[T1_leafdictnew,dictT1]" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "def dictionary():" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    [T1_leafdictnew,dictT1] = mergeKeys()" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    T1_leafdict = {}" >> ${NEWPYCHAIN}
	    echo "    " >> ${NEWPYCHAIN}
	    echo "    for key,arr in T1_leafdictnew.items():" >> ${NEWPYCHAIN}
	    echo "        tmp = []" >> ${NEWPYCHAIN}
	    echo "        for i in range(0,numDatFiles):" >> ${NEWPYCHAIN}
	    echo "             tmp = np.append(tmp, T1_leafdictnew[key][i])" >> ${NEWPYCHAIN}
	    echo "        T1_leafdict[key] = tmp" >> ${NEWPYCHAIN}
	    echo "    " >> ${NEWPYCHAIN}
	    echo "    return[T1_leafdict]" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "def sendArraytoFile():" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    [T1_leafdict] = dictionary()" >> ${NEWPYCHAIN}
	    echo "    " >> ${NEWPYCHAIN}
	    echo "    T1 = np.array([])" >> ${NEWPYCHAIN}
	    echo "    T1_hist = []" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    for key,arr in T1_leafdict.items():" >> ${NEWPYCHAIN}
	    echo "        T1 = np.append(T1,key)" >> ${NEWPYCHAIN}
	    echo "        T1_hist.append(arr)" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    print(\"\n\nLoading chained data to file, this may take a few minutes.\")" >> ${NEWPYCHAIN}
	    echo "    np.savez(chainName, leafName=T1, histData=T1_hist)" >> ${NEWPYCHAIN}
	    echo "        " >> ${NEWPYCHAIN}
	    echo "def main() :" >> ${NEWPYCHAIN}
	    echo "" >> ${NEWPYCHAIN}
	    echo "    sendArraytoFile()" >> ${NEWPYCHAIN}
	    echo "    " >> ${NEWPYCHAIN}
	    echo "if __name__=='__main__': main()	    " >> ${NEWPYCHAIN}
	    python ${NEWPYCHAIN}	    
	    break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

