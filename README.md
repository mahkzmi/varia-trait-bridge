# 🧬 Varia Trait-Bridge

**Interpretable Genotype-to-Phenotype Screening for Salinity Stress.**

Varia Trait-Bridge is a lightweight, explainable machine learning tool that predicts salinity stress in plants based on gene expression data. It identifies the key genes driving the prediction, bridging the gap between "black-box" AI and actionable biological insights.

[![Live Demo](https://img.shields.io/badge/Live_Demo-View_App-brightgreen)](https://mahkzmi.github.io/varia-trait-bridge/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 The Problem

In modern plant breeding, AI models often excel on clean laboratory data but fail to generalize to real field conditions (such as salinity or drought stress). Furthermore, most deep learning models act as "black boxes"—a geneticist cannot see *why* a specific genotype was classified as stress-tolerant. 

Without interpretability, these models are hard to trust and difficult to integrate into commercial breeding pipelines.

## 💡 Our Solution

**Varia Trait-Bridge** demonstrates how we can make AI transparent. 

1. **Real Data:** The model is trained on the public **NCBI GEO GSE199590** dataset (RNA-seq data of *Arabidopsis thaliana* under 100 mM NaCl stress).
2. **Prediction:** It classifies samples as either "Control" or "Salinity-stressed".
3. **Interpretability (XAI):** It uses a Random Forest model to extract **Feature Importance**. The tool visualizes the top genes that contributed most to the decision, allowing geneticists to cross-reference AI results with known biological pathways.

## 🚀 Live Demo

Experience the interactive dashboard here:  
👉 **[Launch Varia Trait-Bridge](https://mahkzmi.github.io/varia-trait-bridge/)**

*(No installation required. Runs entirely in your browser.)*

## 📂 Repository Structure

- `index.html` — The frontend interface (Interactive dashboard with animations).
- `app.py` — The backend Python/Streamlit code used for data processing and model training.
- `real_gene_data.csv` — The extracted and cleaned dataset (50 key genes, 44 samples) from GSE199590.
- `requirements.txt` — Python dependencies for running `app.py` locally.

## 🛠 Tech Stack

- **Data Processing:** Python, Pandas, Scikit-learn
- **Frontend:** HTML, CSS, JavaScript
- **Data Source:** NCBI GEO GSE199590

## 👩‍💻 Running Locally

If you want to run the Streamlit version locally:

1. Clone the repository:

   git clone https://github.com/mahkzmi/varia-trait-bridge.git
   cd varia-trait-bridge
   
Install dependencies:

bash
pip install -r requirements.txt
Run the app:

bash
streamlit run app.py


Built with 💡 by Varia Studio
Digital tools for modern agriculture.
variastudio.framer.website | mah.kzmi21@gmail.com
