import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# ========================================================
# 1. DEKLARASI VARIABEL GLOBAL (Mencegah NameError)
# ========================================================
rf_model = None
if_model = None
scaler = None

# ========================================================
# 2. FUNGSI DINAMIS PEMUATAN MODEL (.PKL)
# ========================================================
@st.cache_resource
def load_trained_models():
    # Menentukan jalur absolut berbasis lokasi file ini berada
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    rf_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'model', 'rf_model.pkl'))
    if_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'model', 'if_model.pkl'))
    scaler_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'model', 'scaler.pkl'))
    
    with open(rf_path, 'rb') as f:
        rf = pickle.load(f)
    with open(if_path, 'rb') as f:
        iforest = pickle.load(f)
    with open(scaler_path, 'rb') as f:
        scl = pickle.load(f)
        
    return rf, iforest, scl

# ========================================================
# 3. EKSEKUSI PEMUATAN MODEL KE VARIABEL GLOBAL
# ========================================================
try:
    rf_model, if_model, scaler = load_trained_models()
    st.success("✅ Mesin Kecerdasan Buatan (Model .pkl) Berhasil Dimuat.")
except Exception as e:
    st.error(f"❌ Gagal memuat berkas model. Periksa folder 'model/'. Detail Error: {e}")
    st.stop() # Menghentikan eksekusi halaman secara total jika model gagal dimuat

# ========================================================
# 4. TAMPILAN ANTARMUKA (ANTARMUKA PENGGUNA)
# ========================================================
st.title("🔍 3. Prediction / Analysis Real-Time")
st.markdown("---")
st.subheader("Formulir Parameter Transaksi Nasabah")

with st.form("fraud_prediction_form"):
    col1, col2, col3 = st.columns(3)
    
    # Input nilai fitur utama (V1 - V5)
    v1 = col1.number_input("Komponen Fitur V1", value=-1.35)
    v2 = col2.number_input("Komponen Fitur V2", value=0.25)
    v3 = col3.number_input("Komponen Fitur V3", value=1.78)
    v4 = col1.number_input("Komponen Fitur V4", value=0.89)
    v5 = col2.number_input("Komponen Fitur V5", value=-0.45)
    
    # Input parameter fisik transaksi
    amount = col1.number_input("Nilai Nominal Transaksi (USD $)", min_value=0.0, value=99.90)
    time = col2.number_input("Indeks Waktu Transaksi (Detik)", min_value=0.0, value=45000.0)
    
    selected_method = st.selectbox(
        "Pilih Mesin Algoritma Evaluasi:",
        ["Random Forest (Classification - Pendekatan Historis)", 
         "Isolation Forest (Anomaly Detection - Pendekatan Perilaku)"]
    )
    
    submit_btn = st.form_submit_button("Proses Evaluasi Transaksi")
# ========================================================
# 5. LOGIKA PROSES PREDIKSI DATA (Dinamis Sesuai Fitur Model)
# ========================================================
if submit_btn:
    # 1. Deteksi secara otomatis berapa jumlah fitur yang diminta oleh Random Forest Anda
    try:
        num_features = rf_model.n_features_in_
    except AttributeError:
        num_features = 8 # Pasang nilai 8 sebagai fallback sesuai pesan error
        
    # 2. Bangun matriks input dengan jumlah kolom yang pas (bukan 29 lagi, tapi 8)
    input_vector = np.zeros((1, num_features))
    
    # 3. Masukkan nilai dari form ke dalam vektor input (maksimal sebanyak kolom yang tersedia)
    # Kita petakan fitur form yang ada ke ruang input matriks baru
    features_from_form = [v1, v2, v3, v4, v5]
    for i in range(min(len(features_from_form), num_features - 2)):
        input_vector[0, i] = features_from_form[i]
    
    # 4. Melakukan standardisasi input fisik ke dua kolom terakhir matriks
    scaled_amt = (amount - 88.3) / 250.1
    scaled_tm = (time - 94813.0) / 47488.0
    
    if num_features >= 2:
        input_vector[0, -2] = scaled_amt
        input_vector[0, -1] = scaled_tm
    elif num_features == 1:
        input_vector[0, -1] = scaled_amt

    prediction = 0 # Nilai inisialisasi awal hasil prediksi
    
    # 5. Eksekusi model dengan jumlah dimensi yang sudah sinkron
    if "Random Forest" in selected_method:
        prediction = rf_model.predict(input_vector)[0]
    else:
        # Menyesuaikan input vektor untuk Isolation Forest jika jumlah fiturnya berbeda
        try:
            if_num_features = if_model.n_features_in_
            if_input_vector = np.zeros((1, if_num_features))
            # Isi nilai semampunya sesuai dimensi Isolation Forest
            for i in range(min(num_features, if_num_features)):
                if_input_vector[0, i] = input_vector[0, i]
            raw_pred_if = if_model.predict(if_input_vector)[0]
        except:
            raw_pred_if = if_model.predict(input_vector)[0]
            
        prediction = 1 if raw_pred_if == -1 else 0

    # Menampilkan Output Analisis Akhir Ke Layar Web
    st.markdown("---")
    st.subheader("Hasil Analisis Sistem:")
    if prediction == 1:
        st.error("⚠️ Peringatan Sistem: Transaksi Terindikasi Kuat Sebagai Tindakan FRAUD / KECURANGAN!")
    else:
        st.success("✅ Verifikasi Berhasil: Transaksi Dinyatakan NORMAL dan Aman Dioperasikan.")