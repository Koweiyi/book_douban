/*
 Navicat Premium Data Transfer

 Source Server         : conn_team06
 Source Server Type    : MariaDB
 Source Server Version : 100229
 Source Host           : www.91iedu.com:3391
 Source Schema         : team06

 Target Server Type    : MariaDB
 Target Server Version : 100229
 File Encoding         : 65001

 Date: 23/06/2020 18:13:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for douban_user
-- ----------------------------
DROP TABLE IF EXISTS `douban_user`;
CREATE TABLE `douban_user`  (
  `user_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `user_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户名',
  `user_address` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '用户地址',
  `join_date` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '用户加入豆瓣日期',
  PRIMARY KEY (`user_id`, `user_name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
