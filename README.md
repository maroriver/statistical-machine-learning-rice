# Statistical Machine Learning — Bab 10: Klasifikasi Varietas Beras

**Kode dan materi praktik pendamping buku _Statistical Machine Learning_, Bab 10: “Studi Kasus dan Implementasi Statistical Machine Learning”.**

Repositori ini menyediakan eksperimen klasifikasi dua varietas beras, **Cammeo** dan **Osmancik**, menggunakan Python dan Google Colab. Materi disusun untuk pembaca pemula: mulai dari memahami data, membuat model, hingga membaca hasil evaluasinya.

**Penulis:** Ir. Jarot Budiasto, S.T., M.T. — Universitas Musamus, Merauke, Indonesia.

[![Buka di Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maroriver/statistical-machine-learning-rice/blob/main/notebooks/Bab10_Rice_Statistical_ML.ipynb)

**Tautan utama:** [Notebook Google Colab](https://colab.research.google.com/github/maroriver/statistical-machine-learning-rice/blob/main/notebooks/Bab10_Rice_Statistical_ML.ipynb) · [Notebook di GitHub](notebooks/Bab10_Rice_Statistical_ML.ipynb) · [Dataset resmi UCI](https://archive.ics.uci.edu/dataset/545/rice)

> **Catatan:** Contoh ini mengklasifikasikan *fitur morfologi numerik* yang sudah diekstraksi dari citra beras. Notebook **tidak** menerima gambar mentah sebagai masukan dan **bukan** sistem klasifikasi siap pakai untuk industri.

## 1. Tujuan pembelajaran

Setelah mengikuti notebook, pembaca diharapkan mampu:

1. mengenali variabel, kelas target, dan statistik deskriptif suatu dataset;
2. memeriksa kualitas data serta membagi data pelatihan dan pengujian;
3. melatih tiga algoritma klasifikasi sederhana menggunakan `scikit-learn`;
4. memahami standardisasi fitur dan alasan penggunaan `Pipeline`;
5. membaca hasil validasi silang, *accuracy*, *precision*, *recall*, *Macro-F1*, serta *confusion matrix*; dan
6. menafsirkan keterbatasan hasil prediksi secara proporsional.

## 2. Cara menjalankan di Google Colab

1. Klik tombol **Buka di Google Colab** di atas.
2. Pastikan notebook yang terbuka bernama `Bab10_Rice_Statistical_ML.ipynb`.
3. Pilih **Runtime → Change runtime type → CPU** jika diperlukan.
4. Jalankan **Runtime → Run all** (atau **Jalankan semua**).
5. Baca keluaran setiap tahap. Notebook akan mencoba mengambil dataset secara otomatis dari UCI dan membuat folder hasil serta arsip ZIP untuk disimpan.

Tidak diperlukan instalasi Python di komputer pribadi. Apabila pengunduhan dataset mengalami kendala, unduh berkas `Rice_Cammeo_Osmancik.arff` atau ZIP dari [halaman UCI](https://archive.ics.uci.edu/dataset/545/rice), unggah ke lingkungan kerja Colab, lalu jalankan ulang sel pemuatan data sesuai petunjuk notebook.

### Alternatif menjalankan secara lokal

Jika Python sudah terpasang, unduh atau *clone* repositori ini, kemudian jalankan:

```bash
git clone https://github.com/maroriver/statistical-machine-learning-rice.git
cd statistical-machine-learning-rice
python -m pip install -r requirements.txt
jupyter notebook notebooks/Bab10_Rice_Statistical_ML.ipynb
```

Perintah `jupyter notebook` memerlukan Jupyter yang terpasang secara terpisah jika belum tersedia. Untuk pembaca pemula, **Google Colab tetap menjadi pilihan yang dianjurkan**.

## 3. Dataset dan rancangan eksperimen

Dataset [Rice (Cammeo and Osmancik)](https://archive.ics.uci.edu/dataset/545/rice) dari UCI Machine Learning Repository berisi **3.810 observasi**, **7 fitur numerik**, dan **2 kelas**. Fitur-fitur tersebut adalah `Area`, `Perimeter`, `Major_Axis_Length`, `Minor_Axis_Length`, `Eccentricity`, `Convex_Area`, dan `Extent`.

| Komponen | Konfigurasi |
|---|---|
| Pemeriksaan data | Tidak ditemukan nilai hilang, duplikasi identik, atau konflik label pada hasil audit |
| Pembagian data | 80% pelatihan (3.048) dan 20% pengujian (762), terstratifikasi |
| Reproduksibilitas | `random_state=42` |
| Logistic Regression | `StandardScaler` + `LogisticRegression(max_iter=1500)` |
| K-Nearest Neighbors (KNN) | `StandardScaler` + `KNeighborsClassifier(n_neighbors=5)` |
| Decision Tree | `DecisionTreeClassifier(max_depth=4)` |
| Validasi | `StratifiedKFold` 5 lipatan pada data pelatihan |
| Pemilihan model | Rata-rata *Macro-F1* validasi silang tertinggi |
| Evaluasi akhir | *Accuracy*, *precision*, *recall*, *Macro-F1*, dan *confusion matrix* pada data pengujian |

Standardisasi dilakukan **di dalam `Pipeline`**, sehingga parameter standardisasi dipelajari dari data pelatihan, bukan dari data pengujian.

## 4. Hasil eksperimen acuan

Berikut adalah hasil **eksekusi terdahulu pada dataset UCI asli** yang telah diaudit dan digunakan di dalam Bab 10. Angka ini **bukan** hasil yang dihitung ulang ketika README disusun.

| Algoritma | CV Macro-F1 | Akurasi pengujian | Macro-F1 pengujian | Kesalahan |
|---|---:|---:|---:|---:|
| **Logistic Regression** | **0,9317** | **91,60%** | **0,9138** | **64** |
| K-Nearest Neighbors | 0,9250 | 90,94% | 0,9072 | 69 |
| Decision Tree | 0,9221 | 91,21% | 0,9099 | 67 |

**Logistic Regression dipilih berdasarkan hasil validasi silang pada data pelatihan**, bukan karena melihat hasil pengujian. Dari 762 observasi pengujian, model ini memprediksi **698 dengan benar dan 64 dengan salah**.

*Confusion matrix* model terpilih (baris = kelas aktual; kolom = kelas prediksi):

| Aktual \ Prediksi | Cammeo | Osmancik |
|---|---:|---:|
| Cammeo | 288 | 38 |
| Osmancik | 26 | 410 |

Perbedaan performa ketiga algoritma relatif kecil dan tidak membuktikan keunggulan universal satu algoritma. Nilai hasil dapat berubah jika data, pembagian sampel, atau lingkungan perangkat lunak berubah.

## 5. Struktur berkas repositori

```text
statistical-machine-learning-rice/
├── README.md
├── notebooks/
│   └── Bab10_Rice_Statistical_ML.ipynb
├── results/
│   ├── Tabel_10_1_Deskripsi_Fitur.csv
│   ├── Tabel_10_2_Audit_Dataset.csv
│   ├── Tabel_10_3_Pembagian_Data.csv
│   ├── Tabel_10_4_Hasil_Validasi_Silang.csv
│   ├── Tabel_10_5_Perbandingan_Model_Test.csv
│   ├── Tabel_10_6_Metrik_Per_Kelas.csv
│   ├── Prediksi_Pengujian.csv
│   └── Metadata_Eksperimen.json
├── figures/
│   └── Gambar_10_1 sampai Gambar_10_5 (.png)
├── data/README.md
├── docs/
│   ├── BOOK_ALIGNMENT.md
│   ├── FINAL_AUDIT.md
│   └── PUBLISHING_CHECKLIST.md
├── scripts/validate_repo.py
├── requirements.txt
├── requirements-reference.txt
├── CITATION.cff
└── LICENSE
```

Berkas di [`results/`](results/) merupakan keluaran acuan yang telah diaudit. Lima gambar dalam [`figures/`](figures/) mengikuti penomoran naskah buku. **Gambar 10.3 adalah diagram alur editorial**, sedangkan gambar lainnya berkaitan dengan visualisasi eksperimen. Detail pemetaan tersedia pada [`docs/BOOK_ALIGNMENT.md`](docs/BOOK_ALIGNMENT.md).

## 6. Pemeriksaan hasil dan reproduksibilitas

Dari direktori utama repositori, jalankan:

```bash
python scripts/validate_repo.py
```

Skrip ini **memeriksa konsistensi berkas hasil referensi**, termasuk metrik, prediksi individual, dan kelengkapan gambar/tabel. Skrip tersebut **tidak** melatih ulang model atau mengunduh ulang dataset. Untuk menjalankan ulang eksperimen, gunakan notebook Google Colab.

Lingkungan yang tercatat pada eksekusi referensi: Python **3.13.16**, NumPy **2.1.3**, pandas **2.2.3**, dan scikit-learn **1.6.1**. Versi SciPy dan Matplotlib tidak tercatat lengkap pada metadata lama. Lihat [`requirements-reference.txt`](requirements-reference.txt) untuk pendekatan dependensi referensi; file tersebut bukan *environment lock* yang menjamin hasil identik di semua sistem.

## 7. Sumber data, lisensi, dan sitasi

**Dataset:** *Rice (Cammeo and Osmancik)* (2019), UCI Machine Learning Repository. DOI: [10.24432/C5MW4Z](https://doi.org/10.24432/C5MW4Z). Dataset dilisensikan dengan **Creative Commons Attribution 4.0 International (CC BY 4.0)** dan tetap memerlukan atribusi kepada sumber aslinya.

**Kode repositori:** menggunakan [MIT License](LICENSE). Lisensi kode tidak menggantikan ketentuan lisensi dataset UCI. Data ARFF mentah dan citra asli tidak disertakan di repositori ini.

Apabila menggunakan kode atau hasilnya dalam tugas, publikasi, atau bahan ajar, cantumkan sumber dataset UCI dan atribusi repositori ini. Metadata sitasi perangkat lunak tersedia di [`CITATION.cff`](CITATION.cff).

**Repositori:** https://github.com/maroriver/statistical-machine-learning-rice

## 8. Batasan penggunaan

Eksperimen ini ditujukan untuk **pembelajaran**, bukan untuk mengesahkan varietas beras secara komersial. Hasil dari satu pembagian data pelatihan–pengujian dan satu dataset tidak menjamin kinerja yang sama pada varietas lain atau citra yang diambil menggunakan kondisi berbeda. Pembaca dianjurkan memahami kesalahan klasifikasi, tidak hanya membandingkan angka akurasi.

---

**Materi pendamping Bab 10 — _Statistical Machine Learning_**  
Ir. Jarot Budiasto, S.T., M.T. · Universitas Musamus, Merauke, Indonesia
