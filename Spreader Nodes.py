# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:14:03 2020

@author: CSE9
"""
import operator
from collections import OrderedDict 
from itertools import combinations

edges=[]
nodes=[]
count=0
edges1=[]

path_set='C:\\Users\\Sovan Saha\\Desktop\\Desktop 14-09-2023\\Dekstop Activities 5\\monkeypox\\spreader nodes\\'

gtr=open(path_set+'edgert_dtls.txt','w')

f1=open(path_set+'edge_ratio.txt','w')
f2=open(path_set+'node_com_level1_level2.txt','w')
ff3=open(path_set+'node_weight.txt','w')

with open(path_set+'merged_Copy_0.9_Copy.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    for line in stripped:
        line1=line.split()
        count=count+1
        if count!=1:
            nodes.append(line1[0])
            nodes.append(line1[1])
            edges.append((line1[0],line1[1])) 
            edges1.append((line1[0]+','+line1[1])) 
        
up_nodes=list(set(nodes))
up_edges=list(set(edges))
up_edges1=list(set(edges1))

d = {}
for i in up_nodes:
    keys = i
    values = '#FFA500'
    d[keys] = values
    
#print(d)

keys=[]
color_map=[]
for key in d:
    keys.append(key)
    color_map.append(d[key])
    
#print(keys)
#print(color_map)


import networkx as nx
G=nx.Graph()

# add nodes and edges (color can be html color name or hex code)
for key in d:
    G.add_node(str(key),color=str(d[key]))

G.add_edges_from(up_edges)


def jcrd(a,b):
    
    neighbors_a=[]
    neighbors_b=[]
    
    for line in up_edges1:
        line=line.strip('\t')
        if a in line:
            hld=line.split(',')
            if a==hld[0]:
                neighbors_a.append(hld[1])
            if a==hld[1]:
                neighbors_a.append(hld[0])
        if b in line:
            hld=line.split(',')
            if b==hld[0]:
                neighbors_b.append(hld[1])
            if b==hld[1]:
                neighbors_b.append(hld[0])       
    
    neighbors_a=list(set(neighbors_a))
    neighbors_b=list(set(neighbors_b))
    
    nmrtr=len((set(neighbors_a).intersection(set(neighbors_b))))
    
    dnmntr=len((set(neighbors_a).union(set(neighbors_b))))
    
    sim=float(nmrtr/dnmntr)
    
    #print('sim')
    #print(sim)
    
    result=1-sim

    return result   

#print(list(G.degree(up_nodes)))

#print (up_edges)
#print (up_edges1)


for nd in up_nodes:
    level1_nghbr=[]
    level2_nghbr=[]
    level1=[]
    level2=[]
    nd=nd.strip('\n')
    for line in up_edges1:
        line=line.strip('\n')
        if nd in line:
            hld=line.split(',')
            if nd==hld[0]:
                level1_nghbr.append(hld[1])
                level1.append(hld[1])
            if nd==hld[1]:
                level1_nghbr.append(hld[0])
                level1.append(hld[0])
    level1_nghbr=list(set(level1_nghbr))
    level1=list(set(level1))
    
    degrees1 = [val for (node, val) in G.degree(level1_nghbr)]
    
    #degrees1a = [node for (node, val) in G.degree(level1_nghbr)]
    
    #print('pnt')
    #print(degrees1)
    #print(degrees1a)
    
    l=len(level1_nghbr)+1
    
    
    #print(nd+'|'+str(sum(degrees1))+'|'+str(l))
    
    res=sum(degrees1)/l
    
    
    ff3.writelines(nd+'|'+str(res)+'\n')
    
    #print(level1)
    #print(level1_nghbr)
    #count1=0
    inbtwn=[]
    #print(level1_nghbr)
    for ln in level1_nghbr:
        ln=ln.strip('\n')
        for line in up_edges1:
            line=line.strip('\n')
            if ln in line:
                hld=line.split(',')
                if ln==hld[0]:
                    if hld[1] in level1_nghbr:
                        #count1=count1+1
                        inbtwn.append(line)
                    if hld[1] not in level1_nghbr and  hld[1] != nd:
                        level2_nghbr.append(hld[0]+','+hld[1])
                if ln==hld[1]:
                    if hld[0] in level1_nghbr:
                        inbtwn.append(line)
                    if hld[0] not in level1_nghbr and hld[0]!= nd:
                        level2_nghbr.append(hld[0]+','+hld[1])
    #print(inbtwn)
    count1=len(list(set(inbtwn)))
  
    #print(level2_nghbr)
    count2=len(list(set(level2_nghbr)))
   
    #print(count2)
    com=(count2+1)/(count1+1)
    
    gtr.writelines(nd+'|out|'+str(count2)+'|in|'+str(count1)+'\n')
    #print(com)
    #print(nd+'|'+str(com))
    f1.write(nd+'|'+str(com)+'\n')
    
    for i in level1:
        i=i.strip('\n')
        for line in up_edges1:
            line=line.strip('\n')
            if i in line:
                hld=line.split(',')
                if i==hld[0]:
                    s=''
                    s+=hld[1]
                    level2.append(s)
                else:
                    s=''
                    s+=hld[0]
                    level2.append(s)
    
    #print(nd)
    #print(level2)
    level2=list(set(level2))
    b=[]
    b.append(nd)
    #print(b)
    level2=list(set(level2)-set(b))
    #print(level2)
    #print(level1)
    com=list(set(level1).union(set(level2)))
    #print(com)
    f2.write(nd+'|'+','.join(com)+'\n')
    
f1.close()
f2.close()
ff3.close()
gtr.close()

'''f3=open('node_com_level1_level2.txt','r')
hf=f3.readlines()'''

'''f4=open('edges_jcrd_dismlrty_scr.txt','w')

#change this part
print(len(up_edges1))
for lnn in up_edges1:
    print('ege::::::::'+'|'+lnn)
    lnn=lnn.strip('\t')
    hb=lnn.split(',')
    for bv in hf:
        bv=bv.strip('\t')
        if bv.startswith(hb[0]):
            fd1=bv.split('|')
            first=fd1[1].split(',')
        if bv.startswith(hb[1]):
            fd2=bv.split('|')
            second=fd2[1].split(',')
    compt=1-(len(list(set(first).intersection(set(second))))/len(list(set(first).union(set(second)))))
    f4.writelines(lnn+'|'+str(jcrd(hb[0],hb[1]))+'\n')

f4.close()

f5=open('edges_jcrd_dismlrty_scr.txt','r')
stre=f5.readlines()'''

f6=open(path_set+'nghbrhd_density.txt','w')

# need to change this part also.
for t in up_nodes:
    t=t.strip('\n')
    print(t)
    total=0.0
    level1_hld=[]
    for line in up_edges1:
        line=line.strip('\n')
        if t in line:
            hld=line.split(',')
            if t==hld[0]:
                level1_hld.append(hld[1])
            if t==hld[1]:
                level1_hld.append(hld[0])
    level1_hld=list(set(level1_hld))
    comb=list(combinations(level1_hld,2))
    comb_chng=[','.join(l) for l in comb]
    for e in comb_chng:
        e=e.strip('\n')
        u=e.split(',')
        total+=float(jcrd(u[0],u[1]))
    print('end')
    f6.writelines(t+'|'+str(total)+'\n')
    
f6.close()

f7=open(path_set+'nghbrhd_density.txt','r')
fds=f7.readlines()
f8=open(path_set+'edge_ratio.txt','r')
ghf=f8.readlines()
fff5=open(path_set+'node_weight.txt','r')
tvc=fff5.readlines()

f9=open(path_set+'ultmt_score.txt','w')
fs=open(path_set+'ultmt_score_inclng_node_weight.txt','w')

for t1 in up_nodes:
    t1=t1.strip('\n')
    #score1=0.0
    #score2=0.0
    #score3=0.0
    for bl in ghf:
        bl=bl.strip('\n')
        bk=bl.split('|')
        if t1 == bk[0]:
            score1=float(bk[1])
            break
    for po in fds:
        po=po.strip('\n')
        re=po.split('|')
        if t1 == re[0]:
            score2=float(re[1])
            break
        
    #print('yyyyy|'+t1+'|'+str(score1)+'|'+str(score2)+'|'+str(score1*score2))
    score=round(score1*score2,2)
    
    f9.writelines(t1+'|'+str(score)+'\n')
    
    for po1 in tvc:
        po1=po1.strip('\n')
        re1=po1.split('|')
        if t1 == re1[0]:
            score3=float(re1[1])
            break
        
    ult_score=(score1*score2)+score3
    
    fs.writelines(t1+'|'+str(ult_score)+'\n')
            
f9.close() 
fs.close()

de=open(path_set+'ultmt_score.txt','r')
tn=de.readlines()

ga=open(path_set+'ultmt_score_desc_order.txt','w')

d = {}
for i in tn:
    i=i.strip('\n')
    ji=i.split('|')
    keys = ji[0]
    values = float(ji[1])
    d[keys] = values
    
sorted_d = OrderedDict(dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True)))

for nm, vl in sorted_d.items(): 
    ga.writelines(nm+"|"+str(vl)+'\n') 
    
ga.close()


de1=open(path_set+'ultmt_score_inclng_node_weight.txt','r')
tn1=de1.readlines()

ga1=open(path_set+'ultmt_score_inclng_node_weight_desc_order.txt','w')

d1 = {}
for i1 in tn1:
    i1=i1.strip('\n')
    ji1=i1.split('|')
    keys = ji1[0]
    values = float(ji1[1])
    d1[keys] = values
    
sorted_d1 = OrderedDict(dict( sorted(d1.items(), key=operator.itemgetter(1),reverse=True)))

for nm1, vl1 in sorted_d1.items(): 
    ga1.writelines(nm1+"|"+str(vl1)+'\n') 
    
ga1.close()

#select top 50 percent

ga1=open(path_set+'ultmt_score_inclng_node_weight_desc_order.txt','r')
tn1=ga1.readlines()
count_lines=(50*len(tn1))//100
print(count_lines)

ga2=open(path_set+'top_20_percent.txt','w')

with open(path_set+'ultmt_score_inclng_node_weight_desc_order.txt') as myfile:
    firstNlines=myfile.readlines()[0:count_lines+1]
    
for i in firstNlines:
    ga2.writelines(i)
    
ga2.close()

    
 
    
    


    
    
    
