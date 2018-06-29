# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:02:56 2018

@author: ovj

%reset does magic


"""

import os
import numpy as np
import WITec_Script_LowLVL as witec   # the folder containing this file needs to be added to the python Pathmanager (under Tools in Spyder)

#%%


name = "myscript2" # name of this script
author = "Jan Overbeck" # author of script
description = "test script" 

dir = r'C:\Users\ovj\Desktop'

filepath = os.path.join(dir,name+'.rscp')


#%%

#==============================================================================
# Power Series
#==============================================================================

witec.RamScript = []
witec.sspec_tint(5)

powerList = 2.**(np.arange(8)-2)

for p in powerList:
    witec.laser_power(p)
    witec.sspec_name("MyName_%3.2fmW_continued" %p)
    witec.sspec_start()
    
    
script_powerSeries = witec.RamScript
    

#%%

#==============================================================================
# Define Point Grid in XY
#==============================================================================

start = [23.45, 70.0, 0.0] # top left corner of array
size = [20,20]

startX = start[0]
startY = start[1]
startZ = start[2]

sizeX = size[0]
sizeY = size[1]


gridX = np.arange(sizeX)+startX
gridY = np.arange(sizeY)+startY
#gridZ = [-1,0,1]

                                
pointlist = []


#for z in gridZ:
for y in gridY:
    for x in gridX:
        pointlist.append([x,y])            

#%%

#==============================================================================
# Create script for single spectra at points
#==============================================================================

witec.RamScript = []
witec.sspec_tint(2)

for p in pointlist:
        try:
            witec.piezoX(p[0])
        except:
            print("No valid 2D/3D coordinates")
            break
        try:
            witec.piezoY(p[1])
        except:
            print("No valid 2D/3D coordinates")
            break            
        try:
            witec.piezoZ(p[2])
        except:
            pass
        witec.sspec_start()
        
        
script_sspec_matrix = witec.RamScript


#for i in sspec_matrix:
#    print(i)
    
    
    
#%%

script_out = []

header = "<HEADER>\n"+"<Name>"+name+"</Name>\n"+"<Author>"+author+"</Author>\n"+"<Description>"+description+"</Description>\n"+"</HEADER>\n"

script_out.append(header)
script_out.append("<SCRIPT>\n") #script start

#==============================================================================
# Append Script Parts to be saved after this
#==============================================================================
                 
script_out.append(script_powerSeries)
script_out.append(script_sspec_matrix)
script_out.append(witec.)
#==============================================================================
# Append before this
#==============================================================================

script_out.append("</SCRIPT>\n") #script end

    
#%%
#==============================================================================
# Saving to file                 
#==============================================================================
def a2s(a): #anything to string
    outstring = ''
    if isinstance(a, list):
        for item in a:
            outstring +=  str(a2s(item))
    else:
        outstring = str(a)
    return outstring



with open(filepath, mode='w+') as f:            
    f.write(a2s(script_out))
