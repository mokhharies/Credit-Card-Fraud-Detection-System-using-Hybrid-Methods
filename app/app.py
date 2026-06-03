import streamlit as st
import pickle
import os

# Konfigurasi Halaman Utama
st.set_page_config(
    page_title="FraudGuard Systems",
    page_icon="🛡️",
    layout="wide"
)

# Judul Utama Aplikasi di Beranda
st.title("🛡️ Sistem Deteksi Kecurangan Kartu Kredit")
st.subheader("Pendekatan Hybrid Data Mining: Klasifikasi & Deteksi Anomali")
st.markdown("---")

# Menggunakan Tabs untuk memisahkan Home dan About di halaman utama
tab1, tab2 = st.tabs(["🏠 1. Home", "ℹ️ 5. About"])

with tab1:
    st.markdown("""
    ### Deskripsi Proyek
    Proyek *data mining* ini dirancang khusus untuk memitigasi risiko kerugian finansial akibat kejahatan pemalsuan transaksi kartu kredit. 
    Dengan memanfaatkan karakteristik dataset yang sangat tidak seimbang (*highly imbalanced*), sistem ini menerapkan solusi inovatif berupa **metode hybrid**:
    * **Random Forest Classifier** untuk menyaring pola kecurangan terstruktur yang sudah terekam pada riwayat data masa lalu.
    * **Isolation Forest** untuk mendeteksi deviasi spasial baru yang berpotensi sebagai serangan kejahatan siber varian baru (*unseen anomalies*).
    
    ### Alur Kerja Framework
    Proyek ini dibangun secara sistematis menggunakan standar industri **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*), mulai dari penyelarasan tujuan bisnis hingga tahap implementasi sistem berbasis web operasional secara real-time.
    
    ### Identitas Anggota Kelompok
    * MOKHAMAD HARIES EKO SANTOSO (NIM: 25051905002) *
    * ISNAN BUROCHIM              (NIM: 25051905007) *
        """)

with tab2:
    st.markdown("""
    ### Penjelasan Metode Hybrid
    1. **Classification (Random Forest)**
       Algoritma pembelajaran terbimbing (*supervised learning*) berbasis *ensemble* pohon keputusan. Bekerja sangat efisien pada data tabular berdimensi tinggi untuk meminimalkan nilai *False Negative* agar tidak ada transaksi ilegal yang lolos.
    
    2. **Anomaly Detection (Isolation Forest)**
       Algoritma pembelajaran tidak terbimbing (*unsupervised learning*) yang mengisolasi titik data abnormal di dalam ruang metrik fitur. Sangat tangguh dalam mengenali pola anomali tanpa membutuhkan label kelas target operasional.
    
    ### Referensi Dataset
    * **Sumber:** *Credit Card Fraud Detection Dataset* (ULB - Université Libre de Bruxelles), diakses via platform Kaggle Research Data.
    * **Dimensi Transaksi:** Transformasi komponen utama (PCA) $V1$ hingga $V28$ dikombinasikan dengan metrik waktu (*Time*) dan nilai nominal (*Amount*).
    """)