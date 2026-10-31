# Audit terakhir Rice v1.0 → Paket GitHub v1.1

## Status dan cakupan

**LULUS audit konsistensi keluaran**; hasil asli yang disimpan belum dieksekusi ulang pada saat pembuatan repositori karena unduhan UCI tidak tersedia di lingkungan penyusunan. Semua pengujian prediksi individual, CSV, metadata, dan berkas gambar dilakukan terhadap arsip hasil pengguna.

| Pemeriksaan | Hasil |
|---|---|
| Dataset dan checksum | 3.810 baris, 7 prediktor, 0 missing, 0 duplikasi; SHA-256 ARFF dari metadata tercatat |
| Split | 3.048 training + 762 testing; seed 42; stratified |
| Metode | LR (scaler), KNN k=5 (scaler), Tree max_depth=4 |
| Cross-validation | StratifiedKFold 5, hanya training; pilih Macro-F1 tertinggi |
| Pemilihan model | Logistic Regression, Macro-F1 CV = 0,9316705424 |
| Test Logistic Regression | Accuracy 0,9160104987; Macro-F1 0,913800905; 64 salah |
| Confusion matrix | [[288,38],[26,410]] (Cammeo, Osmancik) |
| Penomoran buku | 6 tabel & 5 gambar tercantum sesuai Bab 10 |
| Akses data | UCI 545, DOI 10.24432/C5MW4Z, lisensi CC BY 4.0; data mentah tidak dibundel |

## Perbaikan nonmetodologis

- Menyamakan nama output CSV dan PNG dengan urutan yang digunakan dalam naskah A5.
- Menambahkan Tabel 10.1 (kamus fitur) dan Tabel 10.6 (per kelas) agar tersedia secara otomatis setelah notebook selesai.
- Menambahkan pemeriksaan hash data referensi sebagai peringatan jika sumber berubah.
- Menambahkan petunjuk README, lisensi kode, referensi dataset, manifest dependensi, dan petunjuk publikasi GitHub.
- Menjaga ketiga model dan seluruh parameternya agar angka pembanding tidak berubah karena perubahan rancangan.

## Catatan terbuka

- Eksekusi asli sebelumnya menggunakan Python 3.13.16, NumPy 2.1.3, pandas 2.2.3, scikit-learn 1.6.1; metadata tidak mencatat versi SciPy dan Matplotlib.
- Tidak ada bukti eksperimen bisa memperoleh angka identik pada setiap versi pustaka atau platform; jalankan ulang notebook pada Colab sebelum memberi tautan di buku.
- Rilis GitHub, URL Colab aktual, dan QR belum dibuat karena belum ada informasi URL repositori final. **Tidak ada publikasi jarak jauh yang dilakukan.**

## Kesetiaan tabel cetak

Tabel 10.1 memuat tujuh prediktor **dan** kolom target `Class`; Tabel 10.2 memuat jumlah kelas; Tabel 10.3 memuat total observasi; Tabel 10.6 memuat baris rata-rata macro. Keempatnya telah dipastikan tercermin dalam ekspor notebook dan berkas acuan.
