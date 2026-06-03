import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("📈 4. Advanced Visualization")
st.markdown("---")

@st.cache_data
def load_visualization_data():
    try:
        df_plot = pd.read_csv('../dataset/creditcard.csv', nrows=2000)
        return df_plot
    except:
        np.random.seed(42)
        dummy = pd.DataFrame(np.random.randn(200, 3), columns=['V1', 'V2', 'Amount'])
        dummy['Class'] = np.random.choice([0, 1], size=200, p=[0.9, 0.1])
        return dummy

df_plot = load_visualization_data()

st.subheader("Analisis Klaster Ruang Geometris Komponen V1 vs V2")
st.markdown("Grafik scatter plot di bawah ini menunjukkan sebaran posisi data transaksi normal dibandingkan dengan letak data fraud.")

fig, ax = plt.subplots(figsize=(8, 4))
sns.scatterplot(
    x='V1', y='V2', 
    hue='Class', 
    data=df_plot, 
    palette='coolwarm', 
    alpha=0.8, 
    ax=ax
)
ax.set_title("Sebaran Fitur Spasial Transaksi")
st.pyplot(fig)

st.subheader("Matriks Matriks Korelasi Komponen Fitur Utama")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.heatmap(df_plot.corr(), cmap='viridis', annot=False, ax=ax2)
st.pyplot(fig2)