#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2020-01-30 22:26:41 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

import uproot as up
import sys

inputROOT = sys.argv[1]
inputTree = sys.argv[2]

# Opens root file and gets tree info
rfile = up.open(inputROOT)
Tree1 = rfile[inputTree]

allTrees = Tree1.allkeys()

print allTrees

def search(term):

    for word in term.split():
        print word
        j=0
        for i in range(0,len(allTrees)):
            if word in allTrees[i].split()[0]:
                print "_"*(len(allTrees[i])+4)
                print "|",allTrees[i], "|"
                j+=1
        if j == 0:
            print "| ERROR: Term '%s' not defined," % word
            print "  if multiple words use parentheses!"

def main() :

    while True:
        user_search = raw_input("Search for leaf name: ")
        search(user_search)
        while True:
            again = raw_input("Would you like to search again? ").lower()
            if again.startswith('n'):
                return # exit the whole function
            elif again.startswith('y'):
                break # exit just this inner loop
    
if __name__=='__main__': main()
