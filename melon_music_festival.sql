-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 12:43 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `melon_music_festival`
--

-- --------------------------------------------------------

--
-- Table structure for table `mmf_stage`
--

CREATE TABLE `mmf_stage` (
  `full_name` varchar(100) NOT NULL,
  `stage_type` varchar(100) NOT NULL,
  `ticket_type` varchar(100) NOT NULL,
  `pack` int(3) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mmf_stage`
--

INSERT INTO `mmf_stage` (`full_name`, `stage_type`, `ticket_type`, `pack`, `price`) VALUES
('Exlin Wu', 'Sky Rocket Melon Stage, Sugar Kiss Melon Stage, Honey Globe Melon Stage', 'VIP', 1, 1650),
('Fai', 'Honey Globe Melon Stage', 'VIP', 1, 550),
('Balqis Nabila', 'Honey Globe Melon Stage', 'VIP', 1, 550),
('Suri', 'Sky Rocket Melon Stage', 'VIP', 1, 550),
('Moo', 'Honey Globe Melon Stage', 'VIP', 1, 550),
('Raja Farah', 'Sugar Kiss Melon Stage', 'General Admission', 2, 700),
('Fareth Haikal', 'Sky Rocket Melon Stage', 'VIP', 3, 1650),
('Lee Xi Jia', 'Sugar Kiss Melon Stage, Honey Globe Melon Stage', 'General Admission', 3, 2100),
('Najwa Amanina', 'Honey Globe Melon Stage', 'VIP', 1, 550),
('Aziz Harun', 'Sugar Kiss Melon Stage', 'General Admission', 2, 700);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
