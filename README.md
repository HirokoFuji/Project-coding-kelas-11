# Aplikasi Jadwal Mingguan Sekolah

Aplikasi manajemen jadwal mingguan sekolah sederhana. Dibuat dengan Flask (mengikuti arsitektur MVC).

## Fitur

- Manajemen jadwal harian (Senin-Sabtu)
- Tambah, edit, dan hapus aktivitas
- Pengelompokan jadwal berdasarkan hari
- Informasi detail aktivitas (waktu, lokasi, deskripsi)

## Cara Pakai

1. Install Python 3.x
2. Install package yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan aplikasi:
   ```bash
   python run.py
   ```
4. Buka browser dan akses http://localhost:5000

## Cara Penggunaan

1. Buka halaman utama untuk melihat jadwal mingguan
2. Klik "Tambah" untuk menambahkan aktivitas baru
3. Isi detail aktivitas:
   - Pilih hari
   - Masukkan waktu mulai dan selesai
   - Tulis nama aktivitas
   - Tambahkan lokasi (opsional)
   - Tambahkan deskripsi (opsional)
4. Klik tombol "Ubah" untuk mengedit aktivitas
5. Klik tombol "Hapus" untuk menghapus aktivitas

## Struktur Jadwal

### Hari Aktif
- Senin
- Selasa
- Rabu
- Kamis
- Jumat
- Sabtu

### Informasi Aktivitas
- Waktu mulai dan selesai
- Nama aktivitas
- Lokasi (opsional)
- Deskripsi (opsional)

## Teknologi

- Backend: Python Flask
- Database: SQLite
- Frontend: HTML, CSS, Bootstrap 5
- Icons: Bootstrap Icons

## Struktur Database

### Schedule
- id (Primary Key)
- day (Hari: Senin-Sabtu)
- start_time (Waktu mulai)
- end_time (Waktu selesai)
- activity (Nama aktivitas)
- location (Lokasi, opsional)
- description (Deskripsi, opsional)
- created_at (Waktu dibuat)
- updated_at (Waktu diupdate)

## Penjelasan Kode

### Model (Database)
- Schedule: Menyimpan data jadwal aktivitas

### Route (Controller)
- /: Halaman utama (daftar jadwal)
- /add: Halaman tambah aktivitas
- /edit/<id>: Halaman edit aktivitas
- /delete/<id>: Hapus aktivitas

### Template (View)
- base.html: Template dasar
- index.html: Tampilan daftar jadwal
- add.html: Form tambah aktivitas
- edit.html: Form edit aktivitas

### Fungsi Utama
- get_all(): Ambil semua jadwal
- get_by_id(): Ambil jadwal berdasarkan ID
- get_by_day(): Ambil jadwal berdasarkan hari
- save(): Simpan jadwal baru/update
- delete(): Hapus jadwal

## Panduan Penggunaan

1. Lihat Jadwal
   - Buka halaman utama
   - Jadwal dikelompokkan per hari
   - Urutan berdasarkan waktu

2. Tambah Aktivitas
   - Klik tombol "Tambah"
   - Isi form aktivitas
   - Klik "Tambah Aktivitas"

3. Edit Aktivitas
   - Klik tombol "Ubah" pada aktivitas
   - Ubah informasi yang diinginkan
   - Klik "Simpan Perubahan"

4. Hapus Aktivitas
   - Klik tombol "Hapus" pada aktivitas
   - Konfirmasi penghapusan

-- Marvello Revand Sunaryo [Kelas XI IPA IV] 