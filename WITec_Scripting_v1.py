# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:02:56 2018

@author: ovj

%reset does magic


"""
#%load_ext autoreload
#%autoreload 2


import os
import numpy as np
import WITec_Script_LowLVL as witec   # the folder containing this file needs to be added to the python Pathmanager (under Tools in Spyder)

#%%


name = "PolarScanSSpecOnPointMatrix" # name of this script
author = "Jan Overbeck, Oli" # author of script
description = "s.o" 

dir = r'C:\Users\ovj\Desktop\RamanScriptTest'

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
gridX=[]
gridY=[]

start = [0., 0., 0.0] # top left corner of array
size = [7,7]

# to be extemely explicit...
startX = start[0]
startY = start[1]
startZ = start[2]
sizeX = size[0]
sizeY = size[1]


stepX=250  #um
stepY=250  #um

gridX = stepX*(np.arange(sizeX)+startX)         
gridY = stepY*(np.arange(sizeY)+startY)
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
#==============================================================================
# Script for driving motorized stage to points in pointlist and aquiring single spectrum
#==============================================================================

polarization = np.arange(0, 180.1, 20, float)
myname="SampleNameDescriptor"

witec.RamScript = []
witec.sspec_tint(2)

for p in pointlist:
    #go to position
    try:
        witec.motorStageX(p[0])
    except:
        print("No valid 2D/3D coordinates")
        break
    try:
        witec.motorStageY(p[1])
    except:
        print("No valid 2D/3D coordinates")
        break            
    #do polarization scan
    for pol in polarization:
        witec.pol785(pol)
        witec.sspec_name(myname+"_X=%f_Y=%f_Polin=%f"%(p[0],p[1],pol))
        witec.sspec_start()
    witec.pol785(-40)
    
script_sspec_matrix_motorStage = witec.RamScript      
    
#%%

script_out = []

header = "<HEADER>\n"+"<Name>"+name+"</Name>\n"+"<Author>"+author+"</Author>\n"+"<Description>"+description+"</Description>\n"+"</HEADER>\n"

script_out.append(header)
script_out.append("<SCRIPT>\n") #script start

#==============================================================================
# Append Script Parts to be saved after this
#==============================================================================
                 
#script_out.append(script_powerSeries)
script_out.append(script_sspec_matrix_motorStage)
#script_out.append(witec.)
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
