import streamlit as st
import pandas as pd
import numpy as np
import os

st.title("📊 2. Dataset Overview")
st.markdown("---")

st.markdown("""
### Karakteristik dan Ringkasan Data
Dataset memuat riwayat transaksi riil kartu kredit oleh pemegang kartu dari wilayah Eropa. Di bawah ini disajikan cuplikan matriks data serta ringkasan statistik deskriptif untuk memahami sebaran nilai parameter transaksi.
""")

# Memuat data sampel secara aman menggunakan jalur absolut dinamis
@st.cache_data
def load_meta_data():
    try:
        # Dapatkan jalur folder tempat file ini berada
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Mundur dua level ke folder utama, lalu masuk ke folder dataset
        csv_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'dataset', 'creditcard.csv'))
        
        # Membaca 5000 baris pertama agar pemuatan halaman web cepat
        df_view = pd.read_csv(csv_path, nrows=5000)
        return df_view, False
    except Exception as e:
        # Fallback menggunakan data sintetis jika file asli tidak ditemukan
        np.random.seed(42)
        columns_dummy = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount', 'Class']
        dummy_df = pd.DataFrame(np.random.randn(100, 31), columns=columns_dummy)
        dummy_df['Class'] = np.random.choice([0, 1], size=100, p=[0.95, 0.05])
        return dummy_df, True

# Eksekusi pemuatan data
df_view, is_dummy = load_meta_data()

# Menampilkan pesan peringatan hanya jika sistem menggunakan data sintetis
if is_dummy:
    st.warning("Mode Demonstrasi: Memuat data sintetis karena file 'creditcard.csv' di folder dataset tidak terdeteksi.")

# --- BAGIAN TAMPILAN MATRIKS DATA DAN STATISTIK ---
st.subheader("Sampel Matriks Data Transaksi (Top 5 Baris)")
st.dataframe(df_view.head())

st.subheader("Statistik Deskriptif Parameter Transaksi")
st.dataframe(df_view.describe())

st.subheader("Statistik Distribusi Kelas Target")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sampel Data Asli", "284,807 Baris")
col2.metric("Proporsi Kasus Fraud", "492 Transaksi")
col3.metric("Rasio Ketimpangan Kelas", "0.172 %")