import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

class cropModuleClass():
    def initializeModuleforRun(self):
        pass

    def dotimeStep(self,currentTimeStep, fmResult):
        if fmResult[3] > 0.5:
            print(currentTimeStep, " Medium high land is goint to be crop damaged")
        if fmResult[4] > 0.5:
            print(currentTimeStep, " high land is goint to be crop damaged")
        
    def postProssesing(self):
        pass
    
    




