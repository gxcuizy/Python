DROP TABLE IF EXISTS province;
CREATE TABLE province (
  id int NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  name varchar(16) NOT NULL DEFAULT '' COMMENT '省份名称',
  code varchar(8) NOT NULL DEFAULT '' COMMENT '省份编码',
  PRIMARY KEY (id)
) CHARSET=utf8 COMMENT='省份表';


DROP TABLE IF EXISTS city;
CREATE TABLE city (
  id int NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  code varchar(8) NOT NULL DEFAULT '' COMMENT '城市名称',
  name varchar(32) NOT NULL DEFAULT '' COMMENT '城市编码',
  province_code varchar(8) NOT NULL DEFAULT '' COMMENT '省份编码',
  PRIMARY KEY (id)
)CHARSET=utf8 COMMENT='城市表';


DROP TABLE IF EXISTS area;
CREATE TABLE area (
  id int NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  name varchar(32) NOT NULL DEFAULT '' COMMENT '区域名称',
  code varchar(8) NOT NULL DEFAULT '' COMMENT '区域编码',
  city_code varchar(8) NOT NULL DEFAULT '' COMMENT '城市编码',
  PRIMARY KEY (id)
)CHARSET=utf8 COMMENT='区域表';