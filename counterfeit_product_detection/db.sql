/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - fake_product
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`fake_product` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `fake_product`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add bill',7,'add_bill'),
(26,'Can change bill',7,'change_bill'),
(27,'Can delete bill',7,'delete_bill'),
(28,'Can view bill',7,'view_bill'),
(29,'Can add category',8,'add_category'),
(30,'Can change category',8,'change_category'),
(31,'Can delete category',8,'delete_category'),
(32,'Can view category',8,'view_category'),
(33,'Can add distributor_table',9,'add_distributor_table'),
(34,'Can change distributor_table',9,'change_distributor_table'),
(35,'Can delete distributor_table',9,'delete_distributor_table'),
(36,'Can view distributor_table',9,'view_distributor_table'),
(37,'Can add login_table',10,'add_login_table'),
(38,'Can change login_table',10,'change_login_table'),
(39,'Can delete login_table',10,'delete_login_table'),
(40,'Can view login_table',10,'view_login_table'),
(41,'Can add order',11,'add_order'),
(42,'Can change order',11,'change_order'),
(43,'Can delete order',11,'delete_order'),
(44,'Can view order',11,'view_order'),
(45,'Can add product',12,'add_product'),
(46,'Can change product',12,'change_product'),
(47,'Can delete product',12,'delete_product'),
(48,'Can view product',12,'view_product'),
(49,'Can add user_table',13,'add_user_table'),
(50,'Can change user_table',13,'change_user_table'),
(51,'Can delete user_table',13,'delete_user_table'),
(52,'Can view user_table',13,'view_user_table'),
(53,'Can add shop_table',14,'add_shop_table'),
(54,'Can change shop_table',14,'change_shop_table'),
(55,'Can delete shop_table',14,'delete_shop_table'),
(56,'Can view shop_table',14,'view_shop_table'),
(57,'Can add shop_req_master',15,'add_shop_req_master'),
(58,'Can change shop_req_master',15,'change_shop_req_master'),
(59,'Can delete shop_req_master',15,'delete_shop_req_master'),
(60,'Can view shop_req_master',15,'view_shop_req_master'),
(61,'Can add shop_req_details',16,'add_shop_req_details'),
(62,'Can change shop_req_details',16,'change_shop_req_details'),
(63,'Can delete shop_req_details',16,'delete_shop_req_details'),
(64,'Can view shop_req_details',16,'view_shop_req_details'),
(65,'Can add shop_product',17,'add_shop_product'),
(66,'Can change shop_product',17,'change_shop_product'),
(67,'Can delete shop_product',17,'delete_shop_product'),
(68,'Can view shop_product',17,'view_shop_product'),
(69,'Can add shop_bill',18,'add_shop_bill'),
(70,'Can change shop_bill',18,'change_shop_bill'),
(71,'Can delete shop_bill',18,'delete_shop_bill'),
(72,'Can view shop_bill',18,'view_shop_bill'),
(73,'Can add order_details',19,'add_order_details'),
(74,'Can change order_details',19,'change_order_details'),
(75,'Can delete order_details',19,'delete_order_details'),
(76,'Can view order_details',19,'view_order_details'),
(77,'Can add manufacturer_table',20,'add_manufacturer_table'),
(78,'Can change manufacturer_table',20,'change_manufacturer_table'),
(79,'Can delete manufacturer_table',20,'delete_manufacturer_table'),
(80,'Can view manufacturer_table',20,'view_manufacturer_table'),
(81,'Can add manufacture_product',21,'add_manufacture_product'),
(82,'Can change manufacture_product',21,'change_manufacture_product'),
(83,'Can delete manufacture_product',21,'delete_manufacture_product'),
(84,'Can view manufacture_product',21,'view_manufacture_product'),
(85,'Can add distributor_req_master',22,'add_distributor_req_master'),
(86,'Can change distributor_req_master',22,'change_distributor_req_master'),
(87,'Can delete distributor_req_master',22,'delete_distributor_req_master'),
(88,'Can view distributor_req_master',22,'view_distributor_req_master'),
(89,'Can add distributor_req_details',23,'add_distributor_req_details'),
(90,'Can change distributor_req_details',23,'change_distributor_req_details'),
(91,'Can delete distributor_req_details',23,'delete_distributor_req_details'),
(92,'Can view distributor_req_details',23,'view_distributor_req_details'),
(93,'Can add distributor_product',24,'add_distributor_product'),
(94,'Can change distributor_product',24,'change_distributor_product'),
(95,'Can delete distributor_product',24,'delete_distributor_product'),
(96,'Can view distributor_product',24,'view_distributor_product'),
(97,'Can add bill_details',25,'add_bill_details'),
(98,'Can change bill_details',25,'change_bill_details'),
(99,'Can delete bill_details',25,'delete_bill_details'),
(100,'Can view bill_details',25,'view_bill_details'),
(101,'Can add return_table',26,'add_return_table'),
(102,'Can change return_table',26,'change_return_table'),
(103,'Can delete return_table',26,'delete_return_table'),
(104,'Can view return_table',26,'view_return_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$720000$jy9qsoyAbEP6db5zNFfsFN$Ms3Z6P0+NGNXU6oKHLaDXOjjVA/pLnZquNknnXG1pyQ=','2024-04-25 08:35:08.675831',1,'admin','','','admin@gmail.com',1,1,'2024-04-12 08:09:40.268047');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'fake_product','bill'),
(25,'fake_product','bill_details'),
(8,'fake_product','category'),
(24,'fake_product','distributor_product'),
(23,'fake_product','distributor_req_details'),
(22,'fake_product','distributor_req_master'),
(9,'fake_product','distributor_table'),
(10,'fake_product','login_table'),
(21,'fake_product','manufacture_product'),
(20,'fake_product','manufacturer_table'),
(11,'fake_product','order'),
(19,'fake_product','order_details'),
(12,'fake_product','product'),
(26,'fake_product','return_table'),
(18,'fake_product','shop_bill'),
(17,'fake_product','shop_product'),
(16,'fake_product','shop_req_details'),
(15,'fake_product','shop_req_master'),
(14,'fake_product','shop_table'),
(13,'fake_product','user_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-01-31 06:31:55.805161'),
(2,'auth','0001_initial','2024-01-31 06:31:56.826373'),
(3,'admin','0001_initial','2024-01-31 06:31:57.288787'),
(4,'admin','0002_logentry_remove_auto_add','2024-01-31 06:31:57.323255'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-01-31 06:31:57.349367'),
(6,'contenttypes','0002_remove_content_type_name','2024-01-31 06:31:57.549098'),
(7,'auth','0002_alter_permission_name_max_length','2024-01-31 06:31:57.694235'),
(8,'auth','0003_alter_user_email_max_length','2024-01-31 06:31:57.735192'),
(9,'auth','0004_alter_user_username_opts','2024-01-31 06:31:57.743165'),
(10,'auth','0005_alter_user_last_login_null','2024-01-31 06:31:57.861108'),
(11,'auth','0006_require_contenttypes_0002','2024-01-31 06:31:57.865111'),
(12,'auth','0007_alter_validators_add_error_messages','2024-01-31 06:31:57.875641'),
(13,'auth','0008_alter_user_username_max_length','2024-01-31 06:31:57.941449'),
(14,'auth','0009_alter_user_last_name_max_length','2024-01-31 06:31:58.057227'),
(15,'auth','0010_alter_group_name_max_length','2024-01-31 06:31:58.096599'),
(16,'auth','0011_update_proxy_permissions','2024-01-31 06:31:58.118999'),
(17,'auth','0012_alter_user_first_name_max_length','2024-01-31 06:31:58.233073'),
(18,'fake_product','0001_initial','2024-01-31 06:32:01.408612'),
(19,'sessions','0001_initial','2024-01-31 06:32:01.458596'),
(20,'fake_product','0002_manufacture_product_size','2024-02-19 08:51:16.831888'),
(21,'fake_product','0003_auto_20240219_1510','2024-02-19 09:41:07.810838'),
(22,'fake_product','0004_alter_product_price','2024-02-19 10:35:54.668109'),
(23,'fake_product','0005_distributor_req_master_amount','2024-02-20 06:04:29.350439'),
(24,'fake_product','0006_auto_20240223_1249','2024-02-23 07:20:34.021718'),
(25,'fake_product','0007_auto_20240301_1533','2024-03-01 10:03:17.823044'),
(26,'fake_product','0008_shop_req_master_amount','2024-03-01 11:39:46.580392'),
(27,'fake_product','0009_auto_20240320_1232','2024-03-20 07:03:05.774435'),
(28,'fake_product','0010_alter_order_details_product','2024-03-20 07:20:34.679505'),
(29,'fake_product','0011_alter_order_details_product','2024-03-20 07:24:04.266992'),
(30,'fake_product','0002_auto_20240327_2124','2024-03-27 15:54:33.611992'),
(31,'fake_product','0003_bill_bill_details','2024-03-27 15:55:29.509288'),
(32,'fake_product','0004_product_stock','2024-03-27 18:28:52.136823'),
(33,'fake_product','0005_alter_product_stock','2024-03-31 06:52:33.610663'),
(34,'fake_product','0006_auto_20240402_1448','2024-04-02 09:19:08.825244'),
(35,'fake_product','0007_order_gst','2024-04-02 09:22:28.906321'),
(36,'fake_product','0008_return_table_status','2024-04-02 10:27:13.552522');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('18fvryj69aijr046nhuewzuto5i0evhn','.eJxVjsEOwiAQRP-FsyFdtyzEo3e_gSywlWoDSWlPjf9um_Sg13kzL7Mpz-uS_dpk9mNSNwXq8psFjm8pB0gvLs-qYy3LPAZ9VPRJm37UJNP97P4JMre8rynFARCABhRwxgZJkQFYsCPTG0voOKIEuhpnEVwK5GAQwk5sH_pul07HP6DPF9pYObQ:1rzuZQ:_oxx8TEIo2-HxJ-4QIpHsLy40SPgTPWK5p1gzZ8yVGo','2024-05-09 08:35:08.679260'),
('56pzi9r2fccqpt2kudftr490etkwyqmg','eyJsaWQiOjE1LCJtaWQiOjYsInBpZCI6NTUsInMiOjEwLCJhbXQiOjQ2MTY3fQ:1ripmw:nfBoE7RnKPUDojjEdsZJxHUgpbDYJL1uL-0TOipyTpw','2024-03-23 06:02:30.148388'),
('6u7nk7qo48nsz6ahkzjbmt7hmsd4hg5z','.eJxVjsEOwiAQRP-FsyFdtyzEo3e_gSywlWoDSWlPjf9um_Sg13kzL7Mpz-uS_dpk9mNSNwXq8psFjm8pB0gvLs-qYy3LPAZ9VPRJm37UJNP97P4JMre8rynFARCABhRwxgZJkQFYsCPTG0voOKIEuhpnEVwK5GAQwk5sH_pul07HPzCfL9pWObM:1rvCYj:ahfPGFbVSMcAvNi6u7dNN-Xy_0pycuLSCz_8xqQiafo','2024-04-26 08:46:57.730743'),
('6w85dzedqwdrugycke3h5h8vs6ig9a25','eyJsaWQiOjE2LCJkaWQiOjMsInNwaWQiOjQ2LCJzIjoxM30:1rmQiu:kGUe0OSwngV7KeVsQZvhOLSGyDdbKqRQo4NZYVn7Lbc','2024-04-02 04:05:12.660374'),
('7rbcf0z4dpq9e0i5lc1l7t5cwa60jf5t','.eJxVjsEOwiAQRP-FsyFdtyzEo3e_gSywlWoDSWlPjf9um_Sg13kzL7Mpz-uS_dpk9mNSNwXq8psFjm8pB0gvLs-qYy3LPAZ9VPRJm37UJNP97P4JMre8rynFARCABhRwxgZJkQFYsCPTG0voOKIEuhpnEVwK5GAQwk5sH_pul07HPzCfL9pWObM:1rvD5f:tQM98sO7WuihmAmR7KW4XIAK1EzOJMaFZNle_ZoRqr0','2024-04-26 09:20:59.353778'),
('87ux4taffk9eujec5cikadzddegy39fo','eyJsaWQiOjE2fQ:1rqqM2:yq78Q1sVlJfuSoY11n2C5JjLeNKh4FWu1AaYux42d1Q','2024-04-14 08:15:50.514227'),
('9u5iwv1e22sa5o65fzmer449prvttjha','eyJsaWQiOjEsInBpZCI6M30:1rWWVm:Q7ZULUEb2sw0cdGAW8RKW1Fkd1uQIYFFf-YWW5ml46w','2024-02-18 07:01:54.928101'),
('arb9nkax2ebrs9ksl70jjozamj2kv8ck','.eJxVjsEOwiAQRP-FsyFdtyzEo3e_gSywlWoDSWlPjf9um_Sg13kzL7Mpz-uS_dpk9mNSNwXq8psFjm8pB0gvLs-qYy3LPAZ9VPRJm37UJNP97P4JMre8rynFARCABhRwxgZJkQFYsCPTG0voOKIEuhpnEVwK5GAQwk5sH_pul07HP3CfL9pcObY:1rweVb:6G2XELuHm4aP0dl2053-gIuy4SL6PjQVQJIZ1DwUVqY','2024-04-30 08:49:43.612527'),
('auqg3qy8l9ghmacazvs6kxgbs16harmb','eyJsaWQiOjE2LCJwaWQiOjMsIm9pZCI6MTN9:1rrXqq:6E9dNUPVsxUIsHab51IIvcP79tG-jwz88C63CXtxJgk','2024-04-16 06:42:32.931160'),
('aw02p53v6hvzhm32kj8q676irkamoezo','eyJsaWQiOjE2fQ:1rmnm6:Zry0aCzqLMRrXq7zGFgrOSwE0E-WQrFRjtKv3fILT0s','2024-04-03 04:42:02.280991'),
('boewujkmsmp88g9k4nvvb3ep83qsea2a','eyJsaWQiOjE2fQ:1rlkXW:N3PUUgHyOMtVovWgxbxeNGVVyuz2yLuuaBsouGGOrPU','2024-03-31 07:02:38.710465'),
('d1n8uecaqh08o4zwwply8ifn25fcitpt','eyJsaWQiOjE2fQ:1rmnm6:Zry0aCzqLMRrXq7zGFgrOSwE0E-WQrFRjtKv3fILT0s','2024-04-03 04:42:02.281986'),
('f7115pfrtngmc0u2tks6y4p4284nup67','eyJsaWQiOjF9:1ratKd:i5-yA0J2ZOmBPwQ0ZSTzw2fF7GSF9tWiJR4222EWkZM','2024-03-01 08:12:27.167616'),
('ff8s950as9bdfft7hicc8wx85gv3i0gm','eyJsaWQiOjE2LCJkaWQiOjN9:1rfzAJ:uf1xCx3EuAGaLPy46uEivjEju5fLFIxWRoeGlK2KzTk','2024-03-15 09:26:51.953003'),
('g2xtfwe7gsps3ivlm559ku39eq12rzof','eyJsaWQiOjE2fQ:1rqA3l:H4jolEVU692S2u-ey2XHPJAo_MknwPr0lRLaI4-IOcg','2024-04-12 11:06:09.225862'),
('jdlf32uqhfsdcmba3jmm04jai2glcf4v','eyJsaWQiOjE2LCJwaWQiOjE5fQ:1rsy6h:hu6fA1KlUgunh8icOIwwHpwMBqDAGtXwQ6oHtGJDIO8','2024-04-20 04:56:47.307386'),
('mcorlgeiugro5ghjqsdds69pd7875rh1','eyJsaWQiOjE2LCJkaWQiOjMsInNwaWQiOjUzLCJzIjoxMH0:1rlkTG:8bmzSYxaD1FPJF-XtzKXZ5m_e3Vk5kZf1F5Xb97fBqs','2024-03-31 06:58:14.594233'),
('nf5i9uuh7vvlo8aotd1my573oxpshr45','eyJsaWQiOjE4fQ:1rd27d:kIQKu5-foRT69YCfZiN2jKU2EwhbmXNSV9zQZQOloYo','2024-03-07 05:59:53.899799'),
('oit1af1j190yu8a6fpfxvvypo5zfsbzr','eyJsaWQiOjF9:1rqqxA:SxbmtimR5KkVQi7z1DUIA2Cxq83lQHS0Y-nfLkZmi54','2024-04-14 08:54:12.815597'),
('oqqczbyao5l1rnljtmc5rpwaunarboqi','eyJsaWQiOjEsInBpZCI6NX0:1rZSzS:044hCcOOsLRRLODR8c41gcxRUf-jwdhKJYVUjBSzCLk','2024-02-26 09:52:42.965060'),
('ppqkxcs3d95hbscx08sz8vmvfau5k2sv','.eJxVjsEOwiAQRP-FsyFdtyzEo3e_gSywlWoDSWlPjf9um_Sg13kzL7Mpz-uS_dpk9mNSNwXq8psFjm8pB0gvLs-qYy3LPAZ9VPRJm37UJNP97P4JMre8rynFARCABhRwxgZJkQFYsCPTG0voOKIEuhpnEVwK5GAQwk5sH_pul07HP_h8AaDrOX4:1rwGlk:02W4UVN6XgAFRTQYkAKQL9nyuFFLO0KuRhgJhSGZZqM','2024-04-29 07:28:48.292294'),
('te8ufze5cz76lg0ofrvnww1dr8628a3c','.eJxVjsEOwiAQRP-FsyFdtyzEo3e_gSywlWoDSWlPjf9um_Sg13kzL7Mpz-uS_dpk9mNSNwXq8psFjm8pB0gvLs-qYy3LPAZ9VPRJm37UJNP97P4JMre8rynFARCABhRwxgZJkQFYsCPTG0voOKIEuhpnEVwK5GAQwk5sH_pul07HP3CfL9pcObY:1rvCXK:O78I4EBWqOSfzM21U-8_Jilj3DfSh7DJ27o5_gMdPwc','2024-04-26 08:45:30.788252'),
('u99rxi4ba0giruuqhi2uwc098mwf60h7','eyJsaWQiOjE2LCJkaWQiOjMsInBpZCI6NTV9:1rip6o:CxwPCqQFiqUQ-05tsEtr-My7jigzF097sX3nS6l68_k','2024-03-23 05:18:58.015086'),
('ujty9lmpgf86y6ph9czzhlkblp4r75pp','eyJsaWQiOjE2fQ:1rlkXX:KRZC0iA6yuFHzTvqX1yUprXBl2Hzd6IxMfQqjJddhsQ','2024-03-31 07:02:39.462111'),
('uqxele73c1ezthjt7d2d5a1q7b9rfn24','.eJxVjsEOwiAQRP-FsyFdtyzEo3e_gSywlWoDSWlPjf9um_Sg13kzL7Mpz-uS_dpk9mNSNwXq8psFjm8pB0gvLs-qYy3LPAZ9VPRJm37UJNP97P4JMre8rynFARCABhRwxgZJkQFYsCPTG0voOKIEuhpnEVwK5GAQwk5sH_pul07HP3CfL9pcObY:1rvCFP:0PwgcfoOH85RTIMpkmf8KbUgSq7KxjlbyatM50OZ9yA','2024-04-26 08:26:59.646264'),
('v6fl18fzg857g3xdnhi9eg0o25miik2l','eyJsaWQiOjE4fQ:1rfLMm:G8WFMdWOOdWHMWnMzXC5dHZ-AO3_bFu2WFgM7cwQL0Y','2024-03-13 14:57:04.026909'),
('zlnkyo27o47oi7ke33vhttvhemx5wwjl','eyJsaWQiOjE2LCJkaWQiOjMsInNwaWQiOjQ2LCJzIjozMH0:1rmQcE:ytYzEA07stk31xCnHkowflbBJnr2qPQ5TG2GD5amfrk','2024-04-02 03:58:18.849994');

/*Table structure for table `fake_product_bill` */

DROP TABLE IF EXISTS `fake_product_bill`;

CREATE TABLE `fake_product_bill` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user` varchar(20) NOT NULL,
  `ph_no` bigint NOT NULL,
  `date` date NOT NULL,
  `amount` int NOT NULL,
  `status` varchar(100) NOT NULL,
  `SHOP_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_bill_SHOP_id_fc168a67_fk_fake_product_shop_table_id` (`SHOP_id`),
  CONSTRAINT `fake_product_bill_SHOP_id_fc168a67_fk_fake_product_shop_table_id` FOREIGN KEY (`SHOP_id`) REFERENCES `fake_product_shop_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_bill` */

insert  into `fake_product_bill`(`id`,`user`,`ph_no`,`date`,`amount`,`status`,`SHOP_id`) values 
(52,'DANISH',7865432345,'2024-04-17',1425,'Paid',8);

/*Table structure for table `fake_product_bill_details` */

DROP TABLE IF EXISTS `fake_product_bill_details`;

CREATE TABLE `fake_product_bill_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` int NOT NULL,
  `quantity` int NOT NULL,
  `BILL_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_bill_de_BILL_id_ee509d03_fk_fake_prod` (`BILL_id`),
  KEY `fake_product_bill_de_PRODUCT_id_274d6278_fk_fake_prod` (`PRODUCT_id`),
  CONSTRAINT `fake_product_bill_de_BILL_id_ee509d03_fk_fake_prod` FOREIGN KEY (`BILL_id`) REFERENCES `fake_product_bill` (`id`),
  CONSTRAINT `fake_product_bill_de_PRODUCT_id_274d6278_fk_fake_prod` FOREIGN KEY (`PRODUCT_id`) REFERENCES `fake_product_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_bill_details` */

insert  into `fake_product_bill_details`(`id`,`amount`,`quantity`,`BILL_id`,`PRODUCT_id`) values 
(61,1425,1,52,19);

/*Table structure for table `fake_product_category` */

DROP TABLE IF EXISTS `fake_product_category`;

CREATE TABLE `fake_product_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category` varchar(100) NOT NULL,
  `details` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_category` */

insert  into `fake_product_category`(`id`,`category`,`details`) values 
(4,'Jean Men','Regular fit\r\n'),
(5,'Shirt Men','Full sleeve'),
(11,'Shirt Ladies','Full sleeve'),
(12,'Jean Ladies','Blue color.'),
(13,'T shirt Men','Loose fit'),
(14,'T shirt Ladies','Loose fit\r\n'),
(15,'Shorts Men','Regular fit.'),
(16,'Jacket Ladies','Fit jacket');

/*Table structure for table `fake_product_distributor_product` */

DROP TABLE IF EXISTS `fake_product_distributor_product`;

CREATE TABLE `fake_product_distributor_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `DISTRIBUTOR_REQUEST_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_distrib_DISTRIBUTOR_REQUEST__e7e03472_fk_fake_prod` (`DISTRIBUTOR_REQUEST_id`),
  CONSTRAINT `fake_product_distrib_DISTRIBUTOR_REQUEST__e7e03472_fk_fake_prod` FOREIGN KEY (`DISTRIBUTOR_REQUEST_id`) REFERENCES `fake_product_distributor_req_details` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1927 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_distributor_product` */

insert  into `fake_product_distributor_product`(`id`,`status`,`date`,`DISTRIBUTOR_REQUEST_id`) values 
(1857,'na','2024-04-16',146),
(1858,'na','2024-04-16',146),
(1859,'na','2024-04-16',146),
(1860,'na','2024-04-16',146),
(1861,'na','2024-04-16',146),
(1862,'Available','2024-04-16',146),
(1863,'Available','2024-04-16',146),
(1864,'Available','2024-04-16',146),
(1865,'Available','2024-04-16',146),
(1866,'Available','2024-04-16',146),
(1867,'na','2024-04-16',147),
(1868,'na','2024-04-16',147),
(1869,'na','2024-04-16',147),
(1870,'na','2024-04-16',147),
(1871,'na','2024-04-16',147),
(1872,'na','2024-04-16',147),
(1873,'na','2024-04-16',147),
(1874,'na','2024-04-16',147),
(1875,'na','2024-04-16',147),
(1876,'na','2024-04-16',147),
(1877,'Available','2024-04-17',148),
(1878,'Available','2024-04-17',148),
(1879,'Available','2024-04-17',148),
(1880,'Available','2024-04-17',148),
(1881,'Available','2024-04-17',148),
(1882,'Available','2024-04-17',148),
(1883,'Available','2024-04-17',148),
(1884,'Available','2024-04-17',148),
(1885,'Available','2024-04-17',148),
(1886,'Available','2024-04-17',148),
(1887,'na','2024-04-17',149),
(1888,'na','2024-04-17',149),
(1889,'na','2024-04-17',149),
(1890,'na','2024-04-17',149),
(1891,'na','2024-04-17',149),
(1892,'Available','2024-04-17',149),
(1893,'Available','2024-04-17',149),
(1894,'Available','2024-04-17',149),
(1895,'Available','2024-04-17',149),
(1896,'Available','2024-04-17',149),
(1897,'na','2024-04-17',150),
(1898,'na','2024-04-17',150),
(1899,'na','2024-04-17',150),
(1900,'na','2024-04-17',150),
(1901,'na','2024-04-17',150),
(1902,'Available','2024-04-17',150),
(1903,'Available','2024-04-17',150),
(1904,'Available','2024-04-17',150),
(1905,'Available','2024-04-17',150),
(1906,'Available','2024-04-17',150),
(1907,'Available','2024-04-19',151),
(1908,'Available','2024-04-19',151),
(1909,'Available','2024-04-19',151),
(1910,'Available','2024-04-19',151),
(1911,'Available','2024-04-19',151),
(1912,'Available','2024-04-19',151),
(1913,'Available','2024-04-19',151),
(1914,'Available','2024-04-19',151),
(1915,'Available','2024-04-19',151),
(1916,'Available','2024-04-19',151),
(1917,'na','2024-04-25',152),
(1918,'na','2024-04-25',152),
(1919,'na','2024-04-25',152),
(1920,'na','2024-04-25',152),
(1921,'na','2024-04-25',152),
(1922,'Available','2024-04-25',152),
(1923,'Available','2024-04-25',152),
(1924,'Available','2024-04-25',152),
(1925,'Available','2024-04-25',152),
(1926,'Available','2024-04-25',152);

/*Table structure for table `fake_product_distributor_req_details` */

DROP TABLE IF EXISTS `fake_product_distributor_req_details`;

CREATE TABLE `fake_product_distributor_req_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `DISTRIBUTOR_MASTER_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_distrib_DISTRIBUTOR_MASTER_i_fa74aab6_fk_fake_prod` (`DISTRIBUTOR_MASTER_id`),
  KEY `fake_product_distrib_PRODUCT_id_b98d6994_fk_fake_prod` (`PRODUCT_id`),
  CONSTRAINT `fake_product_distrib_DISTRIBUTOR_MASTER_i_fa74aab6_fk_fake_prod` FOREIGN KEY (`DISTRIBUTOR_MASTER_id`) REFERENCES `fake_product_distributor_req_master` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=154 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_distributor_req_details` */

insert  into `fake_product_distributor_req_details`(`id`,`quantity`,`DISTRIBUTOR_MASTER_id`,`PRODUCT_id`) values 
(146,10,92,83),
(147,10,93,80),
(148,10,94,79),
(149,10,95,75),
(150,10,96,52),
(151,10,97,69),
(152,10,98,80),
(153,10,99,86);

/*Table structure for table `fake_product_distributor_req_master` */

DROP TABLE IF EXISTS `fake_product_distributor_req_master`;

CREATE TABLE `fake_product_distributor_req_master` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `DISTRIBUTOR_id` bigint NOT NULL,
  `MANFACTURER_id` bigint NOT NULL,
  `amount` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_distrib_DISTRIBUTOR_id_a83350b0_fk_fake_prod` (`DISTRIBUTOR_id`),
  KEY `fake_product_distrib_MANFACTURER_id_daa3fc30_fk_fake_prod` (`MANFACTURER_id`),
  CONSTRAINT `fake_product_distrib_DISTRIBUTOR_id_a83350b0_fk_fake_prod` FOREIGN KEY (`DISTRIBUTOR_id`) REFERENCES `fake_product_distributor_table` (`id`),
  CONSTRAINT `fake_product_distrib_MANFACTURER_id_daa3fc30_fk_fake_prod` FOREIGN KEY (`MANFACTURER_id`) REFERENCES `fake_product_manufacturer_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_distributor_req_master` */

insert  into `fake_product_distributor_req_master`(`id`,`status`,`date`,`DISTRIBUTOR_id`,`MANFACTURER_id`,`amount`) values 
(92,'Accepted','2024-04-16',3,6,13200),
(93,'Accepted','2024-04-16',3,6,12000),
(94,'Accepted','2024-04-17',3,6,18000),
(95,'Accepted','2024-04-17',3,6,12340),
(96,'Accepted','2024-04-17',3,6,14000),
(97,'Accepted','2024-04-19',3,6,14000),
(98,'Accepted','2024-04-25',3,6,12000),
(99,'pending','2024-04-25',3,6,18700);

/*Table structure for table `fake_product_distributor_table` */

DROP TABLE IF EXISTS `fake_product_distributor_table`;

CREATE TABLE `fake_product_distributor_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `ph_no` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `proof` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_distrib_LOGIN_id_8d428a3a_fk_fake_prod` (`LOGIN_id`),
  CONSTRAINT `fake_product_distrib_LOGIN_id_8d428a3a_fk_fake_prod` FOREIGN KEY (`LOGIN_id`) REFERENCES `fake_product_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_distributor_table` */

insert  into `fake_product_distributor_table`(`id`,`name`,`place`,`ph_no`,`photo`,`proof`,`email`,`LOGIN_id`) values 
(3,'DAS','manahalli',8547344533,'d2.jpeg','d2_fKlw2dS.jpeg','das1@gmail.com',15),
(5,'GOVIND','Kammanahalli',9876564357,'d1_52Yf09n.jpeg','d1_JZQhyYL.jpeg','ghd@gmail.com',26),
(7,'ASHOK','HSR Layout',8765679087,'d3_CrHLXyo.jpeg','d3_GfzCWnZ.jpeg','ashok@gmail.com',32),
(8,'Samurai ','Rajajinagar',7337833112,'d11.jpeg','d11_2euzSSG.jpeg','samurai@gmail.com',41),
(9,'AB Clothing','Krishnarajapura',8765432345,'d12.jpg','d12_X1KaVZI.jpg','abcloth@gmail.com',42),
(10,'FAB','Sudhama Nagar',8976545567,'d7.jpeg','d7_GYEinJV.jpeg','fab@gmail.com',43),
(11,'EVERON FASHION','Tirupur',8734013725,'d4.jpeg','d4_8EKXklZ.jpeg','everon@gmail.com',44),
(12,'ANUGRAHA','Adugodi',9980013677,'d8.jpeg','d8_Au5kH47.jpeg','anugraha@gmail.com',45),
(13,'Global Shades','Karnataka',8760456245,'d6.jpg','d6_oeXDSo7.jpg','globalshades@gmail.com',46),
(14,'UNIQUE','Bayatarayanapura',9980133884,'d10.jpeg','d10_UDeMnb1.jpeg','unique@gmail.com',47),
(15,'PARDHA','Kengeri',9875423098,'d4_T2r7t4N.jpeg','d9.jpeg','pardha@gmail.com',63);

/*Table structure for table `fake_product_login_table` */

DROP TABLE IF EXISTS `fake_product_login_table`;

CREATE TABLE `fake_product_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_login_table` */

insert  into `fake_product_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','Admin@123','admin'),
(15,'dist','Dist@123','distributor'),
(16,'shop','Shop@123','shop'),
(18,'man','Man@123','manufacturer'),
(23,'man1','Man1@123','rejected'),
(24,'shop2','Shop2@123','rejected'),
(26,'dist1','Dist1@123','rejected'),
(27,'man2','Man2@123','manufacturer'),
(30,'ARAVIND','Aravind@123','rejected'),
(32,'ashok','Ashok@123','distributor'),
(33,'lee1','Lee1@123','shop'),
(34,'wranglcity','Wranglcity@12','shop'),
(35,'DenimMG','Denimmg@123','manufacturer'),
(36,'Mahan','Mahan@123','rejected'),
(37,'Liyok','Liyok@123','manufacturer'),
(38,'Shahi','Shahi@123','manufacturer'),
(39,'Mother','Mother@123','rejected'),
(40,'Prakash','Prakash@123','manufacturer'),
(41,'Samurai ','Samurai@123','distributor'),
(42,'AB Clothing','Abclothing2123','rejected'),
(43,'FAB','Fab12@123','distributor'),
(44,'Everon','Everon@123','distributor'),
(45,'anugraha','Anugraha@12','distributor'),
(46,'Global','Global@123','distributor'),
(47,'Unique','Unique@123','distributor'),
(52,'Shidu','Shidu@123','user'),
(53,'Salha','Salha@123','user'),
(60,'Neda','Neda@123','user'),
(61,'Afeef','Afeef@124','user'),
(62,'Rajas','Rajas@123','manufacturer'),
(63,'Pardha','Pardha@123','distributor'),
(64,'Brandware','Brand@123','shop'),
(65,'Sheza','Sheza@123','user');

/*Table structure for table `fake_product_manufacture_product` */

DROP TABLE IF EXISTS `fake_product_manufacture_product`;

CREATE TABLE `fake_product_manufacture_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `stock` int NOT NULL,
  `date` date NOT NULL,
  `MANFACTURER_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  `size` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_manufac_MANFACTURER_id_896882a8_fk_fake_prod` (`MANFACTURER_id`),
  KEY `fake_product_manufac_PRODUCT_id_5cf5eb74_fk_fake_prod` (`PRODUCT_id`),
  CONSTRAINT `fake_product_manufac_MANFACTURER_id_896882a8_fk_fake_prod` FOREIGN KEY (`MANFACTURER_id`) REFERENCES `fake_product_manufacturer_table` (`id`),
  CONSTRAINT `fake_product_manufac_PRODUCT_id_5cf5eb74_fk_fake_prod` FOREIGN KEY (`PRODUCT_id`) REFERENCES `fake_product_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_manufacture_product` */

insert  into `fake_product_manufacture_product`(`id`,`stock`,`date`,`MANFACTURER_id`,`PRODUCT_id`,`size`) values 
(23,30,'2024-02-22',6,16,'S'),
(25,30,'2024-02-21',6,15,'S'),
(33,30,'2024-03-02',6,3,'S'),
(34,40,'2024-03-02',6,3,'M'),
(35,50,'2024-03-02',6,14,'M'),
(36,50,'2024-03-02',6,14,'M'),
(37,50,'2024-03-02',6,17,'S'),
(38,100,'2024-03-02',6,17,'M'),
(39,40,'2024-03-03',6,24,'S'),
(40,50,'2024-03-05',6,24,'M'),
(41,80,'2024-03-05',6,24,'L'),
(42,80,'2024-03-05',6,24,'XL'),
(43,40,'2024-03-04',6,23,'S'),
(44,60,'2024-03-04',6,23,'M'),
(45,80,'2024-03-04',6,23,'L'),
(46,30,'2024-03-04',6,22,'S'),
(47,50,'2024-03-04',6,22,'M'),
(48,100,'2024-03-04',6,22,'L'),
(49,100,'2024-03-04',6,22,'XL'),
(50,50,'2024-03-04',6,18,'S'),
(51,50,'2024-03-04',6,19,'M'),
(52,40,'2024-03-04',6,20,'S'),
(53,100,'2024-03-05',6,20,'M'),
(54,80,'2024-03-05',6,21,'S'),
(55,40,'2024-03-05',6,21,'M'),
(56,70,'2024-03-06',6,15,'M'),
(57,80,'2024-03-06',6,16,'L'),
(58,50,'2024-03-06',6,14,'S'),
(59,100,'2024-03-06',6,3,'L'),
(60,50,'2024-03-07',6,3,'S'),
(61,40,'2024-03-08',6,14,'M'),
(62,50,'2024-03-08',6,16,'L'),
(63,60,'2024-03-08',6,24,'M'),
(64,60,'2024-03-09',6,19,'M'),
(65,60,'2024-03-09',6,18,'M'),
(66,45,'2024-03-09',6,23,'S'),
(67,45,'2024-03-10',6,22,'S'),
(68,60,'2024-03-10',6,21,'L'),
(69,15,'2024-03-10',6,20,'L'),
(71,60,'2024-03-11',6,17,'XL'),
(72,5,'2024-03-11',6,14,'L'),
(73,15,'2024-03-11',6,3,'XL'),
(75,10,'2024-03-18',6,16,'S'),
(76,40,'2024-03-18',6,16,'M'),
(77,5,'2024-03-19',6,19,'S'),
(78,40,'2024-03-20',6,14,'L'),
(79,20,'2024-03-20',6,24,'S'),
(80,10,'2024-03-21',6,17,'S'),
(81,50,'2024-04-12',6,15,'S'),
(82,50,'2024-04-15',6,26,'S'),
(83,60,'2024-04-16',6,19,'S'),
(84,50,'2024-04-19',6,24,'M'),
(85,50,'2024-04-25',6,23,'S'),
(86,25,'2024-04-25',6,23,'S'),
(87,50,'2024-04-25',6,22,'L'),
(88,50,'2024-04-25',6,26,'M'),
(89,50,'2024-04-25',6,19,'L');

/*Table structure for table `fake_product_manufacturer_table` */

DROP TABLE IF EXISTS `fake_product_manufacturer_table`;

CREATE TABLE `fake_product_manufacturer_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `ph_no` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `proof` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_manufac_LOGIN_id_08eb74ca_fk_fake_prod` (`LOGIN_id`),
  CONSTRAINT `fake_product_manufac_LOGIN_id_08eb74ca_fk_fake_prod` FOREIGN KEY (`LOGIN_id`) REFERENCES `fake_product_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_manufacturer_table` */

insert  into `fake_product_manufacturer_table`(`id`,`name`,`place`,`ph_no`,`photo`,`proof`,`email`,`LOGIN_id`) values 
(6,'DEVIKA','Koramangala',7865643423,'m3.jpg','m3_QVswaum.jpg','devika@gmail.com',18),
(9,'SERVA','Madiwala',7865432345,'m2_iHkvHM5.jpeg','m2_KcUD2fm.jpeg','serva@gmail.com',23),
(10,'ASF','Manahalli',9677563456,'m2_0xd9xrB.jpeg','deter-counterfeiting.pdf','asf@gmail.com',27),
(11,'ARAVIND','Koramangala',8976789054,'m3_1wBqigP.jpg','m3_aNULFEC.jpg','aravind@gmail.com',30),
(13,'DENIM','MG Road',9876543245,'m4.jpeg','m4_rRTRTbd.jpeg','denimmg@gmail.com',35),
(14,'MAHAN','KR Road',8976567890,'m5.jpg','m5_F23zD0E.jpg','mahan@gmail.com',36),
(15,'LIYOK','Chickpet',9878854534,'m6.jpg','m6_kDPnDbO.jpg','liyok@gmail.com',37),
(16,'Shahi','Arkere',8026481095,'sahi.jpg','sahi_0yOzpgp.jpg','shahi@gmail.com',38),
(17,'Mother Land Garments','Mamulpet',8022208873,'moth.jpeg','moth_zFv9662.jpeg','motherlandgarments@gmail.com',39),
(18,'Prakash Fabrics','Chickpet',9538204085,'m7.jpg','m3_GqCCyT1.jpg','prakashfabrics@gmail.com',40),
(19,'RAJAS','Electronic city',9876543457,'m8.jpg','d5.jpg','rajas@gmail.com',62);

/*Table structure for table `fake_product_order` */

DROP TABLE IF EXISTS `fake_product_order`;

CREATE TABLE `fake_product_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `amount` int NOT NULL,
  `USER_id` bigint NOT NULL,
  `gst` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_order_USER_id_6416612b_fk_fake_prod` (`USER_id`),
  CONSTRAINT `fake_product_order_USER_id_6416612b_fk_fake_prod` FOREIGN KEY (`USER_id`) REFERENCES `fake_product_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=150 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_order` */

insert  into `fake_product_order`(`id`,`status`,`date`,`amount`,`USER_id`,`gst`) values 
(147,'Paid','2024-04-17',1200,5,1296),
(148,'Paid','2024-04-25',1320,5,1425),
(149,'cart','2024-04-25',1200,5,1296);

/*Table structure for table `fake_product_order_details` */

DROP TABLE IF EXISTS `fake_product_order_details`;

CREATE TABLE `fake_product_order_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `ORDER_id` bigint NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  `size` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_order_d_ORDER_id_17c0d870_fk_fake_prod` (`ORDER_id`),
  KEY `fake_product_order_d_PRODUCT_id_4fc01e48_fk_fake_prod` (`PRODUCT_id`),
  CONSTRAINT `fake_product_order_d_ORDER_id_17c0d870_fk_fake_prod` FOREIGN KEY (`ORDER_id`) REFERENCES `fake_product_order` (`id`),
  CONSTRAINT `fake_product_order_d_PRODUCT_id_4fc01e48_fk_fake_prod` FOREIGN KEY (`PRODUCT_id`) REFERENCES `fake_product_shop_req_details` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=206 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_order_details` */

insert  into `fake_product_order_details`(`id`,`quantity`,`ORDER_id`,`PRODUCT_id`,`size`) values 
(203,1,147,94,'S'),
(204,1,148,95,'S'),
(205,1,149,94,'S');

/*Table structure for table `fake_product_product` */

DROP TABLE IF EXISTS `fake_product_product`;

CREATE TABLE `fake_product_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pname` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `photo` varchar(100) NOT NULL,
  `price` double NOT NULL,
  `size` varchar(60) NOT NULL,
  `CATEGORY_id` bigint NOT NULL,
  `stock` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_product_CATEGORY_id_7a31f178_fk_fake_prod` (`CATEGORY_id`),
  CONSTRAINT `fake_product_product_CATEGORY_id_7a31f178_fk_fake_prod` FOREIGN KEY (`CATEGORY_id`) REFERENCES `fake_product_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_product` */

insert  into `fake_product_product`(`id`,`pname`,`description`,`photo`,`price`,`size`,`CATEGORY_id`,`stock`) values 
(3,'Wog','skinny,light blue','skinny.jpeg',1200,'[\'S\', \'M\', \'L\']',4,51),
(14,'Solid Shirt','Black color','black-shirt_XEtHPBv.jpg',1145,'[\'S\', \'M\', \'L\', \'XL\']',5,4),
(15,'Fit Frame','skinny','regular fit_XDvXLIr.jpg',1400,'[\'S\', \'M\', \'L\', \'XL\', \'XXL\']',4,77),
(16,'Crew neck','Regular fit','crew neck_N4JUyBT.jpeg',1234,'[\'S\', \'M\', \'L\', \'XL\', \'XXL\']',13,2),
(17,'Sweater','Orange color','sweat.jpg',1200,'[\'S\', \'M\', \'L\', \'XL\', \'XXL\']',13,7),
(18,'Polo','White color.','polo_B0ToxjI.jpg',1450,'[\'S\', \'M\', \'L\', \'XL\', \'XXL\']',13,48),
(19,'Track','Track pant.','track m.jpg',1320,'[\'M\', \'L\', \'XL\']',4,4),
(20,'Sweate','Sweater for women','sweat w.jpg',1400,'[\'S\', \'M\', \'L\', \'XL\']',14,49),
(21,'Men Blue','Slim fit','shorts m.jpg',1399,'[\'S\', \'M\', \'L\', \'XL\']',15,50),
(22,'Solid Blue','Relaxed fit\r\n','jacket.jpg',2999,'[\'S\', \'M\', \'L\', \'XL\']',16,52),
(23,'Striped','Fit t shirt','striped w.jpg',1870,'[\'S\', \'M\', \'L\']',14,35),
(24,'Straight Jean','Regular fit','straight w.jpg',1800,'[\'S\', \'M\', \'L\', \'XL\', \'XXL\']',4,9),
(26,'Comfort','Loose fit','comfort_PCZcGIG.jpg',1800,'[\'S\', \'M\', \'L\', \'XL\']',4,0);

/*Table structure for table `fake_product_return_table` */

DROP TABLE IF EXISTS `fake_product_return_table`;

CREATE TABLE `fake_product_return_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `reason` varchar(30) NOT NULL,
  `ORDER_id` bigint NOT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_return__ORDER_id_d3ccef41_fk_fake_prod` (`ORDER_id`),
  CONSTRAINT `fake_product_return__ORDER_id_d3ccef41_fk_fake_prod` FOREIGN KEY (`ORDER_id`) REFERENCES `fake_product_order_details` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_return_table` */

insert  into `fake_product_return_table`(`id`,`date`,`reason`,`ORDER_id`,`status`) values 
(15,'2024-04-25','     Damage Product',203,'Accepted');

/*Table structure for table `fake_product_shop_product` */

DROP TABLE IF EXISTS `fake_product_shop_product`;

CREATE TABLE `fake_product_shop_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `DISTRIBUTOR_PRODUCT_id` bigint NOT NULL,
  `SHOP_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_shop_pr_DISTRIBUTOR_PRODUCT__1c15e6f0_fk_fake_prod` (`DISTRIBUTOR_PRODUCT_id`),
  KEY `fake_product_shop_pr_SHOP_id_90901751_fk_fake_prod` (`SHOP_id`),
  CONSTRAINT `fake_product_shop_pr_DISTRIBUTOR_PRODUCT__1c15e6f0_fk_fake_prod` FOREIGN KEY (`DISTRIBUTOR_PRODUCT_id`) REFERENCES `fake_product_distributor_product` (`id`),
  CONSTRAINT `fake_product_shop_pr_SHOP_id_90901751_fk_fake_prod` FOREIGN KEY (`SHOP_id`) REFERENCES `fake_product_shop_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=816 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_shop_product` */

insert  into `fake_product_shop_product`(`id`,`status`,`date`,`DISTRIBUTOR_PRODUCT_id`,`SHOP_id`) values 
(786,'na','2024-04-16',1867,8),
(787,'Available','2024-04-16',1868,8),
(788,'Available','2024-04-16',1869,8),
(789,'Available','2024-04-16',1870,8),
(790,'Available','2024-04-16',1871,8),
(791,'Available','2024-04-16',1872,8),
(792,'Available','2024-04-16',1873,8),
(793,'Available','2024-04-16',1874,8),
(794,'Available','2024-04-16',1875,8),
(795,'Available','2024-04-16',1876,8),
(796,'na','2024-04-16',1857,8),
(797,'na','2024-04-16',1858,8),
(798,'Available','2024-04-16',1859,8),
(799,'Available','2024-04-16',1860,8),
(800,'Available','2024-04-16',1861,8),
(801,'Available','2024-04-19',1897,8),
(802,'Available','2024-04-19',1898,8),
(803,'Available','2024-04-19',1899,8),
(804,'Available','2024-04-19',1900,8),
(805,'Available','2024-04-19',1901,8),
(806,'Available','2024-04-25',1887,8),
(807,'Available','2024-04-25',1888,8),
(808,'Available','2024-04-25',1889,8),
(809,'Available','2024-04-25',1890,8),
(810,'Available','2024-04-25',1891,8),
(811,'Available','2024-04-25',1917,8),
(812,'Available','2024-04-25',1918,8),
(813,'Available','2024-04-25',1919,8),
(814,'Available','2024-04-25',1920,8),
(815,'Available','2024-04-25',1921,8);

/*Table structure for table `fake_product_shop_req_details` */

DROP TABLE IF EXISTS `fake_product_shop_req_details`;

CREATE TABLE `fake_product_shop_req_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `PRODUCT_id` bigint NOT NULL,
  `SHOP_MASTER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_shop_re_SHOP_MASTER_id_0f6f78db_fk_fake_prod` (`SHOP_MASTER_id`),
  KEY `fake_product_shop_re_PRODUCT_id_c61450d3_fk_fake_prod` (`PRODUCT_id`),
  CONSTRAINT `fake_product_shop_re_PRODUCT_id_c61450d3_fk_fake_prod` FOREIGN KEY (`PRODUCT_id`) REFERENCES `fake_product_manufacture_product` (`id`),
  CONSTRAINT `fake_product_shop_re_SHOP_MASTER_id_0f6f78db_fk_fake_prod` FOREIGN KEY (`SHOP_MASTER_id`) REFERENCES `fake_product_shop_req_master` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_shop_req_details` */

insert  into `fake_product_shop_req_details`(`id`,`quantity`,`PRODUCT_id`,`SHOP_MASTER_id`) values 
(94,9,80,75),
(95,5,83,76),
(96,5,69,77),
(97,5,75,78),
(98,5,80,79);

/*Table structure for table `fake_product_shop_req_master` */

DROP TABLE IF EXISTS `fake_product_shop_req_master`;

CREATE TABLE `fake_product_shop_req_master` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `DISTRIBUTOR_id` bigint NOT NULL,
  `SHOP_id` bigint NOT NULL,
  `amount` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_shop_re_DISTRIBUTOR_id_75719c8c_fk_fake_prod` (`DISTRIBUTOR_id`),
  KEY `fake_product_shop_re_SHOP_id_95393caf_fk_fake_prod` (`SHOP_id`),
  CONSTRAINT `fake_product_shop_re_DISTRIBUTOR_id_75719c8c_fk_fake_prod` FOREIGN KEY (`DISTRIBUTOR_id`) REFERENCES `fake_product_distributor_table` (`id`),
  CONSTRAINT `fake_product_shop_re_SHOP_id_95393caf_fk_fake_prod` FOREIGN KEY (`SHOP_id`) REFERENCES `fake_product_shop_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_shop_req_master` */

insert  into `fake_product_shop_req_master`(`id`,`status`,`date`,`DISTRIBUTOR_id`,`SHOP_id`,`amount`) values 
(75,'Accepted','2024-04-16',3,8,6000),
(76,'Accepted','2024-04-16',3,8,6600),
(77,'Accepted','2024-04-19',3,8,7000),
(78,'Accepted','2024-04-25',3,8,6170),
(79,'Accepted','2024-04-25',3,8,6000);

/*Table structure for table `fake_product_shop_table` */

DROP TABLE IF EXISTS `fake_product_shop_table`;

CREATE TABLE `fake_product_shop_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `ph_no` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `proof` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_shop_ta_LOGIN_id_81c2992d_fk_fake_prod` (`LOGIN_id`),
  CONSTRAINT `fake_product_shop_ta_LOGIN_id_81c2992d_fk_fake_prod` FOREIGN KEY (`LOGIN_id`) REFERENCES `fake_product_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_shop_table` */

insert  into `fake_product_shop_table`(`id`,`name`,`place`,`ph_no`,`photo`,`proof`,`email`,`LOGIN_id`) values 
(8,'wranglee','Manglore',9847438967,'s1.jpeg','s1_wZkwoLx.jpeg','wranglee@gmail.com',16),
(11,'ASS','Electronic city',8765456789,'s2_u4INyRi.jpeg','s2_5ViNDf8.jpeg','ass@gmail.com',24),
(13,'Lee','Manhalli',9876545678,'s7.jpg','s7_TuvBpfj.jpg','lee1@gmail.com',33),
(14,'Wrangler City','Shivapuram',8976787654,'s8.jpeg','s8_wY2KFri.jpeg','wranglercity@gmail.com',34),
(15,'Brand Ware','Koramangala',7947106231,'s5.jpeg','d5_SseLkEz.jpg','brandware@gmail.com',64);

/*Table structure for table `fake_product_user_table` */

DROP TABLE IF EXISTS `fake_product_user_table`;

CREATE TABLE `fake_product_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `pin` bigint NOT NULL,
  `ph_no` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fake_product_user_ta_LOGIN_id_b8360860_fk_fake_prod` (`LOGIN_id`),
  CONSTRAINT `fake_product_user_ta_LOGIN_id_b8360860_fk_fake_prod` FOREIGN KEY (`LOGIN_id`) REFERENCES `fake_product_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `fake_product_user_table` */

insert  into `fake_product_user_table`(`id`,`name`,`place`,`post`,`pin`,`ph_no`,`email`,`LOGIN_id`) values 
(4,'Shihad','kgm','kgm',673521,9847438967,'shihad@gmail.con',52),
(5,'Salha','ckl','pdl',673571,9544358016,'nksalha@gmail.com',53),
(12,'Neda','ekm','ekm',675432,9876543234,'nedanjb@gmail.com',60),
(13,'Afeef','ehm','egn',675432,9876543234,'afeef@gmail.com',61),
(14,'Sheza','oms','oms',675432,9876545678,'sheza@gmail.com',65);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
