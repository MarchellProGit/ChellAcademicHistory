-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 23, 2024 at 04:19 PM
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
-- Database: `db_jobseeker`
--

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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
