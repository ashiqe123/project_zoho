-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2023 at 01:46 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zohodb`
--

-- --------------------------------------------------------

--
-- Table structure for table `zohoapp_customer`
--

CREATE TABLE `zohoapp_customer` (
  `id` bigint(20) NOT NULL,
  `customerName` varchar(100) DEFAULT NULL,
  `customerType` varchar(100) DEFAULT NULL,
  `companyName` varchar(100) DEFAULT NULL,
  `customerEmail` varchar(100) DEFAULT NULL,
  `customerWorkPhone` varchar(100) DEFAULT NULL,
  `customerMobile` varchar(100) DEFAULT NULL,
  `skype` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `department` varchar(100) DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  `GSTTreatment` varchar(100) DEFAULT NULL,
  `placeofsupply` varchar(100) DEFAULT NULL,
  `Taxpreference` varchar(100) DEFAULT NULL,
  `currency` varchar(100) DEFAULT NULL,
  `OpeningBalance` int(11) DEFAULT NULL,
  `PaymentTerms` varchar(100) DEFAULT NULL,
  `PriceList` varchar(100) DEFAULT NULL,
  `PortalLanguage` varchar(100) DEFAULT NULL,
  `Facebook` varchar(100) DEFAULT NULL,
  `Twitter` varchar(100) DEFAULT NULL,
  `Attention` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `Address1` varchar(100) DEFAULT NULL,
  `Address2` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `zipcode` varchar(100) DEFAULT NULL,
  `phone1` varchar(100) DEFAULT NULL,
  `fax` varchar(100) DEFAULT NULL,
  `CPsalutation` varchar(100) DEFAULT NULL,
  `Firstname` varchar(100) DEFAULT NULL,
  `Lastname` varchar(100) DEFAULT NULL,
  `CPemail` varchar(100) DEFAULT NULL,
  `CPphone` varchar(100) DEFAULT NULL,
  `CPmobile` varchar(100) DEFAULT NULL,
  `CPskype` varchar(100) DEFAULT NULL,
  `CPdesignation` varchar(100) DEFAULT NULL,
  `CPdepartment` varchar(100) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `zohoapp_customer`
--
ALTER TABLE `zohoapp_customer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `zohoapp_customer_user_id_3f99e967_fk_auth_user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `zohoapp_customer`
--
ALTER TABLE `zohoapp_customer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `zohoapp_customer`
--
ALTER TABLE `zohoapp_customer`
  ADD CONSTRAINT `zohoapp_customer_user_id_3f99e967_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
