-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 16, 2021 at 05:57 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `luanvantotnghiep`
--

-- --------------------------------------------------------

--
-- Table structure for table `binh_luan`
--

CREATE TABLE `binh_luan` (
  `BL_MA` int(11) NOT NULL,
  `ND_MA` int(11) NOT NULL,
  `TP_MA` int(11) NOT NULL,
  `BL_THOI_GIAN` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `BL_NOI_DUNG` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `binh_luan`
--

INSERT INTO `binh_luan` (`BL_MA`, `ND_MA`, `TP_MA`, `BL_THOI_GIAN`, `BL_NOI_DUNG`) VALUES
(1, 3, 1, '2021-11-16', 'Boom hang!');

-- --------------------------------------------------------

--
-- Table structure for table `chi_tiet_dang_ky_mua`
--

CREATE TABLE `chi_tiet_dang_ky_mua` (
  `TP_MA` int(11) NOT NULL,
  `DKM_MA` int(11) NOT NULL,
  `CTDKM_SO_LUONG` float DEFAULT NULL,
  `CTDKM_GHI_CHU` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `CTDKM_TRANG_THAI` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `chi_tiet_dang_ky_mua`
--

INSERT INTO `chi_tiet_dang_ky_mua` (`TP_MA`, `DKM_MA`, `CTDKM_SO_LUONG`, `CTDKM_GHI_CHU`, `CTDKM_TRANG_THAI`) VALUES
(1, 2, 30, '16', 1),
(1, 4, 0, '14', 2),
(2, 5, 3, '3 mua le', 1);

-- --------------------------------------------------------

--
-- Table structure for table `chi_tiet_nhu_cau_mua`
--

CREATE TABLE `chi_tiet_nhu_cau_mua` (
  `DMTP_MA` int(11) NOT NULL,
  `NCM_MA` int(11) NOT NULL,
  `DMDVT_MA` int(11) NOT NULL,
  `CTNCM_SO_LUONG` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dang_ky_mua`
--

CREATE TABLE `dang_ky_mua` (
  `DKM_MA` int(11) NOT NULL,
  `ND_MA` int(11) DEFAULT NULL,
  `DKM_THOI_GIAN` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `DKM_VI_TRI_BAN_DO` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `DKM_DIA_CHI` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `dang_ky_mua`
--

INSERT INTO `dang_ky_mua` (`DKM_MA`, `ND_MA`, `DKM_THOI_GIAN`, `DKM_VI_TRI_BAN_DO`, `DKM_DIA_CHI`) VALUES
(2, 3, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam'),
(4, 6, '2021-11-16', '10.0330904|105.788655', 'Công Viên Bến Ninh Kiều, 38 Đường Hai Bà Trưng, Tân An, Ninh Kiều, Cần Thơ, Việt Nam'),
(5, 3, '2021-11-16', '10.0349302|105.7536628', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam');

-- --------------------------------------------------------

--
-- Table structure for table `danh_muc_don_vi_tinh`
--

CREATE TABLE `danh_muc_don_vi_tinh` (
  `DMDVT_MA` int(11) NOT NULL,
  `DMDVT_TEN` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `danh_muc_don_vi_tinh`
--

INSERT INTO `danh_muc_don_vi_tinh` (`DMDVT_MA`, `DMDVT_TEN`) VALUES
(1, 'Kilogram'),
(2, 'Thùng'),
(3, 'Gói');

-- --------------------------------------------------------

--
-- Table structure for table `danh_muc_thuc_pham`
--

CREATE TABLE `danh_muc_thuc_pham` (
  `DMTP_MA` int(11) NOT NULL,
  `DMTP_TEN` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `DMTP_MA_DMTM_CHA` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `danh_muc_thuc_pham`
--

INSERT INTO `danh_muc_thuc_pham` (`DMTP_MA`, `DMTP_TEN`, `DMTP_MA_DMTM_CHA`) VALUES
(1, 'Thịt', NULL),
(2, 'Củ', NULL),
(3, 'Rau', NULL),
(4, 'Trái cây', NULL),
(5, 'Nấm', NULL),
(6, 'Trứng', NULL),
(7, 'Đồ hộp', NULL),
(8, 'Khác', NULL),
(9, 'Thịt heo', 1),
(10, 'Thịt bò', 1),
(11, 'Cà rốt', 2),
(12, 'Khoai lang', 2),
(13, 'Rau muống', 3),
(14, 'Bắp cải', 3),
(15, 'Cà chua', 4),
(16, 'Bí đỏ', 4),
(17, 'Nấm mèo', 5),
(18, 'Nấm kim châm', 5),
(19, 'Trứng gà', 6),
(20, 'Trứng vịt', 6);

-- --------------------------------------------------------

--
-- Table structure for table `dm_don_vi_tinh_dm_thuc_pham`
--

CREATE TABLE `dm_don_vi_tinh_dm_thuc_pham` (
  `DMTP_MA` int(11) NOT NULL,
  `DMDVT_MA` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `dm_don_vi_tinh_dm_thuc_pham`
--

INSERT INTO `dm_don_vi_tinh_dm_thuc_pham` (`DMTP_MA`, `DMDVT_MA`) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(12, 1),
(13, 1),
(14, 1),
(15, 1),
(16, 1),
(17, 1),
(18, 1),
(19, 1),
(20, 1);

-- --------------------------------------------------------

--
-- Table structure for table `nguoi_dung`
--

CREATE TABLE `nguoi_dung` (
  `ND_MA` int(11) NOT NULL,
  `ND_HO_TEN` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ND_DIA_CHI` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ND_SO_DIEN_THOAI` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ND_EMAIL` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ND_MAT_KHAU` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ND_TAI_KHOAN` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `nguoi_dung`
--

INSERT INTO `nguoi_dung` (`ND_MA`, `ND_HO_TEN`, `ND_DIA_CHI`, `ND_SO_DIEN_THOAI`, `ND_EMAIL`, `ND_MAT_KHAU`, `ND_TAI_KHOAN`) VALUES
(1, 'Nguyễn Đức Trọng', 'Vĩnh Long', '078693635', 'trongb1709576@student.ctu.edu.vn', 'trong', 'trong'),
(2, 'Lý Thanh Tân', 'An Giang', '0123456789', 'tan@gmail.com.vn', 'tan', 'tan'),
(3, 'Đoàn Dự', 'Vĩnh Long', '0987654321', 'doandu@gmail.com.vn', 'doandu', 'doandu'),
(4, 'Nguyễn Đức Minh', 'Vĩnh Long', '078693635', 'nguyenducminh@gmail.com.vn', '123', 'nguyenducminh'),
(5, 'Lý Thanh Hải', 'An Giang', '0123456789', 'lythanhhai@gmail.com.vn', '123', 'lythanhhai'),
(6, 'Đoàn Chính Thuần', 'Vĩnh Long', '0987654321', 'doanchinhthuan@gmail.com.vn', '123', 'doanchinhthuan');

-- --------------------------------------------------------

--
-- Table structure for table `nhu_cau_mua`
--

CREATE TABLE `nhu_cau_mua` (
  `NCM_MA` int(11) NOT NULL,
  `ND_MA` int(11) NOT NULL,
  `NCM_THOI_GIAN` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `NCM_DIA_CHI` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `NCM_VI_TRI_BAN_DO` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `thuc_pham`
--

CREATE TABLE `thuc_pham` (
  `TP_MA` int(11) NOT NULL,
  `DMDVT_MA` int(11) NOT NULL,
  `ND_MA` int(11) NOT NULL,
  `DMTP_MA` int(11) NOT NULL,
  `TP_TEN` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `TP_MO_TA` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `TP_HINH_ANH` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `TP_DON_GIA` int(11) DEFAULT NULL,
  `TP_SO_LUONG` float DEFAULT NULL,
  `TP_NGAY_BAN` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `TP_VI_TRI_BAN_DO` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `TP_DIA_CHI` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `TP_SUAT_BAN` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `thuc_pham`
--

INSERT INTO `thuc_pham` (`TP_MA`, `DMDVT_MA`, `ND_MA`, `DMTP_MA`, `TP_TEN`, `TP_MO_TA`, `TP_HINH_ANH`, `TP_DON_GIA`, `TP_SO_LUONG`, `TP_NGAY_BAN`, `TP_VI_TRI_BAN_DO`, `TP_DIA_CHI`, `TP_SUAT_BAN`) VALUES
(1, 1, 1, 9, 'Thịt heo', 'Quaerat porro ut numquam. Sit velit modi ut etincidunt quaerat. Numquam dolore etincidunt etincidunt ut. Voluptatem dolore labore non quiquia. Voluptatem quaerat dolor ut non neque. Dolore porro quisquam etincidunt quisquam labore numquam. Etincidunt quaerat consectetur sed. Tempora tempora amet dolorem ut labore est quisquam. Eius aliquam quiquia etincidunt dolor. Porro tempora sit numquam tempora.\n\nSit sed adipisci non sed. Etincidunt quisquam ut neque quiquia amet quaerat labore. Consectetur ', 'static/images/5c4f5b65-132b-4811-b7b7-b08ce60632be.jpg', 28000, 470, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', 30),
(2, 1, 1, 9, 'Thịt heo', 'Etincidunt magnam eius eius. Modi quiquia etincidunt velit aliquam. Numquam quaerat quiquia etincidunt neque amet. Adipisci magnam ipsum quaerat velit dolor voluptatem. Neque tempora etincidunt quisquam quaerat non magnam labore. Tempora numquam adipisci porro ut quisquam dolore. Dolor numquam sed quaerat ut ut quisquam amet. Sed dolorem porro ut modi ut dolore voluptatem.\n\nVoluptatem sed numquam magnam magnam quaerat non. Labore magnam ut modi. Numquam neque consectetur sed quisquam est etincid', 'static/images/d451e062-bece-45b5-a893-93b5b8ebae0b.jpg', 15000, 20, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(3, 1, 1, 9, 'Thịt heo', 'Voluptatem etincidunt non amet. Dolor modi etincidunt adipisci. Eius labore tempora sed quiquia. Quisquam adipisci non eius ut porro. Sit ipsum labore ut sit eius numquam. Labore quaerat amet quiquia. Quisquam porro neque voluptatem sit. Sed quisquam ipsum sed modi. Etincidunt sit numquam quiquia dolor neque modi est. Consectetur aliquam quaerat numquam.\n\nAliquam labore adipisci sit eius tempora tempora. Dolor ut etincidunt quaerat magnam. Amet consectetur dolorem voluptatem. Etincidunt magnam v', 'static/images/7a64af9d-52ec-4c29-97b5-ea95d7a75ee7.jpg', 21000, 24, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(4, 1, 1, 9, 'Thịt heo', 'Quisquam consectetur quiquia eius velit porro dolore dolorem. Labore amet sed dolor eius consectetur etincidunt. Numquam sed tempora amet non. Ipsum porro sit velit adipisci amet. Dolor dolorem est tempora etincidunt.\n\nModi voluptatem dolore sed. Adipisci est porro est tempora magnam dolorem ut. Voluptatem non est tempora etincidunt labore. Voluptatem numquam consectetur quisquam magnam sed velit etincidunt. Ut est dolorem est non modi aliquam numquam.\n\nModi magnam porro etincidunt numquam porro', 'static/images/b2b1fb3b-c982-448d-bd5d-a8727e68a13b.jpg', 18000, 18, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(5, 1, 1, 10, 'Thịt bò', 'Eius numquam amet aliquam. Porro quiquia quaerat aliquam dolor ipsum est. Numquam non velit adipisci numquam quisquam tempora. Ipsum dolorem ut quaerat. Ipsum dolor ipsum neque quaerat tempora. Aliquam est ipsum adipisci.\n\nEst ut ut quiquia. Aliquam non sit voluptatem modi magnam etincidunt non. Quisquam ut consectetur quiquia dolor neque non. Ut tempora labore numquam quaerat. Quaerat dolor non dolore. Ipsum eius dolor labore.\n\nTempora sed porro numquam non sit. Tempora dolore numquam numquam p', 'static/images/62bd6875-118b-4d4b-8a8b-00300c4d4aba.jpg', 29000, 21, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(6, 1, 1, 10, 'Thịt bò', 'Dolor ut aliquam sit dolorem porro ipsum consectetur. Dolorem amet etincidunt dolore consectetur etincidunt. Sed quaerat amet ipsum ut voluptatem aliquam. Neque sit aliquam magnam numquam. Non modi labore voluptatem consectetur etincidunt. Adipisci ipsum velit amet. Eius ut adipisci est. Amet dolorem consectetur consectetur dolore quaerat numquam porro.\n\nAmet dolor porro tempora aliquam ut neque. Etincidunt sit neque amet non. Ipsum dolorem magnam ipsum voluptatem. Amet amet velit numquam. Adipi', 'static/images/02ae9592-0ec5-41e6-8411-a5a087012017.jpg', 21000, 23, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(7, 1, 1, 10, 'Thịt bò', 'Dolor amet numquam quiquia sit aliquam quiquia. Eius dolor dolor quiquia. Quisquam quisquam dolor labore quaerat amet velit. Non etincidunt est numquam dolor eius. Labore est quiquia dolore ipsum. Consectetur eius amet velit tempora. Est etincidunt quisquam magnam modi eius.\n\nVelit sit labore est quaerat. Aliquam ipsum modi voluptatem consectetur amet modi quisquam. Porro quiquia voluptatem ipsum ut tempora quisquam. Numquam quaerat amet tempora voluptatem. Ipsum amet ut sed. Non aliquam amet si', 'static/images/2b3ee1c6-b8d9-4165-9904-7ce12ae4df81.jpg', 14000, 24, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(8, 1, 1, 10, 'Thịt bò', 'Eius aliquam labore quisquam dolore dolor neque dolor. Quiquia sed porro sed eius. Quisquam etincidunt modi adipisci porro sed ut ipsum. Tempora sit tempora voluptatem quisquam. Dolor quaerat adipisci ipsum. Etincidunt aliquam quisquam quiquia neque.\n\nEtincidunt dolor sit adipisci tempora modi ipsum. Adipisci aliquam dolore aliquam. Ipsum amet magnam etincidunt est quisquam quaerat quiquia. Numquam magnam consectetur voluptatem ut labore dolorem. Consectetur etincidunt numquam quaerat quiquia. T', 'static/images/a53adad2-cde6-4e23-b81a-5fc189d4217b.jpg', 23000, 23, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(9, 1, 1, 15, 'Cà chua', 'Neque dolor dolore numquam quaerat. Amet ipsum quaerat quaerat. Eius ipsum ipsum ipsum tempora neque sed. Quiquia porro etincidunt magnam modi eius. Aliquam labore porro labore magnam quaerat adipisci aliquam.\n\nAmet non modi dolor. Ut voluptatem numquam amet dolore ipsum. Neque dolorem quaerat dolore. Dolore porro sed magnam. Velit quaerat non porro sit dolore.\n\nConsectetur amet adipisci quiquia sit. Velit labore adipisci porro amet labore neque tempora. Ipsum numquam dolor sed velit adipisci ut', 'static/images/ce5e26f9-3145-4adc-a75c-fdf4f7777fdf.jpg', 18000, 19, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(10, 1, 1, 15, 'Cà chua', 'Tempora dolorem etincidunt sit. Ut ut consectetur ipsum dolorem adipisci numquam. Eius quiquia quisquam quiquia voluptatem sit est. Aliquam quiquia adipisci adipisci sit sit est. Voluptatem sit voluptatem sit. Voluptatem amet adipisci aliquam dolore. Sit dolore sit porro.\n\nNeque modi non amet est porro quisquam. Quaerat magnam est voluptatem dolorem non est amet. Dolorem etincidunt tempora velit eius magnam dolorem velit. Ipsum velit modi voluptatem dolor dolor est. Quisquam est adipisci volupta', 'static/images/d788f92b-34c2-408c-bbeb-414b21f2a523.jpg', 17000, 15, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(11, 1, 1, 15, 'Cà chua', 'Quaerat amet eius adipisci. Non ipsum etincidunt labore ut quiquia. Numquam quiquia aliquam etincidunt tempora dolore dolorem. Non quiquia adipisci aliquam est aliquam modi sed. Consectetur aliquam tempora quiquia dolorem aliquam. Sit aliquam est sed tempora quaerat non. Non magnam dolorem amet consectetur voluptatem. Non consectetur est sed aliquam dolore. Dolore sed neque magnam adipisci dolore.\n\nTempora dolorem porro aliquam non porro. Etincidunt amet porro magnam sit. Labore sit labore conse', 'static/images/1ae7f523-35cc-4f9c-82ee-eedbfc727888.jpg', 19000, 15, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(12, 1, 1, 15, 'Cà chua', 'Dolor quisquam etincidunt etincidunt. Etincidunt modi sed numquam. Consectetur eius quaerat velit modi eius modi ut. Eius voluptatem magnam sit ut etincidunt. Ut etincidunt etincidunt non numquam dolorem quiquia etincidunt. Tempora tempora voluptatem consectetur labore. Sit tempora tempora quaerat neque adipisci tempora.\n\nVoluptatem consectetur etincidunt magnam non amet. Labore tempora adipisci porro etincidunt. Amet velit dolor porro quisquam non adipisci dolor. Magnam magnam ut dolore volupta', 'static/images/c72d5639-4471-4a00-aa59-9bc59f7fa3e9.jpg', 25000, 26, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(13, 1, 2, 9, 'Thịt heo', 'Dolor ipsum aliquam labore. Etincidunt eius eius amet est quiquia ipsum etincidunt. Est eius quiquia consectetur est modi dolore ipsum. Porro non magnam etincidunt modi ut tempora. Quiquia porro non dolor labore dolor ipsum porro. Dolor sit neque dolor velit sit.\n\nEtincidunt velit dolore eius. Etincidunt quiquia quiquia dolore sed aliquam dolor. Voluptatem non eius consectetur ut magnam. Velit non dolor sed ipsum. Consectetur dolorem aliquam aliquam. Ipsum ut dolorem porro velit ut est porro. Al', 'static/images/9ddb1b6b-3e39-43da-9f1f-c259b607a783.jpg', 20000, 16, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(14, 1, 2, 9, 'Thịt heo', 'Aliquam etincidunt quisquam adipisci consectetur modi dolore. Amet magnam quisquam ut porro. Est ipsum dolor dolore voluptatem neque. Neque dolorem quaerat numquam dolorem etincidunt aliquam. Amet etincidunt ut aliquam modi magnam labore est. Aliquam eius numquam porro. Ipsum non neque adipisci magnam. Ipsum amet dolore dolor dolore ipsum quiquia quaerat.\n\nAliquam magnam quisquam consectetur quisquam. Neque adipisci modi etincidunt sit voluptatem dolore. Voluptatem dolore sed eius ut numquam. Qu', 'static/images/9da8f8e7-2ebe-40b7-b99a-56be2f390c19.jpg', 12000, 24, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(15, 1, 2, 9, 'Thịt heo', 'Quiquia ut voluptatem voluptatem non voluptatem. Quaerat etincidunt magnam sit. Voluptatem neque dolore adipisci quiquia. Ut velit amet ut non consectetur amet dolorem. Quiquia quisquam est sit sit dolor sed. Ut numquam ut dolorem dolorem non neque neque. Quisquam est labore dolorem aliquam labore. Dolorem magnam dolore velit. Labore dolor magnam ut voluptatem neque etincidunt labore. Eius voluptatem sed labore consectetur quisquam aliquam.\n\nQuiquia porro magnam ipsum labore porro. Dolor non con', 'static/images/315f7794-5f38-47b8-9e57-de91c93c18a0.jpg', 20000, 17, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(16, 1, 2, 9, 'Thịt heo', 'Quaerat dolorem amet sed velit numquam. Magnam modi modi magnam ipsum adipisci numquam quisquam. Ipsum ipsum dolore aliquam tempora velit aliquam. Ut adipisci consectetur est est sed. Labore velit neque aliquam numquam est dolor.\n\nNeque est sit labore modi modi dolor modi. Dolor ut quaerat velit sed numquam adipisci. Numquam eius ut tempora etincidunt quisquam porro dolorem. Est non quaerat dolorem velit numquam modi ut. Labore magnam ipsum aliquam tempora. Labore non etincidunt neque. Modi nequ', 'static/images/00806d0c-a609-40e0-971f-7f23d8591a54.jpg', 25000, 29, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(17, 1, 2, 10, 'Thịt bò', 'Ipsum dolor ipsum ipsum magnam. Aliquam aliquam aliquam consectetur dolor quiquia dolore. Labore quaerat magnam dolore. Ut amet sit ipsum numquam. Sit dolorem non magnam neque consectetur est amet. Dolore quisquam neque consectetur voluptatem sed. Quaerat etincidunt velit dolorem quaerat consectetur dolore.\n\nSed magnam consectetur non. Quisquam modi porro quaerat modi sit magnam. Aliquam adipisci eius quisquam dolore numquam. Quisquam neque est eius quiquia consectetur est quaerat. Dolorem numqu', 'static/images/1b335dfb-9fff-421d-975f-138f7a5ef3fb.jpg', 21000, 18, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(18, 1, 2, 10, 'Thịt bò', 'Modi quisquam quaerat quaerat voluptatem quiquia adipisci eius. Adipisci modi labore quaerat sed quiquia non. Ut voluptatem dolorem eius aliquam sit. Dolorem porro dolorem labore sed dolorem numquam. Sit eius quisquam adipisci est est. Adipisci quiquia tempora neque. Aliquam etincidunt non tempora sed consectetur numquam.\n\nNeque aliquam dolore est adipisci sit est voluptatem. Numquam labore aliquam adipisci neque neque sit. Est tempora etincidunt adipisci ipsum. Magnam quaerat eius quiquia dolor', 'static/images/65c09530-51cf-4b48-ac79-396a53f01d09.jpg', 20000, 22, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(19, 1, 2, 10, 'Thịt bò', 'Ipsum est quisquam aliquam sit. Adipisci dolor quisquam labore amet aliquam sit. Etincidunt tempora neque ut adipisci dolore dolor aliquam. Ut ut velit sit dolor porro ipsum. Consectetur tempora dolor velit.\n\nEst neque quiquia dolore numquam. Eius dolorem consectetur dolorem tempora labore. Voluptatem non modi magnam. Etincidunt adipisci dolore consectetur quaerat voluptatem. Ut porro numquam sit magnam modi ipsum modi.\n\nSit labore sit voluptatem modi etincidunt. Eius est sit porro dolore quisqu', 'static/images/0928b33e-0d74-40e8-8b02-4ccc7bf02743.jpg', 28000, 15, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(20, 1, 2, 10, 'Thịt bò', 'Dolore modi non amet sed est. Tempora non non ut. Adipisci sed neque etincidunt numquam. Dolore quisquam dolorem quisquam dolor quiquia. Modi magnam velit dolore non tempora.\n\nNumquam numquam quisquam dolore. Eius dolor dolor labore. Tempora dolore quiquia dolorem dolorem magnam sit. Quisquam voluptatem tempora sit quaerat dolorem. Magnam dolor quaerat dolore amet dolore dolorem amet. Porro numquam aliquam labore tempora aliquam. Non sit est eius non. Sed adipisci voluptatem sit ipsum. Porro mod', 'static/images/f171c6da-60d2-4f20-8aea-5f3bfde22767.jpg', 18000, 27, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(21, 1, 2, 15, 'Cà chua', 'Labore voluptatem dolorem sed. Labore amet quiquia modi etincidunt. Numquam dolore quiquia est. Quisquam sed ut magnam sed numquam quiquia. Non sit eius labore velit ut tempora consectetur. Labore amet non velit porro amet modi numquam. Non velit ipsum amet quaerat amet amet magnam. Velit ipsum labore magnam velit modi.\n\nMagnam dolore dolorem neque amet modi. Etincidunt ut dolore sit dolore neque. Quaerat ipsum tempora magnam quisquam est etincidunt. Est aliquam aliquam numquam labore labore neq', 'static/images/b0318905-3d31-409d-a5bc-22f16eda4be4.jpg', 24000, 22, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(22, 1, 2, 15, 'Cà chua', 'Dolore magnam non porro neque sit. Dolorem numquam labore magnam dolorem magnam aliquam amet. Porro consectetur dolor etincidunt. Amet sit sed sed. Est dolorem velit quaerat quaerat velit est. Quisquam porro magnam dolore non. Eius adipisci aliquam consectetur neque dolorem quaerat. Sit neque quiquia quaerat aliquam voluptatem ipsum labore. Magnam ut non quisquam dolore eius ipsum. Sed consectetur dolor amet sit ipsum voluptatem eius.\n\nNeque quaerat aliquam consectetur eius aliquam. Quaerat modi', 'static/images/fa1fa00e-d782-4059-b641-c8b413b0171e.jpg', 18000, 25, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(23, 1, 2, 15, 'Cà chua', 'Ipsum sit ut dolore ut. Consectetur quisquam amet ipsum sit porro. Voluptatem eius etincidunt dolore magnam. Etincidunt tempora sed labore labore ipsum. Tempora quaerat dolor adipisci tempora quisquam sit. Neque etincidunt quiquia dolore tempora adipisci quisquam. Porro non ipsum dolore. Dolorem consectetur amet quaerat tempora modi. Voluptatem quiquia quiquia dolore magnam amet dolore voluptatem. Voluptatem quiquia consectetur numquam.\n\nSed quiquia est magnam non. Voluptatem sit ipsum adipisci ', 'static/images/d36cc1b8-ebd9-4940-93f9-f59f11b3280a.jpg', 23000, 23, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(24, 1, 2, 15, 'Cà chua', 'Sed tempora quisquam consectetur. Quaerat etincidunt eius ipsum consectetur. Sit labore porro adipisci. Quaerat ut magnam non numquam etincidunt tempora. Ipsum amet sit amet ut dolore amet. Ut non aliquam dolor etincidunt ipsum etincidunt. Non labore magnam porro ut. Porro dolorem labore labore quaerat.\n\nNon non adipisci quiquia. Eius neque ut quaerat etincidunt. Velit velit sed tempora amet quisquam. Consectetur quiquia voluptatem voluptatem adipisci est sit eius. Tempora ut sit magnam dolorem ', 'static/images/a4244994-fa53-4480-9ae5-70d2c2d99c49.jpg', 27000, 18, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(25, 1, 3, 9, 'Thịt heo', 'Quiquia adipisci consectetur magnam neque numquam dolore dolor. Numquam sit sit sit tempora porro numquam neque. Dolor adipisci sit amet. Tempora porro neque velit velit ipsum est tempora. Etincidunt ipsum consectetur magnam etincidunt modi. Etincidunt neque neque quiquia consectetur ipsum. Ut velit magnam consectetur. Aliquam eius ut non.\n\nTempora numquam ut dolor quaerat aliquam. Ipsum porro sit est porro etincidunt. Dolorem eius velit labore dolorem est. Labore modi neque ut porro ut magnam u', 'static/images/5d8e5a69-1b58-4435-b202-c0ccbfb90e73.jpg', 25000, 28, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(26, 1, 3, 9, 'Thịt heo', 'Aliquam modi modi sed. Eius est porro sed est. Sit etincidunt consectetur neque non sed non ut. Labore dolorem ut tempora. Quisquam neque ut amet quisquam. Neque labore consectetur est dolore etincidunt adipisci. Aliquam sit aliquam ipsum dolor magnam.\n\nQuisquam neque labore non modi aliquam quaerat. Quiquia quisquam aliquam ipsum eius etincidunt. Porro sit eius ut dolor sed est velit. Voluptatem modi tempora porro ipsum consectetur non. Dolorem amet dolore consectetur eius sit dolor.\n\nDolorem n', 'static/images/15063732-796b-443c-aa02-a2e3f0d3e235.jpg', 19000, 22, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(27, 1, 3, 9, 'Thịt heo', 'Numquam sit sed adipisci etincidunt tempora modi. Quiquia sit non tempora dolor non modi. Est neque dolore tempora non. Quaerat dolorem adipisci est non tempora ut ipsum. Sed velit dolor adipisci consectetur modi ut modi. Numquam magnam porro eius. Numquam dolorem non dolor sit non. Sed porro quiquia porro magnam aliquam.\n\nDolorem sed consectetur porro. Quaerat sit dolorem ipsum. Dolorem ipsum modi aliquam. Sit sit etincidunt voluptatem est velit velit. Amet consectetur consectetur ipsum quisqua', 'static/images/4d3e6f1f-5255-4508-a1b2-ac5cfaf44f16.jpg', 28000, 26, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(28, 1, 3, 9, 'Thịt heo', 'Quisquam modi consectetur non aliquam neque etincidunt ut. Velit non sed non etincidunt. Quaerat dolore velit dolor tempora ut modi ut. Ipsum modi velit dolorem magnam voluptatem etincidunt porro. Sed quiquia dolore consectetur modi. Sit dolor ut dolorem tempora ut voluptatem voluptatem. Dolore dolore ut sed ut velit. Sit sed etincidunt ut tempora modi. Velit voluptatem dolorem voluptatem quisquam sit ut.\n\nDolorem labore non est aliquam voluptatem dolorem. Neque eius labore dolor adipisci consec', 'static/images/cc032ab7-1425-488e-b0fb-1b3cddc9ac41.jpg', 28000, 28, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(29, 1, 3, 10, 'Thịt bò', 'Dolorem quiquia eius ut neque neque. Dolore etincidunt dolore dolorem ut neque. Velit adipisci quisquam non neque aliquam ut. Dolorem est quisquam velit. Dolorem sit dolor aliquam.\n\nAdipisci ipsum labore dolor. Consectetur quaerat neque consectetur dolor dolor magnam dolor. Est numquam modi sed etincidunt velit magnam. Porro voluptatem dolorem tempora numquam velit porro sed. Sit dolorem labore dolorem amet. Quisquam modi velit non labore.\n\nAliquam dolore dolorem eius sed modi amet. Adipisci ips', 'static/images/ab276cf5-9644-4f4a-a47c-fa9eeece15bd.jpg', 24000, 18, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(30, 1, 3, 10, 'Thịt bò', 'Porro ipsum quisquam dolorem amet adipisci. Dolorem velit ipsum non numquam velit labore quisquam. Etincidunt velit non adipisci. Magnam ut velit est sit est adipisci. Modi eius dolorem ut dolor.\n\nSit est ut eius quiquia non sit. Amet labore sit dolore. Ut porro modi aliquam magnam. Est dolorem neque velit. Magnam adipisci quiquia adipisci magnam quiquia etincidunt magnam. Quaerat consectetur adipisci eius est dolor. Aliquam quiquia ipsum consectetur eius. Dolore neque sit labore quisquam eius. ', 'static/images/6208b646-b61d-42fc-96a0-714bc2284a23.jpg', 19000, 30, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(31, 1, 3, 10, 'Thịt bò', 'Voluptatem dolor etincidunt sed. Non sed ut voluptatem quisquam porro quaerat dolor. Numquam quiquia dolore quiquia consectetur tempora est quaerat. Quisquam sed dolore aliquam dolorem. Adipisci etincidunt labore quiquia quaerat quaerat. Etincidunt quiquia amet non porro dolorem numquam.\n\nAdipisci ut consectetur est labore. Porro quiquia magnam adipisci. Ut neque ut voluptatem porro numquam sit amet. Quaerat est neque aliquam velit quiquia eius voluptatem. Labore velit etincidunt numquam dolore.', 'static/images/52e243b7-9df1-41ad-818c-83671b3ae628.jpg', 24000, 25, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(32, 1, 3, 10, 'Thịt bò', 'Modi amet velit quaerat. Dolore labore dolorem quiquia etincidunt. Ipsum modi non non modi numquam. Dolore quiquia labore est voluptatem dolore tempora adipisci. Consectetur adipisci quisquam quiquia magnam sit. Quiquia ipsum porro amet. Neque quaerat non magnam non quiquia eius.\n\nVelit velit dolore aliquam ipsum quaerat amet. Voluptatem magnam est tempora sed ipsum. Quiquia non ipsum consectetur ut quiquia. Dolor aliquam ut modi. Tempora tempora aliquam sit porro.\n\nQuaerat dolore sed non. Amet ', 'static/images/96308fe3-55f5-45c6-93c4-f70ca5c4a526.jpg', 17000, 27, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(33, 1, 3, 15, 'Cà chua', 'Numquam voluptatem dolorem dolorem amet quaerat. Neque numquam porro numquam. Dolorem etincidunt eius modi sed ut quaerat. Voluptatem est eius labore dolor eius. Quisquam neque dolorem neque etincidunt. Labore ipsum aliquam quisquam aliquam. Aliquam velit eius adipisci neque. Eius non non numquam aliquam. Modi consectetur etincidunt tempora velit.\n\nEst eius sed adipisci. Sit modi consectetur magnam sed adipisci ut. Dolor eius quisquam ipsum magnam. Consectetur adipisci quisquam tempora ipsum ali', 'static/images/7bf54d83-e38b-4d38-9aed-ddc3ca302b90.jpg', 14000, 24, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(34, 1, 3, 15, 'Cà chua', 'Adipisci sit est velit etincidunt. Aliquam etincidunt ut velit adipisci. Non sed magnam dolorem modi modi ipsum. Quiquia quiquia velit neque. Neque dolore porro consectetur dolorem. Porro amet quaerat dolor est porro. Porro ut est neque. Dolor adipisci amet aliquam adipisci. Neque magnam consectetur aliquam amet. Quaerat est labore eius quaerat sed porro.\n\nMagnam tempora magnam numquam amet. Ut velit dolor adipisci ut sed sit. Adipisci dolor aliquam aliquam voluptatem tempora sed. Voluptatem ut ', 'static/images/791aaba5-d547-45f9-9fd7-70658d7cefc3.jpg', 29000, 30, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(35, 1, 3, 15, 'Cà chua', 'Ut est numquam amet quaerat adipisci neque quisquam. Quaerat neque modi dolor sit magnam ipsum. Tempora quaerat ipsum ut dolorem velit. Eius eius quaerat magnam. Magnam modi magnam est aliquam neque amet. Consectetur est magnam tempora consectetur. Voluptatem sit consectetur magnam.\n\nConsectetur tempora non tempora. Est sed voluptatem quisquam dolore. Numquam labore non magnam. Consectetur ipsum porro dolor quiquia adipisci. Aliquam modi sed dolore. Dolore aliquam amet dolorem ipsum ut. Tempora ', 'static/images/6e09ef8b-86cc-47fe-9c19-7e8856c18c6b.jpg', 29000, 26, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(36, 1, 3, 15, 'Cà chua', 'Voluptatem dolorem labore ut est dolore eius. Quisquam quisquam amet velit voluptatem adipisci. Quiquia etincidunt sed numquam labore magnam. Non velit consectetur aliquam dolor consectetur est est. Neque non labore numquam quisquam dolor amet. Voluptatem dolorem sed porro non. Modi aliquam adipisci numquam dolore consectetur etincidunt. Amet non dolorem etincidunt dolore porro. Etincidunt sed aliquam velit ipsum. Velit amet consectetur labore ipsum etincidunt.\n\nAliquam sed adipisci dolor. Est n', 'static/images/deb64e34-13c2-4ebc-92b4-5009a39f6155.jpg', 20000, 24, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(37, 1, 4, 9, 'Thịt heo', 'Dolor amet quaerat dolore neque dolor. Dolore ut dolore numquam. Numquam porro tempora numquam dolorem ipsum voluptatem magnam. Voluptatem dolorem ipsum dolorem numquam adipisci. Numquam eius voluptatem est dolor velit. Adipisci magnam magnam quaerat est numquam tempora. Quisquam sed eius modi non neque.\n\nUt magnam quiquia numquam amet labore. Porro consectetur dolorem sed. Etincidunt dolore sed non. Ut non magnam etincidunt. Tempora sit consectetur dolore numquam quiquia sed. Quisquam porro sit', 'static/images/187dba18-68cd-4113-84c8-6b4f87d42e88.jpg', 12000, 21, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(38, 1, 4, 9, 'Thịt heo', 'Quaerat non sed adipisci. Modi etincidunt consectetur etincidunt magnam. Voluptatem dolorem est neque dolorem tempora. Neque quisquam modi etincidunt consectetur dolor non. Magnam magnam modi etincidunt eius. Quiquia sit eius sed numquam. Quisquam sed sit consectetur dolor porro quiquia est. Quisquam dolore ipsum dolor. Amet dolore neque non tempora numquam.\n\nQuaerat dolor sed quiquia consectetur quisquam. Adipisci porro eius sed tempora. Modi dolor non dolor dolore aliquam dolore. Aliquam quisq', 'static/images/413f1d6d-b5e3-43a0-8b0f-b450e1eea468.jpg', 25000, 30, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(39, 1, 4, 9, 'Thịt heo', 'Dolore porro sed neque sed quisquam porro consectetur. Aliquam non velit amet. Est dolore adipisci etincidunt dolorem. Velit voluptatem quisquam quaerat consectetur. Etincidunt adipisci etincidunt porro tempora quaerat quaerat magnam. Aliquam neque numquam neque.\n\nDolorem dolore eius dolor. Numquam quiquia quiquia sit. Labore sed etincidunt aliquam eius velit dolore. Quaerat velit etincidunt labore. Consectetur dolore quisquam magnam modi magnam sed. Numquam quaerat porro etincidunt modi. Modi s', 'static/images/c41b61af-0c90-481f-af14-8e7caf2ed46b.jpg', 24000, 18, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(40, 1, 4, 9, 'Thịt heo', 'Modi dolore quaerat adipisci. Dolorem dolor labore quaerat ut. Aliquam porro quisquam neque numquam labore tempora. Neque quaerat labore neque non neque ut magnam. Est adipisci neque non neque sit. Ut porro porro sed ipsum magnam. Modi quisquam adipisci ipsum sed voluptatem aliquam. Sed neque voluptatem dolor velit magnam. Amet sed quaerat eius quisquam sed.\n\nIpsum non quaerat voluptatem magnam sed. Aliquam ut modi sit porro dolore amet. Sed tempora consectetur eius neque non quisquam. Etincidun', 'static/images/c379e4b4-7536-49ae-9dcf-6c883fa003ba.jpg', 26000, 20, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(41, 1, 4, 10, 'Thịt bò', 'Ipsum neque eius dolor non numquam amet voluptatem. Porro adipisci consectetur quiquia. Modi magnam non est velit adipisci. Adipisci ut dolor est dolorem est. Ipsum dolore adipisci tempora dolor quiquia. Porro est aliquam tempora aliquam neque. Non eius tempora quisquam quisquam quisquam est numquam.\n\nSed labore labore neque quisquam. Dolor adipisci ut est adipisci ipsum tempora. Non sit ipsum magnam velit. Quisquam ut tempora aliquam dolor labore aliquam voluptatem. Etincidunt non non porro qui', 'static/images/24ac8617-6a3d-4e28-9363-901e951e9a89.jpg', 15000, 24, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(42, 1, 4, 10, 'Thịt bò', 'Ut quaerat voluptatem numquam eius aliquam. Quisquam labore magnam sed. Voluptatem eius dolore eius. Neque tempora sed velit. Dolorem neque numquam porro numquam consectetur. Modi velit modi labore dolorem ut ipsum ut. Est velit neque non. Neque aliquam quaerat non sed. Etincidunt sed ipsum dolor.\n\nSit modi dolorem etincidunt. Eius ut dolore quisquam. Quisquam ipsum sed neque tempora. Quaerat sit magnam tempora ipsum dolorem non adipisci. Sit quaerat dolore quisquam quiquia amet adipisci. Aliqua', 'static/images/d11ddccd-88f5-4edc-975c-2a4074d06696.jpg', 12000, 16, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(43, 1, 4, 10, 'Thịt bò', 'Quaerat voluptatem dolorem numquam magnam porro. Non labore adipisci magnam. Non magnam velit quaerat. Adipisci est est aliquam. Ut dolore velit porro sit velit. Neque velit aliquam porro adipisci tempora dolorem aliquam. Tempora modi dolore magnam dolor non. Labore labore dolorem dolore sed numquam. Ipsum est sit ipsum.\n\nAliquam aliquam modi sit. Consectetur dolore ipsum etincidunt etincidunt quiquia quisquam. Velit est velit labore amet. Dolorem etincidunt velit dolor. Tempora modi numquam mod', 'static/images/5e4d8ecf-4894-4574-8374-3af38308b900.jpg', 16000, 19, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(44, 1, 4, 10, 'Thịt bò', 'Magnam magnam quisquam sit ut. Sit ut amet adipisci voluptatem. Sit quaerat etincidunt non. Consectetur consectetur modi modi. Aliquam eius voluptatem labore eius eius. Eius est consectetur non velit dolor. Eius velit dolorem tempora ipsum modi. Etincidunt neque quaerat sit adipisci tempora. Magnam magnam adipisci quaerat adipisci ut velit. Numquam voluptatem labore adipisci dolor etincidunt sit.\n\nDolore dolorem etincidunt dolor consectetur etincidunt. Ut sit amet labore quisquam dolor porro. Vo', 'static/images/3b6b2462-da6d-43e2-8947-494362e43e53.jpg', 14000, 21, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(45, 1, 4, 15, 'Cà chua', 'Etincidunt voluptatem velit tempora non. Aliquam aliquam ut dolore consectetur porro ut numquam. Labore adipisci ipsum amet magnam ut porro. Aliquam non dolor voluptatem. Velit porro quaerat etincidunt est dolore. Neque quiquia ipsum ut amet consectetur consectetur dolorem. Quiquia adipisci quiquia adipisci. Voluptatem amet neque porro ut quisquam.\n\nVelit adipisci tempora sed quaerat est numquam est. Amet modi amet labore dolorem tempora. Tempora ipsum dolor dolorem. Porro neque porro numquam qu', 'static/images/af4a690b-34f1-4713-8626-aa20c9c5c114.jpg', 28000, 23, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(46, 1, 4, 15, 'Cà chua', 'Voluptatem dolor voluptatem magnam. Velit numquam est magnam dolorem aliquam ut. Dolorem labore voluptatem voluptatem. Voluptatem ut dolor ut adipisci quaerat. Numquam eius dolorem magnam dolor voluptatem. Est quisquam est ut. Dolor dolore amet porro. Ipsum sit numquam sed neque numquam numquam. Voluptatem non numquam ut est quisquam.\n\nIpsum adipisci modi amet ut. Sed ut est velit modi quiquia amet. Est quaerat ut etincidunt adipisci numquam est. Dolore velit non dolor quisquam dolorem est porro', 'static/images/aef099d5-dcbf-49d0-90d8-9ee3073aaa8e.jpg', 26000, 17, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(47, 1, 4, 15, 'Cà chua', 'Porro dolorem consectetur quisquam est adipisci consectetur. Voluptatem sed est neque adipisci. Sit adipisci sed porro quisquam. Voluptatem quaerat ipsum ut quaerat. Ut quisquam amet dolor quisquam porro. Aliquam non neque non. Velit tempora dolorem etincidunt est ut. Dolore quisquam labore voluptatem neque dolore. Magnam adipisci etincidunt modi labore magnam. Sed magnam ipsum dolor quaerat dolore amet neque.\n\nQuiquia neque sit quaerat est aliquam. Eius non sit est porro quisquam. Eius etincidu', 'static/images/f3d0d668-c4f7-48ef-93ce-9af7092a19a6.jpg', 27000, 19, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(48, 1, 4, 15, 'Cà chua', 'Numquam magnam magnam eius magnam labore magnam aliquam. Modi voluptatem quaerat ipsum consectetur voluptatem. Modi eius etincidunt non tempora amet aliquam etincidunt. Voluptatem quisquam ut modi dolorem amet ipsum. Modi magnam labore dolore eius. Etincidunt ipsum ut quiquia tempora dolorem tempora porro. Dolorem amet dolor numquam. Velit velit adipisci labore non magnam. Magnam labore aliquam tempora dolorem modi. Amet neque ut sit magnam etincidunt quaerat.\n\nEtincidunt sed numquam modi porro.', 'static/images/b4eb6302-b55c-4bda-850a-1d6fc21a28e4.jpg', 28000, 25, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(49, 1, 5, 9, 'Thịt heo', 'Adipisci sit sed quaerat amet. Quiquia dolor ut labore aliquam sed. Amet aliquam quiquia quiquia dolor dolorem. Neque amet voluptatem quisquam. Ut quaerat eius dolore amet dolore. Quiquia porro sit etincidunt eius magnam numquam quiquia. Sed quiquia dolore numquam labore magnam. Consectetur ut magnam sit consectetur quiquia. Amet ut eius eius labore sit amet quisquam. Quisquam est dolore modi labore etincidunt neque ipsum.\n\nAmet magnam tempora dolor labore. Aliquam quaerat sed amet voluptatem am', 'static/images/77a8574c-2802-4351-8ce4-e3e356c1cfa9.jpg', 19000, 21, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(50, 1, 5, 9, 'Thịt heo', 'Dolorem voluptatem consectetur sit dolore neque dolorem. Modi aliquam voluptatem non dolorem. Sed amet sed modi est. Dolore aliquam ipsum quisquam. Amet eius velit quiquia quaerat aliquam. Eius quiquia sit quaerat. Sed numquam quisquam quisquam est dolore aliquam ipsum. Etincidunt velit magnam sit velit. Quaerat aliquam consectetur amet dolore ipsum voluptatem labore.\n\nNumquam tempora aliquam dolorem quaerat tempora dolor eius. Modi ut sed sit est. Sed porro numquam dolorem. Aliquam dolore non u', 'static/images/857a12fc-8964-497b-b0cf-32e08ff4dcc3.jpg', 22000, 19, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(51, 1, 5, 9, 'Thịt heo', 'Labore magnam sed voluptatem. Velit etincidunt quiquia etincidunt tempora dolor est ipsum. Ut sed quaerat quisquam. Etincidunt eius sit modi. Quiquia quiquia neque modi non numquam. Modi porro sed quisquam tempora. Dolor voluptatem dolorem modi magnam aliquam dolor. Numquam voluptatem dolore eius velit. Est sit ipsum non magnam eius tempora ipsum.\n\nPorro voluptatem porro porro non ut tempora. Non quiquia dolorem est dolorem velit. Velit tempora est quaerat amet aliquam ut tempora. Adipisci sit n', 'static/images/dad17868-25f7-47a9-8b90-06e31802b62a.jpg', 25000, 28, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(52, 1, 5, 9, 'Thịt heo', 'Numquam non magnam sed ut. Eius aliquam non sit dolor quaerat. Sit neque consectetur etincidunt sed modi. Adipisci labore ut aliquam. Ut tempora numquam quaerat. Aliquam dolore numquam etincidunt etincidunt adipisci est. Dolor quisquam eius dolore tempora modi dolor.\n\nIpsum sed ut magnam est quaerat modi dolore. Dolore consectetur amet labore. Quisquam magnam voluptatem etincidunt velit aliquam. Quisquam numquam eius sed numquam. Voluptatem quiquia tempora adipisci adipisci magnam.\n\nIpsum non co', 'static/images/c66ed711-e27d-48cb-9688-076374019a7b.jpg', 21000, 21, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(53, 1, 5, 10, 'Thịt bò', 'Modi ipsum amet ipsum ipsum quiquia. Etincidunt voluptatem etincidunt eius quisquam etincidunt. Voluptatem magnam quisquam consectetur est. Non magnam quisquam voluptatem quisquam quiquia. Dolorem dolor quisquam aliquam neque neque consectetur ut. Adipisci non quaerat velit amet numquam. Labore porro consectetur est. Quisquam modi ut magnam numquam magnam. Velit non modi ipsum.\n\nEtincidunt etincidunt non tempora dolore eius. Dolor neque adipisci dolor sed ipsum eius porro. Amet est etincidunt do', 'static/images/ecd1812c-ed88-4528-b248-7743f6cb5a23.jpg', 24000, 29, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(54, 1, 5, 10, 'Thịt bò', 'Quaerat sed adipisci amet ipsum porro dolor ipsum. Eius dolorem ut ipsum magnam porro non. Voluptatem quaerat est voluptatem ut. Non velit quiquia neque. Aliquam voluptatem quiquia voluptatem.\n\nAmet porro dolor magnam neque non. Neque sed quaerat velit numquam eius velit. Aliquam ut est eius aliquam dolor modi. Dolorem dolor non quaerat sit aliquam est dolor. Sed porro amet est est. Consectetur eius neque labore porro sit tempora ipsum. Adipisci consectetur adipisci quaerat ut porro.\n\nLabore neq', 'static/images/1158b84a-ed74-4cff-8b04-d6aaf6bf4a12.jpg', 22000, 30, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(55, 1, 5, 10, 'Thịt bò', 'Magnam dolore velit aliquam velit sed. Dolore modi dolor amet. Non quaerat quiquia sit ipsum. Tempora magnam dolorem modi. Adipisci eius adipisci sed dolore neque. Sit labore tempora dolor. Sed consectetur porro adipisci etincidunt. Ipsum adipisci est velit.\n\nQuaerat adipisci modi dolor ut velit est. Ut ut consectetur eius etincidunt dolor. Dolorem non neque ut tempora velit dolor magnam. Neque dolorem magnam numquam eius labore. Etincidunt adipisci etincidunt numquam numquam. Non eius ipsum neq', 'static/images/b6f64f98-14d0-4c15-9d1b-32f19cbc3535.jpg', 14000, 17, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(56, 1, 5, 10, 'Thịt bò', 'Consectetur voluptatem sit ut aliquam etincidunt numquam numquam. Dolore eius velit neque. Etincidunt sit quaerat magnam. Quaerat tempora etincidunt eius etincidunt. Amet etincidunt labore quisquam ipsum dolorem labore eius. Sit aliquam dolore velit quiquia. Aliquam quiquia tempora consectetur amet. Velit sed eius labore non.\n\nAmet aliquam sit dolore velit quaerat. Quaerat est aliquam sit consectetur tempora neque. Ipsum quiquia est porro quiquia. Ipsum dolorem dolorem non sed voluptatem modi do', 'static/images/88718af8-d65f-423b-b144-f37d7365e371.jpg', 24000, 18, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(57, 1, 5, 15, 'Cà chua', 'Voluptatem voluptatem magnam dolorem velit est quiquia quisquam. Etincidunt numquam ut voluptatem etincidunt ut ut. Sit non aliquam eius. Adipisci voluptatem dolorem modi. Dolore est voluptatem velit porro. Aliquam etincidunt adipisci dolore eius tempora porro velit. Voluptatem dolore neque adipisci est sit labore.\n\nVoluptatem tempora adipisci neque consectetur quisquam. Porro non ut est magnam dolorem eius. Modi labore tempora dolor dolor dolor tempora est. Ipsum consectetur sit dolorem. Aliqua', 'static/images/a18d5687-3942-48f5-be6a-a844a33a0260.jpg', 18000, 19, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(58, 1, 5, 15, 'Cà chua', 'Modi magnam magnam adipisci ut. Adipisci consectetur tempora adipisci porro numquam non eius. Dolore modi ipsum velit ut dolor. Amet etincidunt quisquam porro ut dolorem amet. Amet ipsum quisquam modi. Sed numquam non est neque ut. Eius amet quaerat etincidunt quiquia eius quiquia est. Quiquia amet quaerat etincidunt consectetur non. Dolore velit consectetur modi voluptatem. Velit numquam est adipisci voluptatem quaerat.\n\nVoluptatem voluptatem ut dolore tempora. Eius dolorem quiquia voluptatem. ', 'static/images/5ec85073-81e9-49e6-95b7-7da504a1e588.jpg', 19000, 25, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(59, 1, 5, 15, 'Cà chua', 'Dolor adipisci quiquia porro est modi. Dolor labore ipsum voluptatem ipsum consectetur etincidunt. Quisquam dolorem sit eius non eius quisquam numquam. Ut eius tempora adipisci velit amet dolorem quiquia. Tempora sit adipisci labore quisquam modi. Eius dolor etincidunt adipisci amet. Labore dolore neque sed. Consectetur numquam quisquam non.\n\nNeque est modi ut amet ipsum magnam. Porro eius labore dolorem aliquam modi. Ut tempora ut dolore eius ut dolor ut. Voluptatem voluptatem consectetur quaer', 'static/images/8c631033-8a06-4b21-b562-746feb8d256d.jpg', 29000, 20, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(60, 1, 5, 15, 'Cà chua', 'Magnam porro quaerat quiquia adipisci quaerat. Magnam dolor neque numquam tempora quaerat. Numquam aliquam tempora est amet dolorem. Numquam non aliquam est dolor voluptatem. Ipsum dolorem dolorem adipisci ut.\n\nAdipisci est ipsum quiquia. Dolor neque quisquam tempora est quiquia. Tempora magnam velit non quisquam quiquia. Quisquam tempora etincidunt sed. Velit magnam sed porro porro tempora porro. Tempora dolorem consectetur dolore magnam quaerat. Quisquam adipisci tempora dolore tempora sed sit', 'static/images/b6277425-5b21-4aee-b12b-9b2a45949166.jpg', 25000, 17, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(61, 1, 6, 9, 'Thịt heo', 'Quaerat modi quiquia neque non etincidunt consectetur. Non quaerat neque non eius magnam consectetur. Aliquam aliquam dolore sit. Etincidunt eius voluptatem numquam. Sit est tempora quiquia ipsum quisquam dolorem quisquam. Eius adipisci quiquia dolor magnam. Adipisci numquam adipisci adipisci quiquia non. Labore aliquam etincidunt etincidunt voluptatem ut eius amet. Consectetur est quiquia est. Sit neque consectetur modi aliquam etincidunt quiquia.\n\nLabore quaerat sit dolore. Non quaerat neque n', 'static/images/5506f530-4721-4d39-a0fd-1a321232a552.jpg', 28000, 28, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(62, 1, 6, 9, 'Thịt heo', 'Eius ipsum est porro numquam labore. Est dolor est ut quisquam dolor. Magnam consectetur magnam aliquam amet sit. Sit consectetur numquam numquam quaerat tempora dolore dolore. Labore dolorem eius dolor.\n\nEius modi dolore velit modi sed etincidunt. Est ut quaerat non dolore voluptatem voluptatem. Dolorem quaerat neque quisquam amet sit adipisci. Quisquam labore porro numquam quisquam porro. Dolorem modi modi quaerat porro modi sit numquam. Sed modi est quaerat. Adipisci etincidunt amet aliquam. ', 'static/images/a7e07f79-be51-4964-9a73-f8981f8433da.jpg', 15000, 24, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(63, 1, 6, 9, 'Thịt heo', 'Dolore adipisci quaerat ut aliquam est modi numquam. Quaerat aliquam dolore modi non tempora aliquam. Velit modi tempora velit. Etincidunt etincidunt dolorem adipisci quaerat adipisci magnam. Etincidunt aliquam quaerat velit neque.\n\nAmet ipsum etincidunt porro quisquam quiquia. Non modi tempora numquam quisquam. Neque dolorem etincidunt tempora. Ut sed quiquia quaerat eius. Sit voluptatem magnam quaerat. Modi consectetur quiquia adipisci dolore tempora. Porro dolore ut consectetur eius. Eius qui', 'static/images/6c344379-2691-432f-a464-923471d4f399.jpg', 29000, 20, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(64, 1, 6, 9, 'Thịt heo', 'Dolor porro eius adipisci ipsum. Adipisci ipsum dolor dolore ipsum. Quiquia quisquam aliquam amet aliquam magnam. Numquam eius dolor sit non adipisci amet quisquam. Ut tempora etincidunt quaerat.\n\nEtincidunt ut amet magnam eius. Dolorem adipisci quiquia magnam dolore numquam magnam magnam. Magnam porro adipisci consectetur non adipisci. Ut labore quisquam numquam quaerat adipisci. Amet est eius velit non. Ut non ut velit magnam sed. Etincidunt tempora quisquam labore aliquam est neque. Porro con', 'static/images/c76d1ec9-49fe-4f82-95b7-f8306b2b5c5e.jpg', 15000, 24, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(65, 1, 6, 10, 'Thịt bò', 'Eius aliquam etincidunt sit modi quisquam adipisci. Ipsum voluptatem sit ut numquam amet. Labore dolorem adipisci magnam. Tempora voluptatem non modi labore magnam. Etincidunt ut magnam adipisci consectetur numquam adipisci modi. Aliquam sit non quaerat sit tempora. Amet tempora voluptatem aliquam adipisci etincidunt.\n\nModi dolor tempora etincidunt quiquia dolor. Neque aliquam consectetur modi numquam eius. Est dolore porro quaerat sed est dolor. Aliquam est quaerat tempora voluptatem voluptatem', 'static/images/b14692e7-588d-4de7-ac1f-2e1a102d002a.jpg', 21000, 16, '2021-11-16', '10.0342277|105.755296', 'Số 179 Nguyễn Văn Cừ, Phường An Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(66, 1, 6, 10, 'Thịt bò', 'Quiquia est dolore dolore neque. Etincidunt eius non etincidunt. Quisquam non sit sed. Magnam aliquam adipisci ipsum. Magnam consectetur etincidunt est porro dolore ut amet. Neque eius velit quiquia consectetur. Dolore sed numquam tempora. Dolorem quiquia neque quisquam numquam. Eius dolorem quisquam dolor. Dolor adipisci sit non non.\n\nQuisquam sit aliquam consectetur voluptatem etincidunt consectetur. Dolorem non aliquam modi numquam eius aliquam tempora. Modi sit labore sed consectetur magnam ', 'static/images/3b5d0e91-b101-471e-a3a3-fa1d49b0e891.jpg', 25000, 21, '2021-11-16', '10.024829|105.7746337', '209 Đường 30 Tháng 4, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(67, 1, 6, 10, 'Thịt bò', 'Sed adipisci labore adipisci non tempora. Quisquam consectetur quiquia quiquia velit sed porro. Velit consectetur adipisci tempora ut neque. Eius tempora dolor quisquam porro velit. Numquam tempora labore aliquam. Dolorem sed etincidunt magnam modi ut sed. Magnam ipsum amet velit modi amet ut.\n\nModi dolor labore labore ut numquam. Porro ut dolor ut non quisquam numquam. Est non neque quisquam magnam amet etincidunt ipsum. Neque quisquam voluptatem aliquam voluptatem quiquia est consectetur. Dolo', 'static/images/deaad4e8-375f-481c-9eb0-8c7ba8450b4c.jpg', 14000, 20, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(68, 1, 6, 10, 'Thịt bò', 'Est porro non dolorem quisquam. Ut numquam etincidunt tempora. Dolor consectetur numquam adipisci adipisci. Amet est etincidunt modi voluptatem modi. Ipsum numquam magnam aliquam modi. Labore aliquam dolore quiquia consectetur neque. Non etincidunt voluptatem magnam velit velit.\n\nDolore numquam tempora ut modi eius. Sed eius voluptatem ipsum sed. Numquam modi dolore modi est. Numquam voluptatem ut eius numquam quisquam ipsum eius. Labore quiquia ut quaerat dolorem. Dolore magnam numquam ipsum qu', 'static/images/8bbe4bb6-9ae4-4707-902f-e4edbc7fb166.jpg', 14000, 23, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(69, 1, 6, 15, 'Cà chua', 'Numquam quiquia velit sed quiquia. Neque amet aliquam sit. Velit porro velit magnam voluptatem tempora ut. Dolore modi modi non dolore porro modi. Modi aliquam sit adipisci sit quaerat dolore quisquam. Aliquam dolore magnam numquam dolor etincidunt tempora ut. Est dolore consectetur eius. Quaerat sed etincidunt non eius sed adipisci est.\n\nPorro dolor dolor dolorem quaerat. Est sit amet sit sit labore. Eius labore est tempora. Amet quisquam sed sit numquam quisquam. Dolor ipsum ipsum sit aliquam ', 'static/images/7c9b521b-b62a-4e26-a722-6ed8629d716c.jpg', 14000, 18, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(70, 1, 6, 15, 'Cà chua', 'Adipisci numquam neque est numquam. Voluptatem magnam etincidunt non adipisci. Velit dolore quaerat velit. Sit etincidunt adipisci sed sit amet. Quaerat neque etincidunt dolor. Modi consectetur numquam adipisci modi quiquia non.\n\nModi dolore amet labore consectetur dolorem. Amet modi dolor dolor eius non neque quisquam. Voluptatem velit est neque est dolor ipsum tempora. Quisquam dolorem quisquam porro eius numquam. Quaerat labore tempora sit dolorem. Sed quaerat dolore magnam. Eius ipsum sit mo', 'static/images/4952e47b-ea7b-43b6-8bea-bfe8bb9661f4.jpg', 16000, 19, '2021-11-16', '10.0425844|105.7665141', '84 Mậu Thân, An Hoà, Ninh Kiều, Cần Thơ, Việt Nam', NULL);
INSERT INTO `thuc_pham` (`TP_MA`, `DMDVT_MA`, `ND_MA`, `DMTP_MA`, `TP_TEN`, `TP_MO_TA`, `TP_HINH_ANH`, `TP_DON_GIA`, `TP_SO_LUONG`, `TP_NGAY_BAN`, `TP_VI_TRI_BAN_DO`, `TP_DIA_CHI`, `TP_SUAT_BAN`) VALUES
(71, 1, 6, 15, 'Cà chua', 'Tempora adipisci eius ut labore adipisci numquam eius. Sed consectetur ipsum voluptatem amet quiquia porro quisquam. Adipisci consectetur adipisci velit amet. Tempora voluptatem est ipsum velit velit tempora numquam. Quisquam dolorem quisquam voluptatem dolore est sed eius. Velit modi est quaerat quiquia quaerat est. Quaerat ut etincidunt voluptatem sed quaerat numquam. Amet numquam sit labore quiquia est. Adipisci modi est adipisci modi ipsum dolorem quisquam.\n\nEst magnam amet neque dolorem ame', 'static/images/3084a97f-588a-48a4-83f9-4fe60ff620be.jpg', 16000, 17, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL),
(72, 1, 6, 15, 'Cà chua', 'Sed quiquia sit dolor dolorem. Labore quaerat dolorem quiquia sed eius voluptatem dolor. Voluptatem modi etincidunt eius modi sit voluptatem. Adipisci labore ut voluptatem etincidunt sit numquam quaerat. Sed neque quaerat labore amet neque. Eius quiquia ut magnam ipsum. Dolore quaerat consectetur eius neque tempora velit neque. Amet magnam amet aliquam tempora quaerat. Dolor dolore dolorem voluptatem.\n\nAdipisci aliquam magnam adipisci. Eius modi numquam adipisci modi eius tempora. Consectetur qu', 'static/images/fd89db21-a6e4-43d9-ad47-220fa5e808cd.jpg', 14000, 29, '2021-11-16', '10.0299337|105.7706153', 'Khu II, Đ. 3/2, Xuân Khánh, Ninh Kiều, Cần Thơ, Việt Nam', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `binh_luan`
--
ALTER TABLE `binh_luan`
  ADD PRIMARY KEY (`BL_MA`),
  ADD KEY `FK_BL_TP` (`TP_MA`),
  ADD KEY `FK_ND_BL` (`ND_MA`);

--
-- Indexes for table `chi_tiet_dang_ky_mua`
--
ALTER TABLE `chi_tiet_dang_ky_mua`
  ADD PRIMARY KEY (`TP_MA`,`DKM_MA`),
  ADD KEY `FK_CTDKM_DKM` (`DKM_MA`);

--
-- Indexes for table `chi_tiet_nhu_cau_mua`
--
ALTER TABLE `chi_tiet_nhu_cau_mua`
  ADD PRIMARY KEY (`DMTP_MA`,`NCM_MA`,`DMDVT_MA`),
  ADD KEY `FK_CTNCM_NCM` (`NCM_MA`),
  ADD KEY `FK_DMDVT_CTNCM` (`DMDVT_MA`);

--
-- Indexes for table `dang_ky_mua`
--
ALTER TABLE `dang_ky_mua`
  ADD PRIMARY KEY (`DKM_MA`),
  ADD KEY `FK_ND_DKM` (`ND_MA`);

--
-- Indexes for table `danh_muc_don_vi_tinh`
--
ALTER TABLE `danh_muc_don_vi_tinh`
  ADD PRIMARY KEY (`DMDVT_MA`);

--
-- Indexes for table `danh_muc_thuc_pham`
--
ALTER TABLE `danh_muc_thuc_pham`
  ADD PRIMARY KEY (`DMTP_MA`);

--
-- Indexes for table `dm_don_vi_tinh_dm_thuc_pham`
--
ALTER TABLE `dm_don_vi_tinh_dm_thuc_pham`
  ADD PRIMARY KEY (`DMTP_MA`,`DMDVT_MA`),
  ADD KEY `FK_DM_DON_VI_TINH_DM_THUC_PHAM2` (`DMDVT_MA`);

--
-- Indexes for table `nguoi_dung`
--
ALTER TABLE `nguoi_dung`
  ADD PRIMARY KEY (`ND_MA`);

--
-- Indexes for table `nhu_cau_mua`
--
ALTER TABLE `nhu_cau_mua`
  ADD PRIMARY KEY (`NCM_MA`),
  ADD KEY `FK_ND_NCM` (`ND_MA`);

--
-- Indexes for table `thuc_pham`
--
ALTER TABLE `thuc_pham`
  ADD PRIMARY KEY (`TP_MA`),
  ADD KEY `FK_BAN` (`ND_MA`),
  ADD KEY `FK_DMDVT_TP` (`DMDVT_MA`),
  ADD KEY `FK_DMTP_TP` (`DMTP_MA`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `binh_luan`
--
ALTER TABLE `binh_luan`
  MODIFY `BL_MA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `dang_ky_mua`
--
ALTER TABLE `dang_ky_mua`
  MODIFY `DKM_MA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `danh_muc_don_vi_tinh`
--
ALTER TABLE `danh_muc_don_vi_tinh`
  MODIFY `DMDVT_MA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `danh_muc_thuc_pham`
--
ALTER TABLE `danh_muc_thuc_pham`
  MODIFY `DMTP_MA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `nguoi_dung`
--
ALTER TABLE `nguoi_dung`
  MODIFY `ND_MA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `nhu_cau_mua`
--
ALTER TABLE `nhu_cau_mua`
  MODIFY `NCM_MA` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `thuc_pham`
--
ALTER TABLE `thuc_pham`
  MODIFY `TP_MA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `binh_luan`
--
ALTER TABLE `binh_luan`
  ADD CONSTRAINT `FK_BL_TP` FOREIGN KEY (`TP_MA`) REFERENCES `thuc_pham` (`TP_MA`),
  ADD CONSTRAINT `FK_ND_BL` FOREIGN KEY (`ND_MA`) REFERENCES `nguoi_dung` (`ND_MA`);

--
-- Constraints for table `chi_tiet_dang_ky_mua`
--
ALTER TABLE `chi_tiet_dang_ky_mua`
  ADD CONSTRAINT `FK_CTDKM_DKM` FOREIGN KEY (`DKM_MA`) REFERENCES `dang_ky_mua` (`DKM_MA`),
  ADD CONSTRAINT `FK_CTKDM_TP` FOREIGN KEY (`TP_MA`) REFERENCES `thuc_pham` (`TP_MA`);

--
-- Constraints for table `chi_tiet_nhu_cau_mua`
--
ALTER TABLE `chi_tiet_nhu_cau_mua`
  ADD CONSTRAINT `FK_CTNCM_DMTP` FOREIGN KEY (`DMTP_MA`) REFERENCES `danh_muc_thuc_pham` (`DMTP_MA`),
  ADD CONSTRAINT `FK_CTNCM_NCM` FOREIGN KEY (`NCM_MA`) REFERENCES `nhu_cau_mua` (`NCM_MA`),
  ADD CONSTRAINT `FK_DMDVT_CTNCM` FOREIGN KEY (`DMDVT_MA`) REFERENCES `danh_muc_don_vi_tinh` (`DMDVT_MA`);

--
-- Constraints for table `dang_ky_mua`
--
ALTER TABLE `dang_ky_mua`
  ADD CONSTRAINT `FK_ND_DKM` FOREIGN KEY (`ND_MA`) REFERENCES `nguoi_dung` (`ND_MA`);

--
-- Constraints for table `dm_don_vi_tinh_dm_thuc_pham`
--
ALTER TABLE `dm_don_vi_tinh_dm_thuc_pham`
  ADD CONSTRAINT `FK_DM_DON_VI_TINH_DM_THUC_PHAM` FOREIGN KEY (`DMTP_MA`) REFERENCES `danh_muc_thuc_pham` (`DMTP_MA`),
  ADD CONSTRAINT `FK_DM_DON_VI_TINH_DM_THUC_PHAM2` FOREIGN KEY (`DMDVT_MA`) REFERENCES `danh_muc_don_vi_tinh` (`DMDVT_MA`);

--
-- Constraints for table `nhu_cau_mua`
--
ALTER TABLE `nhu_cau_mua`
  ADD CONSTRAINT `FK_ND_NCM` FOREIGN KEY (`ND_MA`) REFERENCES `nguoi_dung` (`ND_MA`);

--
-- Constraints for table `thuc_pham`
--
ALTER TABLE `thuc_pham`
  ADD CONSTRAINT `FK_BAN` FOREIGN KEY (`ND_MA`) REFERENCES `nguoi_dung` (`ND_MA`),
  ADD CONSTRAINT `FK_DMDVT_TP` FOREIGN KEY (`DMDVT_MA`) REFERENCES `danh_muc_don_vi_tinh` (`DMDVT_MA`),
  ADD CONSTRAINT `FK_DMTP_TP` FOREIGN KEY (`DMTP_MA`) REFERENCES `danh_muc_thuc_pham` (`DMTP_MA`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
