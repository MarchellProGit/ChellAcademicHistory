-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 04, 2024 at 05:19 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `belajar_session`
--
CREATE DATABASE IF NOT EXISTS `belajar_session` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `belajar_session`;

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id`, `name`, `description`) VALUES
(1, 'Marchel', 'gac');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'satu', 'satu');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data`
--
ALTER TABLE `data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Database: `crud_system`
--
CREATE DATABASE IF NOT EXISTS `crud_system` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `crud_system`;
--
-- Database: `dbmahasiswa`
--
CREATE DATABASE IF NOT EXISTS `dbmahasiswa` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `dbmahasiswa`;

-- --------------------------------------------------------

--
-- Table structure for table `emp`
--

CREATE TABLE `emp` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `address` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `emp`
--

INSERT INTO `emp` (`id`, `name`, `email`, `phone`, `address`) VALUES
(1, 'John Doe', 'johndoe@example.com', '1234567890', '123 Main St, City A'),
(2, 'Jane Smith', 'janesmith@example.com', '0987654321', '456 Oak St, City B'),
(3, 'Michael Johnson', 'michaelj@example.com', '1122334455', '789 Pine St, City C'),
(4, 'Emily Davis', 'emilyd@example.com', '2233445566', '101 Maple St, City D'),
(5, 'David Brown', 'davidb@example.com', '3344556677', '202 Elm St, City E');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emp`
--
ALTER TABLE `emp`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `emp`
--
ALTER TABLE `emp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- Database: `dbparkir`
--
CREATE DATABASE IF NOT EXISTS `dbparkir` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `dbparkir`;

-- --------------------------------------------------------

--
-- Table structure for table `tbparkir`
--

CREATE TABLE `tbparkir` (
  `id` int(11) NOT NULL,
  `nim` varchar(9) NOT NULL,
  `nama` varchar(45) NOT NULL,
  `status` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbparkir`
--

INSERT INTO `tbparkir` (`id`, `nim`, `nama`, `status`) VALUES
(1, '670007', 'Bowo', 'Aktif'),
(2, '670007', 'Waldi', 'Tidak Aktif'),
(3, '670007', 'DS', 'Aktif');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbparkir`
--
ALTER TABLE `tbparkir`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbparkir`
--
ALTER TABLE `tbparkir`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- Database: `dbtugas3dpj`
--
CREATE DATABASE IF NOT EXISTS `dbtugas3dpj` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `dbtugas3dpj`;

-- --------------------------------------------------------

--
-- Table structure for table `emp`
--

