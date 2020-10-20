/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : 127.0.0.1:3306
 Source Schema         : awesome

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 20/10/2020 18:06:20
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for blogs
-- ----------------------------
DROP TABLE IF EXISTS `blogs`;
CREATE TABLE `blogs` (
  `id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_image` varchar(500) NOT NULL,
  `name` varchar(50) NOT NULL,
  `summary` varchar(200) NOT NULL,
  `content` mediumtext NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blogs
-- ----------------------------
BEGIN;
INSERT INTO `blogs` VALUES ('00160274704468526932a144ea440dfb094b2b152189f40000', '0016027430757796e60ea4fd2c14dd4a36cf89ad9bf64db000', 'zhangsan', 'http://www.gravatar.com/avatar/bf2c904672ef0c7e86a0c7482af210e6?d=mm&s=120', '第1篇日志', '这是一个测试', '继续测试', 1602747044.68563);
INSERT INTO `blogs` VALUES ('00160274709779536173532b7b64b93ba9a428579be393e000', '0016027430757796e60ea4fd2c14dd4a36cf89ad9bf64db000', 'zhangsan', 'http://www.gravatar.com/avatar/bf2c904672ef0c7e86a0c7482af210e6?d=mm&s=120', '第2篇日志', '我继续测试', '我继续测试', 1602747097.79544);
INSERT INTO `blogs` VALUES ('001602747294623373955c99f79439f90c7204807d8ccb9000', '0016027430757796e60ea4fd2c14dd4a36cf89ad9bf64db000', 'zhangsan', 'http://www.gravatar.com/avatar/bf2c904672ef0c7e86a0c7482af210e6?d=mm&s=120', '第3篇日志', '这是第三篇日志', '这是第三篇日志', 1602747294.62384);
COMMIT;

-- ----------------------------
-- Table structure for comments
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
  `id` varchar(50) NOT NULL,
  `blog_id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_image` varchar(500) NOT NULL,
  `content` mediumtext NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comments
-- ----------------------------
BEGIN;
INSERT INTO `comments` VALUES ('00160274510952699836ce5327b4137b78c357ccced1649000', '1', '0016027430757796e60ea4fd2c14dd4a36cf89ad9bf64db000', 'zhangsan', 'http://www.gravatar.com/avatar/bf2c904672ef0c7e86a0c7482af210e6?d=mm&s=120', '13121', 1602745109.52605);
COMMIT;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `name` varchar(50) NOT NULL,
  `image` varchar(500) NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_email` (`email`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
BEGIN;
INSERT INTO `users` VALUES ('0016027430757796e60ea4fd2c14dd4a36cf89ad9bf64db000', 'zhangsan@163.com', '9e8a10b05f5d89924475425a7422b564fec456f7', 1, 'zhangsan', 'http://www.gravatar.com/avatar/bf2c904672ef0c7e86a0c7482af210e6?d=mm&s=120', 1602743075.7803);
INSERT INTO `users` VALUES ('001602746232496285b716c5c844504b834df3c9e62d3be000', 'lisi@163.com', '4bd23044d0cb60cf0d086c2c010401c75a87804b', 0, 'lisi', 'http://www.gravatar.com/avatar/1354ced4c4c59f5621929a15a20b5039?d=mm&s=120', 1602746232.49664);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
