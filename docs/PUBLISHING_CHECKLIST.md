# Checklist penerbitan GitHub

1. Buat repositori **public** bernama `statistical-machine-learning-bab10-rice` (atau ganti sesuai kebutuhan).
2. Unggah isi folder **ini**, bukan file ZIP sebagai satu berkas.
3. Pastikan `README.md` muncul di halaman utama dan `notebooks/Bab10_Rice_Statistical_ML.ipynb` bisa dibuka.
4. Sesuaikan `USERNAME` pada pola URL Colab di README setelah repositori benar-benar dibuat.
5. Verifikasi tautan Colab: `https://colab.research.google.com/github/USERNAME/statistical-machine-learning-bab10-rice/blob/main/notebooks/Bab10_Rice_Statistical_ML.ipynb` (pengguna dan nama repositori aktual).
6. Jalankan **Run all** di Google Colab dengan dataset UCI resmi. Pastikan nama file keluaran sama dengan `docs/BOOK_ALIGNMENT.md`; catat versi lingkungan.
7. Di GitHub klik **Releases → Draft a new release** dan buat tag `v1.0.0` untuk snapshot kode yang dirujuk buku. Jangan mengubah tag setelah cetak.
8. Setelah terbit, buat QR code menuju URL rilis atau repositori aktual; sebelum itu tidak boleh mencetak URL contoh yang belum valid.
9. Cantumkan URL dan tanggal akses dalam naskah Bab 10 (Subbab 10.4) setelah link final diketahui.
10. Tinjau lisensi MIT (kode) dan CC BY 4.0 (dataset) sebelum publikasi.

**Jangan masukkan** kunci API, token, data pribadi, kredensial, file mentah yang tidak berizin, atau notebook output yang menyingkap informasi sensitif.
