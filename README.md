# Statistical Machine Learning — Bab 10 (UCI Rice)

Kode pendamping buku **Statistical Machine Learning**, Bab 10: *Studi Kasus dan Implementasi Statistical Machine Learning*.

Eksperimen pembelajaran mengklasifikasikan dua varietas beras, **Cammeo** dan **Osmancik**, berdasarkan tujuh fitur numerik dari citra butir beras. Ini **bukan** model pengenal gambar mentah atau aplikasi siap produksi. Target pembacanya adalah pemula.

## Mulai dari sini

1. Buka [Google Colab](https://colab.research.google.com/).
2. Pilih **File → Open notebook → GitHub**, lalu cari repositori ini setelah dipublikasikan; atau unggah [`notebooks/Bab10_Rice_Statistical_ML.ipynb`](notebooks/Bab10_Rice_Statistical_ML.ipynb).
3. Gunakan runtime **CPU** dan pilih **Runtime → Run all**.
4. Notebook mengambil dataset langsung dari UCI dan menghasilkan ZIP berisi tabel, grafik, serta metadata pada folder kerja Colab.

**Tautan satu klik Open in Colab:** setelah mengunggah repositori, gunakan pola berikut (ganti `USERNAME` dengan nama pengguna GitHub sebenarnya):

```text
https://colab.research.google.com/github/USERNAME/statistical-machine-learning-bab10-rice/blob/main/notebooks/Bab10_Rice_Statistical_ML.ipynb
```

Jangan mencetak URL sementara di atas dalam buku. Gunakan URL GitHub aktual atau permalink ke tag rilis `v1.0.0`.

## Metode dan hasil referensi

| Komponen | Konfigurasi / hasil acuan |
|---|---|
| Dataset | UCI Rice (Cammeo and Osmancik), 3.810 baris, 7 fitur |
| Audit | 0 missing; 0 duplikasi identik; 0 konflik label |
| Pembagian | Stratified 80:20 (`random_state=42`) → 3.048 train + 762 test |
| Model | Logistic Regression, KNN (`k=5`), Decision Tree (`max_depth=4`) |
| Validasi | Stratified 5-fold, training only; pilihan menurut CV Macro-F1 |
| Model terpilih | Logistic Regression; CV Macro-F1 = **0,9317** |
| Testing | Accuracy **0,9160**; Macro-F1 **0,9138**; 698 benar / 64 salah |
| Confusion matrix | Aktual Cammeo: 288 benar + 38 salah; aktual Osmancik: 410 benar + 26 salah |

Angka di atas berasal dari eksekusi **dataset asli** yang telah diaudit, bukan hasil baru yang dibuat saat paket ini disusun. Reproduksi pada mesin dan versi pustaka lain mungkin sedikit berbeda.

## Struktur repositori

```text
notebooks/                 Notebook Google Colab yang bisa dijalankan
results/                   CSV/JSON keluaran referensi yang telah diaudit
figures/                   Gambar 10.1–10.5 sesuai buku (10.3 ialah diagram alur editorial)
data/                      Petunjuk sumber data; tidak ada dataset mentah dibundel
docs/                      Peta tabel/gambar & petunjuk publikasi
scripts/                   Pemeriksaan konsistensi hasil
README.md                  Panduan pembaca
requirements.txt           Dependensi Python
requirements-reference.txt Versi pustaka inti pada eksekusi referensi
CITATION.cff               Cara mengutip repositori pendamping
LICENSE                    Lisensi MIT untuk kode asli repositori
```

**Catatan penomoran:** notebook awal menyebut gambar validasi sebagai 10.3 dan *confusion matrix* sebagai 10.4. Versi GitHub memperbaikinya menjadi **Gambar 10.4** dan **Gambar 10.5**, sesuai buku. **Gambar 10.3** merupakan diagram alur penulis dan disertakan sebagai aset editorial. Nomor tabel juga diselaraskan dengan naskah cetak.

## Sumber dan atribusi dataset

- **Rice (Cammeo and Osmancik)**, UCI Machine Learning Repository (2019), DOI [10.24432/C5MW4Z](https://doi.org/10.24432/C5MW4Z).
- [Halaman resmi dataset](https://archive.ics.uci.edu/dataset/545/rice). Dataset berlisensi **CC BY 4.0**. Kode sumber repositori ini terpisah dan menggunakan **MIT License**.
- Rekaman sumber data untuk hasil buku: SHA-256 berkas ARFF `1af97883100c89de2ea2972f7a28d428f4f1c14711a61defc0b0569e9eb65665`.

Tidak ada citra butir beras mentah atau file ARFF yang disertakan dalam repositori. Notebook mengambil data UCI saat dijalankan.

## Reproduksibilitas

- Python pada eksekusi referensi: **3.13.16**; NumPy **2.1.3**, pandas **2.2.3**, scikit-learn **1.6.1**. Versi SciPy dan Matplotlib eksekusi referensi tidak tersimpan pada metadata lama, sehingga tidak boleh diklaim sudah terkunci.
- Jalankan `pip install -r requirements-reference.txt` bila ingin mendekati lingkungan referensi; pada Colab umumnya perpustakaan inti sudah tersedia.
- Jalankan `python scripts/validate_repo.py` dari akar repositori untuk memeriksa angka referensi, matriks kebingungan, kelengkapan aset, dan konsistensi nama.

## Batasan

Satu pemisahan train–test dan lima lipatan CV pada training belum membuktikan kemampuan generalisasi pada kondisi akuisisi citra lain. Jangan mengubah model setelah meninjau hasil test lalu menganggap test yang sama sebagai evaluasi independen baru.

## Sitasi

Saat menggunakan notebook, kutip **repositori ini setelah dipublikasikan** dan juga dataset UCI (DOI di atas). Lihat `CITATION.cff`. Publikasi kode tidak mengubah lisensi dataset.
