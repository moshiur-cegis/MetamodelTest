import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

class floodModuleClass():
    def initializeModuleforRun(self):
        self.area = pd.read_csv(r'data\S-Curve.csv')
        #for x in area.iterrows():
        #temp = x.split(',')
        #print(x[1][0], ",",x[1][1] )
        #print(area.head(5))
        self.wl = pd.read_csv(r'data\Grid_1.csv',sep=',', index_col=0, parse_dates=True)
        self.up = pd.read_csv(r'data\upazila.csv')
        self.upazila = []
        self.upazila_emb = []
        for x in self.up.iterrows():
            for y in range(2, 8):
                if x[1][8]==0:
                    self.upazila.append(x[1][y])
                else:
                    self.upazila_emb.append(x[1][8])
                    break;
                
            #print(x[1][0], ",",x[1][2] )
        self.upazila
        self.upazila_emb

    def dotimeStep(self,currentTimStep):
         #wl.iloc[currentTimStep]
        waterDepth = []
        Wl_temp= self.wl.iloc[currentTimStep]["WL"]
        vll= (Wl_temp>self.upazila[0]) & (Wl_temp < self.upazila[1])
        vllWD= Wl_temp-self.upazila[0]
        if vllWD <=0:
            vllWD=0
        waterDepth.append(vllWD)
        #print("%.2f" %(vllWD))
        ll= (Wl_temp>self.upazila[1]) & (Wl_temp < self.upazila[2])
        llWD= Wl_temp-self.upazila[1]
        if llWD <=0:
            llWD=0
        waterDepth.append(llWD)   
        mll= (Wl_temp>self.upazila[2]) & (Wl_temp < self.upazila[3])
        mllWD= Wl_temp-self.upazila[2]
        if mllWD <=0:
            mllWD=0
        waterDepth.append(mllWD)
        mhl= (Wl_temp>self.upazila[2]) & (Wl_temp < self.upazila[3])
        mhlWD= Wl_temp-self.upazila[2]
        if mhlWD <=0:
            mhlWD=0
        waterDepth.append(mhlWD)
        hl= (Wl_temp>self.upazila[2]) & (Wl_temp < self.upazila[3])
        hlWD= Wl_temp-self.upazila[2]
        if hlWD <=0:
            hlWD=0
        waterDepth.append(hlWD)
        
        Parea = []
        for elv in self.upazila:
            for area_temp in self.area.iterrows():
                if area_temp[1][1]>= elv:
                    Parea.append(area_temp[1][0])
                    break
        floodDuration=[10,7,5,4,3]
        
  
        return waterDepth, Parea, floodDuration
        
    
        
        
#        ll = wl[(wl>=upazila[1]) & (wl < upazila[2])].count()
#        mll = wl[(wl>=upazila[2]) & (wl < upazila[3])].count()
#        mhl = wl[(wl>=upazila[3]) & (wl < upazila[4])].count()
#        hl = wl[(wl>=upazila[4]) & (wl < upazila[5])].count()
#        ff = wl[wl>upazila[5]].count()
#        days =[]
#        days.append(vll[0])
#        days.append(ll[0])
#        days.append(mll[0])
#        days.append(mhl[0])
#        days.append(hl[0])
#        days.append(ff[0])
        return
    
    
    def postProssesing(self):
      pass
#        fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True, figsize= (10,10))
#        self.wl.plot(ax=axes[0], drawstyle = "steps", label ="whole Time series")
#        self.wl.plot(ax=axes[1], drawstyle = "steps", label ="whole Time series")
#        for y in self.upazila:
#            self.wl[self.wl>y].plot(ax=axes[0], drawstyle = "steps")
#        for t in self.upazila_emb:
#            self.wl[self.wl>t].plot(ax=axes[1], drawstyle = "steps")
#        L=axes[0].legend()
#        L.get_texts()[0].set_text('VLL')
#        L.get_texts()[1].set_text('LL')
#        L.get_texts()[2].set_text('MLL')
#        L.get_texts()[3].set_text('HL')
#        L.get_texts()[4].set_text('VHL')
#        L.get_texts()[5].set_text('FFL')
#        L1=axes[1].legend()
#        L1.get_texts()[0].set_text('WL')
#        L1.get_texts()[1].set_text('Avobe Intervention')
#        plt.show()

    
    




