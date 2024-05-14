DROP TABLE IF EXISTS ``.``;
CREATE TABLE ``.``
(
    `id`        INT(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `create_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `active_at` DATETIME  DEFAULT NULL COMMENT '激活标志',
    `update_at` DATETIME  DEFAULT NULL COMMENT '更新标志',
    `delete_at` DATETIME  DEFAULT NULL COMMENT '逻辑删除标志',
    PRIMARY KEY (`id`)
) Engine = InnoDB
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;