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
-- Table structure for table `robotmodels`
--

DROP TABLE IF EXISTS `robotmodels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `robotmodels` (
  `model_id` int NOT NULL AUTO_INCREMENT,
  `manufacturer` varchar(100) DEFAULT NULL,
  `model_name` varchar(100) NOT NULL,
  `model_type` varchar(50) DEFAULT NULL,
  `payload_capacity` decimal(10,2) DEFAULT NULL,
  `reach` decimal(5,2) DEFAULT NULL,
  `energy_rating` decimal(5,2) DEFAULT NULL,
  `specifications` json DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`model_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `robotmodels`
--

LOCK TABLES `robotmodels` WRITE;
/*!40000 ALTER TABLE `robotmodels` DISABLE KEYS */;
INSERT INTO `robotmodels` VALUES (1,'Kuka','PAI-214','Painting',53.75,1.19,3.01,'{\"axes\": 6, \"max_speed\": 204}','2021-01-01 00:00:00','2021-01-01 00:00:00'),(2,'Kuka','PAI-858','Painting',183.83,0.72,4.80,'{\"axes\": 4, \"max_speed\": 195}','2021-01-01 00:00:00','2021-01-01 00:00:00'),(3,'ABB','PAI-338','Painting',125.80,0.57,2.79,'{\"axes\": 6, \"max_speed\": 818}','2021-01-01 00:00:00','2021-01-01 00:00:00'),(4,'Kuka','WEL-529','Welding',83.07,1.97,8.28,'{\"axes\": 4, \"max_speed\": 877}','2021-01-01 00:00:00','2021-01-01 00:00:00'),(5,'ABB','WEL-814','Welding',113.39,1.19,2.94,'{\"axes\": 5, \"max_speed\": 204}','2021-01-01 00:00:00','2021-01-01 00:00:00'),(6,'ABB','WEL-489','Welding',64.51,2.62,6.43,'{\"axes\": 4, \"max_speed\": 847}','2021-01-01 00:00:00','2021-01-01 00:00:00');
/*!40000 ALTER TABLE `robotmodels` ENABLE KEYS */;
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
