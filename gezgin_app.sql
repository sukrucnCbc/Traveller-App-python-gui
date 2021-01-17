-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 08 Tem 2020, 23:04:28
-- Sunucu sürümü: 10.4.11-MariaDB
-- PHP Sürümü: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `test`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `acente_kullanici`
--

CREATE TABLE `acente_kullanici` (
  `kullanici_adi` varchar(8) COLLATE utf8_turkish_ci NOT NULL,
  `sifre` varchar(8) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullanicilar`
--

CREATE TABLE `kullanicilar` (
  `kullanici_ID` int(11) NOT NULL,
  `ad_soyad` varchar(55) COLLATE utf8_turkish_ci NOT NULL,
  `e_posta` varchar(55) COLLATE utf8_turkish_ci NOT NULL,
  `tel_no` varchar(12) COLLATE utf8_turkish_ci NOT NULL,
  `sifre` varchar(10) COLLATE utf8_turkish_ci NOT NULL,
  `sifre_tekrar` varchar(10) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kullanicilar`
--

INSERT INTO `kullanicilar` (`kullanici_ID`, `ad_soyad`, `e_posta`, `tel_no`, `sifre`, `sifre_tekrar`) VALUES
(4, 'Şükrücan Cebeci', 'sukrucan@gmail.com', '5061510717', '123456', '123456'),
(7, 'Emirhan', 'emirhan@gmail.com', '5525258005', '123456', '123456'),
(10, 'Doğukan Ergin', 'dogi@gmali.com', '5064565465', 'dofi123', 'dogi123'),
(12, 'Kaan ', 'Erbakan', '50000000', '123456', '123456'),
(13, '', '', '', '', '');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `odemeler`
--

CREATE TABLE `odemeler` (
  `id` int(255) NOT NULL,
  `ad_soyad` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `e_posta` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `tel_no` varchar(12) COLLATE utf8_turkish_ci NOT NULL,
  `kart_no` varchar(16) COLLATE utf8_turkish_ci NOT NULL,
  `skt` varchar(5) COLLATE utf8_turkish_ci NOT NULL,
  `cvv` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `odemeler`
--

INSERT INTO `odemeler` (`id`, `ad_soyad`, `e_posta`, `tel_no`, `kart_no`, `skt`, `cvv`) VALUES
(1, 'emirhan cebeci', 'emirhan@gmail.com', '5525258005', '1471808116710686', '278', 10),
(2, 'ASD', 'ASD', '54646546', '654654654654', '255', 20),
(3, 'ASD', 'ASD', '54646546', '654654654654', '255', 20),
(4, '', '', '', '', '', 0),
(5, '', '', '', '', '', 0),
(6, '', '', '', '', '', 0);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `seferler`
--

CREATE TABLE `seferler` (
  `sefer_kodu` int(8) NOT NULL,
  `firma_adi` varchar(55) COLLATE utf8_turkish_ci NOT NULL,
  `kalkis_ist` varchar(55) COLLATE utf8_turkish_ci NOT NULL,
  `varis_ist` varchar(55) COLLATE utf8_turkish_ci NOT NULL,
  `sefer_tarihi` varchar(9) COLLATE utf8_turkish_ci DEFAULT NULL,
  `saat` time NOT NULL,
  `fiyat` int(3) NOT NULL,
  `arac_plaka` varchar(9) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `seferler`
--

INSERT INTO `seferler` (`sefer_kodu`, `firma_adi`, `kalkis_ist`, `varis_ist`, `sefer_tarihi`, `saat`, `fiyat`, `arac_plaka`) VALUES
(123, 'METRO TURİZM', 'TRABZON', 'İSTANBUL', '12.08.202', '00:00:00', 200, '61AA061'),
(123, 'METRO TURİZM', 'TRABZON', 'İSTANBUL', '12/08/202', '00:00:00', 200, '61AA061'),
(789, 'Nilüfer', 'Trabzon', 'Kocaeli', '05.08.202', '00:00:18', 190, '61AB054'),
(789, 'Nilüfer', 'Trabzon', 'Kocaeli', '05/08/202', '18:20:00', 190, '61AB054'),
(753, 'Fındıkkale', 'Trabzon', 'Kocaeli', '12.10.202', '18:00:00', 160, '61AB055'),
(753, 'Fındıkkale', 'Trabzon', 'Kocaeli', '12.10.202', '18:00:00', 160, '61AB055'),
(951, 'Mis Amasya Tur', 'SAMSUN', 'RİZE', '5', '21:00:00', 80, '55 AB053'),
(564321, 'MİS AMASYA TUR', 'Trabzo', '', NULL, '00:00:00', 0, ''),
(44554, 'Ali Osman Ulusoy', 'İSTANBUL', 'TRABZON', '3', '00:00:15', 180, '34sa061'),
(0, 'Firma Seç', 'Şehir Seç', 'Şehir Seç', 'Gün', '00:00:00', 0, ''),
(2590, 'Nilüfer', 'Trabzon', 'Kocaeli', '05/08/202', '20:00:00', 180, '41KT610'),
(2591, 'Nilüfer', 'Trabzon', 'Kocaeli', '05/08/202', '21:00:00', 180, '41KT400'),
(2590, 'Nilüfer', 'Trabzon', 'Kocaeli', '05/08/202', '20:00:00', 180, '41KT610'),
(2591, 'Nilüfer', 'Trabzon', 'Kocaeli', '05/08/202', '21:00:00', 180, '41KT400'),
(4061, 'Ali Osman Ulusoy', 'İzmir', 'Ankara', '05/08/202', '02:00:00', 180, '06İA35'),
(4006, 'Ali Osman Ulusoy', 'İzmir', 'Ankara', '05/08/202', '05:00:00', 180, '06KT852'),
(4061, 'Ali Osman Ulusoy', 'İzmir', 'Ankara', '05/08/202', '02:00:00', 180, '06İA35'),
(4006, 'Ali Osman Ulusoy', 'İzmir', 'Ankara', '05/08/202', '05:00:00', 180, '06KT852'),
(5050, 'Fındıkkale', 'Trabzon', 'Kocaeli', '12/10/202', '15:00:00', 190, '53TR950'),
(6060, 'Fındıkkale', 'Trabzon', 'Kocaeli', '12/10/202', '22:00:00', 150, '55TR450'),
(5050, 'Fındıkkale', 'Trabzon', 'Kocaeli', '12/10/202', '15:00:00', 190, '53TR950'),
(6060, 'Fındıkkale', 'Trabzon', 'Kocaeli', '12/10/202', '22:00:00', 150, '55TR450'),
(125, 'METRO TURİZM', 'Trabzon', 'İstanbul', '12/08/202', '05:05:00', 150, '34TRÜ330'),
(126, 'METRO TURİZM', 'Trabzon', 'İstanbul', '18/08/202', '00:00:07', 190, '61VK580'),
(125, 'METRO TURİZM', 'Trabzon', 'İstanbul', '12/08/202', '05:05:00', 150, '34TRU330'),
(126, 'METRO TURİZM', 'Trabzon', 'İstanbul', '12/08/202', '00:00:07', 190, '61VK580'),
(9500, 'Mis Amasya Tur', 'Samsun', 'Rize', '5', '22:00:00', 150, '55SS150'),
(9600, 'Mis Amasya Tur', 'Samsun', 'Rize', '5', '23:00:00', 160, '55SM998'),
(9500, 'Mis Amasya Tur', 'Samsun', 'Rize', '5', '22:00:00', 150, '55SS150'),
(9600, 'Mis Amasya Tur', 'Samsun', 'Rize', '5', '23:00:00', 160, '55SM998');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `kullanicilar`
--
ALTER TABLE `kullanicilar`
  ADD PRIMARY KEY (`kullanici_ID`);

--
-- Tablo için indeksler `odemeler`
--
ALTER TABLE `odemeler`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `kullanicilar`
--
ALTER TABLE `kullanicilar`
  MODIFY `kullanici_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Tablo için AUTO_INCREMENT değeri `odemeler`
--
ALTER TABLE `odemeler`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
