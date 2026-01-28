# Computational drug repurposing study for Alzheimer’s disease using spreader nodes

# Abstract
<p align="justify">
Alzheimer’s Disease (AD), a neurodegenerative condition marked by gradual cognitive deterioration, significantly affects both the persons diagnosed and their families. At present, there is no efficacious cure for AD, and existing treatments offer only minimal clinical alleviation. This paper presents a computational methodology for drug repurposing in AD by first identifying differentially expressed genes (DEGs) from three specific human brain regions: the Entorhinal Cortex, Prefrontal Cortex, and Superior Parietal Lobe, considering multiple Braak stages (2-6) for both males and females. The DEGs are utilized to generate gene-gene interaction networks (GGINs) through the STRING database. The genes affecting disease transmission are discovered by the Spreadability Index (SI), a metric that quantifies the topological impact of genes within the network. Key spreader genes found across all DEG samples are examined for their role in biological pathways utilizing Reactome, revealing substantial relevance to the aetiology of AD. A dual drug repurposing technique is employed by targeting these disseminator genes, utilizing data from DrugBank and the Drug Gene Interaction Database (DGIdb). This methodology has produced multiple intriguing therapeutic candidates pertinent to AD, including Zinc compounds, Ketoconazole (DrugBank ID: DB01026), and Rifabutin (DrugBank ID: DB00615). Molecular docking investigations further validated the advantageous binding affinities of the relevant repurposed medicines to the critical AD-associated target phospholipase D3 (PDB ID: 8VT5), reinforcing their prospective therapeutic benefits for AD.
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
| **#** | **👤 Gender** | **🧠 Brain Region** | **🧪 Sample Comparison** |
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
