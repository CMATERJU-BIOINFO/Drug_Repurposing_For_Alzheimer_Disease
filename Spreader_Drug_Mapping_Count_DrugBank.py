# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 00:05:33 2020

@author: COD
"""

import operator
from collections import OrderedDict 

path_set='C:\\Users\\Sovan\\Desktop\\Desktop 27-08-2025\\AD1 SN\\Female PC Check braak stage\\Regional Prefontal cortex\\'


f7=open(path_set+'spreaders.txt','r')
fds=f7.readlines()

f8=open(path_set+'all.txt','r')
ghf=f8.readlines()

f76=open(path_set+'3.txt','w')

str1=[]

for t in fds:
    t=t.strip('\n')
    str1.append(t)
    
#str1=list(set(str1))
#print(len(str1))

drug_id=[]
#drug_name=[]

for e in str1:
    e=e.strip('\n')
    s2=''
    s2+=e
    s2=s2.strip()
    for r in ghf:
        r=r.strip('\n')
        hld=r.split('\t')
        s1=''
        s1+=hld[1]
        s1=s1.strip()
        if s2==s1:         
            if ';' in hld[4]:
                tc=hld[4].split(';')
                
                #drug_name.append(hld[2])
                for r in tc:
                    r=r.strip('\n')
                    sw=''
                    sw+=r
                    sw=sw.strip()
                    drug_id.append(s2+'|'+sw+'|'+hld[3])
            else:
                sw=''
                sw+=hld[4]
                sw=sw.strip()
                drug_id.append(s2+'|'+sw+'|'+hld[3])
            
#drug_name1=list(set(drug_name))
drug_id1=list(set(drug_id))

#print ('total no. of unique drugs:'+str(len(drug_id1)))

#print ('unique drugs:'+str(drug_id1))

'''d1={}
for t in drug_name1:
    t=t.strip('\n')
    d1[t]=drug_name.count(t)
    
sorted_d = OrderedDict(sorted(d1.items(), key=operator.itemgetter(1),reverse=True))

for nm, vl in sorted_d.items(): 
    print(nm+"|"+str(vl)+'\n') '''
    
d2={}
for t in drug_id1:
    t=t.strip('\n')
    d2[t]=drug_id.count(t)
    
sorted_d = OrderedDict(sorted(d2.items(), key=operator.itemgetter(1),reverse=True))

for nm, vl in sorted_d.items(): 
    f76.writelines(nm+'\n')
    #print(nm+"|"+str(vl)+'\n') 
    
f76.close()            

f76=open(path_set+'3.txt','r')
eq=f76.readlines()

fg=open(path_set+'drugbank idnamemapping.txt','r')
rd=fg.readlines()

dc=open(path_set+'3_new.txt','w')

for t in eq:
    t=t.strip('\n')
    f=t.split('|')
    s1=''
    s1+=f[1]
    s1=s1.strip()
    for g in rd:
        g=g.strip('\n')
        cv=g.split('\t')
        s2=''
        s2+=cv[0]
        s2=s2.strip()
        if s1==s2:
            dc.writelines(t+'|'+cv[1]+'\n')
            break
            
dc.close()

dcfg=open(path_set+'3_new.txt','r')
dg_ln=dcfg.readlines()
dg_nm=[]

for t in dg_ln:
    t=t.strip('\n')
    f=t.split('|')
    dg_nm.append(f[1])
    
dg_nm=list(set(dg_nm))
#print(len(dg_nm))

for e in dg_nm:
    count=0
    s1=[]
    for t in dg_ln:
        t=t.strip('\n')
        f=t.split('|')
        if e==f[1]:
            count+=1
            fi=''
            fi+=f[3]
            s1.append(fi)
    list_of_strings = list(set(s1))
    joined_string = " ".join(list_of_strings)
    print(e+'|'+str(count)+'|'+joined_string)
    

            



        