-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: mysqldb:3306
-- Waktu pembuatan: 01 Jun 2023 pada 11.27
-- Versi server: 8.0.33
-- Versi PHP: 8.0.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `capstone_db`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `HISTORY`
--

CREATE TABLE `HISTORY` (
  `ID_HISTORY` varchar(64) NOT NULL,
  `USERNAME` varchar(100) DEFAULT NULL,
  `ID_INPUT` varchar(64) DEFAULT NULL,
  `ID_RESULT` varchar(64) DEFAULT NULL,
  `DATE` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `HISTORY`
--

INSERT INTO `HISTORY` (`ID_HISTORY`, `USERNAME`, `ID_INPUT`, `ID_RESULT`, `DATE`) VALUES
('HKJ876YUII', 'thoriq666', 'RE5TY76UHJ', 'Y765HGB809', '2023-05-26');

-- --------------------------------------------------------

--
-- Struktur dari tabel `INFORMATION`
--

CREATE TABLE `INFORMATION` (
  `ID_INFO` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `TANAMAN` varchar(100) NOT NULL,
  `PENYAKIT` varchar(200) NOT NULL,
  `DESKRIPSI` text NOT NULL,
  `SOLUSI` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `INFORMATION`
--

INSERT INTO `INFORMATION` (`ID_INFO`, `TANAMAN`, `PENYAKIT`, `DESKRIPSI`, `SOLUSI`) VALUES
('O89YUGHY98', 'chili', 'leaf_spot', 'Bercak daun atau biasa disebut dengan Frog Eyes. Penyebab penyakit ini adalah Cercospora capsici sejenis cendawan atau Jamur antagonis perusak tanaman. Penyakit bercak daun cabai adalah salah satu penyakit terpenting yang menyerang cabai di Indonesia. Penyakit ini distimulir oleh kondisi lembab dan suhu relatif tinggi. Penyakit bercak daun cabai dapat menyebabkan kerusakan sejak dari persemaian sampai tanaman cabai berbuah. Penyakit ini menyebabkan masalah serius terhadap perkembangan tanaman cabai. Serangan jamur ini berkembang pesat pada saat musim hujan dengan kondisi lahan yang lembab, sehingga perlu adanya pengaturan jarak tanam yang lebih lebar untuk mengatur kelembabannya.\r\n', 'Pengendalian secara mekanis dilakukan dengan mencabut atau memusnahkan tanaman yang terserang, melakukan rotasi tanaman, serta menanam bibit yang bebas penyakit pada lahan yang tidak terkontaminasi penyakit. Selain itu lakukan pula sanitasi kebun, penyiangan atau pembersihan gulma di sekitar tanaman untuk mengurangi kelembaban di areal sekitar penanaman. Keberadaan gulma ini juga bisa menjadi tanaman inang bagi hama penyakit. Sedangkan pengendalian secara kimiawi adalah pengendalian dengan menggunakan zat kimia. Karena penyakit bercak daun cabai ini disebabkan oleh jamur atau cendawan, maka pengendaliannya dapat dilakukan dengan menyemprotkan fungisida. Fungisida yang digunakan adalah fungisida sistemik dengan bahan aktif azoksistrobin dan difenokonazol. Adapun dosisnya adalah 10 ml per 16 liter air atau sesuaikan saja dengan dosis yang tertera pada label kemasan. Cara aplikasinya adalah dengan menyemprotkannya pada seluruh bagian tanaman baik itu tanaman yang sudah terinfeksi ataupun tanaman sehat.\r\n'),
('UI876HJE5T', 'chili', 'leaf curl', 'Penyakit keriting daun merupakan penyakit virus yang menyerang tanaman cabai. Penyakit ini disebabkan oleh virus keriting daun cabai (ChiLCV), yang merupakan anggota dari keluarga Geminiviridae. ChiLCV ditularkan oleh lalat putih, yaitu serangga kecil yang memakan getah tanaman.Gejala penyakit daun keriting antara lain: Daun melengkung ke atas, Kerutan daun, Menguningnya daun, Ukuran daun mengecil, Pemendekan ruas, Pertumbuhan terhambat, Mengurangi produksi buah\r\n', 'Tidak ada obat untuk penyakit keriting daun. Namun, ada sejumlah tindakan pencegahan yang dapat dilakukan untuk mengurangi risiko infeksi, seperti: Menggunakan varietas tanaman cabai yang kebal hama, Menanam tanaman cabe di daerah yang tidak ada lalat putih, Menggunakan sabun atau minyak insektisida untuk mengendalikan lalat putih, Membuang tanaman yang terinfeksi dari kebun, Jika Anda mencurigai bahwa tanaman cabai Anda memiliki penyakit keriting daun, anda dapat menghubungi kantor penyuluh pertanian setempat untuk informasi lebih lanjut tentang cara mengelola penyakit tersebut.\r\n'),
('Y79UJ600IO', 'chili', 'healthy', 'Tanaman Cabai Sehat', '-');

-- --------------------------------------------------------

--
-- Struktur dari tabel `INPUT`
--

CREATE TABLE `INPUT` (
  `ID_INPUT` varchar(64) NOT NULL,
  `ID_HISTORY` varchar(64) DEFAULT NULL,
  `FILENAME` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `INPUT`
--

INSERT INTO `INPUT` (`ID_INPUT`, `ID_HISTORY`, `FILENAME`) VALUES
('RE5TY76UHJ', 'HKJ876YUII', 'gambar.png');

-- --------------------------------------------------------

--
-- Struktur dari tabel `RESULT`
--

CREATE TABLE `RESULT` (
  `ID_RESULT` varchar(64) NOT NULL,
  `ID_HISTORY` varchar(64) DEFAULT NULL,
  `ID_INFO` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `RESULT`
--

INSERT INTO `RESULT` (`ID_RESULT`, `ID_HISTORY`, `ID_INFO`) VALUES
('Y765HGB809', 'HKJ876YUII', 'UI876HJE5T');

-- --------------------------------------------------------

--
-- Struktur dari tabel `USER`
--

CREATE TABLE `USER` (
  `USERNAME` varchar(100) NOT NULL,
  `NAME` varchar(128) NOT NULL,
  `PASSWORD` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `USER`
--

INSERT INTO `USER` (`USERNAME`, `NAME`, `PASSWORD`) VALUES
('thoriq123456', 'ThoriqLigarHaidar123', '$5$rounds=535000$NzQDlzh1wSo0dXmT$basuUFM9KcANEpibMK1aBrCHDG0jjTAkDZRC.z.ccy5'),
('thoriq666', 'ThoriqLigarHaidar', '$5$rounds=535000$MIAcZRvN8ccziS0j$g2wvh3tfZE9bWH5NvYN36NZSLeLqiDAueql8mdgHRz6'),
('thoriqhaidar3', 'ThoriqLigarHaidar', '12345678'),
('thoriqhdar3', 'ThoriqLigarHaidar', '12345678'),
('thoriqhidar3', 'Thoriq Ligar Haidar', '12345678');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `HISTORY`
--
ALTER TABLE `HISTORY`
  ADD PRIMARY KEY (`ID_HISTORY`),
  ADD KEY `FK_RELATIONSHIP_1` (`USERNAME`),
  ADD KEY `FK_RELATIONSHIP_4` (`ID_INPUT`),
  ADD KEY `FK_RELATIONSHIP_5` (`ID_RESULT`);

--
-- Indeks untuk tabel `INFORMATION`
--
ALTER TABLE `INFORMATION`
  ADD PRIMARY KEY (`ID_INFO`);

--
-- Indeks untuk tabel `INPUT`
--
ALTER TABLE `INPUT`
  ADD PRIMARY KEY (`ID_INPUT`),
  ADD KEY `FK_RELATIONSHIP_2` (`ID_HISTORY`);

--
-- Indeks untuk tabel `RESULT`
--
ALTER TABLE `RESULT`
  ADD PRIMARY KEY (`ID_RESULT`),
  ADD KEY `FK_RELATIONSHIP_3` (`ID_HISTORY`),
  ADD KEY `ID_INFO` (`ID_INFO`);

--
-- Indeks untuk tabel `USER`
--
ALTER TABLE `USER`
  ADD PRIMARY KEY (`USERNAME`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `HISTORY`
--
ALTER TABLE `HISTORY`
  ADD CONSTRAINT `FK_RELATIONSHIP_1` FOREIGN KEY (`USERNAME`) REFERENCES `USER` (`USERNAME`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `FK_RELATIONSHIP_4` FOREIGN KEY (`ID_INPUT`) REFERENCES `INPUT` (`ID_INPUT`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `FK_RELATIONSHIP_5` FOREIGN KEY (`ID_RESULT`) REFERENCES `RESULT` (`ID_RESULT`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ketidakleluasaan untuk tabel `INPUT`
--
ALTER TABLE `INPUT`
  ADD CONSTRAINT `FK_RELATIONSHIP_2` FOREIGN KEY (`ID_HISTORY`) REFERENCES `HISTORY` (`ID_HISTORY`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Ketidakleluasaan untuk tabel `RESULT`
--
ALTER TABLE `RESULT`
  ADD CONSTRAINT `FK_RELATIONSHIP_3` FOREIGN KEY (`ID_HISTORY`) REFERENCES `HISTORY` (`ID_HISTORY`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
