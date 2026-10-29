import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import plotly.express as px

st.set_page_config(page_title="Varia Trait-Bridge", layout="wide")

st.title("Varia Trait-Bridge")
st.markdown("Interpretable Genotype-to-Phenotype Screening")

st.write("This tool predicts salinity stress in plants based on gene expression data and identifies the key genes responsible for the prediction.")

uploaded_file = st.file_uploader("Upload your gene expression CSV (e.g., GSE199590 format)", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        
        if 'Status' not in df.columns:
            st.error("Error: CSV must contain a 'Status' column (Salinity / Control).")
        else:
            X = df.drop('Status', axis=1)
            y = df['Status']
            
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X, y)
            
            df['Prediction'] = model.predict(X)
            df['Confidence'] = model.predict_proba(X).max(axis=1)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Predictions")
                st.dataframe(df[['Status', 'Prediction', 'Confidence']], use_container_width=True)
            
            with col2:
                st.subheader("Feature Importance")
                importances = model.feature_importances_
                feat_df = pd.DataFrame({'Gene': X.columns, 'Importance': importances})
                feat_df = feat_df.sort_values(by='Importance', ascending=False)
                
                fig = px.bar(feat_df, x='Importance', y='Gene', orientation='h', 
                             color='Importance', color_continuous_scale='Greens')
                fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=400)
                st.plotly_chart(fig, use_container_width=True)
                
            st.info("Interpretability: The chart shows which genes the model relies on most. This allows geneticists to cross-reference predictions with known biological pathways.")
            
    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info(" Please upload the sample_data.csv file to see the magic happen.")