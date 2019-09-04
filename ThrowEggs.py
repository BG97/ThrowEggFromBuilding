# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:48:03 2019

@author: benny
"""
import numpy as np


#F（M，N）= Min（Max（ F（M-X，N）+ 1， F（X-1，N-1） + 1）），1<=X<=M
def getMinStep_less_space(eggNum,floorNum):
    if eggNum<1 or floorNum<1:
        return 0
    
    #store to previous Cache for eggNum-1
    preCache = np.zeros((floorNum + 1),dtype=int)
    
    #store to current Cache for eggNum
    currentCache = np.zeros((floorNum + 1),dtype=int)
    
    for i in range(1,floorNum+1):
        currentCache[i]=i
        
        
    for n in range(2,eggNum):
        #store into previous cache and initialize the current cache
        preCache=currentCache
        for i in range(1,floorNum+1):
            currentCache[i]=i
        
        for m in range(1,floorNum+1):
            for k in range(1,m-1):
                currentCache[m]=min(currentCache[m],1+max(preCache[k-1],currentCache[m-k]))
        
    return currentCache[floorNum]
    


    

def getMinStep(eggNum,floorNum):
    if eggNum<1 or floorNum<1:
        print(0)
    
    #store to previous Cache for eggNum-1
    #preCache = np.zeros((eggNum+1,floorNum + 1),dtype=int)
    
    #store to current Cache for eggNum
    currentCache = np.zeros((eggNum+1,floorNum + 1),dtype=int)
    
    for i in range(1,eggNum+1):
        for j in range(1,floorNum+1):
            currentCache[i][j]=j
        
        
    for n in range(2,eggNum+1):
        #store into previous cache and initialize the current cache
        #preCache=currentCache
        #print(preCache)
        #for i in range(1,floorNum+1):
           # currentCache[i][j]=i
        #print(currentCache)
        for m in range(1,floorNum+1):
            #print(m)
            for k in range(1,m):
                #print(k)
                currentCache[n][m]=min(currentCache[n][m],1+max(currentCache[n-1][k-1],currentCache[n][m-k]))

    return(currentCache[eggNum][floorNum])


print(getMinStep(5,500))
    
