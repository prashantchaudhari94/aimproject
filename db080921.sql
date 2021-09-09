-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: packer
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `article` (
  `article_id` int NOT NULL AUTO_INCREMENT,
  `article_name` varchar(25) DEFAULT NULL,
  `base_material` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`article_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `article_list`
--

DROP TABLE IF EXISTS `article_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `article_list` (
  `article_list_id` int NOT NULL AUTO_INCREMENT,
  `enquiry_id` int DEFAULT NULL,
  `visit_id` int DEFAULT NULL,
  `drawing_room` varchar(100) DEFAULT NULL,
  `center_room` varchar(100) DEFAULT NULL,
  `bed_room` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`article_list_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cost_table`
--

DROP TABLE IF EXISTS `cost_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cost_table` (
  `cost_id` int NOT NULL AUTO_INCREMENT,
  `stock_id` int DEFAULT NULL,
  `memo_id` int DEFAULT NULL,
  `qty_issued` int DEFAULT NULL,
  `qty_returned` int DEFAULT NULL,
  `cost_to_memo` int DEFAULT NULL,
  `current_stock` int DEFAULT NULL,
  PRIMARY KEY (`cost_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `enquiry`
--

DROP TABLE IF EXISTS `enquiry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enquiry` (
  `enquiry_id` int NOT NULL AUTO_INCREMENT,
  `enquiry_mode` varchar(25) DEFAULT NULL,
  `enq_date` datetime DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `mobile_no` bigint DEFAULT NULL,
  `email_id` varchar(25) DEFAULT NULL,
  `date_tentative` date DEFAULT NULL,
  `address_load` varchar(100) DEFAULT NULL,
  `address_unload` varchar(100) DEFAULT NULL,
  `house_size_load` int DEFAULT NULL,
  `house_area_unload` int DEFAULT NULL,
  `floor_no_load` int DEFAULT NULL,
  `floor_no_unload` int DEFAULT NULL,
  `lift_available_load` tinyint(1) DEFAULT NULL,
  `lift_available_unload` tinyint(1) DEFAULT NULL,
  `visit_req` tinyint(1) DEFAULT NULL,
  `inv_req` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`enquiry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `enquiry1`
--

DROP TABLE IF EXISTS `enquiry1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enquiry1` (
  `enquiry_no_id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `date_of_enquiry` date DEFAULT NULL,
  `party_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `party_mobile_no` varchar(11) DEFAULT NULL,
  `party_mail_id` varchar(40) DEFAULT NULL,
  `tentative_shifting_date` date DEFAULT NULL,
  `address_loading` varchar(100) DEFAULT NULL,
  `city_loading` varchar(25) DEFAULT NULL,
  `address_unloading` varchar(100) DEFAULT NULL,
  `city_unloading` varchar(25) DEFAULT NULL,
  `household_size` int DEFAULT NULL,
  `lift_availability_loading` varchar(50) DEFAULT NULL,
  `lift_availability_unloading` varchar(50) DEFAULT NULL,
  `floor_no_loading` int DEFAULT NULL,
  `floor_no_unloading` int DEFAULT NULL,
  `preferred_visit_date` date DEFAULT NULL,
  `insurance_required` varchar(50) DEFAULT NULL,
  `visit_required` varchar(50) DEFAULT NULL,
  `package` varchar(10) DEFAULT NULL,
  `memo_id` int DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`enquiry_no_id`)
) ENGINE=InnoDB AUTO_INCREMENT=148 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `executive`
--

DROP TABLE IF EXISTS `executive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `executive` (
  `executive_id` int NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `email_id` varchar(25) DEFAULT NULL,
  `contact_no` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`executive_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fright`
--

DROP TABLE IF EXISTS `fright`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fright` (
  `fright_id` int NOT NULL AUTO_INCREMENT,
  `vehicle_type` varchar(20) DEFAULT NULL,
  `covered` tinyint(1) DEFAULT NULL,
  `owned` tinyint(1) DEFAULT NULL,
  `registration_No` varchar(20) DEFAULT NULL,
  `base_rate` int DEFAULT NULL,
  `height` int DEFAULT NULL,
  `width` int DEFAULT NULL,
  `length` int DEFAULT NULL,
  `rto_compliant` tinyint(1) DEFAULT NULL,
  `driver_caretaker` varchar(15) DEFAULT NULL,
  `driver_mob` int DEFAULT NULL,
  PRIMARY KEY (`fright_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `house_size`
--

DROP TABLE IF EXISTS `house_size`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `house_size` (
  `house_size_id` int NOT NULL AUTO_INCREMENT,
  `article_name` varchar(25) DEFAULT NULL,
  `base_material` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`house_size_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `labour_master`
--

DROP TABLE IF EXISTS `labour_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `labour_master` (
  `labour_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `adhar_card_no` varchar(12) DEFAULT NULL,
  `phone_no` varchar(12) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `wage_p_day` int DEFAULT NULL,
  `referred_by` varchar(40) DEFAULT NULL,
  `police_verification` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`labour_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `material`
--

DROP TABLE IF EXISTS `material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material` (
  `material_id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `material_name` varchar(40) DEFAULT NULL,
  `purchse_UM` int DEFAULT NULL,
  `consumption_UM` int DEFAULT NULL,
  `returnable` tinyint(1) DEFAULT NULL,
  `dep_percen_per_usage` int DEFAULT NULL,
  `op_stk_at_inception` int DEFAULT NULL,
  `stock_UM` int DEFAULT NULL,
  `op_stk_rate` int DEFAULT NULL,
  `Qty_issued` int DEFAULT NULL,
  PRIMARY KEY (`material_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `memo`
--

DROP TABLE IF EXISTS `memo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `memo` (
  `memo_id` int NOT NULL AUTO_INCREMENT,
  `memo_date` date DEFAULT NULL,
  `visit_no_id` int DEFAULT NULL,
  `enquiry_no_id` int DEFAULT NULL,
  `consignor` varchar(40) DEFAULT NULL,
  `consignor_address` varchar(100) DEFAULT NULL,
  `consignee` varchar(40) DEFAULT NULL,
  `consingnee_address` varchar(100) DEFAULT NULL,
  `driver_name` varchar(40) DEFAULT NULL,
  `driver_allowance` int DEFAULT NULL,
  `superviser_name` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `superviser_amt` int DEFAULT NULL,
  `good_description` varchar(500) DEFAULT NULL,
  `truck_no` varchar(12) DEFAULT NULL,
  `truck_owner` varchar(40) DEFAULT NULL,
  `labour_name` varchar(100) DEFAULT NULL,
  `labour_charges` int DEFAULT NULL,
  `fright_charges` int DEFAULT NULL,
  PRIMARY KEY (`memo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `quotation`
--

DROP TABLE IF EXISTS `quotation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quotation` (
  `quotation_no_id` int NOT NULL AUTO_INCREMENT,
  `enquiry_no_id` int DEFAULT NULL,
  `visit_no_id` int DEFAULT NULL,
  `party_name` varchar(50) DEFAULT NULL,
  `quotation_date` date DEFAULT NULL,
  `charges_type` varchar(15) DEFAULT NULL,
  `details` varchar(600) DEFAULT NULL,
  `offer_details` varchar(600) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `tax` int DEFAULT NULL,
  `invoice_required` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`quotation_no_id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock` (
  `stock_id` int NOT NULL AUTO_INCREMENT,
  `material_id` int DEFAULT NULL,
  `opening_qty` int DEFAULT NULL,
  `cost_p_unit` int DEFAULT NULL,
  `dep_rate` int DEFAULT NULL,
  `total_stock_value` int DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `uom`
--

DROP TABLE IF EXISTS `uom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uom` (
  `uom_id` int NOT NULL AUTO_INCREMENT,
  `UM_code` int DEFAULT NULL,
  `UM_description` varchar(100) DEFAULT NULL,
  `alt_UM_code` varchar(15) DEFAULT NULL,
  `alt_UM_description` varchar(80) DEFAULT NULL,
  `base_UM_qty` int DEFAULT NULL,
  `alt_uom_qty` int DEFAULT NULL,
  PRIMARY KEY (`uom_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `visit`
--

DROP TABLE IF EXISTS `visit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visit` (
  `visit_no_id` int NOT NULL AUTO_INCREMENT,
  `preferred_visit_date` date DEFAULT NULL,
  `enquiry_no_id` int DEFAULT NULL,
  `visit_Executor_name` varchar(25) DEFAULT NULL,
  `article_list` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`visit_no_id`)
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `visit_customer`
--

DROP TABLE IF EXISTS `visit_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visit_customer` (
  `visit_id` int NOT NULL AUTO_INCREMENT,
  `enquiry_id` int DEFAULT NULL,
  `scheduled_visit_dt` date DEFAULT NULL,
  `visit_dt` date DEFAULT NULL,
  `executive_name` varchar(30) DEFAULT NULL,
  `article_list_id` int DEFAULT NULL,
  `sp_notes` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`visit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-08 15:00:41
