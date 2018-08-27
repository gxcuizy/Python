DROP TABLE IF EXISTS area;
CREATE TABLE area (
  id int NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  name varchar(32) NOT NULL DEFAULT '' COMMENT '区域名称',
  code varchar(8) NOT NULL DEFAULT '' COMMENT '区域编码',
  parent_code varchar(8) NOT NULL DEFAULT '' COMMENT '城市编码',
  level int NOT NULL DEFAULT 0 COMMENT '城市等级：1省份，2城市，3区',
  PRIMARY KEY (id)
)CHARSET=utf8 COMMENT='省市区三级城市表';
