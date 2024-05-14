DROP DATABASE IF EXISTS `log_analysis`;
CREATE DATABASE `log_analysis` DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_general_ci;

# 用户表
DROP TABLE IF EXISTS `log_analysis`.`user`;
CREATE TABLE `log_analysis`.`user`
(
    `id`        INT(20)      NOT NULL AUTO_INCREMENT COMMENT '用户ID',
    `username`  VARCHAR(128) NOT NULL UNIQUE COMMENT '用户名',
    `password`  VARCHAR(128) NOT NULL COMMENT '密码',
    `nickname`  VARCHAR(128) COMMENT '昵称',
    `avatar`    VARCHAR(256) DEFAULT 'static/system/images/avatar.jpg' COMMENT '头像',
    `phone`     VARCHAR(32) COMMENT '电话',
    `email`     VARCHAR(128) COMMENT '邮箱',
    `role`      VARCHAR(128) DEFAULT '普通会员' COMMENT '角色',
    `enable`    INT(10)      DEFAULT 1 COMMENT '启用',
    `create_at` TIMESTAMP    DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_at` DATETIME     DEFAULT NULL COMMENT '创建时间',
    `delete_at` DATETIME     DEFAULT NULL COMMENT '逻辑删除标志',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;
DROP TABLE IF EXISTS `log_analysis`.`login_log`;

# 扫描日志表
DROP TABLE IF EXISTS `log_analysis`.`login_log`;
CREATE TABLE `log_analysis`.`login_log`
(
    `id`          INT(20)      NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `uid`         INT(20)      NOT NULL COMMENT '用户 ID',
    `url`         VARCHAR(256) COMMENT '登录 url',
    `method`      VARCHAR(10) COMMENT '请求方法',
    `ip`          VARCHAR(256) NOT NULL COMMENT '登录 IP',
    `user_agent`  VARCHAR(256) COMMENT '用户代理',
    `description` VARCHAR(128) NOT NULL COMMENT '描述',
    `success`     INT(10) COMMENT '登录是否成功',
    `create_at`   TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_at`   DATETIME  DEFAULT NULL COMMENT '更新标志',
    `delete_at`   DATETIME  DEFAULT NULL COMMENT '逻辑删除标志',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

# 网站信息表
DROP TABLE IF EXISTS `log_analysis`.`site_info`;
CREATE TABLE `log_analysis`.`site_info`
(
    `id`             INT(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `title`          VARCHAR(64) COMMENT '网站标题',
    `logo`           VARCHAR(128) DEFAULT '' COMMENT '网站 logo',
    `site_url`       VARCHAR(256) DEFAULT '' COMMENT '网站 url',
    `keywords`       VARCHAR(128) DEFAULT '' COMMENT '网站关键词',
    `description`    TEXT COMMENT '网站描述',
    `tel`            VARCHAR(128) DEFAULT '' COMMENT '联系电话',
    `site_email`     VARCHAR(128) DEFAULT '' COMMENT '管理员邮箱',
    `site_copyright` VARCHAR(256) DEFAULT '' COMMENT '网站版权信息',
    `create_at`      TIMESTAMP    DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_at`      BOOLEAN      DEFAULT NULL COMMENT '更新时间',
    `delete_at`      BOOLEAN      DEFAULT NULL COMMENT '逻辑删除时间',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

# 站内消息表
DROP TABLE IF EXISTS `log_analysis`.`message`;
CREATE TABLE `log_analysis`.`message`
(
    `id`        INT(20)      NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `content`   VARCHAR(256) NOT NULL COMMENT '内容',
    `from_id`   INT(20)      NOT NULL COMMENT '来源 ID',
    `to_id`     INT(20)      NOT NULL COMMENT '目标 ID',
    `type_id`   INT(20)      NOT NULL COMMENT '消息类型 ID',
    `create_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_at` DATETIME  DEFAULT NULL COMMENT '读取时间',
    `delete_at` DATETIME  DEFAULT NULL COMMENT '逻辑删除标志',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

# 扫描任务表
DROP TABLE IF EXISTS `log_analysis`.`scan_tasks`;
CREATE TABLE `log_analysis`.`scan_tasks`
(
    `id`             INT(20)      NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `uid`            INT(20)      NOT NULL COMMENT '发起用户ID',
    `url`            VARCHAR(128) NOT NULL COMMENT '扫描地址',
    `task_type_id`   INT(20)   DEFAULT 1 COMMENT '任务类型',
    `task_status_id` INT(20)   DEFAULT 1 COMMENT '任务状态 1 进行中 2 完成',
    `create_at`      TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_at`      DATETIME  DEFAULT NULL COMMENT '完成时间',
    `delete_at`      DATETIME  DEFAULT NULL COMMENT '逻辑删除标志',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

# 扫描报告表
DROP TABLE IF EXISTS `log_analysis`.`scan_report`;
CREATE TABLE `log_analysis`.`scan_report`
(
    `id`          INT(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `scan_id`     INT(20) NOT NULL COMMENT '扫描列表 ID',
    `report_path` VARCHAR(256) COMMENT '扫描报告路径',
    `create_at`   TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_at`   DATETIME  DEFAULT NULL COMMENT '更新标志',
    `delete_at`   DATETIME  DEFAULT NULL COMMENT '逻辑删除标志',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

# 用户角色表
DROP TABLE IF EXISTS `log_analysis`.`scan_user_roles`;
CREATE TABLE `log_analysis`.`scan_user_roles`
(
    `id`        INT(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `user_id`   INT(20) NOT NULL COMMENT '用户 ID',
    `role_id`   INT(20) NOT NULL COMMENT '角色 ID',
    `create_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_at` DATETIME  DEFAULT NULL COMMENT '更新标志',
    `delete_at` DATETIME  DEFAULT NULL COMMENT '逻辑删除标志',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

#### 字典表

# 任务状态
DROP TABLE IF EXISTS `log_analysis`.`task_status`;
CREATE TABLE `log_analysis`.`task_status`
(
    `id`        INT(20)     NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `status`    VARCHAR(32) NOT NULL COMMENT '任务状态',
    `create_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_at` DATETIME  DEFAULT NULL COMMENT '更新标志',
    `delete_at` DATETIME  DEFAULT NULL COMMENT '逻辑删除标志',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

INSERT INTO `log_analysis`.`task_status`
    (`status`)
values ('进行中'),
       ('完成'),
       ('失败');

# 任务类型
DROP TABLE IF EXISTS `log_analysis`.`task_type`;
CREATE TABLE `log_analysis`.`task_type`
(
    `id`        INT(20)     NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `type`      VARCHAR(32) NOT NULL COMMENT '任务类型',
    `create_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_at` DATETIME  DEFAULT NULL COMMENT '更新标志',
    `delete_at` DATETIME  DEFAULT NULL COMMENT '逻辑删除标志',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

INSERT INTO `log_analysis`.`task_type`
    (`type`)
values ('公开'),
       ('私有');

# 角色权限表
DROP TABLE IF EXISTS `log_analysis`.`scan_roles`;
CREATE TABLE `log_analysis`.`scan_roles`
(
    `id`        INT(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `role_name` VARCHAR(64) COMMENT '角色名称',
    `create_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_at` DATETIME  DEFAULT NULL COMMENT '更新标志',
    `delete_at` DATETIME  DEFAULT NULL COMMENT '逻辑删除标志',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

INSERT INTO `log_analysis`.`scan_roles`
    (`role_name`)
VALUES ('管理员'),
       ('普通会员');

# 消息类型表
DROP TABLE IF EXISTS `log_analysis`.`message_type`;
CREATE TABLE `log_analysis`.`message_type`
(
    `id`        INT(20)     NOT NULL AUTO_INCREMENT COMMENT 'ID',
    ｀type｀      VARCHAR(32) NOT NULL COMMENT '类型名称',
    `create_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `active_at` DATETIME  DEFAULT NULL COMMENT '激活标志',
    `update_at` DATETIME  DEFAULT NULL COMMENT '更新标志',
    `delete_at` DATETIME  DEFAULT NULL COMMENT '逻辑删除标志',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

INSERT INTO `log_analysis`.`message_type`
    (｀type｀)
VALUES ('系统消息'),
       ('会员消息')