# Can Braak Stage-Based Gene Network Dynamics reveal Sex-Stratified Therapies for Alzheimer's Disease?

# Abstract
<p align="justify">
Alzheimer’s disease (AD) is a progressive neurodegenerative disorder characterized by cognitive decline, synaptic dysfunction, and widespread neuronal loss. Despite extensive research, effective disease-modifying therapies remain limited, highlighting the need for novel therapeutic discovery strategies. This study investigates whether Braak-stage based specific network dynamics combined with a sex-stratified computational framework targeting AD-associated phospholipase D3 (PLD3),  can guide drug repurposing for AD. Differentially expressed genes (DEG) from the three specific human brain regions: Entorhinal Cortex, Prefrontal Cortex, and Superior Parietal Lobe are initially analyzed across Braak stages 2–6 in male and female AD patients. Gene-Gene interaction networks (GGIN) are constructed, and influential disease-propagating spreader genes are prioritized using the Spreadability Index (SI), a network-based measure that quantifies the ability of genes to drive pathological information flow during disease progression. Functional enrichment reveals that these key spreader genes participate in biological processes closely associated with AD progression. A dual drug-repurposing strategy integrating DrugBank and DGIdb identifies several FDA-approved therapeutic candidates, including Rifabutin (DB00615), Hexachlorophene (DB00756), and other promising compounds. To further evaluate their therapeutic relevance, molecular docking studies are performed against PLD3 (PDB ID: 8V5T), a lysosomal protein genetically linked to AD susceptibility and implicated in amyloid-β clearance, endolysosomal trafficking, and neuronal homeostasis. Docking analyses demonstrate favorable binding affinities of several repurposed candidates toward the PLD3 catalytic region, supporting their potential to modulate disease-relevant pathways and restore lysosomal function. Overall, this study presents a Braak-stage aware, sex-stratified network drug framework that integrates disease-propagation analysis, pathway characterization, drug repurposing, and PLD3-targeted molecular docking to identify promising therapeutic candidates for AD. Consequently, this work has the potential to accelerate the development of disease-modifying therapies for AD and it increases the likelihood of regulatory approval following successful clinical trials. All these findings also raise an important question: could understanding how disease-associated molecular networks evolve across disease stages and between sexes open new avenues for identifying effective, repurposable therapies for AD?
</p>

# Computational Model

<img width="1712" height="974" alt="image" src="https://github.com/user-attachments/assets/23be795e-1742-49aa-9f8d-cec3e6f082af"/>

# Input data:
<p align="justify">
The <b>Differentially Integrated Genes (DEG)</b> details for the below samples downloaded from <b>ssREAD database</b> (https://bmblx.bmi.osumc.edu/ssread/) and given as input to the <b>STRING database</b> (https://string-db.org/) is present in the "Data" folder.

## 🔬 Differentially Expressed Genes (DEG) Samples

<div align="left">

| :--: | :------: | :--------: | :----------: |
| :--- | :------: | :--------: | :----------: |
| **#** | **👤 Gender** | **🧠 Brain Region** | **🧪 Sample Comparison (Diseased vs Control)** |
| 1 | 👩 **Female** | 🧠 **EC** | AD00204 vs AD00202 |
| 2 | 👩 **Female** | 🧠 **PC** | AD00103 vs AD00106 |
| 3 | 👩 **Female** | 🧠 **SPL** | AD01206 vs AD01202 |
| 4 | 👨 **Male** | 🧠 **EC** | AD00206 vs AD00201 |
| 5 | 👨 **Male** | 🧠 **EC** | AD00205 vs AD00201 |
| 6 | 👨 **Male** | 🧠 **PC** | AD00803 vs AD00801 |
| 7 | 👨 **Male** | 🧠 **PC** | AD00102 vs AD00101 |
| 8 | 👨 **Male** | 🧠 **PC** | AD00104 vs AD00101 |
| 9 | 👨 **Male** | 🧠 **PC** | AD00108 vs AD00101 |
|10 | 👨 **Male** | 🧠 **SPL** | AD01203 vs AD01201 |
</div>
<div align="left">

**Summary:** 3 Female • 7 Male samples across EC, PC, and SPL brain regions.

</div>





</p>


# Files to run:
<p align="justify">
1. <b>Detection of Spreader Nodes:</b> Run Spreader_Node_Detection.py --> Input/Output Folder: Spreader Node Detection & Gene-Drug Mapping (DrugBank & DGIDB). The spreader node names generated for each of the 10 DEGs are given in the /Data/DEG_details.xlsx
</p> 
<p align="justify">
2. <b>Mapping of Spreaders to Drugs in DrugBank:</b> Run Spreader_Drug_Mapping_Count_DrugBank.py --> Input/Output Folder: Spreader Node Detection & Gene-Drug Mapping (DrugBank & DGIDB).
</p> 
<p align="justify">
3. <b>Mapping of Spreaders to Drugs in DGIdb:</b> Run Spreader_Drug_Mapping_DgiDB.py --> Input/Output Folder: Spreader Node Detection & Gene-Drug Mapping (DrugBank & DGIDB).
</p> 

# Docking

<p align="justify">
<b>Software used : </b>
</p>
<p align="justify">
  1. AutoDock Tool version 1.5.7 
</p>
<p align="justify">
  2. BIOVIA Discovery Studio 2020
</p>
<p align="justify">
  The pdb files for the protein and ligands structures are present in the "Docking_files.zip" folder. The files generated post docking are also present in the respective ligand folders.
</p>
