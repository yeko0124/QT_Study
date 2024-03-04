
create database test_db;

use test_db;

create table test_table
(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY ,
    name VARCHAR(25)
);

insert into test_table(name) values ('프로그래밍');
insert into test_table(name) values ('코딩');

select * from test_table;



####################################################################################

use todo_db;

show tables;

select * from todo_db.todo_author;
select * from todo_db.todo_list;
select * from todo_db.todo_status;

insert into todo_list (todo, save_datetime, deadline, status, author_id) VALUES ('coding study', '2023/10/10', '2024/03/03', 'waiting', 6);

select id, todo, save_datetime, deadline, status, author_id from todo_list;

delete from todo_list where id = 23;
delete from todo_list where id=9 or id=8;

update todo_list set status = 'complete' where id = 3;

desc todo_list;


########################################################################################################3

drop table todo_status;
drop table todo_list;
drop table todo_author;