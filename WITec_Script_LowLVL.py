# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:50:10 2018

@author: ovj
"""

#%reset does magic


'''
Do this with classes!!!
'''



#==============================================================================
# Raman Low-Level Functions
#==============================================================================
global RamScript
RamScript = []
newline = "\n"
sep = "\t"

#%%
#==============================================================================
# Action Commands
#==============================================================================

def wait_done():
    RamScript.append("Wait|SequencerDone"+newline)
    
def wait_ms(delay=0):
    RamScript.append("Wait|Delay|ms"+sep+str(delay)+newline)
    
def wait_user():
    RamScript.append("Wait|UserInput"+newline)

#%%
#
#wait_done()
#wait_ms(50)
#wait_user()
#

#%%
#==============================================================================
# Boolean Commands
#==============================================================================

def query_sequencer_active():
    RamScript.append("Status|Software|Sequencers|IsASequencerActive"+newline)
    
def shutter_open():
    RamScript.append("MultiComm|MicroscopeControl|Laser|Selected|Shutter"+sep+"TRUE"+newline)
    
def shutter_close():
    RamScript.append("MultiComm|MicroscopeControl|Laser|Selected|Shutter"+sep+"FALSE"+newline)

#%%

#query_sequencer_active()
#shutter_open()
#shutter_close()

#%%
#==============================================================================
# Enum Commands
#==============================================================================

def grating_spec1(grooves = 600):
    enum = 2
    if grooves == 600:
        enum = 2   
    elif grooves == 150:
        enum = 1
    elif grooves == 1800:    
        enum = 3
    else:
        print("Invalid grating selection")
    
    RamScript.append("UserParameters|Spectrograph1|Grating"+sep+str(enum)+newline)
    wait_ms(10000)
    
def grating_spec2(grooves = 300):
    enum = 2
    if grooves == 300:
        enum = 2
    elif grooves == 150:
        enum = 1
    elif grooves == 1200:    
        enum = 3
    else:
        print("Invalid grating selection")
    
    RamScript.append("UserParameters|Spectrograph2|Grating"+sep+str(enum)+newline)
    wait_ms(10000)
#%%

#grating_spec1(1800)
#grating_spec2(150)

#%%
#==============================================================================
# Float Commands
#==============================================================================

def laser_power(power=0.1):
        RamScript.append("MultiComm|MicroscopeControl|Laser|Selected|Power"+sep+str(power)+newline)
        
def piezoX(posX=0.0):
    if -100.0 < posX < 100.0:
        RamScript.append("UserParameters|ScanTable|PositionX"+sep+str(posX)+newline)
    else:
        print("Invalid piezo X-range")
            
def piezoY(posY=0.0):
    if -100.0 < posY < 100.0:
        RamScript.append("UserParameters|ScanTable|PositionY"+sep+str(posY)+newline)
    else:
        print("Invalid piezo Y-range")
        
def piezoZ(posZ=0.0):
    if -10.0 < posZ < 10.0:
        RamScript.append("UserParameters|ScanTable|PositionZ"+sep+str(posZ)+newline)        
    else:
        print("Invalid piezo Z-range") 
        
def piezoXYZ(posX=0.0, posY=0.0, posZ=0.0):   
    piezoX(posX)
    piezoY(posY)
    piezoZ(posZ)     

def sspec_tint(tint=1.0):
    RamScript.append("UserParameters|SequencerSingleSpectrum|IntegrationTime"+sep+str(tint)+newline)
    

#%%

#piezoXYZ(300,10,4.01)
#

#%%
#==============================================================================
# Integer Commands
#==============================================================================

def img_scan_lines(lines=10):
    RamScript.append("UserParameters|SequencerScanImage|LinesPerImage"+sep+str(int(lines))+newline)
    
def img_scan_points_per_line(points=10):
    RamScript.append("UserParameters|SequencerScanImage|PointsPerLine"+sep+str(int(points))+newline)
    
def sspec_accum(naccum=1):    
    RamScript.append("UserParameters|SequencerSingleSpectrum|NrOfAccumulations"+sep+str(int(naccum))+newline)

#%%
#
#sspec_accum(4)
#img_scan_lines(5)

#%%
#==============================================================================
# String Commands
#==============================================================================

def img_scan_name(name="Image-Scan"):
    RamScript.append("UserParameters|SequencerScanImage|Naming|DataName"+sep+name+newline)

def line_scan_name(name="Line-Scan"):
    RamScript.append("UserParameters|SequencerScanLine|Naming|DataName"+sep+name+newline)

def sspec_name(name="Spec"):
    RamScript.append("UserParameters|SequencerSingleSpectrum|Naming|DataName"+sep+name+newline)
    
def timeS_name(name="TimeS"):
    RamScript.append("UserParameters|SequencerTimeSeriesSlow|Naming|DataName"+sep+name+newline)

#%%
#
#img_scan_name("test_img")
#
#line_scan_name("myline")
#
#sspec_name("SpecName")
#
#timeS_name("TimeS Jan")

#%%
#==============================================================================
# Trigger Commands
#==============================================================================

def img_scan_start():
    RamScript.append("UserParameters|SequencerScanImage|Start"+newline)
    wait_done()
    
def line_scan_start():
    RamScript.append("UserParameters|SequencerScanLine|Start"+newline)
    wait_done()

def sspec_start():
    RamScript.append("UserParameters|SequencerSingleSpectrum|Start"+newline)
    wait_done()

def timeS_start():
    RamScript.append("UserParameters|SequencerTimeSeriesSlow|Start"+newline)
    wait_done()    

def auto_focus_start():
    RamScript.append("UserParameters|SequencerAutoFocus|Start"+newline)
    wait_done()  
    
def img_scan_center_current():
    RamScript.append("UserParameters|SequencerScanImage|Geometry|CenterAtCurrentPosition"+newline)
    
    
#%%
#img_scan_start()

#%%
#==============================================================================
# Motor Commands
#==============================================================================

def wait_pol():
    RamScript.append("Wait|Movement|Done"+newline)

def pol488(abspol=0):
    RamScript.append("Move|ABS|RayShield488nm"+sep+str(abspol)+newline)
    wait_pol()
    
def pol532(abspol=0):
    RamScript.append("Move|ABS|RayLine532nm"+sep+str(abspol)+newline)
    wait_pol()
    
def pol785(abspol=0):
    RamScript.append("Move|ABS|RayLine785nm"+sep+str(abspol)+newline)
    wait_pol()
    

#%%

#pol532(90)