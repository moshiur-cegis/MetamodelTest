# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 13:14:45 2019

@author: hegnauer
"""

import pandas as pd
import numpy as np

distr_file = r'Tables\discharge_distribution.csv'
distr_df   = pd.read_csv(distr_file, sep=';', index_col=None)

disch_file = r'Tables\discharge_boundary.csv'
disch_df   = pd.read_csv(disch_file, sep=';', index_col=0)
disch_df.index = pd.to_datetime(disch_df.index, format="%d-%m-%Y")

for row in distr_df.iterrows():
    node_id   = row[1][0]
    node_calc = row[1][1]
    if node_id == node_calc:
        ts = disch_df[node_id]
    else:
        calc = distr_df[distr_df.Node == node_id]['Calc'].values
        if '*' in calc[0]:
            node_calc = calc[0].split(' ')[0]
            factor    = calc[0].split(' ')[2]
            ts = disch_df[node_calc] * float(factor)
            disch_df[str(node_id)] = ts
        elif '+' in calc[0]:
            node_calc_1 = calc[0].split(' ')[0]
            node_calc_2 = calc[0].split(' ')[2]
            ts = disch_df[node_calc_1] + disch_df[node_calc_2]
            disch_df[str(node_id)] = ts
        else:
            ts = disch_df[node_calc]
            disch_df[str(node_id)] = ts

disch_df.plot()
disch_df.groupby(disch_df.index.month).mean().plot()