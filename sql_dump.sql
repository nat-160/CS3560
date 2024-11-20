-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: restaurant
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) DEFAULT NULL,
  `customerName` mediumtext,
  `address` mediumtext,
  `phoneNumber` tinytext,
  `email` mediumtext,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'521b9ccefbcd14d179e7a1bb877752870a6d620938b28a66a107eac6e6805b9d0989f45b5730508041aa5e710847d439ea74cd312c9355f1f2dae08d40e41d50','Test Account','3801 W Temple Ave, Pomona, California, United States 91768','9203820293','angelvazquez@cpp.edu');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employeeID` int NOT NULL AUTO_INCREMENT,
  `position` varchar(255) DEFAULT NULL,
  `employeeName` varchar(255) DEFAULT NULL,
  `employeeStatus` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`employeeID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (-1,'manager','Michael','Terminated'),(1,'manager',NULL,NULL),(2,'manager',NULL,NULL),(3,'manager',NULL,NULL),(4,'manager',NULL,NULL),(5,'manager',NULL,NULL),(6,'manager',NULL,NULL),(7,'non manager',NULL,NULL),(8,'non manager',NULL,NULL),(9,'non manager','terminated','moichael'),(10,'non manager','terminated','moichael'),(11,'testPosition','testName','testStatus'),(12,'testPosition','testName','testStatus'),(13,'Dishwasher','Martelle O\'Lynn','terminated'),(14,'Server','Nikolas Liddel','off'),(15,'Host/Hostess','Tris Dunbar','off'),(16,'Server','Farrand Delgadillo','working'),(17,'Manager','Brade Rechert','working'),(18,'Busser','Justinian Giraudel','working'),(19,'Server','Tracey Riveles','off'),(20,'Host/Hostess','Thorvald Peat','off'),(21,'Cook','Raleigh Guile','terminated'),(22,'Manager','Rochella Danbi','terminated'),(23,'Dishwasher','Pennie Bangs','working'),(24,'Manager','Gerri Bendan','off'),(25,'Host/Hostess','Jerri Swanborough','off'),(26,'Bartender','Seumas MacKinnon','terminated'),(27,'Host/Hostess','Almira Deboick','working'),(28,'Manager','Mill Oakwell','terminated'),(29,'Dishwasher','Eddie Tomaselli','terminated'),(30,'Host/Hostess','Carlos Flaonier','off'),(31,'Dishwasher','Glenden Kellart','terminated'),(32,'Busser','Emmey Castille','working'),(33,'Host/Hostess','Arnie Tincombe','off'),(34,'Dishwasher','Obediah Delahunty','off'),(35,'Bartender','Hedy Maypes','terminated'),(36,'Manager','Crin Clashe','terminated'),(37,'Cook','Reeva McSweeney','off'),(38,'Bartender','Boy Goulden','terminated'),(39,'Bartender','Edouard Skittles','terminated'),(40,'Manager','Byrom Wardle','working'),(41,'Cook','Maria Vondrach','working'),(42,'Server','Lyell Courtese','terminated'),(43,'Server','Lyndsay Medling','off'),(44,'Cook','Cristy Pettigree','off'),(45,'Host/Hostess','Velvet Allatt','off'),(46,'Dishwasher','Lilas Cremins','off'),(47,'Host/Hostess','Towney Nobbs','working'),(48,'Dishwasher','Noni Doumic','off'),(49,'Server','Farra Randalston','working'),(50,'Dishwasher','Sadella Wigan','off'),(51,'Bartender','Kalle Gillingham','terminated'),(52,'Host/Hostess','Cristobal Cullrford','terminated'),(53,'Bartender','Wakefield Squire','terminated'),(54,'Host/Hostess','Abelard Golsworthy','off'),(55,'Cook','Amby Kendrew','terminated'),(56,'Busser','Darwin Duffyn','off'),(57,'Bartender','Linzy Fodden','off'),(58,'Dishwasher','Evan Lerego','terminated'),(59,'Busser','Robinson Mosson','terminated'),(60,'Dishwasher','Durand Mostin','off'),(61,'Manager','Patricio Galletly','working'),(62,'Busser','Tish Macellar','off'),(63,'Busser','Niven Mingardo','off'),(64,'Cook','Towney Mearing','off'),(65,'Server','Izak Folonin','working'),(66,'Busser','Sileas Inkle','working'),(67,'Cook','Eliza Thomelin','terminated'),(68,'Host/Hostess','Paula Athelstan','terminated'),(69,'Bartender','Travus O\'Kuddyhy','terminated'),(70,'Host/Hostess','Cathyleen Avard','working'),(71,'Cook','Pamella Banner','working'),(72,'Dishwasher','Anitra Benzie','off'),(73,'Host/Hostess','Walton Kix','terminated'),(74,'Host/Hostess','Juliet Salway','off'),(75,'Cook','Joyous Alvar','working'),(76,'Bartender','Alida Wein','off'),(77,'Bartender','Katy Tomadoni','working'),(78,'Manager','Sollie Harnell','terminated'),(79,'Cook','Kikelia Durek','working'),(80,'Manager','Oliy Garioch','terminated'),(81,'Busser','Dreddy Davenall','working'),(82,'Bartender','Aron Spurdens','terminated'),(83,'Bartender','Trixie Kirkwood','terminated'),(84,'Bartender','Olivia Fitzsimmons','working'),(85,'Cook','Claire Arrowsmith','terminated'),(86,'Server','Robby Podbury','working'),(87,'Busser','Robinia Link','off'),(88,'Bartender','Drew Edridge','off'),(89,'Cook','Meagan Tuhy','terminated'),(90,'Cook','Rene Rusling','terminated'),(91,'Manager','Maje Edgeson','working'),(92,'Bartender','Tim Lithgow','working'),(93,'Manager','Ciro Egentan','working'),(94,'Host/Hostess','Jessalyn Lammiman','working'),(95,'Cook','Anne-marie Jiras','working'),(96,'Dishwasher','Halli Ruslin','terminated'),(97,'Bartender','Finley Axtens','off'),(98,'Cook','Evanne McArte','terminated'),(99,'Manager','Lacey Maplesden','off'),(100,'Busser','Darell Skilbeck','off');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `full_order_details`
