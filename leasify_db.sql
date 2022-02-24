-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 24, 2022 at 06:44 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `leasify_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `admin_name` varchar(30) NOT NULL,
  `admin_email` varchar(254) NOT NULL,
  `admin_pass` varchar(20) NOT NULL,
  `otp` varchar(10) DEFAULT NULL,
  `otp_used` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_name`, `admin_email`, `admin_pass`, `otp`, `otp_used`) VALUES
(1, 'admin', 'arkanmansuri88@gmail.com', 'admin', '99044', 0);

-- --------------------------------------------------------

--
-- Table structure for table `area`
--

CREATE TABLE `area` (
  `a_id` int(11) NOT NULL,
  `a_name` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `area`
--

INSERT INTO `area` (`a_id`, `a_name`) VALUES
(1, 'Maninagar'),
(2, 'Ghatlodiya'),
(3, 'Naranpura'),
(4, 'Raipur'),
(5, 'Shashtrinagar'),
(7, 'Vasna'),
(8, 'Kankariya');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add customer', 7, 'add_customer'),
(26, 'Can change customer', 7, 'change_customer'),
(27, 'Can delete customer', 7, 'delete_customer'),
(28, 'Can view customer', 7, 'view_customer'),
(29, 'Can add owner', 8, 'add_owner'),
(30, 'Can change owner', 8, 'change_owner'),
(31, 'Can delete owner', 8, 'delete_owner'),
(32, 'Can view owner', 8, 'view_owner'),
(33, 'Can add area', 9, 'add_area'),
(34, 'Can change area', 9, 'change_area'),
(35, 'Can delete area', 9, 'delete_area'),
(36, 'Can view area', 9, 'view_area'),
(37, 'Can add house_details', 10, 'add_house_details'),
(38, 'Can change house_details', 10, 'change_house_details'),
(39, 'Can delete house_details', 10, 'delete_house_details'),
(40, 'Can view house_details', 10, 'view_house_details'),
(41, 'Can add house_gallery', 11, 'add_house_gallery'),
(42, 'Can change house_gallery', 11, 'change_house_gallery'),
(43, 'Can delete house_gallery', 11, 'delete_house_gallery'),
(44, 'Can view house_gallery', 11, 'view_house_gallery'),
(45, 'Can add pg_details', 12, 'add_pg_details'),
(46, 'Can change pg_details', 12, 'change_pg_details'),
(47, 'Can delete pg_details', 12, 'delete_pg_details'),
(48, 'Can view pg_details', 12, 'view_pg_details'),
(49, 'Can add pg_gallery', 13, 'add_pg_gallery'),
(50, 'Can change pg_gallery', 13, 'change_pg_gallery'),
(51, 'Can delete pg_gallery', 13, 'delete_pg_gallery'),
(52, 'Can view pg_gallery', 13, 'view_pg_gallery'),
(53, 'Can add tiffin_owner', 14, 'add_tiffin_owner'),
(54, 'Can change tiffin_owner', 14, 'change_tiffin_owner'),
(55, 'Can delete tiffin_owner', 14, 'delete_tiffin_owner'),
(56, 'Can view tiffin_owner', 14, 'view_tiffin_owner'),
(57, 'Can add tiffin_details', 15, 'add_tiffin_details'),
(58, 'Can change tiffin_details', 15, 'change_tiffin_details'),
(59, 'Can delete tiffin_details', 15, 'delete_tiffin_details'),
(60, 'Can view tiffin_details', 15, 'view_tiffin_details'),
(61, 'Can add status', 16, 'add_status'),
(62, 'Can change status', 16, 'change_status'),
(63, 'Can delete status', 16, 'delete_status'),
(64, 'Can view status', 16, 'view_status'),
(65, 'Can add notification', 17, 'add_notification'),
(66, 'Can change notification', 17, 'change_notification'),
(67, 'Can delete notification', 17, 'delete_notification'),
(68, 'Can view notification', 17, 'view_notification'),
(69, 'Can add feedback', 18, 'add_feedback'),
(70, 'Can change feedback', 18, 'change_feedback'),
(71, 'Can delete feedback', 18, 'delete_feedback'),
(72, 'Can view feedback', 18, 'view_feedback'),
(73, 'Can add admin', 19, 'add_admin'),
(74, 'Can change admin', 19, 'change_admin'),
(75, 'Can delete admin', 19, 'delete_admin'),
(76, 'Can view admin', 19, 'view_admin');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `c_id` int(11) NOT NULL,
  `c_name` varchar(30) NOT NULL,
  `c_email` varchar(254) NOT NULL,
  `c_phno` varchar(13) NOT NULL,
  `c_add` varchar(200) NOT NULL,
  `c_pass` varchar(20) NOT NULL,
  `otp` varchar(10) DEFAULT NULL,
  `otp_used` int(11) NOT NULL,
  `c_gender` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`c_id`, `c_name`, `c_email`, `c_phno`, `c_add`, `c_pass`, `otp`, `otp_used`, `c_gender`) VALUES
