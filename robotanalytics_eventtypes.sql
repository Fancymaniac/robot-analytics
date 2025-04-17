-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: robotanalytics
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `eventtypes`
--

DROP TABLE IF EXISTS `eventtypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eventtypes` (
  `event_type_id` int NOT NULL AUTO_INCREMENT,
  `event_name` varchar(100) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `severity` enum('low','medium','high','critical') DEFAULT NULL,
  `recommended_actions` text,
  `frequency_days` int DEFAULT NULL,
  `estimated_duration` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`event_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventtypes`
--

LOCK TABLES `eventtypes` WRITE;
/*!40000 ALTER TABLE `eventtypes` DISABLE KEYS */;
INSERT INTO `eventtypes` VALUES (1,'Sensor Failure','Sensor Failure event','critical','Follow standard procedures',30,30,'2021-01-01 00:00:00','2021-01-01 00:00:00'),(2,'Overheating','Overheating event','high','Follow standard procedures',90,60,'2021-01-01 00:00:00','2021-01-01 00:00:00'),(3,'Power Surge','Power Surge event','low','Follow standard procedures',60,120,'2021-01-01 00:00:00','2021-01-01 00:00:00'),(4,'Calibration Error','Calibration Error event','medium','Follow standard procedures',30,30,'2021-01-01 00:00:00','2021-01-01 00:00:00'),(5,'Maintenance Check','Maintenance Check event','high','Follow standard procedures',30,30,'2021-01-01 00:00:00','2021-01-01 00:00:00'),(6,'Routine Inspection','Routine Inspection event','critical','Follow standard procedures',60,120,'2021-01-01 00:00:00','2021-01-01 00:00:00'),(7,'Software Update','Software Update event','high','Follow standard procedures',30,30,'2021-01-01 00:00:00','2021-01-01 00:00:00'),(8,'Mechanical Issue','Mechanical Issue event','medium','Follow standard procedures',60,120,'2021-01-01 00:00:00','2021-01-01 00:00:00'),(9,'Connectivity Issue','Connectivity Issue event','high','Follow standard procedures',30,60,'2021-01-01 00:00:00','2021-01-01 00:00:00'),(10,'Unexpected Shutdown','Unexpected Shutdown event','critical','Follow standard procedures',90,60,'2021-01-01 00:00:00','2021-01-01 00:00:00');
/*!40000 ALTER TABLE `eventtypes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-16  1:18:48