--

DROP TABLE IF EXISTS `full_order_details`;
/*!50001 DROP VIEW IF EXISTS `full_order_details`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `full_order_details` AS SELECT 
 1 AS `orderID`,
 1 AS `orderstatus`,
 1 AS `orderDate`,
 1 AS `amount`,
 1 AS `customerName`,
 1 AS `phoneNumber`,
 1 AS `email`,
 1 AS `modNote`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `MenuID` int NOT NULL AUTO_INCREMENT,
  `menuName` varchar(255) DEFAULT NULL,
  `startTime` time DEFAULT NULL,
  `endTime` time DEFAULT NULL,
  PRIMARY KEY (`MenuID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Breakfast','05:00:00','11:00:00'),(2,'Lunch','11:00:00','18:00:00'),(3,'Dinner','18:00:00','23:00:00'),(4,'Late Night Cravings','00:00:00','05:00:00');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `menu_entry_details`
--

DROP TABLE IF EXISTS `menu_entry_details`;
/*!50001 DROP VIEW IF EXISTS `menu_entry_details`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `menu_entry_details` AS SELECT 
 1 AS `itemID`,
 1 AS `menuid`,
 1 AS `name`,
 1 AS `price`,
 1 AS `menuDescription`,
 1 AS `image`,
 1 AS `category`,
 1 AS `state`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `menuentry`
--

DROP TABLE IF EXISTS `menuentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menuentry` (
  `menuID` int NOT NULL,
  `itemID` int NOT NULL,
  `state` varchar(45) DEFAULT 'enabled',
  PRIMARY KEY (`menuID`,`itemID`),
  KEY `itemID` (`itemID`),
  CONSTRAINT `menuentry_ibfk_1` FOREIGN KEY (`menuID`) REFERENCES `menu` (`MenuID`),
  CONSTRAINT `menuentry_ibfk_2` FOREIGN KEY (`itemID`) REFERENCES `menuitem` (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menuentry`
--

LOCK TABLES `menuentry` WRITE;
/*!40000 ALTER TABLE `menuentry` DISABLE KEYS */;
INSERT INTO `menuentry` VALUES (1,1,'disabled'),(1,2,'disabled'),(1,3,'enabled'),(1,4,'enabled'),(1,5,'disabled'),(2,1,'enabled'),(2,2,'enabled'),(2,3,'enabled'),(2,4,'disabled'),(2,5,'disabled'),(3,1,'disabled'),(3,2,'disabled'),(3,3,'disabled'),(3,4,'disabled'),(3,5,'enabled'),(4,1,'disabled'),(4,2,'enabled'),(4,3,'disabled'),(4,4,'disabled'),(4,5,'disabled');
/*!40000 ALTER TABLE `menuentry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menuitem`
--

DROP TABLE IF EXISTS `menuitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menuitem` (
  `itemID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `menuDescription` varchar(255) DEFAULT NULL,
  `image` tinytext,
  `category` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`itemID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menuitem`
--

LOCK TABLES `menuitem` WRITE;
/*!40000 ALTER TABLE `menuitem` DISABLE KEYS */;
INSERT INTO `menuitem` VALUES (1,'The Fig-eta Bout It Burger',12.99,'The Fig-eta Bout It Burger is a unique and flavorful sandwich that combines a juicy beef patty with sweet and savory toppings such as caramelized onions, fig jam, and goat cheese.','/static/figs.png','food'),(2,'New Bacon-ings',10.99,'The New Bacon-ings is a delicious sandwich that features a juicy beef patty topped with crispy bacon and melted cheese, all served on a soft bun. Served with a side of fries.','/static/bacon-strips.png','food'),(3,'Thank God It\'s Fried Egg Burger',11.99,'The Thank God It\'s Fried Egg Burger is a delicious sandwich that features a juicy beef patty topped with a freshly fried egg.','/static/hamburger.png','food'),(4,'Breakfast Plate',8.99,'Two eggs cooked to your liking, four strips of bacon, and two hotcakes. The perfect way to start your day.','/static/frying-pan.png','food'),(5,'Fish Platter',13.99,'Chef\'s choice* of fish, served with a side of fries.','/static/tuna.png','food');
/*!40000 ALTER TABLE `menuitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `order_item_details`
--

DROP TABLE IF EXISTS `order_item_details`;
/*!50001 DROP VIEW IF EXISTS `order_item_details`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `order_item_details` AS SELECT 
 1 AS `orderID`,
 1 AS `orderItemID`,
 1 AS `itemID`,
 1 AS `name`,
 1 AS `price`,
 1 AS `specialInstruction`,
 1 AS `quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `orderitem`
--

DROP TABLE IF EXISTS `orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderitem` (
  `orderItemID` int NOT NULL AUTO_INCREMENT,
  `orderID` int DEFAULT NULL,
  `itemID` int DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `specialInstruction` tinytext,
  PRIMARY KEY (`orderItemID`),
  KEY `orderID` (`orderID`),
  KEY `orderitem_ibfk_2_idx` (`itemID`),
  CONSTRAINT `orderitem_ibfk_1` FOREIGN KEY (`orderID`) REFERENCES `orders` (`orderID`),
  CONSTRAINT `orderitem_ibfk_2` FOREIGN KEY (`itemID`) REFERENCES `menuitem` (`itemID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderitem`
--

LOCK TABLES `orderitem` WRITE;
/*!40000 ALTER TABLE `orderitem` DISABLE KEYS */;
INSERT INTO `orderitem` VALUES (1,1,2,NULL,'Please burn it to a crisp. It\'s the only way I like it');
/*!40000 ALTER TABLE `orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `orderID` int NOT NULL AUTO_INCREMENT,
  `customerID` int DEFAULT NULL,
  `orderDate` datetime DEFAULT NULL,
  `modNote` varchar(255) DEFAULT NULL,
  `orderstatus` varchar(255) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  PRIMARY KEY (`orderID`),
  KEY `customerID` (`customerID`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,'2023-05-01 02:25:46',NULL,'-1',10.99);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `full_order_details`
--

/*!50001 DROP VIEW IF EXISTS `full_order_details`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `full_order_details` AS select `orders`.`orderID` AS `orderID`,`orders`.`orderstatus` AS `orderstatus`,`orders`.`orderDate` AS `orderDate`,`orders`.`amount` AS `amount`,`customer`.`customerName` AS `customerName`,`customer`.`phoneNumber` AS `phoneNumber`,`customer`.`email` AS `email`,`orders`.`modNote` AS `modNote` from (`orders` join `customer` on((`customer`.`customer_id` = `orders`.`customerID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `menu_entry_details`
--

/*!50001 DROP VIEW IF EXISTS `menu_entry_details`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `menu_entry_details` AS select `menuitem`.`itemID` AS `itemID`,`menuentry`.`menuID` AS `menuid`,`menuitem`.`name` AS `name`,`menuitem`.`price` AS `price`,`menuitem`.`menuDescription` AS `menuDescription`,`menuitem`.`image` AS `image`,`menuitem`.`category` AS `category`,`menuentry`.`state` AS `state` from (`menuitem` join `menuentry` on((`menuitem`.`itemID` = `menuentry`.`itemID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `order_item_details`
--

/*!50001 DROP VIEW IF EXISTS `order_item_details`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `order_item_details` AS select `orderitem`.`orderID` AS `orderID`,`orderitem`.`orderItemID` AS `orderItemID`,`orderitem`.`itemID` AS `itemID`,`menuitem`.`name` AS `name`,`menuitem`.`price` AS `price`,`orderitem`.`specialInstruction` AS `specialInstruction`,`orderitem`.`Quantity` AS `quantity` from (`orderitem` join `menuitem` on((`menuitem`.`itemID` = `orderitem`.`itemID`))) */;
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

-- Dump completed on 2023-05-01  2:32:23
