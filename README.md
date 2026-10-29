# 🧬 Varia Trait-Bridge

**Interpretable Genotype-to-Phenotype Screening for Salinity Stress**

A lightweight, explainable machine learning tool that predicts salinity stress in plants based on gene expression data, and identifies the key genes driving the prediction.

[![Live Demo](https://img.shields.io/badge/Live_Demo-Online-brightgreen?style=for-the-badge)](https://mahkzmi.github.io/varia-trait-bridge/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 🎯 The Problem

In plant breeding and genomics, AI models often perform well on clean, controlled lab data but struggle to generalize under real-world environmental stress (e.g., salinity). Furthermore, most machine learning models act as "black boxes"—a geneticist cannot see *why* a model made a specific prediction.

## 💡 The Solution: Explainable AI

Varia Trait-Bridge takes publicly available gene expression data from the **GSE199590** dataset (Arabidopsis thaliana subjected to 100 mM NaCl salinity stress) and delivers two things:

1. **Accurate Prediction:** Classifies each sample as "Control" or "Salinity-stressed" with high confidence.
2. **Interpretability:** Extracts and visualizes the top genes (Feature Importance) the model relied upon to make its decision.

This allows geneticists and breeders to cross-reference AI predictions with known biological pathways, accelerating the development of stress-tolerant crops.

## 🚀 Live Demo

👉 **[Try the Live Demo Here](https://mahkzmi.github.io/varia-trait-bridge/)**

*No installation required. Runs entirely in the browser.*

## 📊 Data Source

- **NCBI GEO Accession:** GSE199590
- **Organism:** *Arabidopsis thaliana*
- **Condition:** 100 mM NaCl (Salinity stress) vs. Control (0h)
- **Data Type:** RNA-seq (Raw Read Counts)

## 🛠 Tech Stack

- **Modeling (Python):** `scikit-learn` (Random Forest), `pandas`
- **Frontend (Web):** HTML5, CSS3, Vanilla JavaScript
- **Hosting:** GitHub Pages

## 📁 Repository Structure
varia-trait-bridge/
├── index.html # Interactive web dashboard (Live Demo)
├── app.py # Python Streamlit app (Data processing & ML pipeline)
├── real_gene_data.csv # Processed dataset from GSE199590
├── requirements.txt # Python dependencies for app.py
└── README.md

## 👩‍💻 About Varia Studio

Varia Studio builds digital tools and AI models for modern agriculture. We focus on soil intelligence, computer vision, and decision-support systems.

- 🌐 Website: [variastudio.framer.website](https://variastudio.framer.website)
- 📧 Email: mah.kzmi21@gmail.com

## 📄 License

This project is licensed under the MIT License.

---

<p align="center">
  <i>Built with precision by Varia Studio.</i>
</p>
