import FloodModule as FM 
import Cropmodule as CM
#import DroghtModule as DM 

fmodule = FM.floodModuleClass()
cmodule = CM.cropModuleClass()
#dmodule = DM.DroughtModuleClass()

fmodule.initializeModuleforRun()
cmodule.initializeModuleforRun()
#dmodule.initializeModuleforRun()

for time in range(0, 210):    
    fmResult = fmodule.dotimeStep(time)
    cmodule.dotimeStep(time,fmResult)

fmodule.postProssesing()
cmodule.postProssesing()