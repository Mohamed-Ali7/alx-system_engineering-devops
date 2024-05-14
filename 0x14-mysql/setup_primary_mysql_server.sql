CREATE DATABASE tyrell_corp;
USE tyrell_corp;

CREATE TABLE nexus6 (
    id NOT NULL AUTO_INCREMENT,
    `name` varchar(150),
    PRIMARY KEY (`id`)
    );

INSERT INTO nexus6 (name) VALUES ('Leon');

CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

CREATE USER 'replica_user'@'%' IDENTIFIED WITH mysql_native_password BY 'replica_password';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
