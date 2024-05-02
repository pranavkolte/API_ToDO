-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 02, 2024 at 08:00 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `todoapi`
--

-- --------------------------------------------------------

--
-- Table structure for table `lists`
--

CREATE TABLE `lists` (
  `TID` varchar(256) NOT NULL,
  `UID` varchar(256) NOT NULL,
  `name` varchar(256) NOT NULL,
  `description` varchar(1024) DEFAULT NULL,
  `due` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lists`
--

INSERT INTO `lists` (`TID`, `UID`, `name`, `description`, `due`) VALUES
('11A2A17521', '7c40eb71b34356ba0de8112cb68ad196fdef1f23', 'FOFO', 'make candles', '12/06/2024'),
('77D2DC20A0', '7c40eb71b34356ba0de8112cb68ad196fdef1f23', 'helowa', NULL, NULL),
('96A2E5503C', '7c40eb71b34356ba0de8112cb68ad196fdef1f23', 'kloa', 'jsojdsa', '12664'),
('DD3E06F857', 'ed6ca046840450b021403a27bd8a334c3fa6c990', 'GOOjo', 'jsojdsa', '12664');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `UID` varchar(256) NOT NULL,
  `name` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UID`, `name`, `email`, `password`) VALUES
('079af67e37416ae0e7628b8a9699e9abab6e2261', 'Pranav Kolte', 'pranavk@gmai.com', '03AC674216F3E15C761EE1A5E255F067953623C8B388B4459E13F978D7C846F4'),
('7c40eb71b34356ba0de8112cb68ad196fdef1f23', 'Pranav kolte', 'admin@gmail.com', '03AC674216F3E15C761EE1A5E255F067953623C8B388B4459E13F978D7C846F4'),
('7de1f9896c91e24a1a9e330ba455ccf34887ac60', 'Pranav kolte', 'admin1@gmail.com', '03AC674216F3E15C761EE1A5E255F067953623C8B388B4459E13F978D7C846F4'),
('ed6ca046840450b021403a27bd8a334c3fa6c990', 'Pranav Kolte', 'pranav@gmail.com', '03AC674216F3E15C761EE1A5E255F067953623C8B388B4459E13F978D7C846F4');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `lists`
--
ALTER TABLE `lists`
  ADD PRIMARY KEY (`TID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`UID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
