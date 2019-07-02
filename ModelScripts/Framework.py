import FloodModule as FM 
import Cropmodule as CM 

fmodule = FM.floodModuleClass()
cmodule = CM.cropModuleClass()

fmodule.initializeModuleforRun()
cmodule.initializeModuleforRun()

for time in range(0, 210):    
    fmResult = fmodule.dotimeStep(time)
    cmodule.dotimeStep(time,fmResult)

fmodule.postProssesing()
cmodule.postProssesing()