USE version_db;
show tables;

select * from user_table;
select * from user_history;
select * from version_final_table;
select * from cache_table;
select * from ref_note_table;

desc version_final_table;


INSERT INTO user_table (EMAIL, DEPART) VALUES ('yeko0124@gmail.com', 'Effects');
INSERT INTO user_table (EMAIL, DEPART) VALUES ('ljy@gmail.com', 'Effects');
INSERT INTO user_table (EMAIL, DEPART) VALUES ('rapa@gmail.com', 'System');

INSERT INTO version_final_table (CACHE_NAME, USER_DEPART) VALUES ('usd_rop1_v001.usda', 'Effects');

INSERT INTO cache_table (FINAL_ID, CACHE_PATH) VALUES (1, '/home/rapa/workspace/houdini/pinning_version/geo/pinning_version/usd_rop1/usd_rop1_v001.usda');