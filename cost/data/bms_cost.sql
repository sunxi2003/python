/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : 127.0.0.1:3306
 Source Schema         : bms_cost

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 15/07/2020 14:23:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for set_category_time
-- ----------------------------
DROP TABLE IF EXISTS `set_category_time`;
CREATE TABLE `set_category_time` (
  `id` int NOT NULL AUTO_INCREMENT,
  `month` int NOT NULL,
  `warehouse_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `warehouse_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `category_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `category_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `task_time` decimal(10,5) NOT NULL,
  `unit` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `cre_time` datetime NOT NULL,
  `cre_user` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of set_category_time
-- ----------------------------
BEGIN;
INSERT INTO `set_category_time` VALUES (1, 5, 'B03', '广州01仓', '1007\r\n1007', '鸡肉', 10.00000, '秒', '2020-07-07 15:53:33', '孙喜');
INSERT INTO `set_category_time` VALUES (2, 5, 'B36', '上海02仓', '1007', '鸡肉', 10.00000, '秒', '2020-07-07 15:56:02', '孙喜');
INSERT INTO `set_category_time` VALUES (3, 5, 'B01', '北京01仓', '1007', '鸡肉', 10.00000, '秒', '2020-07-07 16:40:14', '孙喜');
COMMIT;

-- ----------------------------
-- Table structure for set_material_price
-- ----------------------------
DROP TABLE IF EXISTS `set_material_price`;
CREATE TABLE `set_material_price` (
  `id` int NOT NULL AUTO_INCREMENT,
  `month` int NOT NULL,
  `warehouse_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `warehouse_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `material_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `material_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `price` decimal(10,5) NOT NULL,
  `cre_time` datetime NOT NULL,
  `cre_user` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of set_material_price
-- ----------------------------
BEGIN;
INSERT INTO `set_material_price` VALUES (1, 5, 'B36', '上海02仓', 'JY-BD-250', '九曳250g0°冰袋', 0.26000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (2, 5, 'B36', '上海02仓', 'JY-BQLHBWD02', '冰淇淋保温袋345*220*350', 1.02574, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (3, 5, 'B36', '上海02仓', 'JY-BQLHBWD03', '冰淇淋保温袋380*275*375', 1.50000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (4, 5, 'B36', '上海02仓', 'JY-BWD35*40', '保温袋35*40', 0.53000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (5, 5, 'B36', '上海02仓', 'JY-BWD40*50-H', '保温袋40*50-H', 0.73000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (6, 5, 'B36', '上海02仓', 'JY-DFSD', '大防水袋', 0.73000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (7, 5, 'B36', '上海02仓', 'JY-JD', '胶带', 3.35000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (8, 5, 'B36', '上海02仓', 'JY-PMX01', '九曳1号泡沫箱', 2.19974, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (9, 5, 'B36', '上海02仓', 'JY-PMX02', '九曳2号泡沫箱', 2.98000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (10, 5, 'B36', '上海02仓', 'JY-PMX03', '九曳3号泡沫箱', 3.38000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (11, 5, 'B36', '上海02仓', 'JY-PMX04', '九曳4号泡沫箱', 4.85000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (12, 5, 'B36', '上海02仓', 'JY-PXM05', '九曳5号泡沫箱', 4.99000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (13, 5, 'B36', '上海02仓', 'JY-XFSD', '小防水袋', 0.51000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (14, 5, 'B36', '上海02仓', 'SF-FSD', '顺丰防水袋', 0.00000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (15, 5, 'B01', '北京01仓', 'JY-BD-250', '九曳250g0°冰袋', 0.23000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (16, 5, 'B01', '北京01仓', 'JY-BQLHBWD02', '冰淇淋保温袋345*220*350', 1.06619, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (17, 5, 'B01', '北京01仓', 'JY-BQLHBWD03', '冰淇淋保温袋380*275*375', 1.70000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (18, 5, 'B01', '北京01仓', 'JY-BWD35*40', '保温袋35*40', 0.65000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (19, 5, 'B01', '北京01仓', 'JY-BWD40*50-H', '保温袋40*50-H', 0.64000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (20, 5, 'B01', '北京01仓', 'JY-DFSD', '大防水袋', 0.73000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (21, 5, 'B01', '北京01仓', 'JY-JD', '胶带', 3.35000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (22, 5, 'B01', '北京01仓', 'JY-PMX01', '九曳1号泡沫箱', 2.07000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (23, 5, 'B01', '北京01仓', 'JY-PMX02', '九曳2号泡沫箱', 2.75000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (24, 5, 'B01', '北京01仓', 'JY-PMX03', '九曳3号泡沫箱', 3.12000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (25, 5, 'B01', '北京01仓', 'JY-PMX04', '九曳4号泡沫箱', 4.50000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (26, 5, 'B01', '北京01仓', 'JY-PXM05', '九曳5号泡沫箱', 5.25000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (27, 5, 'B01', '北京01仓', 'JY-XFSD', '小防水袋', 0.58000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (28, 5, 'B01', '北京01仓', 'SF-FSD', '顺丰防水袋', 0.00000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (29, 5, 'B03', '广州01仓', 'GZ-PMX-004', '奶茶泡沫箱', 7.30000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (30, 5, 'B03', '广州01仓', 'JY-BD-250', '九曳250g0°冰袋', 0.23000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (31, 5, 'B03', '广州01仓', 'JY-BQLHBWD02', '冰淇淋保温袋345*220*350', 1.13050, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (32, 5, 'B03', '广州01仓', 'JY-BQLHBWD03', '冰淇淋保温袋380*275*375', 1.15000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (33, 5, 'B03', '广州01仓', 'JY-BWD35*40', '保温袋35*40', 0.63000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (34, 5, 'B03', '广州01仓', 'JY-BWD40*50-H', '保温袋40*50-H', 1.18000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (35, 5, 'B03', '广州01仓', 'JY-DFSD', '大防水袋', 0.73000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (36, 5, 'B03', '广州01仓', 'JY-JD', '胶带', 3.35000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (37, 5, 'B03', '广州01仓', 'JY-PMX01', '九曳1号泡沫箱', 2.50000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (38, 5, 'B03', '广州01仓', 'JY-PMX02', '九曳2号泡沫箱', 2.64564, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (39, 5, 'B03', '广州01仓', 'JY-PMX03', '九曳3号泡沫箱', 4.54448, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (40, 5, 'B03', '广州01仓', 'JY-PMX04', '九曳4号泡沫箱', 6.08840, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (41, 5, 'B03', '广州01仓', 'JY-PXM05', '九曳5号泡沫箱', 7.30000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (42, 5, 'B03', '广州01仓', 'JY-XFSD', '小防水袋', 0.51000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (43, 5, 'B03', '广州01仓', 'SF-FSD', '顺丰防水袋', 0.00000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (44, 5, 'B04', '成都仓', 'JY-BD-250', '九曳250g0°冰袋', 0.23000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (45, 5, 'B04', '成都仓', 'JY-BQLHBWD02', '冰淇淋保温袋345*220*350', 1.29429, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (46, 5, 'B04', '成都仓', 'JY-BQLHBWD03', '冰淇淋保温袋380*275*375', 1.15000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (47, 5, 'B04', '成都仓', 'JY-BWD35*40', '保温袋35*40', 0.48000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (48, 5, 'B04', '成都仓', 'JY-BWD40*50-H', '保温袋40*50-H', 0.64000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (49, 5, 'B04', '成都仓', 'JY-DFSD', '大防水袋', 0.74000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (50, 5, 'B04', '成都仓', 'JY-JD', '胶带', 3.35000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (51, 5, 'B04', '成都仓', 'JY-PMX01', '九曳1号泡沫箱', 2.70000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (52, 5, 'B04', '成都仓', 'JY-PMX02', '九曳2号泡沫箱', 3.50000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (53, 5, 'B04', '成都仓', 'JY-PMX03', '九曳3号泡沫箱', 4.00000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (54, 5, 'B04', '成都仓', 'JY-PMX04', '九曳4号泡沫箱', 5.80000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (55, 5, 'B04', '成都仓', 'JY-PXM05', '九曳5号泡沫箱', 5.80000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (56, 5, 'B04', '成都仓', 'JY-XFSD', '小防水袋', 0.41500, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (57, 5, 'B04', '成都仓', 'SF-FSD', '顺丰防水袋', 0.00000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (58, 5, 'B05', '武汉仓', 'JY-BD-250', '九曳250g0°冰袋', 0.23000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (59, 5, 'B05', '武汉仓', 'JY-BQLHBWD02', '冰淇淋保温袋345*220*350', 1.07650, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (60, 5, 'B05', '武汉仓', 'JY-BQLHBWD03', '冰淇淋保温袋380*275*375', 1.15000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (61, 5, 'B05', '武汉仓', 'JY-BWD35*40', '保温袋35*40', 0.51957, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (62, 5, 'B05', '武汉仓', 'JY-BWD40*50-H', '保温袋40*50-H', 0.68462, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (63, 5, 'B05', '武汉仓', 'JY-DFSD', '大防水袋', 0.66000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (64, 5, 'B05', '武汉仓', 'JY-JD', '胶带', 3.35000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (65, 5, 'B05', '武汉仓', 'JY-PMX01', '九曳1号泡沫箱', 2.52000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (66, 5, 'B05', '武汉仓', 'JY-PMX02', '九曳2号泡沫箱', 3.35000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (67, 5, 'B05', '武汉仓', 'JY-PMX03', '九曳3号泡沫箱', 3.80000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (68, 5, 'B05', '武汉仓', 'JY-PMX04', '九曳4号泡沫箱', 5.47000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (69, 5, 'B05', '武汉仓', 'JY-PXM05', '九曳5号泡沫箱', 5.63000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (70, 5, 'B05', '武汉仓', 'JY-RMMD-H', '九曳热敏面单（合成纸）', 0.09500, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (71, 5, 'B05', '武汉仓', 'JY-XFSD', '小防水袋', 0.58000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (72, 5, 'B05', '武汉仓', 'SF-FSD', '顺丰防水袋', 0.00000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (73, 5, 'B08', '沈阳仓', 'JY-BD-250', '九曳250g0°冰袋', 0.28000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (74, 5, 'B08', '沈阳仓', 'JY-BQLHBWD02', '冰淇淋保温袋345*220*350', 1.09250, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (75, 5, 'B08', '沈阳仓', 'JY-BQLHBWD03', '冰淇淋保温袋380*275*375', 1.50000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (76, 5, 'B08', '沈阳仓', 'JY-BWD35*40', '保温袋35*40', 0.79000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (77, 5, 'B08', '沈阳仓', 'JY-BWD40*50-H', '保温袋40*50-H', 1.18000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (78, 5, 'B08', '沈阳仓', 'JY-DFSD', '大防水袋', 0.73000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (79, 5, 'B08', '沈阳仓', 'JY-JD', '胶带', 3.35000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (80, 5, 'B08', '沈阳仓', 'JY-PMX01', '九曳1号泡沫箱', 2.66000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (81, 5, 'B08', '沈阳仓', 'JY-PMX02', '九曳2号泡沫箱', 3.48059, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (82, 5, 'B08', '沈阳仓', 'JY-PMX03', '九曳3号泡沫箱', 4.36000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (83, 5, 'B08', '沈阳仓', 'JY-PMX04', '九曳4号泡沫箱', 5.65319, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (84, 5, 'B08', '沈阳仓', 'JY-PXM05', '九曳5号泡沫箱', 5.83000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (85, 5, 'B08', '沈阳仓', 'JY-XFSD', '小防水袋', 0.51000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (86, 5, 'B08', '沈阳仓', 'SF-FSD', '顺丰防水袋', 0.00000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (87, 5, 'B31', '福州仓', 'JY-BD-250', '九曳250g0°冰袋', 0.30000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (88, 5, 'B31', '福州仓', 'JY-BQLHBWD02', '冰淇淋保温袋345*220*350', 1.03077, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (89, 5, 'B31', '福州仓', 'JY-BQLHBWD03', '冰淇淋保温袋380*275*375', 1.50000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (90, 5, 'B31', '福州仓', 'JY-BWD35*40', '保温袋35*40', 0.53667, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (91, 5, 'B31', '福州仓', 'JY-BWD40*50-H', '保温袋40*50-H', 0.64000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (92, 5, 'B31', '福州仓', 'JY-JD', '胶带', 3.35000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (93, 5, 'B31', '福州仓', 'JY-PMX01', '九曳1号泡沫箱', 2.68800, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (94, 5, 'B31', '福州仓', 'JY-PMX02', '九曳2号泡沫箱', 3.12900, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (95, 5, 'B31', '福州仓', 'JY-PMX03', '九曳3号泡沫箱', 3.61200, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (96, 5, 'B31', '福州仓', 'JY-PMX04', '九曳4号泡沫箱', 5.10300, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (97, 5, 'B31', '福州仓', 'JY-PXM05', '九曳5号泡沫箱', 5.20000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (98, 5, 'B31', '福州仓', 'SF-FSD', '顺丰防水袋', 0.00000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (99, 5, 'B03', '广州01仓', 'JY-HLQ', '葫芦球', 0.27000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (100, 5, 'B03', '广州01仓', 'JY-GB', '九曳干冰', 2.60000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (101, 5, 'B36', '上海02仓', 'JY-HLQ', '葫芦球', 0.32500, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (102, 5, 'B36', '上海02仓', 'JY-GB', '九曳干冰', 2.50000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (103, 5, 'B27', '济南仓', 'JY-PMX02', '九曳2号泡沫箱', 2.92000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (104, 5, 'B27', '济南仓', 'JY-HLQ', '葫芦球', 0.32500, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (105, 5, 'B27', '济南仓', 'JY-BD-250', '九曳250g0°冰袋', 0.23000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (106, 5, 'B27', '济南仓', 'JY-GB', '九曳干冰', 3.40000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (107, 5, 'B27', '济南仓', 'JY-PMX04', '九曳4号泡沫箱', 4.96738, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (108, 5, 'B08', '沈阳仓', 'JY-HLQ', '葫芦球', 0.22000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (109, 5, 'B08', '沈阳仓', 'JY-GB', '九曳干冰', 4.00000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (110, 5, 'B04', '成都仓', 'JY-HLQ', '葫芦球', 0.13500, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (111, 5, 'B04', '成都仓', 'JY-GB', '九曳干冰', 3.90000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (112, 5, 'B31', '福州仓', 'JY-HLQ', '葫芦球', 0.22000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (113, 5, 'B31', '福州仓', 'JY-GB', '九曳干冰', 4.00000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (114, 5, 'B11', '西安仓', 'JY-PMX04', '九曳4号泡沫箱', 6.30000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (115, 5, 'B11', '西安仓', 'JY-HLQ', '葫芦球', 0.27000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (116, 5, 'B11', '西安仓', 'JY-BD-250', '九曳250g0°冰袋', 0.30000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (117, 5, 'B11', '西安仓', 'JY-GB', '九曳干冰', 6.00000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (118, 5, 'B11', '西安仓', 'JY-PMX02', '九曳2号泡沫箱', 3.87000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (119, 5, 'B27', '济南仓', 'JY-PMX03', '九曳3号泡沫箱', 3.67714, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (120, 5, 'B35', '北京03仓', '81000000418', '九曳4#泡沫箱', 3.86000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (121, 5, 'B35', '北京03仓', 'JY-HLQ', '葫芦球', 0.23450, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (122, 5, 'B35', '北京03仓', 'JY-BD-250', '九曳250g0°冰袋', 0.23000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (123, 5, 'B35', '北京03仓', 'JY-GB', '九曳干冰', 2.60000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (124, 5, 'B35', '北京03仓', 'JY-PMX03', '九曳3号泡沫箱', 2.69000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (125, 5, 'B27', '济南仓', 'JY-PMX01', '九曳1号泡沫箱', 2.50252, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (126, 5, 'B35', '北京03仓', 'JY-PMX02', '九曳2号泡沫箱', 2.37000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (127, 5, 'B11', '西安仓', 'JY-PMX03', '九曳3号泡沫箱', 4.60000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (128, 5, 'B11', '西安仓', 'JY-JD', '胶带', 3.35000, '2020-07-08 00:00:00', '陈思宇');
INSERT INTO `set_material_price` VALUES (129, 5, 'B36', '上海02仓', 'JY', '九曳胶带', 3.45000, '2020-07-08 00:00:00', '陈思宇');
COMMIT;

-- ----------------------------
-- Table structure for set_material_stand
-- ----------------------------
DROP TABLE IF EXISTS `set_material_stand`;
CREATE TABLE `set_material_stand` (
  `id` int NOT NULL AUTO_INCREMENT,
  `month` int NOT NULL,
  `warehouse_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `warehouse_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `material_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `material_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `qty` decimal(10,5) NOT NULL,
  `unit` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `cre_time` datetime NOT NULL,
  `cre_user` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of set_material_stand
-- ----------------------------
BEGIN;
INSERT INTO `set_material_stand` VALUES (1, 5, 'B36', '上海02仓', 'JY-JD', '胶带', 0.03850, '卷', '2020-07-07 18:12:21', '孙喜');
INSERT INTO `set_material_stand` VALUES (2, 5, 'B01', '北京01仓', 'JY-JD', '胶带', 0.03850, '卷', '2020-07-07 18:12:21', '孙喜');
INSERT INTO `set_material_stand` VALUES (3, 5, 'B03', '广州01仓', 'JY-JD', '胶带', 0.03850, '卷', '2020-07-07 18:12:21', '孙喜');
INSERT INTO `set_material_stand` VALUES (4, 5, 'B04', '成都仓', 'JY-JD', '胶带', 0.03850, '卷', '2020-07-07 18:12:21', '孙喜');
INSERT INTO `set_material_stand` VALUES (5, 5, 'B05', '武汉仓', 'JY-JD', '胶带', 0.03850, '卷', '2020-07-07 18:12:21', '孙喜');
INSERT INTO `set_material_stand` VALUES (6, 5, 'B08', '沈阳仓', 'JY-JD', '胶带', 0.03850, '卷', '2020-07-07 18:12:21', '孙喜');
INSERT INTO `set_material_stand` VALUES (7, 5, 'B31', '福州仓', 'JY-JD', '胶带', 0.03850, '卷', '2020-07-07 18:12:21', '孙喜');
COMMIT;

-- ----------------------------
-- Table structure for set_operation_price
-- ----------------------------
DROP TABLE IF EXISTS `set_operation_price`;
CREATE TABLE `set_operation_price` (
  `id` int NOT NULL AUTO_INCREMENT,
  `month` int NOT NULL,
  `warehouse_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `warehouse_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `time_price` decimal(50,2) NOT NULL,
  `cre_time` datetime NOT NULL,
  `cre_user` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of set_operation_price
-- ----------------------------
BEGIN;
INSERT INTO `set_operation_price` VALUES (1, 5, 'B36', '上海02仓', 27.38, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (2, 5, 'B01', '北京01仓', 26.98, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (3, 5, 'B03', '广州01仓', 26.58, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (4, 5, 'B04', '成都仓', 26.21, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (5, 5, 'B05', '武汉仓', 27.52, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (6, 5, 'B08', '沈阳仓', 26.21, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (7, 5, 'B31', '福州仓', 26.21, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (8, 6, 'B36', '上海02仓', 27.38, '2020-07-10 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (9, 6, 'B01', '北京01仓', 26.98, '2020-07-10 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (10, 6, 'B03', '广州01仓', 26.58, '2020-07-10 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (11, 6, 'B04', '成都仓', 26.21, '2020-07-10 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (12, 6, 'B05', '武汉仓', 27.52, '2020-07-10 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (13, 6, 'B08', '沈阳仓', 26.21, '2020-07-10 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (14, 6, 'B31', '福州仓', 26.21, '2020-07-10 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (15, 5, 'B27', '济南仓', 26.21, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (16, 5, 'B35', '北京03仓', 26.21, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (17, 5, 'B11', '西安仓', 26.21, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (18, 6, 'B27', '济南仓', 26.21, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (19, 6, 'B35', '北京03仓', 26.21, '2020-07-07 16:24:59', '蒋其虎');
INSERT INTO `set_operation_price` VALUES (20, 6, 'B11', '西安仓', 26.21, '2020-07-07 16:24:59', '蒋其虎');
COMMIT;

-- ----------------------------
-- Table structure for set_pallet_price
-- ----------------------------
DROP TABLE IF EXISTS `set_pallet_price`;
CREATE TABLE `set_pallet_price` (
  `id` int NOT NULL AUTO_INCREMENT,
  `month` int NOT NULL,
  `warehouse_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `warehouse_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `freezer_price` decimal(10,5) NOT NULL,
  `normal_price` decimal(10,5) NOT NULL,
  `cre_time` datetime NOT NULL,
  `cre_user` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of set_pallet_price
-- ----------------------------
BEGIN;
INSERT INTO `set_pallet_price` VALUES (1, 5, 'B36', '上海02仓', 4.50000, 1.80000, '2020-07-06 16:04:22', '孙喜');
INSERT INTO `set_pallet_price` VALUES (2, 5, 'B01', '北京01仓', 4.50000, 1.80000, '2020-07-07 16:04:22', '孙喜');
INSERT INTO `set_pallet_price` VALUES (3, 5, 'B03', '广州01仓', 4.50000, 1.80000, '2020-07-08 16:04:22', '孙喜');
INSERT INTO `set_pallet_price` VALUES (4, 5, 'B04', '成都仓', 4.50000, 1.80000, '2020-07-09 16:04:22', '孙喜');
INSERT INTO `set_pallet_price` VALUES (5, 5, 'B05', '武汉仓', 4.50000, 1.80000, '2020-07-10 16:04:22', '孙喜');
INSERT INTO `set_pallet_price` VALUES (6, 5, 'B08', '沈阳仓', 4.50000, 1.80000, '2020-07-11 16:04:22', '孙喜');
INSERT INTO `set_pallet_price` VALUES (7, 5, 'B31', '福州仓', 4.50000, 1.80000, '2020-07-12 16:04:22', '孙喜');
INSERT INTO `set_pallet_price` VALUES (8, 5, 'B11', '西安仓', 4.50000, 1.80000, '2020-07-10 16:04:22', '孙喜');
INSERT INTO `set_pallet_price` VALUES (9, 5, 'B27', '济南仓', 4.50000, 1.80000, '2020-07-11 16:04:22', '孙喜');
INSERT INTO `set_pallet_price` VALUES (10, 5, 'B35', '北京03仓', 4.50000, 1.80000, '2020-07-12 16:04:22', '孙喜');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
