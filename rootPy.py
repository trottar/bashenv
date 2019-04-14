#! /usr/bin/python

#
# Descriptions:A light code that will convert the leaves of a ROOT file into arrays which can be easily manipulated and plotted in python
# ================================================================
# Time-stamp: "2019-04-13 17:49:35 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

from ROOT import TCanvas, TPad, TFile, TPaveLabel, TPaveText, TTreeReader, TTreeReaderValue
from ROOT import gROOT
from rootpy.interactive import wait
import numpy as np
import time
import sys

rootName = sys.argv[1]

inputROOT = "%s.root" % rootName

tree1 = sys.argv[2]    

def progressBar(value, endvalue, bar_length):

        percent = float(value) / endvalue
        arrow = '=' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write(" \r[{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()

def is_numeric(obj):
    
    attrs = ['__add__', '__sub__', '__mul__', '__div__', '__pow__']
    
    return all(hasattr(obj, attr) for attr in attrs)

def getTree():

    f = TFile.Open(inputROOT,"read")
    if not f or f.IsZombie() :
        exit

    Tree1 = f.Get(tree1)

    print("Tree %s" % tree1)
    print("="*78)
    Tree1.Print()
    print("="*78)
    print("\n")

    return[f,Tree1]

def getLeaves():

    [f,Tree1] = getTree()
    
    T1 = np.array([])

    l1 = Tree1.GetListOfLeaves()
    for i in range(0,l1.GetEntries()) :
        T1_hist = l1.At(i)
        T1 = np.append(T1,str(T1_hist.GetName()))
        
    return[f,T1]

def pullRootFiles():

    [f,T1] = getLeaves()

    # TTree1
    T1string = "Tree1 = f.%s" % tree1
    exec(T1string)
    
    hist = np.empty(shape=(1,1), dtype=np.float128)

    start = time. time()
    
    j=0
    for n in np.nditer(T1):
    # for n in range(20,25): ##debugging
        # progressBar(j,len(T1),70)
        print("\n%s (%i/%i)" % (str(T1[j]),j,len(T1)))
        tmp = loopRoot(T1,Tree1,hist,j)
        hist = np.append(hist,[j,np.asarray(tmp[0])])
        j+=1
        
    # hist is of form [0 array(histogram data) ... N array(histogram data)] where the 0 to N  elements are the leave numbers
    # and histogram data elements are an array containing the data from the leaves
    # T1 contains strings with the names for each leaf (e.g. element 0 = 'e_Inc.')
    # The goal now is to match the 0 to N elements with the strings in T1 to match the string value with there corresponding histogram data
    # hist[0]=0.0, hist[1]=0, hist[2]=[0 0 ... 0] ,hist[3]=1
    
    end = time. time()
    
    print("\nTime to pull root file: %0.1f seconds" % (end-start))
    
    return[hist,T1]

def loopRoot(key,ttree,hist,index):
    
    tmp = []
    i=0
    for e in ttree:
        if is_numeric(getattr(e,key[index])):
            progressBar(i,ttree.GetEntries(),50)
            tmp.append(getattr(e,key[index]))
            # print("%i::Hist:%s" % (i,str(tmp[i])))
        else:
            print("Non-numeric data")
            break
        i+=1
    
    return[tmp]

def define():

    [hist,T1] = pullRootFiles()
    
    # ->Therefore...
    # odd numbers -- 0 to N elements
    # even numbers -- array elements

    T1_hist = []

    k=1
    l=0
    m=0
    for n in range(1,len(hist)):
        if (float((k-1))/2).is_integer(): # odd
            # print("\n%s:" % T1[l]) ##for debugging
            l+=1
        elif (float(k)/2).is_integer(): # even
            T1_hist.append(hist[k])
            # print("%s" % str(T1_hist[m])) ##for debugging
            m+=1
        k+=1

    # This above is correct
    # T1[(0,len(T1))] will give you the leaf names
    # T1_hist[(0,len(T1))] will give you the histogram data for each leaf

    # Next step is to copy this to some type of data file for future use.
    # I would like all the arrays to be saved into the same data file but we will see how practical that will be.

    # From there we can figure out the best way to make cuts and then finally extend  this to the hcana replay files.
    # This works pretty quickly so hopefully it is not bogged down too much by the number of events

    return[T1,T1_hist]

def sendArraytoFile():

    [T1,T1_hist] = define()
    
    np.savez(rootName, leafName=T1, histData=T1_hist)
    

def main() :

    sendArraytoFile()
    
if __name__=='__main__': main()
