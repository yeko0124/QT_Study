CREATE DATABASE version_db;
USE version_db;

drop database version_db;

# (main-accessible) version_final table / version_updated table(stack)
# department table / version_list table ()

CREATE TABLE IF NOT EXISTS user_table
(
    ID int not null AUTO_INCREMENT PRIMARY KEY ,
    EMAIL CHAR(50) NOT NULL,
    DEPART VARCHAR(25) NULL
);

drop table user_table;

CREATE TABLE IF NOT EXISTS version_final_table
(
    ID int not null AUTO_INCREMENT PRIMARY KEY ,
    CACHE_NAME CHAR(50) NOT NULL,
    USER_DEPART CHAR(50) NOT NULL,

    CONSTRAINT FK_final_user_name FOREIGN KEY (USER_DEPART)
    REFERENCES user_table (DEPART)
    ON UPDATE CASCADE ON DELETE CASCADE
);

drop table version_final_table;

drop table user_history;

CREATE TABLE IF NOT EXISTS user_history
(
    ID int not null AUTO_INCREMENT PRIMARY KEY ,
    FINAL_ID int not null,
    USER_ID int not null,

    CONSTRAINT FK_user_history_final_id FOREIGN KEY (FINAL_ID)
    REFERENCES version_final_table (ID)
    ON UPDATE CASCADE ON DELETE CASCADE,

    CONSTRAINT FK_user_history_user_id FOREIGN KEY (USER_ID)
    REFERENCES user_table (ID)
    ON UPDATE CASCADE ON DELETE CASCADE
);

drop table ref_note_table;

CREATE TABLE IF NOT EXISTS ref_note_table
(
    ID int not null AUTO_INCREMENT PRIMARY KEY ,
    NOTE text null,
    CACHE_ID int not null,

    CONSTRAINT FK_ref_note_cache_id FOREIGN KEY (CACHE_ID)
    REFERENCES cache_table (ID)
    ON UPDATE CASCADE ON DELETE CASCADE
);

drop table cache_table;

CREATE TABLE IF NOT EXISTS cache_table
(
    ID int not null AUTO_INCREMENT PRIMARY KEY ,
    FINAL_ID int not null,
    CACHE_PATH varchar(255) not null,

    CONSTRAINT FK_cache_final_id FOREIGN KEY (FINAL_ID)
    REFERENCES version_final_table (ID)
    ON UPDATE CASCADE ON DELETE CASCADE
);

