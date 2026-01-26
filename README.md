# Computational drug repurposing study for Alzheimer’s disease using spreader nodes

# Abstract
Alzheimer’s Disease (AD), a neurodegenerative condition marked by gradual cognitive deterioration, significantly affects both the persons diagnosed and their families. At present, there is no efficacious cure for AD, and existing treatments offer only minimal clinical alleviation. This paper presents a computational methodology for drug repurposing in AD by first identifying differentially expressed genes (DEGs) from three specific human brain regions: the Entorhinal Cortex, Prefrontal Cortex, and Superior Parietal Lobe, considering multiple Braak stages (2-6) for both males and females. The DEGs are utilized to generate gene-gene interaction networks (GGINs) through the STRING database. The genes affecting disease transmission are discovered by the Spreadability Index (SI), a metric that quantifies the topological impact of genes within the network. Key spreader genes found across all DEG samples are examined for their role in biological pathways utilizing Reactome, revealing substantial relevance to the aetiology of AD. A dual drug repurposing technique is employed by targeting these disseminator genes, utilizing data from DrugBank and the Drug Gene Interaction Database (DGIdb). This methodology has produced multiple intriguing therapeutic candidates pertinent to AD, including Zinc compounds, Ketoconazole (DrugBank ID: DB01026), and Rifabutin (DrugBank ID: DB00615). Molecular docking investigations further validated the advantageous binding affinities of the relevant repurposed medicines to the critical AD-associated target phospholipase D3 (PDB ID: 8VT5), reinforcing their prospective therapeutic benefits for AD.

# Computational Model

<img width="1712" height="974" alt="image" src="https://github.com/user-attachments/assets/e78f1bab-1164-49d6-aad1-b8206d901ddd" />

# Files to run:

1. Detection of Spreader Nodes: Spreader Nodes.py --> Input/Output Folder: spreader nodes

