# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 14:27:48 2025

@author: Sovan
"""

import pandas as pd

path='C:\\Users\\Sovan\\Desktop\\Desktop 27-08-2025\\AD1 SN\\Female PC Check braak stage\\Regional Prefontal cortex\\'

df1=pd.read_csv(path+'Gene_to_Drug_Map_DGIDb.csv')

print(df1.head())

f1=open(path+'spreaders.txt','r')

hld1=f1.readlines()

for i in hld1:
    i=i.strip()
    df2=df1[df1['gene_name']==i]
    df2=df2[df2['approved']==True]
    print(df2)
    df2=df2.sort_values("interaction_score", ascending=False)
    df2.to_csv(path+'spreaders_drug_map4.csv',mode='a')