CREATE TABLE `emp` (
  `id` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `alamat` text DEFAULT NULL,
  `program_studi` varchar(100) NOT NULL,
  `umur` int(3) DEFAULT NULL,
  `hobi` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `emp`
--

INSERT INTO `emp` (`id`, `nama`, `alamat`, `program_studi`, `umur`, `hobi`) VALUES
(2, 'SAMUEL GALUH DIAS PRAMUDYA', 'Jl. Kemiri, Salatiga', 'Teknik Informatika', 21, 'Membuat aplikasi,               Bermain game online'),
(3, 'STEVANUS ZAKHARIA HENDRIK SUAWAH', 'Jl. Merbabu, Salatiga', 'Teknik Informatika', 20, 'Pengembangan web,  Ngoding'),
(6, 'YOSUA YOGA DHARMA SAPUTRA', 'Jl. Pattimura, Salatiga', 'Teknik Informatika', 20, 'Ngoding,   Ball'),
(7, 'KEVIN ANTHONY JAYA', 'Jl. Cipto, Salatiga', 'Teknik Informatika', 21, 'Keamanan komputer, Ngoding'),
(10, 'MELANI REGIANA RAMPO', 'Jl. Veteran, Salatiga', 'Teknik Informatika', 20, 'Pemrograman web, Membaca'),
(12, 'SANG KHALIK', 'Jl. Kemiri, Salatiga', 'Teknik Informatika', 99, 'Mengatur Dunia'),
(13, 'MAHASISWA 1', 'Jl. Kemiri, Salatiga', 'Teknik Informatika', 21, 'Membuat aplikasi,         Bermain game online'),
(14, 'MAHASISWA 2', 'Jl. Merbabu, Salatiga', 'Teknik Informatika', 22, 'Membuat aplikasi,           Bermain game onlain'),
(15, 'MAHASISWA 4', 'Jl. Pattimura, Salatiga', 'Teknik Informatika', 21, 'Nyoblos,  Ehay');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emp`
--
ALTER TABLE `emp`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `emp`
--
ALTER TABLE `emp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- Database: `db_bnn`
--
CREATE DATABASE IF NOT EXISTS `db_bnn` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `db_bnn`;

-- --------------------------------------------------------

--
-- Table structure for table `tb_pasien`
--

CREATE TABLE `tb_pasien` (
  `id` int(11) NOT NULL,
  `nama` varchar(45) NOT NULL,
  `kecanduan` varchar(45) NOT NULL,
  `periode` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_pasien`
--

INSERT INTO `tb_pasien` (`id`, `nama`, `kecanduan`, `periode`) VALUES
(1, 'Ageng', 'solar', 2),
(2, 'Langgeng', 'lem', 2),
(5, 's', 's', 2);

-- --------------------------------------------------------

--
-- Table structure for table `tb_petugas`
--

CREATE TABLE `tb_petugas` (
  `id` int(11) NOT NULL,
  `nama` varchar(45) NOT NULL,
  `password` varchar(20) NOT NULL,
  `jabatan` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_petugas`
--

INSERT INTO `tb_petugas` (`id`, `nama`, `password`, `jabatan`) VALUES
(1, 'Sucipto', '1234', 'pembina'),
(2, 'Sutarno', '4321', 'intel');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_pasien`
--
ALTER TABLE `tb_pasien`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tb_petugas`
--
ALTER TABLE `tb_petugas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_pasien`
--
ALTER TABLE `tb_pasien`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tb_petugas`
--
ALTER TABLE `tb_petugas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- Database: `db_gudang`
--
CREATE DATABASE IF NOT EXISTS `db_gudang` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `db_gudang`;

-- --------------------------------------------------------

--
-- Table structure for table `tb_admin`
--

CREATE TABLE `tb_admin` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_admin`
--

INSERT INTO `tb_admin` (`id`, `username`, `password`) VALUES
(1, 'satu', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `tb_barang`
--

CREATE TABLE `tb_barang` (
  `id_barang` int(11) NOT NULL,
  `nama_barang` varchar(255) NOT NULL,
  `kategori_barang` varchar(100) DEFAULT NULL,
  `stok` int(11) NOT NULL,
  `stok_minimum` int(11) NOT NULL,
  `harga_satuan` decimal(10,2) DEFAULT NULL,
  `tanggal_ditambahkan` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_barang`
--

INSERT INTO `tb_barang` (`id_barang`, `nama_barang`, `kategori_barang`, `stok`, `stok_minimum`, `harga_satuan`, `tanggal_ditambahkan`) VALUES
(1, 'Barang A', 'Kategori 1', 50, 10, 100.00, '2024-11-27 15:45:24'),
(2, 'Barang B', 'Kategori 2', 30, 5, 15000.00, '2024-11-27 15:45:24'),
(5, '3', 'Kategori 1', 10, 10, 1000.00, '2024-12-04 15:29:56'),
(6, '', 'Kategori 1', 1, 1, 1.00, '2024-12-04 15:30:21');

-- --------------------------------------------------------

--
-- Table structure for table `tb_laporan_inventaris`
--

CREATE TABLE `tb_laporan_inventaris` (
  `id_laporan` int(11) NOT NULL,
  `id_barang` int(11) NOT NULL,
  `stok_saat_ini` int(11) NOT NULL,
  `tanggal_laporan` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_laporan_inventaris`
--

INSERT INTO `tb_laporan_inventaris` (`id_laporan`, `id_barang`, `stok_saat_ini`, `tanggal_laporan`) VALUES
(1, 1, 50, '2024-11-27 15:45:24'),
(2, 2, 30, '2024-11-27 15:45:24');

-- --------------------------------------------------------

--
-- Table structure for table `tb_notifikasi`
--

CREATE TABLE `tb_notifikasi` (
  `id_notifikasi` int(11) NOT NULL,
  `id_barang` int(11) NOT NULL,
  `pesan` varchar(255) DEFAULT NULL,
  `status` enum('belum_dibaca','dibaca') DEFAULT 'belum_dibaca',
  `tanggal_notifikasi` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_notifikasi`
--

INSERT INTO `tb_notifikasi` (`id_notifikasi`, `id_barang`, `pesan`, `status`, `tanggal_notifikasi`) VALUES
(1, 1, 'Stok rendah untuk Barang A', 'dibaca', '2024-11-27 15:45:24'),
(2, 2, 'Stok rendah untuk Barang B', 'dibaca', '2024-11-27 15:45:24');

-- --------------------------------------------------------

--
-- Table structure for table `tb_transaksi_stok`
--

CREATE TABLE `tb_transaksi_stok` (
  `id_transaksi` int(11) NOT NULL,
  `id_barang` int(11) NOT NULL,
  `jenis_transaksi` enum('masuk','keluar') NOT NULL,
  `jumlah` int(11) NOT NULL,
  `tanggal_transaksi` timestamp NOT NULL DEFAULT current_timestamp(),
  `keterangan` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_transaksi_stok`
--

INSERT INTO `tb_transaksi_stok` (`id_transaksi`, `id_barang`, `jenis_transaksi`, `jumlah`, `tanggal_transaksi`, `keterangan`) VALUES
(1, 1, 'masuk', 20, '2024-11-27 15:45:24', 'Stok awal Barang A'),
(2, 2, 'keluar', 10, '2024-11-27 15:45:24', 'Barang B terjual'),
(4, 2, 'keluar', 1, '2024-11-27 15:45:24', 'keluar'),
(5, 1, 'keluar', 10, '2024-11-27 15:45:24', 'k');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_admin`
--
ALTER TABLE `tb_admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tb_barang`
--
ALTER TABLE `tb_barang`
  ADD PRIMARY KEY (`id_barang`);

--
-- Indexes for table `tb_laporan_inventaris`
--
ALTER TABLE `tb_laporan_inventaris`
  ADD PRIMARY KEY (`id_laporan`),
  ADD KEY `id_barang` (`id_barang`);

--
-- Indexes for table `tb_notifikasi`
--
ALTER TABLE `tb_notifikasi`
  ADD PRIMARY KEY (`id_notifikasi`),
  ADD KEY `id_barang` (`id_barang`);

--
-- Indexes for table `tb_transaksi_stok`
--
ALTER TABLE `tb_transaksi_stok`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_barang` (`id_barang`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_admin`
--
ALTER TABLE `tb_admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_barang`
--
ALTER TABLE `tb_barang`
  MODIFY `id_barang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tb_laporan_inventaris`
--
ALTER TABLE `tb_laporan_inventaris`
  MODIFY `id_laporan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tb_notifikasi`
--
ALTER TABLE `tb_notifikasi`
  MODIFY `id_notifikasi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tb_transaksi_stok`
--
ALTER TABLE `tb_transaksi_stok`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_laporan_inventaris`
--
ALTER TABLE `tb_laporan_inventaris`
  ADD CONSTRAINT `tb_laporan_inventaris_ibfk_1` FOREIGN KEY (`id_barang`) REFERENCES `tb_barang` (`id_barang`) ON DELETE CASCADE;

--
-- Constraints for table `tb_notifikasi`
--
ALTER TABLE `tb_notifikasi`
  ADD CONSTRAINT `tb_notifikasi_ibfk_1` FOREIGN KEY (`id_barang`) REFERENCES `tb_barang` (`id_barang`) ON DELETE CASCADE;

--
-- Constraints for table `tb_transaksi_stok`
--
ALTER TABLE `tb_transaksi_stok`
  ADD CONSTRAINT `tb_transaksi_stok_ibfk_1` FOREIGN KEY (`id_barang`) REFERENCES `tb_barang` (`id_barang`) ON DELETE CASCADE;
--
-- Database: `db_jobseeker`
--
CREATE DATABASE IF NOT EXISTS `db_jobseeker` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `db_jobseeker`;

-- --------------------------------------------------------

--
-- Table structure for table `tb_admin`
--

CREATE TABLE `tb_admin` (
  `admin_id` int(11) NOT NULL,
  `nama_admin` varchar(100) NOT NULL,
  `email_admin` varchar(100) NOT NULL,
  `password_admin` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_admin`
--

INSERT INTO `tb_admin` (`admin_id`, `nama_admin`, `email_admin`, `password_admin`) VALUES
(1, 'adm1', 'adm@gmail.com', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tb_daftar_pekerjaan`
--

CREATE TABLE `tb_daftar_pekerjaan` (
  `daftar_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `lowongan_id` int(11) NOT NULL,
  `status_pendaftaran` enum('Pending','Lolos','Tidak Lolos') DEFAULT 'Pending',
  `tanggal_daftar` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Triggers `tb_daftar_pekerjaan`
--
DELIMITER $$
CREATE TRIGGER `update_status_pendaftaran` AFTER UPDATE ON `tb_daftar_pekerjaan` FOR EACH ROW BEGIN
    IF NEW.status_pendaftaran = 'Lolos' THEN
        UPDATE tb_daftar_pekerjaan SET status_pendaftaran = 'Lolos' WHERE daftar_id = NEW.daftar_id;
    ELSEIF NEW.status_pendaftaran = 'Tidak Lolos' THEN
        UPDATE tb_daftar_pekerjaan SET status_pendaftaran = 'Tidak Lolos' WHERE daftar_id = NEW.daftar_id;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `tb_login`
--

CREATE TABLE `tb_login` (
  `signup_id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `role` enum('Admin','HRD','User') NOT NULL DEFAULT 'User'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_login`
--

INSERT INTO `tb_login` (`signup_id`, `email`, `password`, `created_at`, `role`) VALUES
(1, 'marchell@gmail.com', '$2y$10$CDaIJHrzsxj2fg0uF5yZ4O3iUQGGmu0wHYpD1faSF1oBJuswQzkIG', '2024-12-02 02:48:23', 'User'),
(4, 'marchell1@gmail.com', '$2y$10$..JaTBubteZRORu0nAljueQK8DNi/DB7uViyaWRhk6nywHN1ZbmIy', '2024-12-02 02:50:35', 'User'),
(5, 'marchell1@gmail.co', '$2y$10$XAfBBk2s0H2FkDhlmBa.LerlZiibupjEgSuMWZjKHWI1CSlpZgA4u', '2024-12-02 17:50:23', 'User'),
(6, '12@gmail.com', '$2y$10$f.ePLb592Igk6Ypy41NV4.xq9KNPRTg4FYYMZnb2Q1iNDGcRraCh.', '2024-12-02 17:54:59', 'User'),
(7, 'marchell12@gmail.com', '$2y$10$UshHhLif7qdYerbUZipQh.t5E/y3dZl2IEkJGQGoChjkHSqLl2Hl.', '2024-12-02 17:59:38', 'User'),
(8, 'Marchell1111@gmail.com', '123456', '2024-12-02 18:11:07', 'User'),
(9, 'Marchell11112@gmail.com', '1', '2024-12-02 18:13:22', 'User'),
(18, 'Marchell123@gmail.com', '111', '2024-12-02 18:20:05', 'User'),
(21, '123@gmail.com', '123@gmail.com', '2024-12-02 18:21:47', 'User'),
(23, '111@gmail.com', '111', '2024-12-02 18:24:48', 'User'),
(24, 'oke1@gmail.com', '$2y$10$6WVZpTznMbD8Z8JNQx3dPOO7e4MybyKKazdQ1B7ck7iVfEZgvtVEu', '2024-12-02 20:59:04', 'User'),
(25, 'marchell@example.com', '60e10b72983f6e7932a856c8e31a03ef903eee7c21f9db11577d94c0eba8efca', '2024-12-02 21:08:51', 'HRD'),
(26, 'marchell_admin@example.com', 'b2fa9c1f8b4ba33eb4f5999b456a24a9fa1fabe8b510f3b7a98753fd37b46296', '2024-12-02 21:08:51', 'Admin'),
(27, 'puja@example.com', 'b1202f3d5b1135011c608be5802267be51216ea71bcb944a8671bf8f603f4095', '2024-12-02 21:08:51', 'HRD'),
(28, 'puja_admin@example.com', '79ed8a595610206c07802346665087d5f8da64ff2ce1092ee1042af6a4e79b8d', '2024-12-02 21:08:51', 'Admin'),
(29, 'farhan@example.com', '147bdf8dc60dcea71959ab3cf30567c5445f2ce12b000b9797d54582816c81e9', '2024-12-02 21:08:51', 'HRD'),
(30, 'farhan_admin@example.com', '0e804f8fb0cd8e3dea3eb81a9e3c37839169138cb1f001ca79b03b23167c9d2d', '2024-12-02 21:08:51', 'Admin'),
(32, 'oke2@gmail.com', '$2y$10$zG3QoP9dxdly95ZexQ6c1.ceSHc8x6BbJACTsVHHahvfeEv5ULV8u', '2024-12-02 21:24:08', 'User'),
(33, 'oke3@gmail.com', '$2y$10$BMP5Id7E.eHnpbQIC8l70.wphXV/ya8BuVEB9uVFAvb/l2ZnDbFsu', '2024-12-02 21:26:57', 'User');

-- --------------------------------------------------------

--
-- Table structure for table `tb_lowongan`
--

CREATE TABLE `tb_lowongan` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `deskripsi` text NOT NULL,
  `lokasi` varchar(255) NOT NULL,
  `gaji` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_lowongan`
--

INSERT INTO `tb_lowongan` (`id`, `nama`, `deskripsi`, `lokasi`, `gaji`) VALUES
(1, 'Software Engineer', 'Develop and maintain software applications.', 'Jakarta', 15000000.00),
(2, 'Data Analyst', 'Analyze data and generate insights.', 'Bandung', 12000000.00),
(3, 'Project Manager', 'Manage software development projects.', 'Surabaya', 20000000.00),
(4, 'UI/UX Designer', 'Design user interfaces and user experiences.', 'Yogyakarta', 10000000.00),
(5, 'System Administrator', 'Maintain and manage IT infrastructure.', 'Jakarta', 13000000.00);

-- --------------------------------------------------------

--
-- Table structure for table `tb_pembuka_lowongan`
--

CREATE TABLE `tb_pembuka_lowongan` (
  `pembuka_id` int(11) NOT NULL,
  `nama_pembuka` varchar(100) NOT NULL,
  `email_pembuka` varchar(100) NOT NULL,
  `telepon` varchar(15) DEFAULT NULL,
  `perusahaan_id` int(11) DEFAULT NULL,
  `tipe_pekerjaan` enum('Intern','Full Time') NOT NULL,
  `deskripsi_lowongan` text DEFAULT NULL,
  `kuota_pelamar` int(11) DEFAULT NULL,
  `gaji` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_pembuka_lowongan`
--

INSERT INTO `tb_pembuka_lowongan` (`pembuka_id`, `nama_pembuka`, `email_pembuka`, `telepon`, `perusahaan_id`, `tipe_pekerjaan`, `deskripsi_lowongan`, `kuota_pelamar`, `gaji`) VALUES
(2, 'admin1', 'admin1@gmail.com', '0123456789', 1, 'Intern', 'l1', 100, 50000000.00);

-- --------------------------------------------------------

--
-- Table structure for table `tb_persyaratan_lowongan`
--

CREATE TABLE `tb_persyaratan_lowongan` (
  `persyaratan_id` int(11) NOT NULL,
  `lowongan_id` int(11) NOT NULL,
  `pendidikan_minimal` varchar(50) DEFAULT NULL,
  `pengalaman_kerja_minimal` varchar(50) DEFAULT NULL,
  `kriteria_umum` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_perusahaan`
--

CREATE TABLE `tb_perusahaan` (
  `perusahaan_id` int(11) NOT NULL,
  `nama_perusahaan` varchar(100) NOT NULL,
  `alamat_perusahaan` text DEFAULT NULL,
  `jenis_usaha` varchar(50) DEFAULT NULL,
  `kontak_perusahaan` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_perusahaan`
--

INSERT INTO `tb_perusahaan` (`perusahaan_id`, `nama_perusahaan`, `alamat_perusahaan`, `jenis_usaha`, `kontak_perusahaan`) VALUES
(1, 'p1', 'a1', 'u1', '081');

-- --------------------------------------------------------

--
-- Table structure for table `tb_riwayat_lowongan`
--

CREATE TABLE `tb_riwayat_lowongan` (
  `riwayat_id` int(11) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `lowongan_id` int(11) NOT NULL,
  `aksi` enum('Tambah','Edit','Hapus') NOT NULL,
  `waktu_aksi` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_user_pendaftar`
--

CREATE TABLE `tb_user_pendaftar` (
  `user_id` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `alamat` text DEFAULT NULL,
  `telepon` varchar(15) DEFAULT NULL,
  `pendidikan_terakhir` varchar(50) DEFAULT NULL,
  `pengalaman_kerja` text DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `jenis_kelamin` enum('Laki-laki','Perempuan') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_admin`
--
ALTER TABLE `tb_admin`
  ADD PRIMARY KEY (`admin_id`),
  ADD UNIQUE KEY `email_admin` (`email_admin`);

--
-- Indexes for table `tb_daftar_pekerjaan`
--
ALTER TABLE `tb_daftar_pekerjaan`
  ADD PRIMARY KEY (`daftar_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `lowongan_id` (`lowongan_id`);

--
-- Indexes for table `tb_login`
--
ALTER TABLE `tb_login`
  ADD PRIMARY KEY (`signup_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `tb_lowongan`
--
ALTER TABLE `tb_lowongan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tb_pembuka_lowongan`
--
ALTER TABLE `tb_pembuka_lowongan`
  ADD PRIMARY KEY (`pembuka_id`),
  ADD UNIQUE KEY `email_pembuka` (`email_pembuka`),
  ADD KEY `perusahaan_id` (`perusahaan_id`);

--
-- Indexes for table `tb_persyaratan_lowongan`
--
ALTER TABLE `tb_persyaratan_lowongan`
  ADD PRIMARY KEY (`persyaratan_id`),
  ADD KEY `lowongan_id` (`lowongan_id`);

--
-- Indexes for table `tb_perusahaan`
--
ALTER TABLE `tb_perusahaan`
  ADD PRIMARY KEY (`perusahaan_id`);

--
-- Indexes for table `tb_riwayat_lowongan`
--
ALTER TABLE `tb_riwayat_lowongan`
  ADD PRIMARY KEY (`riwayat_id`),
  ADD KEY `admin_id` (`admin_id`),
  ADD KEY `lowongan_id` (`lowongan_id`);

--
-- Indexes for table `tb_user_pendaftar`
--
ALTER TABLE `tb_user_pendaftar`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_admin`
--
ALTER TABLE `tb_admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_daftar_pekerjaan`
--
ALTER TABLE `tb_daftar_pekerjaan`
  MODIFY `daftar_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_login`
--
ALTER TABLE `tb_login`
  MODIFY `signup_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `tb_lowongan`
--
ALTER TABLE `tb_lowongan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tb_pembuka_lowongan`
--
ALTER TABLE `tb_pembuka_lowongan`
  MODIFY `pembuka_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tb_persyaratan_lowongan`
--
ALTER TABLE `tb_persyaratan_lowongan`
  MODIFY `persyaratan_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_perusahaan`
--
ALTER TABLE `tb_perusahaan`
  MODIFY `perusahaan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tb_riwayat_lowongan`
--
ALTER TABLE `tb_riwayat_lowongan`
  MODIFY `riwayat_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_user_pendaftar`
--
ALTER TABLE `tb_user_pendaftar`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_daftar_pekerjaan`
--
ALTER TABLE `tb_daftar_pekerjaan`
  ADD CONSTRAINT `tb_daftar_pekerjaan_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tb_user_pendaftar` (`user_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `tb_daftar_pekerjaan_ibfk_2` FOREIGN KEY (`lowongan_id`) REFERENCES `tb_pembuka_lowongan` (`pembuka_id`) ON DELETE CASCADE;

--
-- Constraints for table `tb_pembuka_lowongan`
--
ALTER TABLE `tb_pembuka_lowongan`
  ADD CONSTRAINT `tb_pembuka_lowongan_ibfk_1` FOREIGN KEY (`perusahaan_id`) REFERENCES `tb_perusahaan` (`perusahaan_id`) ON DELETE SET NULL;

--
-- Constraints for table `tb_persyaratan_lowongan`
--
ALTER TABLE `tb_persyaratan_lowongan`
  ADD CONSTRAINT `tb_persyaratan_lowongan_ibfk_1` FOREIGN KEY (`lowongan_id`) REFERENCES `tb_pembuka_lowongan` (`pembuka_id`) ON DELETE CASCADE;

--
-- Constraints for table `tb_riwayat_lowongan`
--
ALTER TABLE `tb_riwayat_lowongan`
  ADD CONSTRAINT `tb_riwayat_lowongan_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `tb_admin` (`admin_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `tb_riwayat_lowongan_ibfk_2` FOREIGN KEY (`lowongan_id`) REFERENCES `tb_pembuka_lowongan` (`pembuka_id`) ON DELETE CASCADE;

--
-- Constraints for table `tb_user_pendaftar`
--
ALTER TABLE `tb_user_pendaftar`
  ADD CONSTRAINT `tb_user_pendaftar_ibfk_1` FOREIGN KEY (`email`) REFERENCES `tb_login` (`email`) ON DELETE CASCADE;
--
-- Database: `db_js`
--
CREATE DATABASE IF NOT EXISTS `db_js` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `db_js`;

-- --------------------------------------------------------

--
-- Table structure for table `applications`
--

CREATE TABLE `applications` (
  `application_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `job_id` int(11) NOT NULL,
  `status` enum('pending','lolos','tidak_lolos') DEFAULT 'pending',
  `applied_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `applications`
--

INSERT INTO `applications` (`application_id`, `user_id`, `job_id`, `status`, `applied_at`) VALUES
(1, 5, 1, 'pending', '2024-12-03 14:06:51'),
(2, 6, 1, 'pending', '2024-12-04 02:09:39'),
(3, 7, 1, 'pending', '2024-12-04 03:32:50'),
(4, 7, 2, 'pending', '2024-12-04 03:32:50');

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `job_id` int(11) NOT NULL,
  `title` varchar(150) NOT NULL,
  `description` text NOT NULL,
  `type` enum('intern','full_time') NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `posted_by` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `kuota` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jobs`
--

INSERT INTO `jobs` (`job_id`, `title`, `description`, `type`, `company_name`, `posted_by`, `created_at`, `kuota`) VALUES
(1, 'data', 'data science', 'intern', 'fti', 4, '2024-12-03 13:59:36', 10),
(2, 'software', 'se', 'full_time', 'fti', 4, '2024-12-04 02:44:48', 3),
(3, 'network', 'ne', 'full_time', 'fti', 4, '2024-12-04 03:09:05', 3),
(4, 'tr', 'tr', 'full_time', 'fti', 4, '2024-12-04 03:13:06', 1),
(5, 'tre', 'tr e', 'full_time', 'fti', 4, '2024-12-04 03:34:09', 10);

-- --------------------------------------------------------

--
-- Table structure for table `job_plus`
--

CREATE TABLE `job_plus` (
  `job_plus_id` int(11) NOT NULL,
  `job_id` int(11) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `salary` varchar(100) DEFAULT NULL,
  `requirements` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `job_plus`
--

INSERT INTO `job_plus` (`job_plus_id`, `job_id`, `location`, `salary`, `requirements`) VALUES
(1, 1, 'salatiga', '10000000', 'Tulus, ganteng, cantik, muda, sehat, sejahtera, kaya, spek dewa, dewa koding'),
(2, 2, 'indo', '3000', 'oke'),
(3, 3, 'indo', '30000', 'oke'),
(4, 4, 'indo', '7', 'tr'),
(5, 5, 'salatiga', '30000', 'gacor');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `deskripsi` text NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('pendaftar','admin','pembuka_lowongan') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `deskripsi`, `email`, `password`, `role`, `created_at`) VALUES
(1, '', '', 'user1@gmal.com', '$2y$10$c8qxxP7gnv4613oIRHsmDeJbhsbZyIuNO4Bu868Za1DlOdmn2JrwW', 'pendaftar', '2024-12-03 13:13:32'),
(2, '', '', 'user2@gmal.com', '$2y$10$0it5xA2jNmbca0iqjN7Zuuuy3dzuSCSjsltQCO2nkOOx3mvvPnGBi', 'pendaftar', '2024-12-03 13:15:17'),
(3, 'admin1', '', 'admin1@gmail.com', '123', 'admin', '2024-12-03 13:58:17'),
(4, 'job1', '', 'job1@gmail.com', '123', 'pembuka_lowongan', '2024-12-03 13:58:39'),
(5, 'user3', '', 'user3@gmail.com', '123', 'pendaftar', '2024-12-03 14:06:51'),
(6, '', '', 'responsi@gmail.com', '$2y$10$.PeXfgLNohreirtwHCnore.kM7jYTtYBb0/.JaAzChr7WUBVX.1h.', 'pendaftar', '2024-12-04 02:09:39'),
(7, '', '', 'coba@gmai.com', '$2y$10$aEnjqa5j3SsCkNi.ewVeJeMoAnz2A02dj2wgK.UzoHvFOM/7jAOoi', 'pendaftar', '2024-12-04 03:32:50');

--
-- Triggers `users`
--
DELIMITER $$
CREATE TRIGGER `after_user_insert` AFTER INSERT ON `users` FOR EACH ROW BEGIN
    DECLARE default_job_id INT;

    -- Ambil job_id pertama dari tabel jobs
    SELECT job_id INTO default_job_id FROM jobs LIMIT 1;

    -- Jika job_id ditemukan, masukkan ke tabel applications
    IF default_job_id IS NOT NULL THEN
        INSERT INTO applications (user_id, job_id, status)
        VALUES (NEW.user_id, default_job_id, 'pending');
    END IF;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `after_user_insert_job_plus` AFTER INSERT ON `users` FOR EACH ROW BEGIN
    DECLARE job_id_from_job_plus INT;

    -- Ambil job_id dari tabel job_plus
    SELECT job_id INTO job_id_from_job_plus
    FROM job_plus
    WHERE job_id IN (SELECT job_id FROM jobs WHERE posted_by = NEW.user_id)
    LIMIT 1;

    -- Masukkan ke tabel applications jika job_id ditemukan
    IF job_id_from_job_plus IS NOT NULL THEN
        INSERT INTO applications (user_id, job_id, status)
        VALUES (NEW.user_id, job_id_from_job_plus, 'pending');
    END IF;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `after_user_insert_specific_job` AFTER INSERT ON `users` FOR EACH ROW BEGIN
    DECLARE specific_job_id INT;

    -- Ambil job_id berdasarkan perusahaan yang memposting
    SELECT job_id INTO specific_job_id
    FROM jobs
    WHERE company_name = 'Some Company Name' AND posted_by = NEW.user_id
    LIMIT 1;

    -- Masukkan ke tabel applications jika job_id ditemukan
    IF specific_job_id IS NOT NULL THEN
        INSERT INTO applications (user_id, job_id, status)
        VALUES (NEW.user_id, specific_job_id, 'pending');
    END IF;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `after_user_insert_with_condition` AFTER INSERT ON `users` FOR EACH ROW BEGIN
    DECLARE selected_job_id INT;

    -- Ambil job_id berdasarkan tipe pekerjaan full_time
    SELECT job_id INTO selected_job_id
    FROM jobs
    WHERE type = 'full_time'
    LIMIT 1;

    -- Masukkan ke tabel applications jika job_id ditemukan
    IF selected_job_id IS NOT NULL THEN
        INSERT INTO applications (user_id, job_id, status)
        VALUES (NEW.user_id, selected_job_id, 'pending');
    END IF;
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `applications`
--
ALTER TABLE `applications`
  ADD PRIMARY KEY (`application_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `job_id` (`job_id`);

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`job_id`),
  ADD KEY `posted_by` (`posted_by`);

--
-- Indexes for table `job_plus`
--
ALTER TABLE `job_plus`
  ADD PRIMARY KEY (`job_plus_id`),
  ADD KEY `job_id` (`job_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `applications`
--
ALTER TABLE `applications`
  MODIFY `application_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `jobs`
--
ALTER TABLE `jobs`
  MODIFY `job_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `job_plus`
--
ALTER TABLE `job_plus`
  MODIFY `job_plus_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `applications`
--
ALTER TABLE `applications`
  ADD CONSTRAINT `applications_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `applications_ibfk_2` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`job_id`) ON DELETE CASCADE;

--
-- Constraints for table `jobs`
--
ALTER TABLE `jobs`
  ADD CONSTRAINT `jobs_ibfk_1` FOREIGN KEY (`posted_by`) REFERENCES `users` (`user_id`) ON DELETE CASCADE;

--
-- Constraints for table `job_plus`
--
ALTER TABLE `job_plus`
  ADD CONSTRAINT `job_plus_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`job_id`) ON DELETE CASCADE;
--
-- Database: `db_perpustakaan`
--
CREATE DATABASE IF NOT EXISTS `db_perpustakaan` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `db_perpustakaan`;

-- --------------------------------------------------------

--
-- Table structure for table `tbadmin`
--

CREATE TABLE `tbadmin` (
  `id_admin` int(11) NOT NULL,
  `nama_admin` varchar(255) NOT NULL,
  `email_admin` varchar(255) NOT NULL,
  `password_admin` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbadmin`
--

INSERT INTO `tbadmin` (`id_admin`, `nama_admin`, `email_admin`, `password_admin`) VALUES
(1, 'admin1', 'admin1@gmail.com', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblowongan`
--

CREATE TABLE `tblowongan` (
  `id_lowongan` int(11) NOT NULL,
  `nama_lowongan` varchar(255) NOT NULL,
  `deskripsi_lowongan` text DEFAULT NULL,
  `kualifikasi_lowongan` text DEFAULT NULL,
  `gaji` int(11) DEFAULT NULL,
  `nama_perusahaan` varchar(255) NOT NULL,
  `tanggal_buka_pendaftaran` date DEFAULT NULL,
  `tanggal_tutup_pendaftaran` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tblowongan`
--

INSERT INTO `tblowongan` (`id_lowongan`, `nama_lowongan`, `deskripsi_lowongan`, `kualifikasi_lowongan`, `gaji`, `nama_perusahaan`, `tanggal_buka_pendaftaran`, `tanggal_tutup_pendaftaran`) VALUES
(1, 'lowongan1', 'deskripsi1', 'kualifikasi1', 1, 'perusahaan1', '2024-11-23', '2024-11-24'),
(2, 'lowongan2', 'deskripsi2', 'kualifikasi2', 2, 'perusahaan2', '2024-11-23', '2024-11-24');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbadmin`
--
ALTER TABLE `tbadmin`
  ADD PRIMARY KEY (`id_admin`),
  ADD UNIQUE KEY `email_admin` (`email_admin`);

--
-- Indexes for table `tblowongan`
--
ALTER TABLE `tblowongan`
  ADD PRIMARY KEY (`id_lowongan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbadmin`
--
ALTER TABLE `tbadmin`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tblowongan`
--
ALTER TABLE `tblowongan`
  MODIFY `id_lowongan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- Database: `phpmyadmin`
--
CREATE DATABASE IF NOT EXISTS `phpmyadmin` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
USE `phpmyadmin`;

-- --------------------------------------------------------

--
-- Table structure for table `pma__bookmark`
--

CREATE TABLE `pma__bookmark` (
  `id` int(10) UNSIGNED NOT NULL,
  `dbase` varchar(255) NOT NULL DEFAULT '',
  `user` varchar(255) NOT NULL DEFAULT '',
  `label` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `query` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Bookmarks';

-- --------------------------------------------------------

--
-- Table structure for table `pma__central_columns`
--

CREATE TABLE `pma__central_columns` (
  `db_name` varchar(64) NOT NULL,
  `col_name` varchar(64) NOT NULL,
  `col_type` varchar(64) NOT NULL,
  `col_length` text DEFAULT NULL,
  `col_collation` varchar(64) NOT NULL,
  `col_isNull` tinyint(1) NOT NULL,
  `col_extra` varchar(255) DEFAULT '',
  `col_default` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Central list of columns';

-- --------------------------------------------------------

--
-- Table structure for table `pma__column_info`
--

CREATE TABLE `pma__column_info` (
  `id` int(5) UNSIGNED NOT NULL,
  `db_name` varchar(64) NOT NULL DEFAULT '',
  `table_name` varchar(64) NOT NULL DEFAULT '',
  `column_name` varchar(64) NOT NULL DEFAULT '',
  `comment` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `mimetype` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `transformation` varchar(255) NOT NULL DEFAULT '',
  `transformation_options` varchar(255) NOT NULL DEFAULT '',
  `input_transformation` varchar(255) NOT NULL DEFAULT '',
  `input_transformation_options` varchar(255) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Column information for phpMyAdmin';

-- --------------------------------------------------------

--
-- Table structure for table `pma__designer_settings`
--

CREATE TABLE `pma__designer_settings` (
  `username` varchar(64) NOT NULL,
  `settings_data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Settings related to Designer';

--
-- Dumping data for table `pma__designer_settings`
--

INSERT INTO `pma__designer_settings` (`username`, `settings_data`) VALUES
('root', '{\"angular_direct\":\"direct\",\"relation_lines\":\"true\",\"snap_to_grid\":\"off\"}');

-- --------------------------------------------------------

--
-- Table structure for table `pma__export_templates`
--

CREATE TABLE `pma__export_templates` (
  `id` int(5) UNSIGNED NOT NULL,
  `username` varchar(64) NOT NULL,
  `export_type` varchar(10) NOT NULL,
  `template_name` varchar(64) NOT NULL,
  `template_data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Saved export templates';

-- --------------------------------------------------------

--
-- Table structure for table `pma__favorite`
--

CREATE TABLE `pma__favorite` (
  `username` varchar(64) NOT NULL,
  `tables` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Favorite tables';

-- --------------------------------------------------------

--
-- Table structure for table `pma__history`
--

CREATE TABLE `pma__history` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `username` varchar(64) NOT NULL DEFAULT '',
  `db` varchar(64) NOT NULL DEFAULT '',
  `table` varchar(64) NOT NULL DEFAULT '',
  `timevalue` timestamp NOT NULL DEFAULT current_timestamp(),
  `sqlquery` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='SQL history for phpMyAdmin';

-- --------------------------------------------------------

--
-- Table structure for table `pma__navigationhiding`
--

CREATE TABLE `pma__navigationhiding` (
  `username` varchar(64) NOT NULL,
  `item_name` varchar(64) NOT NULL,
  `item_type` varchar(64) NOT NULL,
  `db_name` varchar(64) NOT NULL,
  `table_name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Hidden items of navigation tree';

-- --------------------------------------------------------

--
-- Table structure for table `pma__pdf_pages`
--

CREATE TABLE `pma__pdf_pages` (
  `db_name` varchar(64) NOT NULL DEFAULT '',
  `page_nr` int(10) UNSIGNED NOT NULL,
  `page_descr` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='PDF relation pages for phpMyAdmin';

-- --------------------------------------------------------

--
-- Table structure for table `pma__recent`
--

CREATE TABLE `pma__recent` (
  `username` varchar(64) NOT NULL,
  `tables` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Recently accessed tables';

--
-- Dumping data for table `pma__recent`
--

INSERT INTO `pma__recent` (`username`, `tables`) VALUES
('root', '[{\"db\":\"db_gudang\",\"table\":\"tb_admin\"},{\"db\":\"db_bnn\",\"table\":\"tb_petugas\"},{\"db\":\"db_gudang\",\"table\":\"tb_laporan_inventaris\"},{\"db\":\"db_gudang\",\"table\":\"tb_notifikasi\"},{\"db\":\"db_js\",\"table\":\"jobs\"},{\"db\":\"db_js\",\"table\":\"applications\"},{\"db\":\"db_js\",\"table\":\"users\"},{\"db\":\"dbmahasiswa\",\"table\":\"emp\"}]');

-- --------------------------------------------------------

--
-- Table structure for table `pma__relation`
--

CREATE TABLE `pma__relation` (
  `master_db` varchar(64) NOT NULL DEFAULT '',
  `master_table` varchar(64) NOT NULL DEFAULT '',
  `master_field` varchar(64) NOT NULL DEFAULT '',
  `foreign_db` varchar(64) NOT NULL DEFAULT '',
  `foreign_table` varchar(64) NOT NULL DEFAULT '',
  `foreign_field` varchar(64) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Relation table';

-- --------------------------------------------------------

--
-- Table structure for table `pma__savedsearches`
--

CREATE TABLE `pma__savedsearches` (
  `id` int(5) UNSIGNED NOT NULL,
  `username` varchar(64) NOT NULL DEFAULT '',
  `db_name` varchar(64) NOT NULL DEFAULT '',
  `search_name` varchar(64) NOT NULL DEFAULT '',
  `search_data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Saved searches';

-- --------------------------------------------------------

--
-- Table structure for table `pma__table_coords`
--

CREATE TABLE `pma__table_coords` (
  `db_name` varchar(64) NOT NULL DEFAULT '',
  `table_name` varchar(64) NOT NULL DEFAULT '',
  `pdf_page_number` int(11) NOT NULL DEFAULT 0,
  `x` float UNSIGNED NOT NULL DEFAULT 0,
  `y` float UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Table coordinates for phpMyAdmin PDF output';

-- --------------------------------------------------------

--
-- Table structure for table `pma__table_info`
--

CREATE TABLE `pma__table_info` (
  `db_name` varchar(64) NOT NULL DEFAULT '',
  `table_name` varchar(64) NOT NULL DEFAULT '',
  `display_field` varchar(64) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Table information for phpMyAdmin';

-- --------------------------------------------------------

--
-- Table structure for table `pma__table_uiprefs`
--

CREATE TABLE `pma__table_uiprefs` (
  `username` varchar(64) NOT NULL,
  `db_name` varchar(64) NOT NULL,
  `table_name` varchar(64) NOT NULL,
  `prefs` text NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Tables'' UI preferences';

-- --------------------------------------------------------

--
-- Table structure for table `pma__tracking`
--

CREATE TABLE `pma__tracking` (
  `db_name` varchar(64) NOT NULL,
  `table_name` varchar(64) NOT NULL,
  `version` int(10) UNSIGNED NOT NULL,
  `date_created` datetime NOT NULL,
  `date_updated` datetime NOT NULL,
  `schema_snapshot` text NOT NULL,
  `schema_sql` text DEFAULT NULL,
  `data_sql` longtext DEFAULT NULL,
  `tracking` set('UPDATE','REPLACE','INSERT','DELETE','TRUNCATE','CREATE DATABASE','ALTER DATABASE','DROP DATABASE','CREATE TABLE','ALTER TABLE','RENAME TABLE','DROP TABLE','CREATE INDEX','DROP INDEX','CREATE VIEW','ALTER VIEW','DROP VIEW') DEFAULT NULL,
  `tracking_active` int(1) UNSIGNED NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Database changes tracking for phpMyAdmin';

-- --------------------------------------------------------

--
-- Table structure for table `pma__userconfig`
--

CREATE TABLE `pma__userconfig` (
  `username` varchar(64) NOT NULL,
  `timevalue` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `config_data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='User preferences storage for phpMyAdmin';

--
-- Dumping data for table `pma__userconfig`
--

INSERT INTO `pma__userconfig` (`username`, `timevalue`, `config_data`) VALUES
('root', '2024-12-04 14:30:53', '{\"Console\\/Mode\":\"collapse\"}');

-- --------------------------------------------------------

--
-- Table structure for table `pma__usergroups`
--

CREATE TABLE `pma__usergroups` (
  `usergroup` varchar(64) NOT NULL,
  `tab` varchar(64) NOT NULL,
  `allowed` enum('Y','N') NOT NULL DEFAULT 'N'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='User groups with configured menu items';

-- --------------------------------------------------------

--
-- Table structure for table `pma__users`
--

CREATE TABLE `pma__users` (
  `username` varchar(64) NOT NULL,
  `usergroup` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Users and their assignments to user groups';

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pma__bookmark`
--
ALTER TABLE `pma__bookmark`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pma__central_columns`
--
ALTER TABLE `pma__central_columns`
  ADD PRIMARY KEY (`db_name`,`col_name`);

--
-- Indexes for table `pma__column_info`
--
ALTER TABLE `pma__column_info`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `db_name` (`db_name`,`table_name`,`column_name`);

--
-- Indexes for table `pma__designer_settings`
--
ALTER TABLE `pma__designer_settings`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `pma__export_templates`
--
ALTER TABLE `pma__export_templates`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `u_user_type_template` (`username`,`export_type`,`template_name`);

--
-- Indexes for table `pma__favorite`
--
ALTER TABLE `pma__favorite`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `pma__history`
--
ALTER TABLE `pma__history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `username` (`username`,`db`,`table`,`timevalue`);

--
-- Indexes for table `pma__navigationhiding`
--
ALTER TABLE `pma__navigationhiding`
  ADD PRIMARY KEY (`username`,`item_name`,`item_type`,`db_name`,`table_name`);

--
-- Indexes for table `pma__pdf_pages`
--
ALTER TABLE `pma__pdf_pages`
  ADD PRIMARY KEY (`page_nr`),
  ADD KEY `db_name` (`db_name`);

--
-- Indexes for table `pma__recent`
--
ALTER TABLE `pma__recent`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `pma__relation`
--
ALTER TABLE `pma__relation`
  ADD PRIMARY KEY (`master_db`,`master_table`,`master_field`),
  ADD KEY `foreign_field` (`foreign_db`,`foreign_table`);

--
-- Indexes for table `pma__savedsearches`
--
ALTER TABLE `pma__savedsearches`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `u_savedsearches_username_dbname` (`username`,`db_name`,`search_name`);

--
-- Indexes for table `pma__table_coords`
--
ALTER TABLE `pma__table_coords`
  ADD PRIMARY KEY (`db_name`,`table_name`,`pdf_page_number`);

--
-- Indexes for table `pma__table_info`
--
ALTER TABLE `pma__table_info`
  ADD PRIMARY KEY (`db_name`,`table_name`);

--
-- Indexes for table `pma__table_uiprefs`
--
ALTER TABLE `pma__table_uiprefs`
  ADD PRIMARY KEY (`username`,`db_name`,`table_name`);

--
-- Indexes for table `pma__tracking`
--
ALTER TABLE `pma__tracking`
  ADD PRIMARY KEY (`db_name`,`table_name`,`version`);

--
-- Indexes for table `pma__userconfig`
--
ALTER TABLE `pma__userconfig`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `pma__usergroups`
--
ALTER TABLE `pma__usergroups`
  ADD PRIMARY KEY (`usergroup`,`tab`,`allowed`);

--
-- Indexes for table `pma__users`
--
ALTER TABLE `pma__users`
  ADD PRIMARY KEY (`username`,`usergroup`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pma__bookmark`
--
ALTER TABLE `pma__bookmark`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pma__column_info`
--
ALTER TABLE `pma__column_info`
  MODIFY `id` int(5) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pma__export_templates`
--
ALTER TABLE `pma__export_templates`
  MODIFY `id` int(5) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pma__history`
--
ALTER TABLE `pma__history`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pma__pdf_pages`
--
ALTER TABLE `pma__pdf_pages`
  MODIFY `page_nr` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pma__savedsearches`
--
ALTER TABLE `pma__savedsearches`
  MODIFY `id` int(5) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- Database: `test`
--
CREATE DATABASE IF NOT EXISTS `test` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `test`;
--
-- Database: `tugas3`
--
CREATE DATABASE IF NOT EXISTS `tugas3` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `tugas3`;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
