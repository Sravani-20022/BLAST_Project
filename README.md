# BLAST_Project
# Comparative Sequence Analysis of Disease Resistance Protein SUMM2 Gene Using BLAST

## Project Overview

This project investigates the disease resistance protein SUMM2 gene in tomato (Solanum lycopersicum) using NCBI BLAST. Sequence alignment was performed to identify homologous genes in related horticultural crops and evaluate their evolutionary conservation.

## Objective

* Retrieve the SUMM2 gene sequence from NCBI.
* Perform sequence alignment using BLASTN.
* Compare the gene sequence with related species.
* Analyze sequence similarity and conservation.
* Visualize BLAST results using Python.

## Background

Plants possess disease resistance genes that help protect them against pathogens. The SUMM2 gene is associated with plant defense mechanisms and immune responses. Comparing this gene across different horticultural crops can provide insights into evolutionary relationships and conserved defense pathways.

## Materials and Tools

* NCBI Gene Database
* NCBI BLASTN
* Python
* Pandas
* Matplotlib
  

## Methodology

### Step 1: Sequence Retrieval

The SUMM2 disease resistance gene sequence was obtained from the NCBI database in FASTA format.

### Step 2: BLAST Analysis

The sequence was analyzed using NCBI BLASTN to identify homologous sequences in related plant species.

### Step 3: Data Collection

Important BLAST parameters were recorded:

* Query Coverage
* Percent Identity
* E-value

### Step 4: Visualization

Python was used to read the BLAST output and generate a bar chart showing sequence similarity among species.

## Results

            Scientific name            Per identity     Query Cover
           Solanum lycopersicum          1.0000         1.00
           Solanum pennellii             0.9916         1.00
           Solanum pimpinellifolium      0.9944         0.72
           Solanum tuberosum             0.8289         0.81
           Solanum stenotomum            0.8290         0.81
           Capsicum annuum               0.8128         0.93
           Solanum verrucosum            0.8192         0.99


## Python Analysis

The BLAST results were imported into Python using Pandas and visualized using Matplotlib. A bar chart was generated to compare sequence identity among species.

## Discussion

The BLAST analysis revealed significant sequence conservation of the SUMM2 disease resistance gene among members of the Solanaceae family. Tomato showed complete sequence identity as the reference sequence, while potato, chilli and others exhibited substantial similarity, indicating a common evolutionary origin and potentially similar disease resistance mechanisms.

## Conclusion

The SUMM2 disease resistance gene is highly conserved among horticultural crops belonging to the Solanaceae family. BLAST sequence alignment and comparative analysis demonstrate the usefulness of bioinformatics tools in studying gene conservation and plant defense mechanisms.

## Repository Structure

SUMM2-BLAST-Horticulture-Project/

├── README.md

├── data/

├── report/

├── images/

└── scripts/

## Future Scope

* Include additional horticultural crops.
* Perform protein sequence analysis using BLASTP.
* Conduct multiple sequence alignment using Clustal Omega.
* Construct detailed phylogenetic trees.
* Study functional domains of disease resistance proteins.

