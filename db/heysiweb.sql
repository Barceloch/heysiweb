-- File name: D:\Cosas de Trabajo\PROYECTOS\Proyecto WEB\heysiweb\db\heysiweb.sql
-- Created by ꨤʰུʰ 


--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` INT NOT NULL DEFAULT 0,
  `name` VARCHAR(50) NOT NULL,
  `content_type_id` INT NOT NULL DEFAULT 0,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id` ASC),
  KEY `auth_permission_1bb8f392` (`content_type_id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` INT NOT NULL DEFAULT 0,
  `user_id` INT NOT NULL DEFAULT 0,
  `permission_id` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id` ASC),
  KEY `auth_user_user_permissions_403f60f` (`user_id` ASC),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id` ASC),
  CONSTRAINT `permission_id_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` INT NOT NULL DEFAULT 0,
  `name` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` INT NOT NULL DEFAULT 0,
  `group_id` INT NOT NULL DEFAULT 0,
  `permission_id` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id` ASC),
  KEY `auth_group_permissions_425ae3c4` (`group_id` ASC),
  KEY `auth_group_permissions_1e014c8f` (`permission_id` ASC),
  CONSTRAINT `permission_id_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` INT NOT NULL DEFAULT 0,
  `user_id` INT NOT NULL DEFAULT 0,
  `group_id` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id` ASC),
  KEY `auth_user_groups_403f60f` (`user_id` ASC),
  KEY `auth_user_groups_425ae3c4` (`group_id` ASC),
  CONSTRAINT `group_id_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` INT NOT NULL DEFAULT 0,
  `username` VARCHAR(30) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(30) NOT NULL,
  `email` VARCHAR(75) NOT NULL,
  `password` VARCHAR(128) NOT NULL,
  `is_staff` TEXT NOT NULL,
  `is_active` TEXT NOT NULL,
  `is_superuser` TEXT NOT NULL,
  `last_login` DATETIME NOT NULL,
  `date_joined` DATETIME NOT NULL,
  PRIMARY KEY (`id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` INT NOT NULL DEFAULT 0,
  `name` VARCHAR(100) NOT NULL,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` INT NOT NULL DEFAULT 0,
  `action_time` DATETIME NOT NULL,
  `user_id` INT NOT NULL DEFAULT 0,
  `content_type_id` INT NULL DEFAULT 0,
  `object_id` TEXT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` TEXT NOT NULL,
  `change_message` TEXT NOT NULL,
  PRIMARY KEY (`id` ASC),
  KEY `django_admin_log_403f60f` (`user_id` ASC),
  KEY `django_admin_log_1bb8f392` (`content_type_id` ASC),
  CONSTRAINT `content_type_id_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `user_id_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` TEXT NOT NULL,
  `expire_date` DATETIME NOT NULL,
  PRIMARY KEY (`session_key` ASC),
  KEY `django_session_3da3d3d8` (`expire_date` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `django_site`
--

CREATE TABLE `django_site` (
  `id` INT NOT NULL DEFAULT 0,
  `domain` VARCHAR(100) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `auth_message`
--

CREATE TABLE `auth_message` (
  `id` INT NOT NULL DEFAULT 0,
  `user_id` INT NOT NULL DEFAULT 0,
  `message` TEXT NOT NULL,
  PRIMARY KEY (`id` ASC),
  KEY `auth_message_403f60f` (`user_id` ASC),
  CONSTRAINT `user_id_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `south_migrationhistory`
--

CREATE TABLE `south_migrationhistory` (
  `id` INT NOT NULL DEFAULT 0,
  `app_name` VARCHAR(255) NOT NULL,
  `migration` VARCHAR(255) NOT NULL,
  `applied` DATETIME NOT NULL,
  PRIMARY KEY (`id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `itemssite_bannerslider`
--

CREATE TABLE `itemssite_bannerslider` (
  `title` VARCHAR(100) NOT NULL,
  `slug` VARCHAR(255) NOT NULL,
  `details` TEXT NOT NULL,
  `slider_img` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`slug` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `itemssite_homeservice`
--

CREATE TABLE `itemssite_homeservice` (
  `id` INT NOT NULL DEFAULT 0,
  `title` VARCHAR(100) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `details` TEXT NOT NULL,
  `language` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `itemssite_faq`
--

CREATE TABLE `itemssite_faq` (
  `id` INT NOT NULL DEFAULT 0,
  `question` VARCHAR(255) NOT NULL,
  `answer` TEXT NOT NULL,
  `language` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `itemssite_homepost`
--

CREATE TABLE `itemssite_homepost` (
  `description` VARCHAR(255) NOT NULL,
  `language` VARCHAR(2) NOT NULL,
  `title` VARCHAR(100) NOT NULL,
  `details` TEXT NOT NULL,
  `id` INT NOT NULL DEFAULT 0,
  `home_img` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `servicespost_city`
--

CREATE TABLE `servicespost_city` (
  `name_city` VARCHAR(40) NOT NULL,
  `machine_name_city` VARCHAR(255) NOT NULL,
  `details` TEXT NOT NULL,
  PRIMARY KEY (`machine_name_city` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `servicespost_zone`
--

CREATE TABLE `servicespost_zone` (
  `name_zone` VARCHAR(40) NOT NULL,
  `machine_name_zone` VARCHAR(255) NOT NULL,
  `details` TEXT NOT NULL,
  `city_id` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`machine_name_zone` ASC),
  KEY `servicespost_zone_586a73b5` (`city_id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `servicespost_album`
--

CREATE TABLE `servicespost_album` (
  `id` INT NOT NULL DEFAULT 0,
  `album_name` VARCHAR(60) NOT NULL,
  PRIMARY KEY (`id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `servicespost_image`
--

CREATE TABLE `servicespost_image` (
  `id` INT NOT NULL DEFAULT 0,
  `album_id` INT NULL DEFAULT 0,
  `title` VARCHAR(60) NULL DEFAULT NULL,
  `description` VARCHAR(50) NOT NULL,
  `image` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id` ASC),
  KEY `servicespost_image_1293c648` (`album_id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `servicespost_servicetype`
--

CREATE TABLE `servicespost_servicetype` (
  `name_type` VARCHAR(40) NOT NULL,
  `machine_name_type` VARCHAR(255) NOT NULL,
  `details` TEXT NOT NULL,
  PRIMARY KEY (`machine_name_type` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `servicespost_comment`
--

CREATE TABLE `servicespost_comment` (
  `id` INT NOT NULL DEFAULT 0,
  `name` VARCHAR(42) NOT NULL,
  `email` VARCHAR(75) NOT NULL,
  `country` VARCHAR(200) NULL DEFAULT NULL,
  `text` TEXT NOT NULL,
  `service_id` VARCHAR(30) NOT NULL,
  `created_on` DATETIME NOT NULL,
  `is_public` TEXT NOT NULL,
  PRIMARY KEY (`id` ASC),
  KEY `servicespost_comment_6f1d73c2` (`service_id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `servicespost_bookroom`
--

CREATE TABLE `servicespost_bookroom` (
  `id` INT NOT NULL DEFAULT 0,
  `name` VARCHAR(42) NOT NULL,
  `email` VARCHAR(75) NOT NULL,
  `country` VARCHAR(200) NOT NULL,
  `date_in` DATE NOT NULL,
  `date_out` DATE NOT NULL,
  `paxs` TEXT NOT NULL,
  `rooms` TEXT NOT NULL,
  `text` TEXT NOT NULL,
  `service_id` VARCHAR(30) NOT NULL,
  `is_confirmed` TEXT NOT NULL,
  `created_on` DATETIME NOT NULL,
  `is_public` TEXT NOT NULL,
  PRIMARY KEY (`id` ASC),
  KEY `servicespost_bookroom_6f1d73c2` (`service_id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `servicespost_reservationkey`
--

CREATE TABLE `servicespost_reservationkey` (
  `id` INT NOT NULL DEFAULT 0,
  `service_key` VARCHAR(40) NOT NULL,
  `s_confirmed` TEXT NOT NULL,
  `client_key` VARCHAR(40) NOT NULL,
  `c_confirmed` TEXT NOT NULL,
  `book_id` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id` ASC),
  KEY `servicespost_reservationkey_752eb95b` (`book_id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `servicespost_servicemodel`
--

CREATE TABLE `servicespost_servicemodel` (
  `service_img` VARCHAR(100) NOT NULL,
  `machine_name` VARCHAR(30) NOT NULL,
  `description` VARCHAR(50) NOT NULL,
  `album_id` INT NULL DEFAULT 0,
  `city_id` VARCHAR(255) NOT NULL,
  `reservations` TEXT NOT NULL,
  `service_type_id` VARCHAR(255) NOT NULL,
  `comments` TEXT NOT NULL,
  `is_premium` TEXT NOT NULL,
  `small_link` VARCHAR(30) NOT NULL,
  `zone_id` VARCHAR(255) NOT NULL,
  `details` TEXT NOT NULL,
  `is_public` TEXT NOT NULL,
  `author_id` INT NOT NULL DEFAULT 0,
  `email` VARCHAR(75) NULL DEFAULT NULL,
  `name` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`machine_name` ASC),
  KEY `servicespost_servicemodel_4bf5c947` (`small_link` ASC),
  KEY `servicespost_servicemodel_337b96ff` (`author_id` ASC),
  KEY `servicespost_servicemodel_1293c648` (`album_id` ASC),
  KEY `servicespost_servicemodel_2957a812` (`zone_id` ASC),
  KEY `servicespost_servicemodel_586a73b5` (`city_id` ASC),
  KEY `servicespost_servicemodel_23ff352c` (`service_type_id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `easy_thumbnails_source`
--

CREATE TABLE `easy_thumbnails_source` (
  `id` INT NOT NULL DEFAULT 0,
  `modified` DATETIME NOT NULL,
  `storage_hash` VARCHAR(40) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id` ASC),
  KEY `easy_thumbnails_source_52094d6e` (`name` ASC),
  KEY `easy_thumbnails_source_3a997c55` (`storage_hash` ASC),
  UNIQUE KEY `easy_thumbnails_source_name__storage_hash` (`name` ASC,`storage_hash` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `easy_thumbnails_thumbnail`
--

CREATE TABLE `easy_thumbnails_thumbnail` (
  `source_id` INT NOT NULL DEFAULT 0,
  `modified` DATETIME NOT NULL,
  `id` INT NOT NULL DEFAULT 0,
  `storage_hash` VARCHAR(40) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id` ASC),
  KEY `easy_thumbnails_thumbnail_3a997c55` (`storage_hash` ASC),
  KEY `easy_thumbnails_thumbnail_7607617b` (`source_id` ASC),
  KEY `easy_thumbnails_thumbnail_52094d6e` (`name` ASC),
  UNIQUE KEY `easy_thumbnails_thumbnail_source_id__name__storage_hash` (`source_id` ASC,`name` ASC,`storage_hash` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `captcha_captchastore`
--

CREATE TABLE `captcha_captchastore` (
  `id` INT NOT NULL DEFAULT 0,
  `challenge` VARCHAR(32) NOT NULL,
  `response` VARCHAR(32) NOT NULL,
  `hashkey` VARCHAR(40) NOT NULL,
  `expiration` DATETIME NOT NULL,
  PRIMARY KEY (`id` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `visits_visit`
--

CREATE TABLE `visits_visit` (
  `object_model` VARCHAR(255) NOT NULL,
  `last_visit` DATETIME NULL DEFAULT '00-00-00 00:00:00',
  `uri` VARCHAR(255) NULL DEFAULT NULL,
  `visits` INT NOT NULL DEFAULT 0,
  `object_id` VARCHAR(255) NOT NULL,
  `visitor_hash` VARCHAR(40) NULL DEFAULT NULL,
  `object_app` VARCHAR(255) NOT NULL,
  `ip_address` VARCHAR(15) NULL DEFAULT NULL,
  `id` INT NOT NULL DEFAULT 0,
  `blocked` TEXT NOT NULL,
  PRIMARY KEY (`id` ASC),
  KEY `visits_visit_4a0a4867` (`ip_address` ASC),
  KEY `visits_visit_7cb683de` (`visitor_hash` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (1,'Can add permission',1,'add_permission');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (2,'Can change permission',1,'change_permission');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (3,'Can delete permission',1,'delete_permission');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (4,'Can add group',2,'add_group');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (5,'Can change group',2,'change_group');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (6,'Can delete group',2,'delete_group');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (7,'Can add user',3,'add_user');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (8,'Can change user',3,'change_user');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (9,'Can delete user',3,'delete_user');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (10,'Can add message',4,'add_message');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (11,'Can change message',4,'change_message');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (12,'Can delete message',4,'delete_message');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (13,'Can add content type',5,'add_contenttype');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (14,'Can change content type',5,'change_contenttype');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (15,'Can delete content type',5,'delete_contenttype');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (16,'Can add session',6,'add_session');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (17,'Can change session',6,'change_session');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (18,'Can delete session',6,'delete_session');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (19,'Can add site',7,'add_site');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (20,'Can change site',7,'change_site');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (21,'Can delete site',7,'delete_site');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (22,'Can add log entry',8,'add_logentry');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (23,'Can change log entry',8,'change_logentry');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (24,'Can delete log entry',8,'delete_logentry');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (25,'Can add migration history',9,'add_migrationhistory');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (26,'Can change migration history',9,'change_migrationhistory');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (27,'Can delete migration history',9,'delete_migrationhistory');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (28,'Can add Objeto del banner',10,'add_bannerslider');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (29,'Can change Objeto del banner',10,'change_bannerslider');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (30,'Can delete Objeto del banner',10,'delete_bannerslider');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (31,'Can add Post de inicio',11,'add_homepost');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (32,'Can change Post de inicio',11,'change_homepost');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (33,'Can delete Post de inicio',11,'delete_homepost');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (34,'Can add Servicio HeySi',12,'add_homeservice');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (35,'Can change Servicio HeySi',12,'change_homeservice');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (36,'Can delete Servicio HeySi',12,'delete_homeservice');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (37,'Can add Pregunta frecuente',13,'add_faq');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (38,'Can change Pregunta frecuente',13,'change_faq');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (39,'Can delete Pregunta frecuente',13,'delete_faq');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (40,'Can add Provincia',14,'add_city');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (41,'Can change Provincia',14,'change_city');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (42,'Can delete Provincia',14,'delete_city');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (43,'Can add Municipio',15,'add_zone');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (44,'Can change Municipio',15,'change_zone');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (45,'Can delete Municipio',15,'delete_zone');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (46,'Can add Galería de fotos',16,'add_album');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (47,'Can change Galería de fotos',16,'change_album');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (48,'Can delete Galería de fotos',16,'delete_album');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (49,'Can add Imágen',17,'add_image');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (50,'Can change Imágen',17,'change_image');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (51,'Can delete Imágen',17,'delete_image');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (52,'41-TRIAL-Can add Tipo de servicio 167',18,'34-TRIAL-add_servicetype 100');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (53,'269-TRIAL-Can change Tipo de servicio 124',18,'78-TRIAL-change_servicetype 258');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (54,'262-TRIAL-Can delete Tipo de servicio 164',18,'5-TRIAL-delete_servicetype 245');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (55,'181-TRIAL-Can add Servicio 27',19,'61-TRIAL-add_servicemodel 191');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (56,'295-TRIAL-Can change Servicio 242',19,'27-TRIAL-change_servicemodel 36');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (57,'291-TRIAL-Can delete Servicio 204',19,'2-TRIAL-delete_servicemodel 153');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (58,'292-TRIAL-Can add Comentario 82',20,'21-TRIAL-add_comment 116');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (59,'218-TRIAL-Can change Comentario 95',20,'47-TRIAL-change_comment 126');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (60,'71-TRIAL-Can delete Comentario 138',20,'69-TRIAL-delete_comment 112');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (61,'167-TRIAL-Can add Reservación 199',21,'235-TRIAL-add_bookroom 294');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (62,'203-TRIAL-Can change Reservación 111',21,'122-TRIAL-change_bookroom 33');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (63,'273-TRIAL-Can delete Reservación 164',21,'141-TRIAL-delete_bookroom 211');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (64,'53-TRIAL-Can add Código de reservación 268',22,'47-TRIAL-add_reservationkey 44');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (65,'262-TRIAL-Can change Código de reservación 57',22,'237-TRIAL-change_reservationkey 259');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (66,'23-TRIAL-Can delete Código de reservación 141',22,'229-TRIAL-delete_reservationkey 178');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (67,'16-TRIAL-Can add source 35',23,'290-TRIAL-add_source 42');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (68,'288-TRIAL-Can change source 106',23,'40-TRIAL-change_source 242');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (69,'64-TRIAL-Can delete source 148',23,'146-TRIAL-delete_source 105');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (70,'290-TRIAL-Can add thumbnail 129',24,'70-TRIAL-add_thumbnail 50');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (71,'6-TRIAL-Can change thumbnail 201',24,'93-TRIAL-change_thumbnail 248');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (72,'129-TRIAL-Can delete thumbnail 23',24,'84-TRIAL-delete_thumbnail 154');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (73,'156-TRIAL-Can add captcha store 140',25,'166-TRIAL-add_captchastore 176');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (74,'131-TRIAL-Can change captcha store 208',25,'144-TRIAL-change_captchastore 39');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (75,'26-TRIAL-Can delete captcha store 223',25,'137-TRIAL-delete_captchastore 238');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (76,'218-TRIAL-Can add visit 282',26,'129-TRIAL-add_visit 41');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (77,'33-TRIAL-Can change visit 215',26,'139-TRIAL-change_visit 258');
INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (78,'204-TRIAL-Can delete visit 30',26,'177-TRIAL-delete_visit 206');

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`,`username`,`first_name`,`last_name`,`email`,`password`,`is_staff`,`is_active`,`is_superuser`,`last_login`,`date_joined`) VALUES (1,'heysi','','','heysiweb@gmail.com','sha1$aa032$0451026436f211d835162905b09e087e1a140680','1','1','1','2014-10-17 11:22:13.304000','2014-10-17 11:22:13.304000');

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (1,'permission','auth','permission');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (2,'group','auth','group');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (3,'user','auth','user');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (4,'message','auth','message');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (5,'content type','contenttypes','contenttype');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (6,'session','sessions','session');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (7,'site','sites','site');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (8,'log entry','admin','logentry');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (9,'migration history','south','migrationhistory');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (10,'Objeto del banner','itemssite','bannerslider');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (11,'Post de inicio','itemssite','homepost');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (12,'Servicio HeySi','itemssite','homeservice');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (13,'Pregunta frecuente','itemssite','faq');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (14,'Provincia','servicespost','city');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (15,'Municipio','servicespost','zone');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (16,'Galería de fotos','servicespost','album');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (17,'Imágen','servicespost','image');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (18,'Tipo de servicio','servicespost','servicetype');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (19,'Servicio','servicespost','servicemodel');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (20,'Comentario','servicespost','comment');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (21,'Reservación','servicespost','bookroom');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (22,'Código de reservación','servicespost','reservationkey');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (23,'source','easy_thumbnails','source');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (24,'thumbnail','easy_thumbnails','thumbnail');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (25,'captcha store','captcha','captchastore');
INSERT INTO `django_content_type` (`id`,`name`,`app_label`,`model`) VALUES (26,'visit','visits','visit');

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`,`domain`,`name`) VALUES (1,'example.com','example.com');

--
-- Dumping data for table `south_migrationhistory`
--

INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (1,'itemssite','0001_initial','2014-10-17 18:32:37.081000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (2,'itemssite','0002_auto__chg_field_homepost_details','2014-10-17 18:32:37.640000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (3,'itemssite','0003_auto__chg_field_homepost_details','2014-10-17 18:32:38.160000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (4,'itemssite','0004_auto__chg_field_homepost_details','2014-10-17 18:32:38.830000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (5,'itemssite','0005_auto__chg_field_homepost_details','2014-10-17 18:32:39.446000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (6,'servicespost','0001_initial','2014-10-17 18:33:09.971000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (7,'servicespost','0002_auto__add_field_servicemodel_small_link','2014-10-17 18:33:11.512000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (8,'servicespost','0003_auto__chg_field_servicemodel_small_link__add_index_servicemodel_small_','2014-10-17 18:33:13.285000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (9,'servicespost','0004_auto__del_field_servicemodel_language','2014-10-17 18:33:15.065000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (10,'easy_thumbnails','0001_initial','2014-10-17 18:33:51.634000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (11,'easy_thumbnails','0002_filename_indexes','2014-10-17 18:33:52.182000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (12,'easy_thumbnails','0003_auto__add_storagenew','2014-10-17 18:33:52.784000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (13,'easy_thumbnails','0004_auto__add_field_source_storage_new__add_field_thumbnail_storage_new','2014-10-17 18:33:54.914000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (14,'easy_thumbnails','0005_storage_fks_null','2014-10-17 18:33:56.985000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (15,'easy_thumbnails','0006_copy_storage','2014-10-17 18:33:57.219000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (16,'easy_thumbnails','0007_storagenew_fks_not_null','2014-10-17 18:33:59.162000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (17,'easy_thumbnails','0008_auto__del_field_source_storage__del_field_thumbnail_storage','2014-10-17 18:34:00.640000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (18,'easy_thumbnails','0009_auto__del_storage','2014-10-17 18:34:00.913000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (19,'easy_thumbnails','0010_rename_storage','2014-10-17 18:34:02.497000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (20,'easy_thumbnails','0011_auto__add_field_source_storage_hash__add_field_thumbnail_storage_hash','2014-10-17 18:34:04.702000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (21,'easy_thumbnails','0012_build_storage_hashes','2014-10-17 18:34:04.884000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (22,'easy_thumbnails','0013_auto__del_storage__del_field_source_storage__del_field_thumbnail_stora','2014-10-17 18:34:06.833000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (23,'easy_thumbnails','0014_auto__add_unique_source_name_storage_hash__add_unique_thumbnail_name_s','2014-10-17 18:34:07.251000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (24,'easy_thumbnails','0015_auto__del_unique_thumbnail_name_storage_hash__add_unique_thumbnail_sou','2014-10-17 18:34:08.430000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (25,'django_wysiwyg','0001_initial','2014-10-17 18:35:16.783000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (26,'tinymce','0001_initial','2014-10-17 18:35:32.471000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (27,'captcha','0001_initial','2014-10-17 18:35:54.668000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (28,'visits','0001_initial','2014-10-17 18:36:11.332000');
INSERT INTO `south_migrationhistory` (`id`,`app_name`,`migration`,`applied`) VALUES (29,'visits','0002_auto__chg_field_visit_uri','2014-10-17 18:36:12.148000');
