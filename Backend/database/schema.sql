-- 创建新数据库
CREATE DATABASE my_track_data_1; 

-- 选择数据库
USE my_track_data_1;  

-- 创建一个名为track_data的表，用于存储数据
CREATE TABLE track_data_1 (
    node VARCHAR(255), 
    moment VARCHAR(255), 
    value DECIMAL(20, 7), 
    PRIMARY KEY (node, moment)
);
-- 单元节点名称
-- 时刻值
-- 存储与特定节点和时刻相关联的数值数据，数据类型为DECIMAL，共20位数字，小数部分为7位
 -- 复合主键，由node和moment字段共同组成。确保在每个节点和每个时刻的数据唯一性


-- 从本地文件加载数据到数据库表  
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/displacement_2.csv'
-- 指定数据将被加载到的目标表
INTO TABLE track_data_1
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
-- 指定CSV文件中的列如何映射到数据库表中的列
(node, moment, value);

-- 从本地文件加载数据到数据库表  
LOAD DATA INFILE '/var/lib/mysql-files/displacement_2.csv'
-- 指定数据将被加载到的目标表
INTO TABLE track_data_1
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
-- 指定CSV文件中的列如何映射到数据库表中的列
(node, moment, value);


-- 删除数据库
DROP DATABASE my_track_data;

-- 展示warnings信息
SHOW WARNINGS;

-- 将track_data_1数据表中的node一列列名改为name
ALTER TABLE track_data_1 CHANGE COLUMN node name VARCHAR(255);