(1, 'Harsh', 'gfdfd', '13151', 'dsfdsfs', 'abc', NULL, 0, 'Male');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(19, 'leasify_admin', 'admin'),
(9, 'leasify_admin', 'area'),
(7, 'leasify_admin', 'customer'),
(18, 'leasify_admin', 'feedback'),
(10, 'leasify_admin', 'house_details'),
(11, 'leasify_admin', 'house_gallery'),
(17, 'leasify_admin', 'notification'),
(8, 'leasify_admin', 'owner'),
(12, 'leasify_admin', 'pg_details'),
(13, 'leasify_admin', 'pg_gallery'),
(16, 'leasify_admin', 'status'),
(15, 'leasify_admin', 'tiffin_details'),
(14, 'leasify_admin', 'tiffin_owner'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-12-16 13:46:30.054055'),
(2, 'auth', '0001_initial', '2021-12-16 13:46:30.739190'),
(3, 'admin', '0001_initial', '2021-12-16 13:46:30.965638'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-12-16 13:46:30.992134'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-12-16 13:46:31.021063'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-12-16 13:46:31.101651'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-12-16 13:46:31.171404'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-12-16 13:46:31.211659'),
(9, 'auth', '0004_alter_user_username_opts', '2021-12-16 13:46:31.229764'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-12-16 13:46:31.298313'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-12-16 13:46:31.303289'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-12-16 13:46:31.314571'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-12-16 13:46:31.337302'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-12-16 13:46:31.359186'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-12-16 13:46:31.399518'),
(16, 'auth', '0011_update_proxy_permissions', '2021-12-16 13:46:31.412477'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-12-16 13:46:31.437083'),
(18, 'leasify_admin', '0001_initial', '2021-12-16 13:46:31.496519'),
(19, 'leasify_admin', '0002_auto_20211205_1150', '2021-12-16 13:46:31.550219'),
(20, 'leasify_admin', '0003_owner', '2021-12-16 13:46:31.593937'),
(21, 'leasify_admin', '0004_auto_20211205_1812', '2021-12-16 13:46:31.698423'),
(22, 'leasify_admin', '0005_auto_20211205_1838', '2021-12-16 13:46:31.744041'),
(23, 'leasify_admin', '0006_alter_area_table', '2021-12-16 13:46:31.756677'),
(24, 'leasify_admin', '0007_house_details', '2021-12-16 13:46:31.898375'),
(25, 'leasify_admin', '0008_house_gallery', '2021-12-16 13:46:31.995179'),
(26, 'leasify_admin', '0009_pg_details', '2021-12-16 13:46:32.260217'),
(27, 'leasify_admin', '0010_auto_20211206_1121', '2021-12-16 13:46:32.330939'),
(28, 'leasify_admin', '0011_pg_gallery', '2021-12-16 13:46:32.453300'),
(29, 'leasify_admin', '0012_tiffin_owner', '2021-12-16 13:46:32.510593'),
(30, 'leasify_admin', '0013_tiffin_details', '2021-12-16 13:46:32.632974'),
(31, 'leasify_admin', '0014_status', '2021-12-16 13:46:33.028214'),
(32, 'leasify_admin', '0015_feedback_notification', '2021-12-16 13:46:33.545071'),
(33, 'leasify_admin', '0016_auto_20211216_1914', '2021-12-16 13:46:33.655185'),
(34, 'leasify_admin', '0017_alter_admin_table', '2021-12-16 13:46:33.673189'),
(35, 'sessions', '0001_initial', '2021-12-16 13:46:33.736858');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2n5vuwjvcgthuecbe0lq9lhh2hz1pr1s', 'eyJ0ZW1haWwiOiJhcmthbm1hbnN1cmk4OEBnbWFpbC5jb20ifQ:1n1MBp:sGMiBWxJ9nh7jgknKEgmBZ1hjjafcrtLkFOX2jaCwRM', '2022-01-09 05:35:25.733743');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `feed_id` int(11) NOT NULL,
  `feed_date` date NOT NULL,
  `feed_desc` varchar(300) NOT NULL,
  `c_id_id` int(11) NOT NULL,
  `h_id_id` int(11) NOT NULL,
  `pg_id_id` int(11) NOT NULL,
  `tiff_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `house_details`
--

CREATE TABLE `house_details` (
  `h_id` int(11) NOT NULL,
  `h_add` varchar(200) NOT NULL,
  `h_imgpath` varchar(200) NOT NULL,
  `h_name` varchar(100) NOT NULL,
  `h_rent` int(11) NOT NULL,
  `h_desc` varchar(300) NOT NULL,
  `h_type` varchar(100) NOT NULL,
  `h_parking` varchar(10) NOT NULL,
  `h_lift` varchar(100) NOT NULL,
  `a_id_id` int(11) NOT NULL,
  `o_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `house_details`
--

INSERT INTO `house_details` (`h_id`, `h_add`, `h_imgpath`, `h_name`, `h_rent`, `h_desc`, `h_type`, `h_parking`, `h_lift`, `a_id_id`, `o_id_id`) VALUES
(1, 'Demo addressssss', 'house1.jpeg', 'Hari Om house', 1000, 'Demo Description', '1bhk', 'Yes', 'Yes', 1, 1),
(2, 'Demo address 1', 'house3.jpg', 'ABC1', 100, 'sadasds', '2bhk', 'Yes', 'Yes', 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `house_gallery`
--

CREATE TABLE `house_gallery` (
  `gallery_id` int(11) NOT NULL,
  `hg_imgpath` varchar(200) NOT NULL,
  `h_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `house_gallery`
--

INSERT INTO `house_gallery` (`gallery_id`, `hg_imgpath`, `h_id_id`) VALUES
(1, 'house1.jpeg', 1),
(2, 'house3.jpg', 2);

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `noti_id` int(11) NOT NULL,
  `noti_desc` varchar(300) NOT NULL,
  `noti_date` date NOT NULL,
  `st_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `owner`
--

CREATE TABLE `owner` (
  `o_id` int(11) NOT NULL,
  `o_type` varchar(30) NOT NULL,
  `o_name` varchar(30) NOT NULL,
  `o_email` varchar(254) NOT NULL,
  `o_phno` varchar(13) NOT NULL,
  `o_add` varchar(200) NOT NULL,
  `o_pass` varchar(20) NOT NULL,
  `otp` varchar(10) DEFAULT NULL,
  `otp_used` int(11) NOT NULL,
  `o_gender` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `owner`
--

INSERT INTO `owner` (`o_id`, `o_type`, `o_name`, `o_email`, `o_phno`, `o_add`, `o_pass`, `otp`, `otp_used`, `o_gender`) VALUES
(1, 'PG Owner', 'Harshh', 'harshtanna404@gmail.com', '12345678', 'Ahemdabad', 'harsh123', NULL, 0, 'Male'),
(2, 'PG Owner', 'Uttam', 'uttammanani@gmail.com', '12345678', 'Ahemdabad', 'uttam123', NULL, 0, 'Male'),
(3, 'House Owner', 'Visha', 'vishatailor14082001@gmail.com', '12345678', 'Ahemdabad', 'visha123', NULL, 0, 'Female'),
(4, 'House Owner', 'prapti', 'harsh123@gmail.com', '464', '4646', '654', NULL, 0, 'Female'),
(5, 'PG Owner', 'abc', 'harsh1234@gmail.com', '12345678', 'Ahemdabad', 'fsefe', NULL, 0, 'Female'),
(6, 'House Owner', 'Uttam', 'harsh12333@gmail.com', '65654', 'gfh', 'fsefe', NULL, 0, 'Male');

-- --------------------------------------------------------

--
-- Table structure for table `pg_details`
--

CREATE TABLE `pg_details` (
  `pg_id` int(11) NOT NULL,
  `pg_add` varchar(200) NOT NULL,
  `pg_imgpath` varchar(200) NOT NULL,
  `pg_name` varchar(100) NOT NULL,
  `pg_rent` int(11) NOT NULL,
  `pg_desc` varchar(300) NOT NULL,
  `pg_beds` int(11) NOT NULL,
  `pg_for` varchar(10) NOT NULL,
  `pg_food` varchar(10) NOT NULL,
  `pg_wifi` varchar(10) NOT NULL,
  `pg_tv` varchar(10) NOT NULL,
  `a_id_id` int(11) NOT NULL,
  `o_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pg_details`
--

INSERT INTO `pg_details` (`pg_id`, `pg_add`, `pg_imgpath`, `pg_name`, `pg_rent`, `pg_desc`, `pg_beds`, `pg_for`, `pg_food`, `pg_wifi`, `pg_tv`, `a_id_id`, `o_id_id`) VALUES
(1, 'Demo Addresss', 'pg1.jpg', 'Sai Ram PG', 1000, 'Demo Description', 1, 'Boys', 'Yes', 'Yes', 'Yes', 1, 1),
(2, 'Abcxyz', 'pg3.jpg', 'ABC PG', 444, 'ddddd', 3, 'Girls', 'Yes', 'Yes', 'Yes', 2, 5);

-- --------------------------------------------------------

--
-- Table structure for table `pg_gallery`
--

CREATE TABLE `pg_gallery` (
  `pg_gallery_id` int(11) NOT NULL,
  `pgg_imgpath` varchar(200) NOT NULL,
  `pg_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pg_gallery`
--

INSERT INTO `pg_gallery` (`pg_gallery_id`, `pgg_imgpath`, `pg_id_id`) VALUES
(1, 'pg1.jpg', 1),
(2, 'pg2.jpg', 2),
(3, 'pg3.jpg', 2);

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `st_id` int(11) NOT NULL,
  `st_desc` varchar(50) NOT NULL,
  `h_id_id` int(11) NOT NULL,
  `o_id_id` int(11) NOT NULL,
  `pg_id_id` int(11) NOT NULL,
  `tiff_id_id` int(11) NOT NULL,
  `to_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tiffin_owner`
--

CREATE TABLE `tiffin_owner` (
  `to_id` int(11) NOT NULL,
  `to_name` varchar(30) NOT NULL,
  `to_email` varchar(254) NOT NULL,
  `to_phno` varchar(13) NOT NULL,
  `to_add` varchar(200) NOT NULL,
  `to_pass` varchar(20) NOT NULL,
  `otp` varchar(10) DEFAULT NULL,
  `otp_used` int(11) NOT NULL,
  `to_gender` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tiffin_owner`
--

INSERT INTO `tiffin_owner` (`to_id`, `to_name`, `to_email`, `to_phno`, `to_add`, `to_pass`, `otp`, `otp_used`, `to_gender`) VALUES
(1, 'Harshh', 'harshtanna404@gmail.com', '12345678', 'Demo Address', 'harsh123', NULL, 0, 'Male'),
(2, 'Uttam', 'uttammaani@gmail.com', '12345678', 'Demo Address', 'uttam123', NULL, 0, 'Male'),
(3, 'Harsh', 'harsh12@gmail.com', '4562', 'hjb', 'harsh123', NULL, 0, 'Male');

-- --------------------------------------------------------

--
-- Table structure for table `tiffn_details`
--

CREATE TABLE `tiffn_details` (
  `tiff_id` int(11) NOT NULL,
  `tiff_title` varchar(100) NOT NULL,
  `tiff_type` varchar(30) NOT NULL,
  `tiff_desc` varchar(300) NOT NULL,
  `tiff_imgpath` varchar(200) NOT NULL,
  `tiff_price` int(11) NOT NULL,
  `to_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tiffn_details`
--

INSERT INTO `tiffn_details` (`tiff_id`, `tiff_title`, `tiff_type`, `tiff_desc`, `tiff_imgpath`, `tiff_price`, `to_id_id`) VALUES
(1, 'small Vegg', 'Lunch', 'Demo Description', 'tiff1.jpg', 100, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`),
  ADD UNIQUE KEY `admin_email` (`admin_email`);

--
-- Indexes for table `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`a_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`c_id`),
  ADD UNIQUE KEY `c_email` (`c_email`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feed_id`),
  ADD KEY `Feedback_c_id_id_2ff2003b_fk_customer_c_id` (`c_id_id`),
  ADD KEY `Feedback_h_id_id_d0545452_fk_House_Details_h_id` (`h_id_id`),
  ADD KEY `Feedback_pg_id_id_da1b5457_fk_PG_details_pg_id` (`pg_id_id`),
  ADD KEY `Feedback_tiff_id_id_5d10770d_fk_Tiffn_Details_tiff_id` (`tiff_id_id`);

--
-- Indexes for table `house_details`
--
ALTER TABLE `house_details`
  ADD PRIMARY KEY (`h_id`),
  ADD KEY `House Details_a_id_id_6a233e02_fk_Area_a_id` (`a_id_id`),
  ADD KEY `House Details_o_id_id_55b23841_fk_owner_o_id` (`o_id_id`);

--
-- Indexes for table `house_gallery`
--
ALTER TABLE `house_gallery`
  ADD PRIMARY KEY (`gallery_id`),
  ADD KEY `House Gallery_h_id_id_e8e7106d_fk_House Details_h_id` (`h_id_id`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`noti_id`),
  ADD KEY `Notification_st_id_id_2c408a00_fk_Status_st_id` (`st_id_id`);

--
-- Indexes for table `owner`
--
ALTER TABLE `owner`
  ADD PRIMARY KEY (`o_id`),
  ADD UNIQUE KEY `o_email` (`o_email`);

--
-- Indexes for table `pg_details`
--
ALTER TABLE `pg_details`
  ADD PRIMARY KEY (`pg_id`),
  ADD KEY `leasify_admin_pg_details_a_id_id_698d782e_fk_Area_a_id` (`a_id_id`),
  ADD KEY `leasify_admin_pg_details_o_id_id_f3dd8def_fk_owner_o_id` (`o_id_id`);

--
-- Indexes for table `pg_gallery`
--
ALTER TABLE `pg_gallery`
  ADD PRIMARY KEY (`pg_gallery_id`),
  ADD KEY `PG_Gallery_pg_id_id_49c6aa4c_fk_PG_details_pg_id` (`pg_id_id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`st_id`),
  ADD KEY `Status_h_id_id_b9269512_fk_House_Details_h_id` (`h_id_id`),
  ADD KEY `Status_o_id_id_e8fc9439_fk_owner_o_id` (`o_id_id`),
  ADD KEY `Status_pg_id_id_53fda0e3_fk_PG_details_pg_id` (`pg_id_id`),
  ADD KEY `Status_tiff_id_id_78c2db70_fk_Tiffn_Details_tiff_id` (`tiff_id_id`),
  ADD KEY `Status_to_id_id_158a0a17_fk_Tiffin_Owner_to_id` (`to_id_id`);

--
-- Indexes for table `tiffin_owner`
--
ALTER TABLE `tiffin_owner`
  ADD PRIMARY KEY (`to_id`),
  ADD UNIQUE KEY `to_email` (`to_email`);

--
-- Indexes for table `tiffn_details`
--
ALTER TABLE `tiffn_details`
  ADD PRIMARY KEY (`tiff_id`),
  ADD KEY `Tiffn_Details_to_id_id_8c7f8168_fk_Tiffin_Owner_to_id` (`to_id_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `area`
--
ALTER TABLE `area`
  MODIFY `a_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `c_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feed_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `house_details`
--
ALTER TABLE `house_details`
  MODIFY `h_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `house_gallery`
--
ALTER TABLE `house_gallery`
  MODIFY `gallery_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `noti_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `owner`
--
ALTER TABLE `owner`
  MODIFY `o_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `pg_details`
--
ALTER TABLE `pg_details`
  MODIFY `pg_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `pg_gallery`
--
ALTER TABLE `pg_gallery`
  MODIFY `pg_gallery_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `status`
--
ALTER TABLE `status`
  MODIFY `st_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tiffin_owner`
--
ALTER TABLE `tiffin_owner`
  MODIFY `to_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tiffn_details`
--
ALTER TABLE `tiffn_details`
  MODIFY `tiff_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `Feedback_c_id_id_2ff2003b_fk_customer_c_id` FOREIGN KEY (`c_id_id`) REFERENCES `customer` (`c_id`),
  ADD CONSTRAINT `Feedback_h_id_id_d0545452_fk_House_Details_h_id` FOREIGN KEY (`h_id_id`) REFERENCES `house_details` (`h_id`),
  ADD CONSTRAINT `Feedback_pg_id_id_da1b5457_fk_PG_details_pg_id` FOREIGN KEY (`pg_id_id`) REFERENCES `pg_details` (`pg_id`),
  ADD CONSTRAINT `Feedback_tiff_id_id_5d10770d_fk_Tiffn_Details_tiff_id` FOREIGN KEY (`tiff_id_id`) REFERENCES `tiffn_details` (`tiff_id`);

--
-- Constraints for table `house_details`
--
ALTER TABLE `house_details`
  ADD CONSTRAINT `House Details_a_id_id_6a233e02_fk_Area_a_id` FOREIGN KEY (`a_id_id`) REFERENCES `area` (`a_id`),
  ADD CONSTRAINT `House Details_o_id_id_55b23841_fk_owner_o_id` FOREIGN KEY (`o_id_id`) REFERENCES `owner` (`o_id`);

--
-- Constraints for table `house_gallery`
--
ALTER TABLE `house_gallery`
  ADD CONSTRAINT `House Gallery_h_id_id_e8e7106d_fk_House Details_h_id` FOREIGN KEY (`h_id_id`) REFERENCES `house_details` (`h_id`);

--
-- Constraints for table `notification`
--
ALTER TABLE `notification`
  ADD CONSTRAINT `Notification_st_id_id_2c408a00_fk_Status_st_id` FOREIGN KEY (`st_id_id`) REFERENCES `status` (`st_id`);

--
-- Constraints for table `pg_details`
--
ALTER TABLE `pg_details`
  ADD CONSTRAINT `leasify_admin_pg_details_a_id_id_698d782e_fk_Area_a_id` FOREIGN KEY (`a_id_id`) REFERENCES `area` (`a_id`),
  ADD CONSTRAINT `leasify_admin_pg_details_o_id_id_f3dd8def_fk_owner_o_id` FOREIGN KEY (`o_id_id`) REFERENCES `owner` (`o_id`);

--
-- Constraints for table `pg_gallery`
--
ALTER TABLE `pg_gallery`
  ADD CONSTRAINT `PG_Gallery_pg_id_id_49c6aa4c_fk_PG_details_pg_id` FOREIGN KEY (`pg_id_id`) REFERENCES `pg_details` (`pg_id`);

--
-- Constraints for table `status`
--
ALTER TABLE `status`
  ADD CONSTRAINT `Status_h_id_id_b9269512_fk_House_Details_h_id` FOREIGN KEY (`h_id_id`) REFERENCES `house_details` (`h_id`),
  ADD CONSTRAINT `Status_o_id_id_e8fc9439_fk_owner_o_id` FOREIGN KEY (`o_id_id`) REFERENCES `owner` (`o_id`),
  ADD CONSTRAINT `Status_pg_id_id_53fda0e3_fk_PG_details_pg_id` FOREIGN KEY (`pg_id_id`) REFERENCES `pg_details` (`pg_id`),
  ADD CONSTRAINT `Status_tiff_id_id_78c2db70_fk_Tiffn_Details_tiff_id` FOREIGN KEY (`tiff_id_id`) REFERENCES `tiffn_details` (`tiff_id`),
  ADD CONSTRAINT `Status_to_id_id_158a0a17_fk_Tiffin_Owner_to_id` FOREIGN KEY (`to_id_id`) REFERENCES `tiffin_owner` (`to_id`);

--
-- Constraints for table `tiffn_details`
--
ALTER TABLE `tiffn_details`
  ADD CONSTRAINT `Tiffn_Details_to_id_id_8c7f8168_fk_Tiffin_Owner_to_id` FOREIGN KEY (`to_id_id`) REFERENCES `tiffin_owner` (`to_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
