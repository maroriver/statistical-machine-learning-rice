# Pemetaan keluaran eksperimen ke Bab 10

| Objek pada naskah | Berkas repositori | Asal/penjelasan |
|---|---|---|
| Tabel 10.1 Deskripsi fitur | `results/Tabel_10_1_Deskripsi_Fitur.csv` | Metadata UCI; disusun sebagai kamus fitur |
| Tabel 10.2 Audit data | `results/Tabel_10_2_Audit_Dataset.csv` | Output notebook asli, nama diselaraskan |
| Tabel 10.3 Pembagian kelas | `results/Tabel_10_3_Pembagian_Data.csv` | Output notebook asli, nama diselaraskan |
| Tabel 10.4 Validasi silang | `results/Tabel_10_4_Hasil_Validasi_Silang.csv` | Output notebook asli |
| Tabel 10.5 Performa data uji | `results/Tabel_10_5_Perbandingan_Model_Test.csv` | Output notebook asli |
| Tabel 10.6 Metrik per kelas | `results/Tabel_10_6_Metrik_Per_Kelas.csv` | Diturunkan dari prediksi asli memakai sklearn |
| Gambar 10.1 Distribusi kelas training | `figures/Gambar_10_1_Distribusi_Kelas.png` | Output notebook asli |
| Gambar 10.2 Scatter training | `figures/Gambar_10_2_Scatter_Training.png` | Output notebook asli |
| Gambar 10.3 Alur eksperimen | `figures/Gambar_10_3_Alur_Eksperimen.png` | Diagram editorial penulis, bukan keluaran perhitungan notebook |
| Gambar 10.4 CV Macro-F1 | `figures/Gambar_10_4_Validasi_Silang.png` | Dari `Gambar_10_3_Validasi_Silang.png` notebook awal |
| Gambar 10.5 Confusion Matrix | `figures/Gambar_10_5_Confusion_Matrix.png` | Dari `Gambar_10_4_Confusion_Matrix.png` notebook awal |

## Hal-hal yang tidak diubah

1. Split 80:20, stratified, seed 42; sampel 3.048/762.
2. Tiga model dan seluruh konfigurasi parameter.
3. Aturan memilih model berdasarkan rata-rata Macro-F1 CV pada training.
4. Hasil test Logistic Regression: 0,9160 accuracy, 0,9138 Macro-F1, 64 salah.

## Yang berubah pada versi GitHub

Penamaan keluaran diselaraskan dengan naskah; Tabel 10.1 dan 10.6 diekspor otomatis oleh notebook; grafik CV dan confusion matrix memakai nomor sesuai buku. Hasil acuan di `results/` berasal dari eksekusi terdahulu atas dataset UCI asli; paket tidak mengklaim melakukan eksekusi ulang dataset asli ketika disusun.
