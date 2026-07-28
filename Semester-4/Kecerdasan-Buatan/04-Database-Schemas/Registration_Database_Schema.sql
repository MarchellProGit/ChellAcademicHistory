-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 25 Nov 2024 pada 02.44
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

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
-- Struktur dari tabel `tbpendaftaran`
--

CREATE TABLE `tbpendaftaran` (
  `id_pendaftaran` int(11) NOT NULL,
  `id_pekerjaan` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `status` varchar(20) NOT NULL,
  `tanggal_daftar` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tbpendaftaran`
--

INSERT INTO `tbpendaftaran` (`id_pendaftaran`, `id_pekerjaan`, `nama`, `email`, `status`, `tanggal_daftar`) VALUES
(14, 672023222, 'marchell', 'marchell@email.com', 'pendaftar', '2024-11-25 01:46:40'),
(15, 672023268, 'puja', 'puja@gmail.com', 'pendaftar', '2024-11-25 01:48:06'),
(16, 1, 'dani', 'dani@gmail.com', 'pendaftar', '2024-11-25 01:55:46'),
(17, 1, 'dani', 'dani@gmail.com', 'pendaftar', '2024-11-25 01:56:08'),
(18, 672023256, 'jo', 'jo@gmail.com', 'pendaftar', '2024-11-25 08:18:38'),
(19, 12, 'eee', 'eee@gmail.com', 'pendaftar', '2024-11-25 08:20:26'),
(20, 12, 'eee', 'eee@gmail.com', 'pendaftar', '2024-11-25 08:22:10');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `tbpendaftaran`
--
ALTER TABLE `tbpendaftaran`
  ADD PRIMARY KEY (`id_pendaftaran`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `tbpendaftaran`
--
ALTER TABLE `tbpendaftaran`
  MODIFY `id_pendaftaran` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
