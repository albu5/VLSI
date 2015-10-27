# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 00:53:09 2015

@author: Ashish
"""

def dec2bin( decnum, width ):
    binlist = [int(x) for x in bin(decnum)[2:]]
    err = width-len(binlist)
    if err>0:
        for i in range(err):
            binlist.insert(0,0)
    return binlist
    
def bin2dec( binlist ):
    decnum = 0
    n = len(binlist)
    for i in range(n):
        decnum = decnum + binlist[i]*(1<<(n-i-1))
    return decnum
