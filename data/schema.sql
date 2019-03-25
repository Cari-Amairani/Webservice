CREATE DATABASE ferre_cadr;

USE ferre_cadr;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs(
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE clientes(
  id integer unsigned NOT NULL PRIMARY KEY AUTO_INCREMENT,
  nombre varchar (50) not null,
  ape_mat varchar (35) not null,
  ape_pat varchar(35) not null,
  telefono varchar(12) not null,
  correo varchar(60) not null
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO clientes(nombre, ape_pat, ape_mat, telefono, correo) VALUES
  ('Carina Amairani','Díaz','Ramírez','7751185359','carina-amairani@hotmail.com'),
  ('Oscar Flavio','Díaz','Ramírez','7751014611','flavioramirez@hotmail.com'),
  ('Beatriz','Ramírez','Duran','7757529834','beatrizramirez011@gemail.com');

INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);


SELECT * FROM users;
SELECT * FROM sessions;

CREATE USER 'cadr'@'localhost' IDENTIFIED BY 'cadr.2019';
GRANT ALL PRIVILEGES ON ferre_cadr.* TO 'cadr'@'localhost';
FLUSH PRIVILEGES;