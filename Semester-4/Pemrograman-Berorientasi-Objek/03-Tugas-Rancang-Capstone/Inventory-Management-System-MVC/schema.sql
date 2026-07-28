-- Membuat Database
CREATE DATABASE IF NOT EXISTS db_gudang;

-- Menggunakan Database
USE db_gudang;

-- Tabel Barang
CREATE TABLE tb_barang (
    id_barang INT AUTO_INCREMENT PRIMARY KEY,
    nama_barang VARCHAR(255) NOT NULL,
    kategori_barang VARCHAR(100),
    stok INT NOT NULL,
    stok_minimum INT NOT NULL,
    harga_satuan DECIMAL(10, 2),
    tanggal_ditambahkan TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabel Transaksi Stok
CREATE TABLE tb_transaksi_stok (
    id_transaksi INT AUTO_INCREMENT PRIMARY KEY,
    id_barang INT NOT NULL,
    jenis_transaksi ENUM('masuk', 'keluar') NOT NULL,
    jumlah INT NOT NULL,
    tanggal_transaksi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    keterangan TEXT,
    FOREIGN KEY (id_barang) REFERENCES tb_barang(id_barang)
    ON DELETE CASCADE
);

-- Tabel Notifikasi
CREATE TABLE tb_notifikasi (
    id_notifikasi INT AUTO_INCREMENT PRIMARY KEY,
    id_barang INT NOT NULL,
    pesan VARCHAR(255),
    status ENUM('belum_dibaca', 'dibaca') DEFAULT 'belum_dibaca',
    tanggal_notifikasi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_barang) REFERENCES tb_barang(id_barang)
    ON DELETE CASCADE
);

-- Tabel Laporan Inventaris
CREATE TABLE tb_laporan_inventaris (
    id_laporan INT AUTO_INCREMENT PRIMARY KEY,
    id_barang INT NOT NULL,
    stok_saat_ini INT NOT NULL,
    tanggal_laporan TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_barang) REFERENCES tb_barang(id_barang)
    ON DELETE CASCADE
);

-- Data Dummy untuk Barang
INSERT INTO tb_barang (nama_barang, kategori_barang, stok, stok_minimum, harga_satuan)
VALUES
('Barang A', 'Kategori 1', 50, 10, 5000.00),
('Barang B', 'Kategori 2', 30, 5, 15000.00),
('Barang C', 'Kategori 1', 20, 5, 7500.00);

-- Data Dummy untuk Transaksi Stok
INSERT INTO tb_transaksi_stok (id_barang, jenis_transaksi, jumlah, keterangan)
VALUES
(1, 'masuk', 20, 'Stok awal Barang A'),
(2, 'keluar', 10, 'Barang B terjual'),
(3, 'masuk', 50, 'Stok tambahan Barang C');

-- Data Dummy untuk Notifikasi
INSERT INTO tb_notifikasi (id_barang, pesan)
VALUES
(1, 'Stok rendah untuk Barang A'),
(2, 'Stok rendah untuk Barang B'),
(3, 'Stok rendah untuk Barang C');

-- Data Dummy untuk Laporan Inventaris
INSERT INTO tb_laporan_inventaris (id_barang, stok_saat_ini)
VALUES
(1, 50),
(2, 30),
(3, 20);
