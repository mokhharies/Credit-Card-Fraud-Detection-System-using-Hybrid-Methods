import streamlit as st
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import pickle
import numpy as np

st.set_page_config(page_title="Model Visualization", layout="wide")

# ==========================================
# 1. PEMUATAN AMAN DATA UJI & MODEL BINER
# ==========================================
@st.cache_resource
def load_evaluation_assets():
    # Memuat objek model
    with open("model/rf_model.pkl", "rb") as f:
        rf_model = pickle.load(f)
    with open("model/if_model.pkl", "rb") as f:
        if_model = pickle.load(f)
        
    # Memuat data uji murni hasil ekspor dari Jupyter Notebook
    # Siasat ini menjamin nilai AUC konsisten 0.97 dan 0.84
    with open("model/X_test_pure.pkl", "rb") as f:
        X_test = pickle.load(f)
    with open("model/y_test_pure.pkl", "rb") as f:
        y_test = pickle.load(f)
        
    return rf_model, if_model, X_test, y_test

# Eksekusi fungsi pemuatan aset
try:
    rf_model, if_model, X_test, y_test = load_evaluation_assets()
except FileNotFoundError:
    st.error("Berkas evaluasi (X_test_pure.pkl / y_test_pure.pkl) tidak ditemukan di folder model.")
    st.info("Pastikan Anda sudah menjalankan perintah ekspor 'pickle.dump' pada data uji di Jupyter Notebook Anda.")
    st.stop()

# ==========================================
# 2. KALKULASI MATRIKS KURVA ROC-AUC
# ==========================================
rf_probs = rf_model.predict_proba(X_test)[:, 1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, rf_probs)
roc_auc_rf = auc(fpr_rf, tpr_rf)

if_scores = -if_model.decision_function(X_test)
fpr_if, tpr_if, _ = roc_curve(y_test, if_scores)
roc_auc_if = auc(fpr_if, tpr_if)

# ==========================================
# 3. TAMPILAN ANTARMUKA GRAFIS STREAMLIT
# ==========================================
st.title("📊 Visualisasi Evaluasi Performa Model")
st.write("Halaman ini menyajikan analisis komparatif performa deteksi fraud antara algoritma Random Forest dan Isolation Forest.")

col1, col2 = st.columns([2, 1])

with col1:
    # Inisialisasi kanvas grafik Matplotlib
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(fpr_rf, tpr_rf, color='blue', lw=2, label=f'Random Forest (AUC = {roc_auc_rf:.2f})')
    ax.plot(fpr_if, tpr_if, color='darkorange', lw=2, label=f'Isolation Forest (AUC = {roc_auc_if:.2f})')
    ax.plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--')
    
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('False Positive Rate (1 - Specificity)')
    ax.set_ylabel('True Positive Rate (Sensitivity)')
    ax.set_title('Receiver Operating Characteristic (ROC) Curve')
    ax.legend(loc="lower right")
    ax.grid(True, alpha=0.3)
    
    # Render ke halaman web
    st.pyplot(fig)

with col2:
    st.subheader("💡 Ringkasan Analisis")
    st.metric(label="AUC - Random Forest", value=f"{roc_auc_rf:.2f}", delta="Supervised")
    st.metric(label="AUC - Isolation Forest", value=f"{roc_auc_if:.2f}", delta="Unsupervised", delta_color="inverse")
    
    st.info(
        "Model Random Forest menunjukkan akurasi diskriminasi superior karena mempelajari pola logis "
        "dari data historis. Di sisi lain, Isolation Forest tetap tangguh mendeteksi variasi fraud baru "
        "berdasarkan karakteristik anomali transaksi tanpa bergantung pada label target."
    )