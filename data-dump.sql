-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: gymdb
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

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
-- Table structure for table `barposition`
--

DROP TABLE IF EXISTS `barposition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barposition` (
  `BarPositionId` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `BarPositionName` varchar(20) NOT NULL,
  PRIMARY KEY (`BarPositionId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barposition`
--

LOCK TABLES `barposition` WRITE;
/*!40000 ALTER TABLE `barposition` DISABLE KEYS */;
INSERT INTO `barposition` VALUES (1,'Low Bar'),(2,'High Bar'),(3,'Front'),(4,'Zercher');
/*!40000 ALTER TABLE `barposition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bartype`
--

DROP TABLE IF EXISTS `bartype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bartype` (
  `BarTypeId` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `BarTypeName` varchar(30) NOT NULL,
  PRIMARY KEY (`BarTypeId`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bartype`
--

LOCK TABLES `bartype` WRITE;
/*!40000 ALTER TABLE `bartype` DISABLE KEYS */;
INSERT INTO `bartype` VALUES (1,'Stiff Bar'),(2,'Squat Bar'),(3,'Deadlift Bar'),(4,'Trap Bar'),(5,'Football Bar'),(6,'Safety Squat Bar');
/*!40000 ALTER TABLE `bartype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deadliftstance`
--

DROP TABLE IF EXISTS `deadliftstance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deadliftstance` (
  `DeadliftStanceId` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `DeadliftStanceName` varchar(45) NOT NULL,
  PRIMARY KEY (`DeadliftStanceId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deadliftstance`
--

LOCK TABLES `deadliftstance` WRITE;
/*!40000 ALTER TABLE `deadliftstance` DISABLE KEYS */;
INSERT INTO `deadliftstance` VALUES (1,'Conventional'),(2,'Sumo');
/*!40000 ALTER TABLE `deadliftstance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `display_exercise`
--

DROP TABLE IF EXISTS `display_exercise`;
/*!50001 DROP VIEW IF EXISTS `display_exercise`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `display_exercise` AS SELECT 
 1 AS `SessionId`,
 1 AS `ExerciseId`,
 1 AS `BarTypeName`,
 1 AS `BarPositionName`,
 1 AS `ExerciseTypeName`,
 1 AS `PinHeight`,
 1 AS `SnatchGrip`,
 1 AS `Pause`,
 1 AS `Belt`,
 1 AS `GripWidthName`,
 1 AS `DeadliftStanceName`,
 1 AS `TempoType`,
 1 AS `StanceWidthName`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `exercise`
--

DROP TABLE IF EXISTS `exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exercise` (
  `ExerciseId` int unsigned NOT NULL AUTO_INCREMENT,
  `SessionId` int unsigned NOT NULL,
  `ExerciseTypeId` int unsigned NOT NULL,
  `StanceWidthId` tinyint unsigned DEFAULT NULL,
  `GripWidthId` tinyint unsigned DEFAULT NULL,
  `BarPositionId` tinyint unsigned DEFAULT NULL,
  `BarTypeId` tinyint unsigned DEFAULT NULL,
  `Belt` tinyint DEFAULT NULL,
  `TempoId` smallint unsigned DEFAULT NULL,
  `Pause` tinyint DEFAULT NULL,
  `PinId` int unsigned DEFAULT NULL,
  `DeadliftStanceId` tinyint unsigned DEFAULT NULL,
  `SnatchGrip` tinyint DEFAULT NULL,
  PRIMARY KEY (`ExerciseId`),
  KEY `fk_session` (`SessionId`),
  KEY `fk_extype` (`ExerciseTypeId`),
  KEY `fk_stance` (`StanceWidthId`),
  KEY `fk_grip` (`GripWidthId`),
  KEY `fk_barpos` (`BarPositionId`),
  KEY `fk_btype` (`BarTypeId`),
  KEY `fk_tempo` (`TempoId`),
  KEY `fk_pin` (`PinId`),
  CONSTRAINT `fk_barpos` FOREIGN KEY (`BarPositionId`) REFERENCES `barposition` (`BarPositionId`),
  CONSTRAINT `fk_btype` FOREIGN KEY (`BarTypeId`) REFERENCES `bartype` (`BarTypeId`),
  CONSTRAINT `fk_extype` FOREIGN KEY (`ExerciseTypeId`) REFERENCES `exercisetype` (`ExerciseTypeId`),
  CONSTRAINT `fk_grip` FOREIGN KEY (`GripWidthId`) REFERENCES `gripwidth` (`GripWidthId`),
  CONSTRAINT `fk_pin` FOREIGN KEY (`PinId`) REFERENCES `pin` (`PinId`),
  CONSTRAINT `fk_session` FOREIGN KEY (`SessionId`) REFERENCES `session` (`SessionId`) ON DELETE CASCADE,
  CONSTRAINT `fk_stance` FOREIGN KEY (`StanceWidthId`) REFERENCES `stancewidth` (`StanceWidthId`),
  CONSTRAINT `fk_tempo` FOREIGN KEY (`TempoId`) REFERENCES `tempo` (`TempoId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercise`
--

LOCK TABLES `exercise` WRITE;
/*!40000 ALTER TABLE `exercise` DISABLE KEYS */;
/*!40000 ALTER TABLE `exercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercisetype`
--

DROP TABLE IF EXISTS `exercisetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exercisetype` (
  `ExerciseTypeId` int unsigned NOT NULL AUTO_INCREMENT,
  `ExerciseTypeName` varchar(45) NOT NULL,
  `DisplayOrder` tinyint NOT NULL,
  PRIMARY KEY (`ExerciseTypeId`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercisetype`
--

LOCK TABLES `exercisetype` WRITE;
/*!40000 ALTER TABLE `exercisetype` DISABLE KEYS */;
INSERT INTO `exercisetype` VALUES (1,'Squat',1),(2,'Bench Press',1),(3,'Deadlift',1),(4,'Chin Up',4),(5,'Bent Over Row',4),(6,'Dumbbell Press',2),(7,'Incline Press',2),(8,'Romanian Deadlift',5),(9,'Stiff Legged Deadlift',5),(10,'Shoulder Press',2),(11,'Bicep Curls',4),(12,'Lateral Raises',2),(13,'Rear Delt Flies',4),(14,'Chest Flies',2),(15,'Tricep Extensions',2),(16,'Bulgarian Split Squats',3),(17,'Hamstring Curls',5),(18,'Leg Extensions',3);
/*!40000 ALTER TABLE `exercisetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gripwidth`
--

DROP TABLE IF EXISTS `gripwidth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gripwidth` (
  `GripWidthId` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `GripWidthName` varchar(30) NOT NULL,
  PRIMARY KEY (`GripWidthId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gripwidth`
--

LOCK TABLES `gripwidth` WRITE;
/*!40000 ALTER TABLE `gripwidth` DISABLE KEYS */;
INSERT INTO `gripwidth` VALUES (1,'Competition Grip'),(2,'Close Grip'),(3,'Wide Grip');
/*!40000 ALTER TABLE `gripwidth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pin`
--

DROP TABLE IF EXISTS `pin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pin` (
  `PinId` int unsigned NOT NULL AUTO_INCREMENT,
  `PinHeight` varchar(20) NOT NULL,
  PRIMARY KEY (`PinId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pin`
--

LOCK TABLES `pin` WRITE;
/*!40000 ALTER TABLE `pin` DISABLE KEYS */;
INSERT INTO `pin` VALUES (1,'No Pin'),(2,'Low Pin'),(3,'Medium Pin'),(4,'High Pin');
/*!40000 ALTER TABLE `pin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session` (
  `SessionId` int unsigned NOT NULL AUTO_INCREMENT,
  `User` int unsigned NOT NULL,
  `SessionDate` date NOT NULL,
  `SessionTime` int unsigned NOT NULL,
  `SessionName` varchar(50) DEFAULT NULL,
  `SessionRPE` tinyint unsigned NOT NULL,
  `SessionAU` smallint GENERATED ALWAYS AS ((`SessionTime` * `SessionRPE`)) VIRTUAL,
  PRIMARY KEY (`SessionId`),
  KEY `fk_user` (`User`),
  CONSTRAINT `fk_user` FOREIGN KEY (`User`) REFERENCES `user` (`UserId`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
INSERT INTO `session` (`SessionId`, `User`, `SessionDate`, `SessionTime`, `SessionName`, `SessionRPE`) VALUES (1,1,'0000-00-00',120,'Test',5);
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sets`
--

DROP TABLE IF EXISTS `sets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sets` (
  `SetId` int unsigned NOT NULL AUTO_INCREMENT,
  `ExerciseId` int unsigned NOT NULL,
  `Reps` int unsigned NOT NULL,
  `Weight` decimal(4,1) unsigned NOT NULL,
  `RPE` decimal(4,1) unsigned NOT NULL,
  PRIMARY KEY (`SetId`),
  KEY `fk_exercise` (`ExerciseId`),
  CONSTRAINT `fk_exercise` FOREIGN KEY (`ExerciseId`) REFERENCES `exercise` (`ExerciseId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sets`
--

LOCK TABLES `sets` WRITE;
/*!40000 ALTER TABLE `sets` DISABLE KEYS */;
/*!40000 ALTER TABLE `sets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stancewidth`
--

DROP TABLE IF EXISTS `stancewidth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stancewidth` (
  `StanceWidthId` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `StanceWidthName` varchar(30) NOT NULL,
  PRIMARY KEY (`StanceWidthId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stancewidth`
--

LOCK TABLES `stancewidth` WRITE;
/*!40000 ALTER TABLE `stancewidth` DISABLE KEYS */;
INSERT INTO `stancewidth` VALUES (1,'Competition Stance'),(2,'Narrow Stance'),(3,'Wide Stance');
/*!40000 ALTER TABLE `stancewidth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tempo`
--

DROP TABLE IF EXISTS `tempo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tempo` (
  `TempoId` smallint unsigned NOT NULL AUTO_INCREMENT,
  `TempoType` char(4) NOT NULL,
  PRIMARY KEY (`TempoId`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tempo`
--

LOCK TABLES `tempo` WRITE;
/*!40000 ALTER TABLE `tempo` DISABLE KEYS */;
INSERT INTO `tempo` VALUES (1,'None'),(2,'210'),(3,'310'),(4,'320'),(5,'510'),(6,'303');
/*!40000 ALTER TABLE `tempo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `UserId` int unsigned NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(25) NOT NULL,
  `LastName` varchar(25) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Username` varchar(45) NOT NULL,
  `Password` char(255) NOT NULL,
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Irene','McNamara','irenemcnamara@gmail.com','irene','123456789');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `display_exercise`
--

/*!50001 DROP VIEW IF EXISTS `display_exercise`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `display_exercise` AS select `e`.`SessionId` AS `SessionId`,`e`.`ExerciseId` AS `ExerciseId`,coalesce(`a`.`BarTypeName`,'') AS `BarTypeName`,coalesce(`b`.`BarPositionName`,'') AS `BarPositionName`,coalesce(`t`.`ExerciseTypeName`,'') AS `ExerciseTypeName`,coalesce(`p`.`PinHeight`,'') AS `PinHeight`,coalesce(`e`.`SnatchGrip`,'') AS `SnatchGrip`,`e`.`Pause` AS `Pause`,`e`.`Belt` AS `Belt`,coalesce(`g`.`GripWidthName`,'') AS `GripWidthName`,coalesce(`d`.`DeadliftStanceName`,'') AS `DeadliftStanceName`,coalesce(`o`.`TempoType`,'') AS `TempoType`,coalesce(`s`.`StanceWidthName`,'') AS `StanceWidthName` from ((((((((`exercise` `e` left join `bartype` `a` on((`e`.`BarTypeId` = `a`.`BarTypeId`))) left join `barposition` `b` on((`e`.`BarPositionId` = `b`.`BarPositionId`))) left join `exercisetype` `t` on((`e`.`ExerciseTypeId` = `t`.`ExerciseTypeId`))) left join `pin` `p` on((`e`.`PinId` = `p`.`PinId`))) left join `gripwidth` `g` on((`e`.`GripWidthId` = `g`.`GripWidthId`))) left join `deadliftstance` `d` on((`e`.`DeadliftStanceId` = `d`.`DeadliftStanceId`))) left join `tempo` `o` on((`e`.`TempoId` = `o`.`TempoId`))) left join `stancewidth` `s` on((`e`.`StanceWidthId` = `s`.`StanceWidthId`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-25 15:23:42
