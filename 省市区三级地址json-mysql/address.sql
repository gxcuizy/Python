DROP TABLE IF EXISTS my_region;
CREATE TABLE `my_region` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '表id',
  `name` varchar(32) DEFAULT NULL COMMENT '地区名称',
  `level` tinyint(4) DEFAULT '0' COMMENT '地区等级 分省市县区',
  `parent_id` int(10) DEFAULT NULL COMMENT '父id',
  `gid` varchar(30) DEFAULT NULL COMMENT '行政区划id',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Index 4` (`parent_id`,`name`),
  KEY `parent_id` (`parent_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='地址表';