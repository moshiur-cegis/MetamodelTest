import FloodModule as FM 
import Cropmodule as CM
import DroughtModule as DM
import IrrigationModule as IM 

fmodule = FM.floodModuleClass()
cmodule = CM.cropModuleClass()
dmodule = DM.DroughtModuleClass()
imodule = IM.IrrigationModuleClass()

fmodule.initializeModuleforRun()
cmodule.initializeModuleforRun()
dmodule.initializeModuleforRun()
imodule.initializeModuleforRun()

for time in range(0, 1):    
    fmResult = fmodule.dotimeStep(time)
    cmodule.dotimeStep(time,fmResult)
    dmodule.dotimeStep(time)
    imodule.dotimeStep(time)

fmodule.postProssesing()
cmodule.postProssesing()
dmodule.postProssesing()
imodule.postProssesing()