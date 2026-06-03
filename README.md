# Credit-Card-Fraud-Detection-System-using-Hybrid-Methods
Sistem deteksi dini tindakan kecurangan (*fraud*) pada transaksi kartu kredit berbasis aplikasi web interaktif menggunakan framework **Streamlit**. Proyek ini menerapkan (*hybrid methods*) yang mengombinasikan algoritma (*supervised learning*) dan (*unsupervised learning*) untuk mengatasi kendala ketimpangan kelas target secara ekstrem.
# 💳 Credit Card Fraud Detection System using Hybrid Methods

Sistem deteksi dini tindakan kecurangan (*fraud*) pada transaksi kartu kredit berbasis aplikasi web interaktif menggunakan framework **Streamlit**. Proyek ini menerapkan pendekatan hibrida (*hybrid methods*) yang mengombinasikan algoritma pembelajaran terawasi (*supervised learning*) dan tak terawasi (*unsupervised learning*) untuk mengatasi kendala ketimpangan kelas target (*imbalanced dataset*) secara ekstrem.

---

## 📌 Anggota Kelompok
* **Mokhamad Haries Eko Santoso** (25051905002)
* **Isnan Burochim** (25051905007)
* **Kelas/Angkatan:** 2025A / 2025
* **Mata Kuliah:** UAS Data Mining

---

## 🚀 Fitur Utama Aplikasi
1. **Dashboard Overview Dataset:** Menyajikan statistik deskriptif, matriks data sampel (top 5 baris), serta visualisasi distribusi kelas target berdasarkan data riil secara *real-time*.
2. **Mesin Evaluasi Hibrida:**
   * **Random Forest Classifier:** Memprediksi status transaksi berdasarkan pola logis dari rekaman data historis.
   * **Isolation Forest:** Mengisolasi pencilan (*outliers*) transaksi secara cepat untuk mendeteksi indikasi anomali varian baru tanpa bias kelas.
3. **Formulir Prediksi Interaktif:** Input parameter transaksi (Fitur Komponen V1-V28, Nominal Transaksi, dan Indeks Waktu) secara dinamis dengan penanganan otomatis penyelarasan dimensi vektor matriks masukan.

---

## 🛠️ Metodologi Pengembangan
Proyek ini mengadopsi kerangka kerja standar industri **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*):
1. **Business Understanding:** Mitigasi kerugian finansial institusi perbankan akibat risiko kejahatan siber.
2. **Data Understanding:** Analisis ketimpangan data asli (284.807 baris transaksi dengan proporsi *fraud* sebesar 0.172%).
3. **Data Preparation:** Pembersihan kolom teks, *encoding* biner, dan transformasi skala (*Feature Scaling*) menggunakan objek standardisasi.
4. **Modeling:** Pelatihan model terpisah untuk menghasilkan berkas model operasional (`rf_model.pkl`, `if_model.pkl`, dan `scaler.pkl`).
5. **Evaluation:** Pengujian berbasis orientasi ketimpangan kelas (*Precision*, *Recall*, dan *F1-Score*).
6. **Deployment:** Implementasi antarmuka berbasis web menggunakan arsitektur Streamlit.

---

## 📂 Struktur Repositori Proyek
```text
UAS_DataMining_Haries Eko-Isnan/
│
├── dataset/
│   └── creditcard.csv                 # Dataset asli perbankan Eropa (Kaggle)
│
├── notebook/
│   └── data_mining_modeling.ipynb     # Eksperimen pra-pemrosesan & pelatihan model
│
├── saved_models/
│   ├── rf_model.pkl                   # Berkas biner model Random Forest
│   ├── if_model.pkl                   # Berkas biner model Isolation Forest
│   └── scaler.pkl                     # Berkas objek normalisasi skala fitur
│
└── app/
    ├── app.py                         # Halaman utama aplikasi web Streamlit
    └── pages/
        ├── 1_Dataset_Overview.py      # Menu ringkasan statistik & matriks data
        └── 2_Fraud_Detection.py       # Menu formulir simulasi prediksi real-time

