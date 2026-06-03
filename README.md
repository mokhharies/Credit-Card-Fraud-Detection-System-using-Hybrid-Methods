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
│   └── analysis.ipynb     # Eksperimen pra-pemrosesan & pelatihan model
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
        └── 2_Prediction_Analysis.py   # Menu formulir simulasi prediksi real-time
        └── 3_Visualization.py         # Menu analisis komparatif performa deteksi fraud antara algoritma Random Forest dan Isolation Forest.

```
## 💻 Panduan Instalasi dan Menjalankan Aplikasi

### 1. Prasyarat Sistem

Pastikan perangkat Anda telah terinstal **Python 3.8+** dan package manager **pip**.
```
```
### 2. Kloning Repositori dan Masuk ke Direktori Kerja

```bash
cd UAS_DataMining_Haries Eko-Isnan

```


### 3. Instalasi Library Dependensi

Instal seluruh pustaka yang diperlukan untuk mendukung komputasi matriks dan antarmuka grafis:


```bash
pip install streamlit pandas numpy scikit-learn

```

### 4. Menjalankan Aplikasi Streamlit

Jalankan server lokal Streamlit melalui Command Prompt (CMD) dari root folder utama:

```bash
streamlit run app/app.py

```

Setelah berhasil dijalankan, sistem akan otomatis membuka browser lokal pada alamat default: `http://localhost:8501`.

---

## 📚 Rujukan Ilmiah

* Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5-32.
* Liu, F. T., Ting, K. M., & Zhou, Z. H. (2008). Isolation forest. Dalam *2008 Eighth IEEE International Conference on Data Mining* (hlm. 413-422). IEEE.
* Wirth, R., & Hipp, J. (2000). CRISP-DM: Towards a standard process model for data mining. Dalam *Proceedings of the 4th International Conference on the Practical Applications of Knowledge Discovery and Data Mining* (hlm. 29-39
