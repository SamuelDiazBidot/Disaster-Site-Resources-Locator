-- MariaDB dump 10.17  Distrib 10.4.12-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: project_db
-- ------------------------------------------------------
-- Server version	10.4.12-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `address` (
  `address_id` int(11) NOT NULL AUTO_INCREMENT,
  `country` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `city` varchar(25) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `street` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `district` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `zipcode` varchar(9) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `longitude` float(7,4) DEFAULT NULL,
  `latitude` float(7,4) DEFAULT NULL,
  PRIMARY KEY (`address_id`)
) ENGINE=InnoDB AUTO_INCREMENT=185 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (1,'Puerto Rico','Mayaguez','calle bosque #15','mayaguez','00680',18.2013,67.1452),(2,'Puerto Rico','gurabo','yerbabuena ciudad jardin','guayama','00778',18.2544,65.9729),(3,'Puerto Rico','ponce','calle jose marin','ponce','00716',18.0111,66.6141),(4,'Puerto Rico','ponce','calle jose bolivar','ponce','00716',18.0111,66.6141),(5,'Puerto Rico','arecibo','calle colon','arecibo','00612',18.4442,66.6464),(6,'Puerto Rico','caguas','calle betances','guayama','00725',18.2388,66.0352),(7,'Puerto Rico','Bayamón','Robles','Arecibo','000377',18.1147,-66.8269),(8,'Puerto Rico','Bayamón','Pájaros','Arecibo','000347',18.3563,-65.8547),(9,'Puerto Rico','Bayamón','Pájaros','Ponce','000133',18.1270,-65.6813),(10,'Puerto Rico','San Juan','Pájaros','Ponce','000690',18.3446,-66.9719),(11,'Puerto Rico','Cabo Rojo','Rosado','Ponce','000548',18.2155,-66.5575),(12,'Puerto Rico','Mayagüez','Bosque','San Juan','000436',18.3724,-66.9737),(13,'Puerto Rico','San Juan','Rosado','Carolina','000251',18.0850,-66.6855),(14,'Puerto Rico','Mayagüez','Bosque','Humacao','000829',18.0948,-66.1723),(15,'Puerto Rico','Cabo Rojo','Las Piedras','Mayagüez','000306',18.2772,-66.9081),(16,'Puerto Rico','Cabo Rojo','Rosado','Ponce','000216',18.1490,-66.1726),(17,'Puerto Rico','San Juan','Bosque','San Juan','000736',18.3242,-66.0895),(18,'Puerto Rico','Cabo Rojo','Rosado','Guayama','000721',18.2943,-66.9606),(19,'Puerto Rico','Mayagüez','Robles','Mayagüez','000676',18.2766,-66.5265),(20,'Puerto Rico','Mayagüez','Pájaros','San Juan','000622',18.3231,-66.5534),(21,'Puerto Rico','Bayamón','Robles','San Juan','000461',18.2168,-65.8599),(22,'Puerto Rico','Cabo Rojo','Rosado','Ponce','000216',18.1490,-66.1726),(23,'Puerto Rico','Cabo Rojo','Bosque','San Juan','000372',18.2620,-65.8451),(24,'Puerto Rico','Cabo Rojo','Rosado','Ponce','00017',18.0911,-66.1354),(25,'Puerto Rico','San Juan','Pájaros','Humacao','000426',18.1145,-66.4079),(26,'Puerto Rico','Bayamón','Bosque','Bayamón','000941',18.0862,-65.8018),(27,'Puerto Rico','Mayagüez','Bosque','Bayamón','000961',18.0696,-67.0187),(28,'Puerto Rico','Bayamón','Rosado','Humacao','000889',18.0994,-66.7500),(29,'Puerto Rico','Mayagüez','Rosado','Humacao','000824',18.2249,-65.9734),(30,'Puerto Rico','Bayamón','Robles','Bayamón','000927',18.1449,-66.8162),(31,'Puerto Rico','Cabo Rojo','Robles','Mayagüez','000613',18.0014,-66.2854),(32,'Puerto Rico','Bayamón','Bosque','Mayagüez','000688',18.0920,-66.0244),(33,'Puerto Rico','San Juan','Bosque','Carolina','000692',18.1311,-66.4083),(34,'Puerto Rico','San Juan','Las Piedras','Mayagüez','000763',18.3360,-66.0596),(35,'Puerto Rico','Cabo Rojo','Bosque','Guayama','000830',18.1893,-66.1891),(36,'Puerto Rico','Cabo Rojo','Pájaros','Bayamón','000946',18.0421,-66.4347),(37,'Puerto Rico','Cabo Rojo','Pájaros','Bayamón','000946',18.0421,-66.4347),(38,'Puerto Rico','Bayamón','Robles','Bayamón','00021',18.3172,-65.6821),(39,'Puerto Rico','Bayamón','Robles','Bayamón','00021',18.3172,-65.6821),(40,'Puerto Rico','Cabo Rojo','Las Piedras','Mayagüez','000306',18.2772,-66.9081),(41,'Puerto Rico','Cabo Rojo','Las Piedras','Mayagüez','000306',18.2772,-66.9081),(42,'Puerto Rico','Mayagüez','Rosado','Guayama','000258',18.3128,-65.7638),(43,'Puerto Rico','Mayagüez','Las Piedras','San Juan','0000',18.1034,-65.9425),(44,'Puerto Rico','Mayagüez','Las Piedras','Mayagüez','000805',18.1301,-65.7341),(45,'Puerto Rico','Cabo Rojo','Las Piedras','San Juan','00091',18.1735,-65.6990),(46,'Puerto Rico','Mayagüez','Las Piedras','Bayamón','00019',18.1073,-66.0953),(47,'Puerto Rico','Bayamón','Bosque','San Juan','000322',18.0513,-66.2509),(48,'Puerto Rico','Bayamón','Robles','Bayamón','000650',18.2514,-66.6558),(49,'Puerto Rico','Bayamón','Bosque','Humacao','00049',18.2335,-66.8584),(50,'Puerto Rico','San Juan','Las Piedras','Bayamón','000693',18.1431,-66.4070),(51,'Puerto Rico','Cabo Rojo','Las Piedras','San Juan','000992',18.1877,-66.7246),(52,'Puerto Rico','Mayagüez','Bosque','Bayamón','000614',18.3266,-65.7645),(53,'Puerto Rico','Bayamón','Robles','Guayama','00025',18.1601,-65.6667),(54,'Puerto Rico','Cabo Rojo','Pájaros','Bayamón','000601',18.1902,-67.1000),(55,'Puerto Rico','Bayamón','Las Piedras','Mayagüez','000996',18.2512,-66.2811),(56,'Puerto Rico','Cabo Rojo','Las Piedras','Guayama','000833',18.1291,-66.1478),(57,'Puerto Rico','Bayamón','Robles','Bayamón','000252',18.2803,-66.4876),(58,'Puerto Rico','Bayamón','Robles','San Juan','000144',18.2945,-66.1900),(59,'Puerto Rico','Bayamón','Pájaros','Mayagüez','000935',18.3685,-65.8683),(60,'Puerto Rico','Bayamón','Pájaros','Carolina','000669',18.0402,-65.7528),(61,'Puerto Rico','San Juan','Las Piedras','Humacao','00066',18.3818,-66.8984),(62,'Puerto Rico','Bayamón','Pájaros','Bayamón','00013',18.1879,-66.8078),(63,'Puerto Rico','Mayagüez','Pájaros','Guayama','000920',18.0590,-66.0981),(64,'Puerto Rico','Cabo Rojo','Las Piedras','Humacao','000933',18.2540,-67.0722),(65,'Puerto Rico','San Juan','Pájaros','Guayama','000299',18.2724,-66.9760),(66,'Puerto Rico','Mayagüez','Robles','Carolina','000636',18.1581,-67.0905),(67,'Puerto Rico','Cabo Rojo','Robles','Guayama','000890',18.2847,-65.8537),(68,'Puerto Rico','Cabo Rojo','Pájaros','Guayama','000749',18.3563,-66.5119),(69,'Puerto Rico','Cabo Rojo','Pájaros','Bayamón','000337',18.1020,-66.7317),(70,'Puerto Rico','Mayagüez','Robles','Humacao','000205',18.1125,-66.4718),(71,'Puerto Rico','San Juan','Robles','San Juan','000880',18.3723,-65.7493),(72,'Puerto Rico','Bayamón','Robles','Humacao','00047',18.0259,-66.1448),(73,'Puerto Rico','Cabo Rojo','Bosque','Carolina','000720',18.3151,-65.8874),(74,'Puerto Rico','Bayamón','Las Piedras','Bayamón','000641',18.1059,-66.3348),(75,'Puerto Rico','San Juan','Rosado','Ponce','000803',18.1815,-66.9133),(76,'Puerto Rico','San Juan','Pájaros','Carolina','000332',18.0161,-66.9135),(77,'Puerto Rico','Mayagüez','Robles','San Juan','000535',18.1268,-66.1696),(78,'Puerto Rico','Bayamón','Rosado','Carolina','000598',18.0578,-65.7886),(79,'Puerto Rico','Mayagüez','Rosado','Guayama','000119',18.0810,-66.8798),(80,'Puerto Rico','San Juan','Las Piedras','Guayama','000790',18.0147,-66.9769),(81,'Puerto Rico','Bayamón','Las Piedras','Carolina','000195',18.3419,-66.1259),(82,'Puerto Rico','Mayagüez','Las Piedras','Humacao','00049',18.0753,-66.9827),(83,'Puerto Rico','Bayamón','Robles','Ponce','000744',18.1020,-65.7862),(84,'Puerto Rico','Mayagüez','Robles','Guayama','000473',18.2623,-65.7760),(85,'Puerto Rico','Mayagüez','Rosado','Humacao','000910',18.1854,-66.0367),(86,'Puerto Rico','Cabo Rojo','Robles','San Juan','000438',18.1847,-65.7440),(87,'Puerto Rico','San Juan','Las Piedras','Bayamón','000516',18.2427,-66.4199),(88,'Puerto Rico','Bayamón','Las Piedras','Ponce','000537',18.3364,-66.7702),(89,'Puerto Rico','Cabo Rojo','Bosque','Guayama','000537',18.3447,-66.4919),(90,'Puerto Rico','Cabo Rojo','Rosado','San Juan','000785',18.2984,-66.3019),(91,'Puerto Rico','San Juan','Robles','Arecibo','000330',18.2840,-66.7766),(92,'Puerto Rico','Cabo Rojo','Pájaros','Mayagüez','000605',18.1850,-66.8981),(93,'Puerto Rico','Bayamón','Pájaros','Carolina','000231',18.3570,-65.7980),(94,'Puerto Rico','Cabo Rojo','Rosado','Guayama','000535',18.0028,-65.9788),(95,'Puerto Rico','Cabo Rojo','Las Piedras','Ponce','000823',18.3362,-66.3786),(96,'Puerto Rico','San Juan','Las Piedras','Arecibo','000458',18.2082,-66.6425),(97,'Puerto Rico','Bayamón','Bosque','Mayagüez','000953',18.1965,-65.9798),(98,'Puerto Rico','Cabo Rojo','Robles','Guayama','000493',18.2305,-66.0966),(99,'Puerto Rico','Mayagüez','Bosque','Arecibo','000468',18.2444,-66.9222),(100,'Puerto Rico','San Juan','Robles','San Juan','000145',18.0501,-66.0898),(101,'Puerto Rico','Bayamón','Pájaros','Bayamón','000294',18.3044,-65.9270),(102,'Puerto Rico','Bayamón','Robles','Mayagüez','000356',18.3670,-67.1132),(103,'Puerto Rico','Mayagüez','Bosque','Guayama','000884',18.2936,-66.3552),(104,'Puerto Rico','Cabo Rojo','Robles','Arecibo','000406',18.0437,-66.4857),(105,'Puerto Rico','Mayagüez','Robles','Guayama','000473',18.2623,-65.7760),(106,'Puerto Rico','Mayagüez','Robles','Guayama','000473',18.2623,-65.7760),(107,'Puerto Rico','Cabo Rojo','Robles','Mayagüez','000818',18.3371,-66.4700),(108,'Puerto Rico','Cabo Rojo','Robles','Mayagüez','000818',18.3371,-66.4700),(109,'Puerto Rico','Cabo Rojo','Robles','Carolina','000590',18.2986,-66.5340),(110,'Puerto Rico','Cabo Rojo','Robles','Carolina','000590',18.2986,-66.5340),(111,'Puerto Rico','Mayagüez','Pájaros','San Juan','000896',18.2462,-65.7682),(112,'Puerto Rico','Mayagüez','Pájaros','San Juan','000896',18.2462,-65.7682),(113,'Puerto Rico','Mayagüez','Las Piedras','Carolina','00099',18.0105,-66.9808),(114,'Puerto Rico','Mayagüez','Las Piedras','Carolina','00099',18.0105,-66.9808),(115,'Puerto Rico','Cabo Rojo','Las Piedras','Mayagüez','000827',18.1899,-66.9521),(116,'Puerto Rico','Cabo Rojo','Las Piedras','Mayagüez','000827',18.1899,-66.9521),(117,'Puerto Rico','Cabo Rojo','Pájaros','Bayamón','000702',18.0767,-66.3698),(118,'Puerto Rico','Cabo Rojo','Pájaros','Bayamón','000702',18.0767,-66.3698),(119,'Puerto Rico','Bayamón','Pájaros','Guayama','000903',18.3563,-66.0207),(120,'Puerto Rico','Bayamón','Pájaros','Guayama','000903',18.3563,-66.0207),(121,'Puerto Rico','Cabo Rojo','Robles','Arecibo','000212',18.3739,-67.0218),(122,'Puerto Rico','Cabo Rojo','Robles','Arecibo','000212',18.3739,-67.0218),(123,'Puerto Rico','San Juan','Las Piedras','Arecibo','000105',18.3034,-65.6978),(124,'Puerto Rico','San Juan','Las Piedras','Arecibo','000105',18.3034,-65.6978),(125,'Puerto Rico','Cabo Rojo','Las Piedras','Humacao','000808',18.2138,-66.6640),(126,'Puerto Rico','Cabo Rojo','Las Piedras','Humacao','000808',18.2138,-66.6640),(127,'Puerto Rico','Bayamón','Las Piedras','Arecibo','000659',18.1990,-66.7162),(128,'Puerto Rico','Bayamón','Las Piedras','Arecibo','000659',18.1990,-66.7162),(129,'Puerto Rico','Mayagüez','Bosque','Bayamón','000891',18.0053,-66.8435),(130,'Puerto Rico','Mayagüez','Bosque','Bayamón','000891',18.0053,-66.8435),(131,'Puerto Rico','Cabo Rojo','Bosque','Guayama','000467',18.3221,-65.9195),(132,'Puerto Rico','Cabo Rojo','Bosque','Guayama','000467',18.3221,-65.9195),(133,'Puerto Rico','Cabo Rojo','Las Piedras','San Juan','000213',18.0225,-65.7494),(134,'Puerto Rico','Cabo Rojo','Las Piedras','San Juan','000213',18.0225,-65.7494),(135,'Puerto Rico','San Juan','Las Piedras','Bayamón','000186',18.1110,-66.1282),(136,'Puerto Rico','San Juan','Las Piedras','Bayamón','000186',18.1110,-66.1282),(137,'Puerto Rico','San Juan','Pájaros','Bayamón','00045',18.1777,-66.6880),(138,'Puerto Rico','San Juan','Pájaros','Bayamón','00045',18.1777,-66.6880),(139,'Puerto Rico','Cabo Rojo','Pájaros','San Juan','000699',18.1637,-66.0134),(140,'Puerto Rico','Cabo Rojo','Pájaros','San Juan','000699',18.1637,-66.0134),(141,'Puerto Rico','Bayamón','Rosado','Humacao','000279',18.0442,-66.6620),(142,'Puerto Rico','Bayamón','Rosado','Humacao','000279',18.0442,-66.6620),(143,'Puerto Rico','Cabo Rojo','Bosque','San Juan','000986',18.2924,-66.6993),(144,'Puerto Rico','Cabo Rojo','Bosque','San Juan','000986',18.2924,-66.6993),(145,'Puerto Rico','Mayagüez','Pájaros','San Juan','000896',18.2462,-65.7682),(146,'Puerto Rico','Mayagüez','Pájaros','San Juan','000896',18.2462,-65.7682),(147,'Puerto Rico','Mayagüez','Pájaros','San Juan','000896',18.2462,-65.7682),(148,'Puerto Rico','San Juan','Robles','Bayamón','000109',18.1956,-66.7575),(149,'Puerto Rico','San Juan','Robles','Bayamón','000109',18.1956,-66.7575),(150,'Puerto Rico','San Juan','Robles','Bayamón','000109',18.1956,-66.7575),(151,'Puerto Rico','Bayamón','Robles','Mayagüez','000356',18.3670,-67.1132),(152,'Puerto Rico','Bayamón','Robles','Mayagüez','000356',18.3670,-67.1132),(153,'Puerto Rico','Bayamón','Robles','Mayagüez','000356',18.3670,-67.1132),(154,'Puerto Rico','Bayamón','Robles','Arecibo','000858',18.2349,-66.9565),(155,'Puerto Rico','Bayamón','Robles','Arecibo','000858',18.2349,-66.9565),(156,'Puerto Rico','Bayamón','Robles','Arecibo','000858',18.2349,-66.9565),(157,'Puerto Rico','San Juan','Las Piedras','San Juan','000565',18.1097,-66.5909),(158,'Puerto Rico','San Juan','Las Piedras','San Juan','000565',18.1097,-66.5909),(159,'Puerto Rico','San Juan','Las Piedras','San Juan','000565',18.1097,-66.5909),(160,'Puerto Rico','Bayamón','Bosque','Guayama','000462',18.3065,-66.2817),(161,'Puerto Rico','Bayamón','Bosque','Guayama','000462',18.3065,-66.2817),(162,'Puerto Rico','Bayamón','Bosque','Guayama','000462',18.3065,-66.2817),(163,'Puerto Rico','Cabo Rojo','Rosado','Arecibo','000181',18.0453,-65.8994),(164,'Puerto Rico','Cabo Rojo','Rosado','Arecibo','000181',18.0453,-65.8994),(165,'Puerto Rico','Cabo Rojo','Rosado','Arecibo','000181',18.0453,-65.8994),(166,'Puerto Rico','San Juan','Robles','Carolina','000560',18.2236,-66.5742),(167,'Puerto Rico','San Juan','Robles','Carolina','000560',18.2236,-66.5742),(168,'Puerto Rico','San Juan','Robles','Carolina','000560',18.2236,-66.5742),(169,'Puerto Rico','Bayamón','Robles','San Juan','000434',18.3442,-66.4783),(170,'Puerto Rico','Bayamón','Robles','San Juan','000434',18.3442,-66.4783),(171,'Puerto Rico','Bayamón','Robles','San Juan','000434',18.3442,-66.4783),(172,'Puerto Rico','San Juan','Robles','Mayagüez','000315',18.0289,-66.0416),(173,'Puerto Rico','San Juan','Robles','Mayagüez','000315',18.0289,-66.0416),(174,'Puerto Rico','San Juan','Robles','Mayagüez','000315',18.0289,-66.0416),(175,'Puerto Rico','Cabo Rojo','Bosque','Humacao','00085',18.2963,-66.9624),(176,'Puerto Rico','San Juan','Bosque','Humacao','000610',18.3719,-66.9120),(177,'Puerto Rico','Bayamón','Robles','Mayagüez','000939',18.2944,-67.1301),(178,'Puerto Rico','Cabo Rojo','Las Piedras','Guayama','000264',18.0732,-67.0438),(179,'Puerto Rico','Bayamón','Rosado','Bayamón','000550',18.0131,-67.0901),(180,'Puerto Rico','Mayagüez','Bosque','Guayama','000884',18.2936,-66.3552),(181,'Puerto Rico','Bayamón','Pájaros','Carolina','000438',18.1136,-67.0237),(182,'Puerto Rico','Cabo Rojo','Bosque','Arecibo','000717',18.0472,-66.8876),(183,'Puerto Rico','Cabo Rojo','Las Piedras','Mayagüez','000803',18.3024,-66.2424),(184,'Puerto Rico','San Juan','Robles','Humacao','000856',18.3477,-66.4366);
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrators`
--

DROP TABLE IF EXISTS `administrators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrators` (
  `administrator_id` int(11) NOT NULL AUTO_INCREMENT,
  `permission_level` int(11) NOT NULL,
  `user_name` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`administrator_id`),
  KEY `user_name` (`user_name`),
  CONSTRAINT `administrators_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `users` (`user_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrators`
--

LOCK TABLES `administrators` WRITE;
/*!40000 ALTER TABLE `administrators` DISABLE KEYS */;
INSERT INTO `administrators` VALUES (1,10,'carlita96'),(3,10,'SomeUser'),(4,10,'Kinpollo'),(5,10,'GenericUser'),(6,10,'OtroUserMas'),(7,10,'deadspacefan'),(8,10,'Garuga'),(9,10,'laZYusER'),(10,10,'SomeSuperUser'),(11,10,'William695486'),(12,10,'William331916'),(13,10,'Michael770653'),(14,10,'Robert522398'),(15,10,'Mary404577'),(16,10,'John800631'),(17,10,'Jennifer151317'),(18,10,'William185759'),(19,10,'John533131'),(20,10,'James872093');
/*!40000 ALTER TABLE `administrators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_information`
--

DROP TABLE IF EXISTS `payment_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment_information` (
  `payment_information_id` int(11) NOT NULL AUTO_INCREMENT,
  `owner_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `card_number` varchar(19) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expiration_date` date NOT NULL,
  `cvv` varchar(4) COLLATE utf8mb4_unicode_ci NOT NULL,
  `requester_id` int(11) NOT NULL,
  PRIMARY KEY (`payment_information_id`),
  KEY `requester_id` (`requester_id`),
  CONSTRAINT `payment_information_ibfk_1` FOREIGN KEY (`requester_id`) REFERENCES `requesters` (`requester_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_information`
--

LOCK TABLES `payment_information` WRITE;
/*!40000 ALTER TABLE `payment_information` DISABLE KEYS */;
INSERT INTO `payment_information` VALUES (1,'John','777360756188004','1991-06-11','188',15),(2,'Linda','8957635712888013','1996-12-18','900',16),(3,'Robert','4101716729791299','1990-07-16','379',17),(4,'Mary','3854162471351550','1991-05-16','164',18),(5,'Patricia','1944595365190840','1997-06-01','928',19),(6,'Mary','829930351916695','1998-11-10','146',20),(7,'Patricia','7807290933181494','1999-10-17','173',21),(8,'Jennifer','675745493941324','1991-09-13','872',22),(9,'William','2638633656923441','1994-12-23','284',23),(10,'William','303574625824523','1991-06-18','416',24);
/*!40000 ALTER TABLE `payment_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `total_payment` decimal(15,2) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  `reservation_id` int(11) NOT NULL,
  `requester_id` int(11) NOT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `reservation_id` (`reservation_id`),
  KEY `requester_id` (`requester_id`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`reservation_id`) REFERENCES `reservations` (`reservation_id`),
  CONSTRAINT `payments_ibfk_2` FOREIGN KEY (`requester_id`) REFERENCES `requesters` (`requester_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,63.69,'1990-09-09',11,56),(2,18.93,'1990-05-01',12,58),(3,371.76,'1997-03-21',13,60),(4,9478.90,'1993-05-17',14,62),(5,39.28,'1991-12-26',15,64),(6,460.90,'1993-06-25',16,66),(7,87.36,'1990-10-27',17,68),(8,2.60,'1997-01-22',18,70),(9,48.97,'1998-07-23',19,72),(10,876.18,'1991-06-09',20,74);
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchases`
--

DROP TABLE IF EXISTS `purchases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `purchases` (
  `purchase_id` int(11) NOT NULL AUTO_INCREMENT,
  `purchase_date` date NOT NULL,
  `supply_id` int(11) NOT NULL,
  `requester_id` int(11) NOT NULL,
  PRIMARY KEY (`purchase_id`),
  KEY `supply_id` (`supply_id`),
  KEY `requester_id` (`requester_id`),
  CONSTRAINT `purchases_ibfk_1` FOREIGN KEY (`supply_id`) REFERENCES `supplies` (`supply_id`),
  CONSTRAINT `purchases_ibfk_2` FOREIGN KEY (`requester_id`) REFERENCES `requesters` (`requester_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchases`
--

LOCK TABLES `purchases` WRITE;
/*!40000 ALTER TABLE `purchases` DISABLE KEYS */;
INSERT INTO `purchases` VALUES (1,'1992-06-22',25,46),(2,'2000-01-19',26,47),(3,'1993-06-02',27,48),(4,'1992-01-02',28,49),(5,'1993-07-27',29,50),(6,'1998-03-17',30,51),(7,'1996-04-16',31,52),(8,'1999-12-03',32,53),(9,'1995-02-18',33,54),(10,'2000-12-23',34,55);
/*!40000 ALTER TABLE `purchases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requesters`
--

DROP TABLE IF EXISTS `requesters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `requesters` (
  `requester_id` int(11) NOT NULL AUTO_INCREMENT,
  `balance` decimal(15,2) DEFAULT NULL,
  `user_name` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`requester_id`),
  KEY `user_name` (`user_name`),
  CONSTRAINT `requesters_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `users` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requesters`
--

LOCK TABLES `requesters` WRITE;
/*!40000 ALTER TABLE `requesters` DISABLE KEYS */;
INSERT INTO `requesters` VALUES (2,140.50,'joseJoestar'),(3,0.00,'marioMan15'),(4,27.83,'starLand12'),(5,722.20,'anusers'),(6,325.20,'estetip'),(7,2.20,'baiabaia'),(8,9014.89,'ADQESFE'),(9,3.71,'QuienSoy'),(10,552.20,'Seeer'),(11,798.45,'IkIk'),(12,3887.51,'Sickick'),(13,7.13,'peterso'),(14,348.94,'Interest'),(15,8565.67,'anewuser'),(16,1.26,'use7'),(17,96.49,'baie8'),(18,30.33,'qes4'),(19,410.54,'dfe5'),(20,3726.48,'qswq5'),(21,202.00,'someus8'),(22,67.18,'Zeus4'),(23,8028.30,'Pollo15'),(24,462.15,'EsteTip9'),(25,1347.99,'UnTiPax'),(26,77.23,'UnTipoAhi'),(27,12.48,'UnTipoAhi14'),(28,9.56,'WooFunciona'),(29,9.52,'Eso Ej 89'),(30,9.38,'QuieroTerm'),(31,47.71,'BadB'),(32,312.44,'BadBu'),(33,19.48,'UnnY'),(34,83.23,'Unknow'),(35,14.43,'None'),(36,778.51,'Ya'),(37,8.47,'YaBata'),(38,821.20,'ImTired'),(39,6120.32,'Jack'),(40,8431.22,'Lol'),(41,4019.60,'Disturbed'),(42,9338.29,'Dinosaurios'),(43,99.21,'Pide'),(44,643.95,'Dioj'),(45,39.40,'Getting'),(46,7071.73,'What'),(47,6.11,'Oh Y741'),(48,5177.88,'JustNumb'),(49,733.93,'POEUY'),(50,33.68,'Youtube'),(51,113.37,'IMCEO'),(52,9900.90,'SonDemasiados'),(53,6679.91,'Aaa'),(54,5.39,'OtroDia'),(55,467.56,'Cnazado'),(56,24.72,'Mary782995'),(57,5.34,'James580747'),(58,4864.27,'Robert939866'),(59,3338.56,'Linda952601'),(60,287.56,'Mary428263'),(61,972.39,'Jennifer243348'),(62,840.46,'Jennifer518644'),(63,3.37,'Linda770034'),(64,3.69,'Jennifer844730'),(65,884.62,'Jennifer405849'),(66,7.10,'Patricia862882'),(67,6.58,'Michael478950'),(68,9236.10,'Robert728057'),(69,2.61,'William639620'),(70,5476.45,'John44455'),(71,99.94,'Jennifer183795'),(72,8605.65,'Robert833321'),(73,4194.97,'Linda519302'),(74,327.38,'Jennifer632351'),(75,6.52,'Patricia31091');
/*!40000 ALTER TABLE `requesters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `requests` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_quantity` int(11) NOT NULL,
  `request_date` date DEFAULT NULL,
  `resource_id` int(11) NOT NULL,
  `requester_id` int(11) NOT NULL,
  PRIMARY KEY (`request_id`),
  KEY `resource_id` (`resource_id`),
  KEY `requester_id` (`requester_id`),
  CONSTRAINT `requests_ibfk_1` FOREIGN KEY (`resource_id`) REFERENCES `resources` (`resource_id`) ON DELETE CASCADE,
  CONSTRAINT `requests_ibfk_2` FOREIGN KEY (`requester_id`) REFERENCES `requesters` (`requester_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
INSERT INTO `requests` VALUES (1,1,'2020-04-20',1,3),(2,3,'2020-04-07',2,2),(3,3,'2020-04-06',4,4),(4,1,'2020-04-07',2,3),(5,3,'2020-04-07',7,2),(6,12,'2020-01-16',8,3),(7,12,'2020-01-16',8,3),(8,47,'1998-09-25',91,27),(9,23,'2000-02-03',92,28),(10,53,'1990-01-11',93,29),(11,39,'1991-07-19',94,30),(12,73,'1994-03-17',95,31),(13,60,'1990-09-09',96,32),(14,72,'1991-11-11',97,33),(15,20,'1995-01-02',98,34),(16,33,'1991-06-10',99,35),(17,98,'1996-04-02',100,36);
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reservations` (
  `reservation_id` int(11) NOT NULL AUTO_INCREMENT,
  `reservation_date` date NOT NULL,
  `reservation_quantity` int(11) NOT NULL,
  `supply_id` int(11) NOT NULL,
  `requester_id` int(11) NOT NULL,
  PRIMARY KEY (`reservation_id`),
  KEY `supply_id` (`supply_id`),
  KEY `requester_id` (`requester_id`),
  CONSTRAINT `reservations_ibfk_1` FOREIGN KEY (`supply_id`) REFERENCES `supplies` (`supply_id`),
  CONSTRAINT `reservations_ibfk_2` FOREIGN KEY (`requester_id`) REFERENCES `requesters` (`requester_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
INSERT INTO `reservations` VALUES (1,'2020-04-24',1,4,4),(2,'1990-07-08',62,15,37),(3,'1999-09-05',63,16,38),(4,'2000-05-07',20,17,39),(5,'1993-01-20',28,18,40),(6,'1994-10-21',23,19,41),(7,'1997-02-06',41,20,42),(8,'1990-06-06',77,21,43),(9,'2000-02-20',36,22,44),(10,'1998-12-09',54,24,45),(11,'1992-09-12',52,35,57),(12,'1991-12-07',6,36,59),(13,'1996-03-06',16,37,61),(14,'1991-12-10',14,38,63),(15,'1992-08-23',35,39,65),(16,'1992-01-26',17,40,67),(17,'1991-07-08',77,41,69),(18,'1991-09-22',88,42,71),(19,'1997-01-15',46,43,73),(20,'1991-09-24',16,44,75);
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources`
--

DROP TABLE IF EXISTS `resources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources` (
  `resource_id` int(11) NOT NULL AUTO_INCREMENT,
  `resource_type` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `resource_name` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `resource_description` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sold` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`resource_id`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources`
--

LOCK TABLES `resources` WRITE;
/*!40000 ALTER TABLE `resources` DISABLE KEYS */;
INSERT INTO `resources` VALUES (1,'waterBottle','nikini','36 8oz bottles value pack',0),(2,'medicine','advil','Total pain relieve',0),(3,'medicine','tylenol','500mg tablets',0),(4,'gasoline','gasolina puma','15 litros',0),(5,'food','gerber baby food','banana flavor',0),(6,'water','nikini','1 gallon',0),(7,'food','carmela','5 cans',0),(8,'water','bottelas de agua','12 bottellas nikini',0),(9,'food','Sazon Goya','36 paquetes sazon goya',1),(10,'Ice','SomeIce','5.lb ice bag.',0),(11,'Power Generators','Planta Portatil','Industrial Power Generator',0),(12,'Heavy Equipment','Digger','Industrial wood saw.',0),(14,'Power Generators','Super Planta','MX100 Power Generator',0),(15,'Water','Cheap Somewhere','1 Water Gallon',0),(16,'Tools','Serrucho','Machine parts.',0),(17,'Water','Home W','1 Water Gallon',0),(20,'Power Generators','Always Working','MX100 Power Generator',0),(21,'Water','Home W','Purified Water',0),(22,'Fuel','Hight Octane Gas','Special fuel 1.gal container.',0),(23,'Fuel','Regular Gas','Gasoline 1.gal container.',0),(24,'Baby Food','Grow Up','Veggies baby food.',0),(25,'Water','Home W','Purified Water',0),(26,'Canned Food','Exotic Food','Canned dog food.',0),(27,'Power Generators','Always Working','MX100 Power Generator',0),(28,'Medical Devices','Batas','MRI',0),(29,'Water','Nikini','Purified Water',0),(30,'Water','Cheap Somewhere','1 Water Gallon',0),(31,'Water','Cheap Somewhere','Purified Water',0),(32,'Clothing','Medias','Elderly clothing.',0),(33,'Baby Food','Healthy BB','Veggies baby food.',0),(34,'Water','Nikini','1 Water Gallon',0),(35,'Medications','EssentialVit','Pain relievers.',0),(36,'Clothing','Gorra','Elderly clothing.',0),(37,'Dry Food','Dry but Good','Dry but Good',0),(38,'Medical Devices','Balanzas','UV lights.',0),(39,'Ice','IceBag','10.lb ice bag.',0),(40,'Medications','Mucinex','Cheap medicine.',0),(41,'Canned Food','Exotic Food','Canned emergency food.',0),(42,'Medications','Mucinex','Cheap medicine.',0),(43,'Ice','SomeIce','10.lb ice bag.',0),(44,'Fuel','Hight Octane Gas','Special fuel 1.gal container.',0),(45,'Clothing','Camisa','Elderly clothing.',0),(46,'Heavy Equipment','Grua','TOMCAT Excavator.',0),(47,'Power Generators','Always Working','Portable Power Generator.',0),(48,'Baby Food','Grow Up','Variety baby food.',0),(49,'Canned Food','Exotic Food','Canned dog food.',0),(50,'Dry Food','Dry but Good','The Gud Stuff',0),(51,'Heavy Equipment','CAT','TOMCAT Excavator.',0),(52,'Medications','Tylenol','Pain relievers.',0),(53,'Heavy Equipment','Drill','Industrial wood saw.',0),(54,'Clothing','Medias','Adult clothing.',0),(55,'Ice','IceBag','5.lb ice bag.',0),(56,'Medical Devices','Balanzas','MRI',0),(57,'Power Generators','Planta Portatil','MX100 Power Generator',0),(58,'Medical Devices','Balanzas','MRI',0),(59,'Clothing','Medias','Elderly clothing.',0),(60,'Heavy Equipment','Drill','TOMCAT Excavator.',0),(61,'Water','Mountain','1 Water Gallon',0),(62,'Heavy Equipment','Grua','TOMCAT Excavator.',0),(63,'Ice','HotIce','10.lb ice bag.',0),(64,'Tools','Carpas','Water hose.',0),(65,'Fuel','Diesel','Diesel 1.gal container.',0),(66,'Canned Food','For Survivors','Canned dog food.',0),(67,'Ice','HotIce','10.lb ice bag.',0),(68,'Dry Food','The Gud Stuff','Dry but Good',0),(69,'Dry Food','The Gud Stuff','The Gud Stuff',0),(70,'Power Generators','Planta Portatil','Industrial Power Generator',0),(71,'Clothing','Pantalon','Adult clothing.',0),(72,'Canned Food','Reserved Foods','Non perishable.',0),(73,'Heavy Equipment','CAT','TOMCAT Excavator.',0),(74,'Fuel','Hight Octane Gas','Diesel 1.gal container.',0),(75,'Baby Food','ForBabies','Variety baby food.',0),(76,'Baby Food','ForBabies','Variety baby food.',0),(77,'Medications','Tamiflu','Pain relievers.',0),(78,'Medications','Tamiflu','Pain relievers.',0),(79,'Ice','IceBag','5.lb ice bag.',0),(80,'Heavy Equipment','Grua','TOMCAT Excavator.',0),(81,'Heavy Equipment','Drill','Battery powered drills.',0),(82,'Power Generators','Super Planta','Industrial Power Generator',0),(83,'Medications','Tamiflu','Pain relievers.',0),(84,'Power Generators','Planta Portatil','Portable Power Generator.',0),(85,'Clothing','Camisa','Adult clothing.',0),(86,'Heavy Equipment','CAT','Industrial wood saw.',0),(87,'Tools','Serrucho','Machine parts.',0),(88,'Fuel','Regular Gas','Diesel 1.gal container.',0),(89,'Medical Devices','Balanzas','MRI',0),(90,'Ice','DryIce','5.lb ice bag.',0),(91,'Ice','SomeIce','5.lb ice bag.',0),(92,'Medical Devices','Estetoscopio','Respiratory assistance.',0),(93,'Power Generators','Planta Portatil','Portable Power Generator.',0),(94,'Medications','Mucinex','Pain relievers.',0),(95,'Power Generators','Always Working','Portable Power Generator.',0),(96,'Water','Nikini','1 Water Gallon',0),(97,'Canned Food','For Survivors','Non perishable.',0),(98,'Heavy Equipment','CAT','TOMCAT Excavator.',0),(99,'Water','Nikini','Purified Water',0),(100,'Clothing','Camisa','Kids clothing.',0),(101,'Heavy Equipment','Digger','TOMCAT Excavator.',0),(102,'Heavy Equipment','Grua','Battery powered drills.',0),(103,'Fuel','Hight Octane Gas','Diesel 1.gal container.',0),(104,'Ice','HotIce','5.lb ice bag.',0),(105,'Power Generators','Super Planta','Portable Power Generator.',0),(106,'Canned Food','Exotic Food','Non perishable.',0),(107,'Canned Food','Exotic Food','Canned dog food.',0),(108,'Baby Food','Grow Up','Veggies baby food.',0),(109,'Tools','Serrucho','Machine parts.',0),(110,'Medications','Mucinex','Cheap medicine.',0),(111,'Clothing','Medias','Adult clothing.',0),(112,'Medical Devices','Balanzas','Respiratory assistance.',0),(113,'Water','Home W','1 Water Gallon',0),(114,'Medical Devices','Estetoscopio','UV lights.',0),(115,'Fuel','Always Full','Diesel 1.gal container.',0),(116,'Clothing','Medias','Adult clothing.',0),(117,'Water','Mountain','Purified Water',0),(118,'Dry Food','The Gud Stuff','Big Can Beef',0),(119,'Water','Mountain','1 Water Gallon',0),(120,'Medical Devices','MRI Scanner','MRI',0),(121,'Ice','IceBag','5.lb ice bag.',0),(122,'Medical Devices','MRI Scanner','MRI',0),(123,'Heavy Equipment','Digger','TOMCAT Excavator.',0),(124,'Dry Food','The Gud Stuff','Big Can Beef',0),(125,'Water','Home W','Purified Water',0),(126,'Heavy Equipment','Digger','Industrial wood saw.',0),(127,'Tools','Destornillador','Machine parts.',0),(128,'Canned Food','Exotic Food','Canned baby food.',0),(129,'Canned Food','Exotic Food','Canned emergency food.',0),(130,'Medical Devices','MRI Scanner','UV lights.',0);
/*!40000 ALTER TABLE `resources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `suppliers` (
  `supplier_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_name` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`supplier_id`),
  KEY `user_name` (`user_name`),
  CONSTRAINT `suppliers_ibfk_1` FOREIGN KEY (`user_name`) REFERENCES `users` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'MannyEng','mannyDiaz70'),(2,'CosNor','dRodRadman'),(3,NULL,'carlita96'),(4,'Andrea de Castro','SomeDude88'),(5,'Samuel','aVerpOf7'),(6,'Pedro','YeaBB88'),(7,'Eric','ImBor'),(8,'El de Haciendo','Decimeloxx'),(9,'Hector','SeriousUser'),(10,'Andrea de Castro','NSFW'),(11,'Samuel','SFW'),(12,'Maluma','COVID'),(13,'Ricky Roselló','NoMore'),(14,'El beibi Trump','Enough'),(15,'Hector','Switch'),(16,'El Vago','Daxter'),(17,'El Vago','Sickiickk'),(18,'El Pelu','Pelota'),(19,'Samuel','Cuantos'),(20,'Michael','Esto'),(21,'Pedro','Mio'),(22,'El beibi Trump','This is'),(23,'El Pelu','OtroMaj7'),(24,'Pedro','Its4'),(25,'Michael','7895'),(26,'Maluma','WannASLEEP'),(27,'J\'Go','Youtu'),(28,'El Vago','Google'),(29,'El Pelu','QUEpaza'),(30,'Samuel','1459A'),(31,'Michael','ESteNo'),(32,'El de Haciendo','ElDoble'),(33,'Michael','Patricia813466'),(34,'El Pelu','Linda757395'),(35,'La Comay','Mary814029'),(36,'El Pelu','William395707'),(37,'Eric','Jennifer213880'),(38,'El de Haciendo','Michael832905'),(39,'La Comay','Mary182501'),(40,'Hector','John112641'),(41,'El Pelu','James148443'),(42,'Bad Bunny','William292379');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplies`
--

DROP TABLE IF EXISTS `supplies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supplies` (
  `supply_id` int(11) NOT NULL AUTO_INCREMENT,
  `supply_quantity` int(11) NOT NULL,
  `supply_date` date DEFAULT NULL,
  `price` decimal(15,2) NOT NULL,
  `resource_id` int(11) NOT NULL,
  `supplier_id` int(11) NOT NULL,
  PRIMARY KEY (`supply_id`),
  KEY `supplier_id` (`supplier_id`),
  KEY `resource_id` (`resource_id`),
  CONSTRAINT `supplies_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`supplier_id`),
  CONSTRAINT `supplies_ibfk_2` FOREIGN KEY (`resource_id`) REFERENCES `resources` (`resource_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplies`
--

LOCK TABLES `supplies` WRITE;
/*!40000 ALTER TABLE `supplies` DISABLE KEYS */;
INSERT INTO `supplies` VALUES (1,15,'2020-04-19',1.00,3,1),(2,100,'2020-04-02',0.00,5,2),(3,400,'2020-04-02',5.00,6,2),(4,1,'2020-04-24',5.00,9,3),(5,92,'1996-02-01',6.60,80,4),(6,95,'1991-03-25',27.88,81,5),(7,95,'1993-12-06',3.26,82,6),(8,32,'1992-08-11',55.32,83,7),(9,54,'1990-11-16',3362.19,84,8),(10,75,'1998-12-28',15.61,85,9),(11,37,'1992-02-04',560.81,86,10),(12,60,'1990-11-17',56.65,87,11),(13,85,'1994-11-28',7.20,88,12),(15,80,'1992-03-01',2.50,101,13),(16,62,'1993-03-04',56.48,102,14),(17,48,'1997-11-06',2673.15,103,15),(18,45,'1996-02-06',3.84,104,16),(19,96,'1999-04-20',220.79,105,17),(20,0,'1993-08-05',877.89,106,18),(21,60,'1990-12-06',7.79,107,19),(22,54,'1999-01-07',684.65,108,20),(23,6,'1994-12-17',2185.40,109,21),(24,37,'1993-03-01',185.70,110,22),(25,49,'1996-04-19',87.25,111,23),(26,55,'1999-05-05',15.64,112,24),(27,19,'2000-03-08',882.46,113,25),(28,69,'1996-04-27',2520.74,114,26),(29,89,'1994-09-13',798.59,115,27),(30,83,'1996-04-16',0.99,116,28),(31,10,'1995-12-28',28.51,117,29),(32,73,'1995-05-26',14.92,118,30),(33,64,'1990-03-15',4.52,119,31),(34,66,'1991-10-15',61.43,120,32),(35,40,'1999-11-11',85.53,121,33),(36,31,'1997-10-14',6.26,122,34),(37,85,'1994-10-06',9167.34,123,35),(38,76,'1997-04-19',4224.23,124,36),(39,18,'1995-04-01',99.45,125,37),(40,53,'1994-07-07',520.85,126,38),(41,19,'1992-04-23',5154.74,127,39),(42,42,'1994-07-27',3744.71,128,40),(43,46,'1996-03-28',28.50,129,41),(44,12,'1999-04-14',62.60,130,42);
/*!40000 ALTER TABLE `supplies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_name` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` char(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dob` date DEFAULT NULL,
  `phone_number` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` int(11) NOT NULL,
  PRIMARY KEY (`user_name`),
  KEY `address` (`address`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`address`) REFERENCES `address` (`address_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('1459A','john@yahoo.com','ba35768f69cb72c907e0e8aa23771427318b342b','Robert','Joseph','1996-07-03','7872475556',139),('7895','robert@hotmail.com','6f1265187b270dd42b5ddc3b3fa13620a60d438b','Linda','Williams','1999-05-23','7878146741',129),('Aaa','jennifer@google.com','f94659e9789225adf9e5054159c83c2c0e025efb','Mary','Williams','1997-11-08','7871398336',140),('ADQESFE','michael@google.com','d3837fdd294ec9a15806b250ab42a39ca3633c26','James','Lopez','1991-03-08','7871434637',64),('anewuser','robert@bing.com','8cf5da23369aa64ec2ccdfbd73aabe04226fb7ff','Mary','Joseph','1999-07-28','7871115775',71),('anusers','mary@upr.edu','26b978754418d12a59fc68c417f219ac77f9bbcd','John','Clarke','1995-02-14','7873784005',61),('aVerpOf7','john@google.com','ef0690f2dae08d9a6d1b5ca4f03983a694834fdd','Michael','Smith','1994-11-21','7878239753',85),('BadB','linda@bing.com','fd61e280e848689c133672e09bbc20bb883608a5','John','Charles','2000-07-19','7873967653',99),('BadBu','michael@hotmail.com','140efbc9ccc94f06ebc17485110be53d39acb73c','Patricia','Smith','1998-12-17','7879449873',100),('baiabaia','jennifer@bing.com','8cf5da23369aa64ec2ccdfbd73aabe04226fb7ff','Linda','Joseph','1994-07-22','7875052566',63),('baie8','patricia@upr.edu','cf8ef8c2a9548f71a0bfe87076e7da81b6c44eea','Linda','Hernandez','1991-06-28','7871374049',73),('carlita96','carla.villanueva3@upr.com','24pp7e8u06985426e122180rp09be2c635hu4t52','Carla','Villanueva','1996-06-12','7876342345',4),('Cnazado','robert@bing.com','5d78eb8fe8512ea2de599de561c066c1e843137b','James','Hernandez','1997-03-12','7870780590',144),('COVID','john@google.com','08128901547197d5650f37f9b0a7f199eb99c262','Linda','Williams','1993-05-27','7873667031',92),('Cuantos','mary@google.com','53ea064fe930b761e08916dcca0ff7610e9e9816','Robert','Smith','1990-08-25','7877486980',117),('Daxter','patricia@bing.com','1c7380f82e12efd8c096d85c6f820d99731bdf0c','Michael','Charles','1998-01-20','7876467373',111),('deadspacefan','ilikedeadspace@deadspace.com','5753dbed109d45138aac07a1f435741ca8d9e28f','Isaac','Clarke','1993-05-02','7875468965',51),('Decimeloxx','john@bing.com','020332fd021b29a2646460ace961400e2c8b4600','Patricia','Smith','1990-06-19','7874080351',88),('dfe5','jennifer@hotmail.com','53ea064fe930b761e08916dcca0ff7610e9e9816','William','Lopez','1991-02-07','7873170908',75),('Dinosaurios','michael@hotmail.com','08128901547197d5650f37f9b0a7f199eb99c262','William','Joseph','1997-12-07','7874717425',116),('Dioj','robert@hotmail.com','ef0690f2dae08d9a6d1b5ca4f03983a694834fdd','John','Lopez','1992-10-19','7871296806',120),('Disturbed','patricia@google.com','ef0690f2dae08d9a6d1b5ca4f03983a694834fdd','Patricia','Charles','1998-01-10','7872518360',114),('dRodRadman','radman@hotmail.com','2y122e8u06985426e1221dio09be2c6e5ba4t52','Diego','Rodriguez','1987-10-13','7879924545',1),('ElDoble','linda@bing.com','f9ba749a539ac2108f0ff48c211dc66fd6359ae9','William','Hernandez','1993-07-18','7874501974',143),('Enough','robert@upr.edu','2825b23ee149483a0cc3560f7b3fb0f1770c3914','Jennifer','Hernandez','1990-05-07','7878875430',107),('Eso Ej 89','linda@google.com','5469e8ef5c51625f2003b32f4ffaa6c7da1d7f9e','Michael','Joseph','1996-06-23','7878544287',97),('ESteNo','william@upr.edu','cf8ef8c2a9548f71a0bfe87076e7da81b6c44eea','Jennifer','Smith','1996-10-20','7870349751',141),('estetip','john@upr.edu','4d90b2718035ac1260687f057bea786d020cfced','Linda','Joseph','1990-06-27','7878836916',62),('EsteTip9','william@upr.edu','fd61e280e848689c133672e09bbc20bb883608a5','Michael','Hernandez','1995-08-02','7877334455',80),('Esto','jennifer@hotmail.com','f94659e9789225adf9e5054159c83c2c0e025efb','James','Williams','1997-02-17','7873477235',119),('Garuga','ilikemh@mhgu.com','163a6a005bd7405d53d297517ef2cf0ba7761808','Fernan','Castro','1990-07-02','7877099858',53),('GenericUser','genuser@gamil.com','19489c6e7bebbbb3ebc0712c2817b0fe7ffbc5b0','MiNmae','TuName','1001-07-04','7874567890',49),('Getting','mary@yahoo.com','643fcb807517b90b8f2e0a0a3374fd3dce6d2064','William','Clarke','1992-08-12','7877082151',124),('Google','william@bing.com','140efbc9ccc94f06ebc17485110be53d39acb73c','James','Rolle','1994-07-06','7876413261',135),('IkIk','robert@yahoo.com','d3837fdd294ec9a15806b250ab42a39ca3633c26','Linda','Smith','1999-08-27','7872840338',67),('ImBor','robert@bing.com','bf17a367635a090c23505ba974a7f3a9358fd07c','William','Smith','1990-11-02','7876358996',87),('IMCEO','john@bing.com','2249f19f896f60d12526d8f37819da852a11ba52','Linda','Joseph','1996-03-18','7873455219',136),('ImTired','robert@google.com','7f205a6455ab0fbe0c58d48e9595f69f051d5a0e','Patricia','Hernandez','1999-02-09','7870889678',108),('Interest','william@yahoo.com','643fcb807517b90b8f2e0a0a3374fd3dce6d2064','James','Lopez','1993-09-21','7877783838',70),('Its4','robert@upr.edu','ef0690f2dae08d9a6d1b5ca4f03983a694834fdd','William','Hernandez','1997-04-05','7877424610',127),('Jack','patricia@google.com','1977ff7dba594a73c42fcea7730ec3380a60cc18','John','Williams','1998-05-06','7878861696',110),('James148443','robert@upr.edu','2825b23ee149483a0cc3560f7b3fb0f1770c3914','Robert','Rolle','1997-11-17','7874684848',170),('James580747','patricia@upr.edu','dff8e60966011938614370d4f8fa30eaa4fd9eb5','Jennifer','Rolle','1990-07-12','7870763604',147),('James872093','linda@yahoo.com','6f1265187b270dd42b5ddc3b3fa13620a60d438b','Linda','Joseph','1995-08-24','7875230971',184),('Jennifer151317','patricia@hotmail.com','4d90b2718035ac1260687f057bea786d020cfced','Michael','Joseph','1990-09-26','7878140857',181),('Jennifer183795','john@yahoo.com','ef0690f2dae08d9a6d1b5ca4f03983a694834fdd','Jennifer','Williams','1998-01-24','7873266711',168),('Jennifer213880','linda@google.com','ba35768f69cb72c907e0e8aa23771427318b342b','Linda','Clarke','1994-07-04','7875360610',158),('Jennifer243348','jennifer@yahoo.com','08128901547197d5650f37f9b0a7f199eb99c262','Mary','Joseph','1991-01-27','7875547041',153),('Jennifer405849','james@google.com','020332fd021b29a2646460ace961400e2c8b4600','William','Lopez','1999-12-01','7878140279',159),('Jennifer518644','james@yahoo.com','4d90b2718035ac1260687f057bea786d020cfced','Mary','Rolle','1998-07-13','7876593752',154),('Jennifer632351','jennifer@upr.edu','ef0690f2dae08d9a6d1b5ca4f03983a694834fdd','Mary','Lopez','1990-11-28','7873363511',172),('Jennifer844730','john@google.com','dff8e60966011938614370d4f8fa30eaa4fd9eb5','William','Smith','1997-12-26','7875495014',157),('John112641','jennifer@google.com','f94659e9789225adf9e5054159c83c2c0e025efb','Jennifer','Clarke','1995-02-01','7872709219',167),('John44455','linda@google.com','ef0690f2dae08d9a6d1b5ca4f03983a694834fdd','Linda','Williams','1995-08-18','7878258340',166),('John533131','robert@upr.edu','38745ed1d344f7223a150b43ab8891b076e72daf','James','Clarke','1990-02-10','7874949112',183),('John800631','james@bing.com','d3837fdd294ec9a15806b250ab42a39ca3633c26','William','Charles','1991-09-14','7876794837',180),('joseJoestar','jJoestar@gmail.com','de922e800698ef26e1221e2009be2ca7e5ba4541','Jose','Joestar','2002-06-12','7876752341',6),('JustNumb','james@upr.edu','0e118a62d5787e2f31ed9b65d9c7dd7815d5e4de','William','Joseph','1999-06-12','7877594165',130),('Kinpollo','kinpollo@pollo.com','38be340f1397fd1969066b041424ad1fcac57766','Pollo','ConPollo','2002-02-07','7878345678',47),('laZYusER','illwork@efficiency.com','6761350e7147bfc85bb8d54395d238149ae183ef','Fernan','LaFleur','1994-11-11','7877297818',55),('Linda519302','john@hotmail.com','f94659e9789225adf9e5054159c83c2c0e025efb','Michael','Charles','1992-08-01','7873036284',171),('Linda757395','john@upr.edu','65e952bccf99053196eb3db9d2f02a4012c8c3b3','Robert','Lopez','1995-06-17','7872149713',149),('Linda770034','james@upr.edu','ef0690f2dae08d9a6d1b5ca4f03983a694834fdd','James','Williams','1997-09-07','7877638228',156),('Linda952601','john@upr.edu','26b978754418d12a59fc68c417f219ac77f9bbcd','Mary','Clarke','1992-02-28','7873901417',150),('Lol','patricia@yahoo.com','cf8ef8c2a9548f71a0bfe87076e7da81b6c44eea','Patricia','Williams','1993-05-07','7875110613',112),('mannyDiaz70','mannyDiaz@eng.com','2yowoe8u06985426e12218uy09be2c6e5ba4t52','Manuel','Diaz','1970-02-22','7872335634',3),('marioMan15','mario1997@gmail.com','xe122e8006985426e1221ew009be2ca7e5ba4552','Mario','Mercado','1997-07-25','7873657890',2),('Mary182501','patricia@bing.com','7f205a6455ab0fbe0c58d48e9595f69f051d5a0e','Mary','Smith','1992-09-17','7878785039',164),('Mary404577','robert@hotmail.com','4fed58c027d388ddab604eea85416588c4e1df18','Robert','Williams','1994-04-22','7878699330',179),('Mary428263','patricia@google.com','fd61e280e848689c133672e09bbc20bb883608a5','Mary','Rolle','1990-01-01','7877216426',151),('Mary782995','robert@google.com','1c7380f82e12efd8c096d85c6f820d99731bdf0c','Jennifer','Clarke','1994-02-05','7875793469',145),('Mary814029','robert@hotmail.com','5469e8ef5c51625f2003b32f4ffaa6c7da1d7f9e','Patricia','Clarke','1997-11-06','7877621828',152),('Michael478950','john@upr.edu','7b558c69733f27ce1d6a7923ded02092c9617c21','Jennifer','Williams','1993-08-27','7874272873',162),('Michael770653','patricia@bing.com','1c7380f82e12efd8c096d85c6f820d99731bdf0c','John','Williams','1994-11-08','7871336341',177),('Michael832905','jennifer@hotmail.com','08128901547197d5650f37f9b0a7f199eb99c262','Mary','Lopez','1993-03-04','7876937579',161),('Mio','robert@google.com','7b558c69733f27ce1d6a7923ded02092c9617c21','Linda','Lopez','1999-09-02','7873866069',121),('NoMore','john@upr.edu','38f6752cab7ca17a0d2b768c265316f2ec848f20','Jennifer','Hernandez','1998-01-27','7877573654',105),('None','james@hotmail.com','2249f19f896f60d12526d8f37819da852a11ba52','James','Hernandez','1996-01-21','7871646972',103),('NSFW','mary@upr.edu','020332fd021b29a2646460ace961400e2c8b4600','Patricia','Williams','1996-09-22','7870745455',90),('Oh Y741','michael@hotmail.com','984984d147767641fe48f5dbf61dc7502b971532','Patricia','Smith','1993-09-01','7878098834',128),('OtroDia','mary@yahoo.com','4d90b2718035ac1260687f057bea786d020cfced','John','Williams','1993-11-04','7870566606',142),('OtroMaj7','william@hotmail.com','0e118a62d5787e2f31ed9b65d9c7dd7815d5e4de','John','Charles','1997-01-14','7876273622',125),('OtroUserMas','otronombre@estoyaburrido.com','df206a4a606b939f7eaa88ec06b919d1fd7c82d5','Simba','Martinez','2003-06-02','7876543456',50),('Patricia31091','patricia@yahoo.com','1977ff7dba594a73c42fcea7730ec3380a60cc18','John','Williams','1991-01-28','7879911714',174),('Patricia813466','michael@yahoo.com','08128901547197d5650f37f9b0a7f199eb99c262','James','Smith','1996-03-24','7875875017',146),('Patricia862882','jennifer@yahoo.com','2825b23ee149483a0cc3560f7b3fb0f1770c3914','Mary','Rolle','1994-07-07','7879488582',160),('Pelota','linda@google.com','9cc583a4cf59c3d2e726d0a1cf89eb491d7b1664','Linda','Rolle','1993-04-10','7878007839',115),('peterso','robert@upr.edu','3f0586073a6845e94fcc9af6add28641b3f7e644','William','Joseph','1991-07-22','7877615772',69),('Pide','james@hotmail.com','6f1265187b270dd42b5ddc3b3fa13620a60d438b','James','Lopez','1990-07-12','7874052406',118),('POEUY','william@google.com','ff075725d25864703ebf6ad06a81f83a210a8dcb','William','Lopez','1991-04-19','7878641379',132),('Pollo15','patricia@bing.com','f94659e9789225adf9e5054159c83c2c0e025efb','James','Lopez','1991-05-23','7870126191',79),('qes4','patricia@bing.com','08128901547197d5650f37f9b0a7f199eb99c262','Michael','Hernandez','1994-11-17','7878294185',74),('qswq5','william@hotmail.com','b63e555f61adefe20f26d8ef16235263e502d2a5','Mary','Smith','1996-11-02','7873535692',76),('QUEpaza','linda@hotmail.com','07e1fa1f9b7e9c8c9d91479a455d5c651e6c917b','William','Rolle','1998-05-19','7876015788',137),('QuienSoy','john@hotmail.com','984984d147767641fe48f5dbf61dc7502b971532','Michael','Williams','1997-06-06','7874608792',65),('QuieroTerm','jennifer@yahoo.com','ed0dab136cdfaa03c9fb0e2a5885f368845c480b','Linda','Clarke','1990-05-24','7877647600',98),('Robert522398','linda@bing.com','3f0586073a6845e94fcc9af6add28641b3f7e644','Jennifer','Rolle','1992-05-17','7879129773',178),('Robert728057','mary@yahoo.com','2249f19f896f60d12526d8f37819da852a11ba52','Linda','Joseph','1991-08-02','7874928633',163),('Robert833321','michael@bing.com','2249f19f896f60d12526d8f37819da852a11ba52','James','Charles','1993-11-27','7874582408',169),('Robert939866','robert@hotmail.com','0e118a62d5787e2f31ed9b65d9c7dd7815d5e4de','Michael','Charles','1990-05-22','7870733510',148),('Seeer','linda@google.com','5469e8ef5c51625f2003b32f4ffaa6c7da1d7f9e','John','Rolle','2000-01-23','7874459269',66),('SeriousUser','mary@bing.com','7b558c69733f27ce1d6a7923ded02092c9617c21','Linda','Lopez','1990-09-25','7879340634',89),('SFW','jennifer@upr.edu','140efbc9ccc94f06ebc17485110be53d39acb73c','Patricia','Clarke','1994-02-15','7875443564',91),('Sickick','james@yahoo.com','ef0690f2dae08d9a6d1b5ca4f03983a694834fdd','William','Joseph','1990-10-11','7872666614',68),('Sickiickk','patricia@hotmail.com','07e1fa1f9b7e9c8c9d91479a455d5c651e6c917b','William','Williams','1995-03-12','7877253818',113),('somedisuser','michael@bing.com','ef0690f2dae08d9a6d1b5ca4f03983a694834fdd','Patricia','Smith','1995-02-21','7873782012',59),('SomeDu88','michael@bing.com','181c7ea979558b81be6c8701200b508ba8ab0c98','Michael','Hernandez','2000-11-21','7878664662',82),('SomedUd88','james@google.com','4d90b2718035ac1260687f057bea786d020cfced','Robert','Smith','1991-10-16','7874702028',83),('SomeDude88','jennifer@yahoo.com','ba35768f69cb72c907e0e8aa23771427318b342b','Michael','Williams','1994-08-05','7879818904',84),('somedudeuser','mary@yahoo.com','1c7380f82e12efd8c096d85c6f820d99731bdf0c','James','Charles','1999-04-05','7878567715',60),('SomeSuperUser','ihopeso@hoping.com','55355280ea1c3fff652c9f28e856393e133068b8','Kratos','FromSparta','1994-12-25','7878115409',56),('someus8','jennifer@google.com','181c7ea979558b81be6c8701200b508ba8ab0c98','Robert','Lopez','1991-02-25','7870274471',77),('SomeUser','anuser@email.com','b939f9e936535a81534e1ff97235e682df56584c','Usu','Ario','1999-07-04','7877652345',46),('SonDemasiados','jennifer@upr.edu','984984d147767641fe48f5dbf61dc7502b971532','Mary','Charles','1993-08-12','7877707548',138),('starLand12','starlang12@gmail.com','iy0w0e8u06985426e122180ry09be2c6e5hu4t52','Monica','Rodriguez','1996-03-05','7872955634',5),('Switch','mary@hotmail.com','984984d147767641fe48f5dbf61dc7502b971532','Jennifer','Charles','1992-11-23','7874214065',109),('thiDude','robert@bing.com','020332fd021b29a2646460ace961400e2c8b4600','Robert','Rolle','1993-09-23','7876148055',81),('This is','james@google.com','181c7ea979558b81be6c8701200b508ba8ab0c98','Robert','Williams','1997-04-24','7879886408',123),('Unknow','william@yahoo.com','9cc583a4cf59c3d2e726d0a1cf89eb491d7b1664','Robert','Clarke','1997-05-04','7878413148',102),('UnnY','jennifer@bing.com','8cf5da23369aa64ec2ccdfbd73aabe04226fb7ff','John','Hernandez','1990-07-08','7879022521',101),('UnTiPax','patricia@hotmail.com','38f6752cab7ca17a0d2b768c265316f2ec848f20','John','Smith','1998-07-18','7879364960',93),('UnTipoAhi','patricia@yahoo.com','35e05f0e4d41b6734f8148f26956d6cf58e4050b','William','Hernandez','1999-12-21','7879227437',94),('UnTipoAhi14','patricia@upr.edu','2825b23ee149483a0cc3560f7b3fb0f1770c3914','Jennifer','Charles','1997-09-11','7875341496',95),('use7','mary@yahoo.com','984984d147767641fe48f5dbf61dc7502b971532','Jennifer','Charles','1999-09-22','7874989047',72),('WannASLEEP','james@bing.com','140efbc9ccc94f06ebc17485110be53d39acb73c','Patricia','Rolle','2000-02-17','7879490077',131),('What','robert@bing.com','4fed58c027d388ddab604eea85416588c4e1df18','Patricia','Clarke','1995-06-19','7871897361',126),('William185759','linda@upr.edu','3f0586073a6845e94fcc9af6add28641b3f7e644','John','Charles','1999-08-12','7877589594',182),('William292379','james@google.com','4d90b2718035ac1260687f057bea786d020cfced','Linda','Clarke','1991-02-20','7871549671',173),('William331916','william@yahoo.com','5469e8ef5c51625f2003b32f4ffaa6c7da1d7f9e','Michael','Rolle','1991-03-21','7875155295',176),('William395707','robert@yahoo.com','b63e555f61adefe20f26d8ef16235263e502d2a5','Michael','Lopez','2000-07-07','7870143766',155),('William639620','linda@upr.edu','ed0dab136cdfaa03c9fb0e2a5885f368845c480b','Patricia','Rolle','2000-04-28','7875354553',165),('William695486','patricia@upr.edu','dff8e60966011938614370d4f8fa30eaa4fd9eb5','Jennifer','Smith','1992-07-20','7874098574',175),('WooFunciona','patricia@upr.edu','ba35768f69cb72c907e0e8aa23771427318b342b','Mary','Clarke','1998-07-15','7873981971',96),('Ya','john@upr.edu','181c7ea979558b81be6c8701200b508ba8ab0c98','William','Williams','1993-02-02','7876428366',104),('YaBata','john@yahoo.com','38745ed1d344f7223a150b43ab8891b076e72daf','James','Lopez','1996-10-25','7875397217',106),('YeaBB88','mary@google.com','1c7380f82e12efd8c096d85c6f820d99731bdf0c','Robert','Clarke','1997-04-02','7873645918',86),('Youtu','mary@hotmail.com','643fcb807517b90b8f2e0a0a3374fd3dce6d2064','Michael','Smith','1992-09-01','7875353922',133),('Youtube','linda@bing.com','e7733e2c6904fb3757f54b1ade0830126104808a','Mary','Joseph','2000-05-07','7876013122',134),('Zeus4','john@bing.com','7f205a6455ab0fbe0c58d48e9595f69f051d5a0e','James','Smith','1990-11-26','7875367185',78);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-05 21:02:41
