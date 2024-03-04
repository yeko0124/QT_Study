CREATE DATABASE todo_db;
USE todo_db;

create table if not exists todo_status
(
#     id int not null auto_increment primary key,
    status varchar(25) not null primary key
);

desc todo_status;

create table todo_author
(
    id int not null auto_increment primary key,
    author varchar(25) null
);

create table todo_list
(
    id int not null auto_increment primary key,
    todo text null,
    save_datetime datetime,
    deadline datetime,
    status varchar(25) not null,
    author_id int not null,

    constraint FK_todo_list_todo_status_status foreign key (status)
        references todo_status (status)
        on update cascade on delete no action,
    constraint FK_todo_list_todo_author_author foreign key (author_id)
        references todo_author (id)
        on update cascade on delete cascade
);

desc todo_list;

# user기반으로 남길건지 / asset 기반(todo기준)으로 남길건지 선택도 해야 함
# 아니면 테이블을 하나 더 만드는 방법도 있음 (user history and todo_history)
create table if not exists todo_history
(
    id int not null auto_increment primary key,
    todo text null,
    save_datetime datetime,
    deadline datetime,
    todo_id int not null,

    constraint FK_todo_history_todo_list_id foreign key (todo_id)
    references todo_list (id)
    on update cascade on delete cascade
);

drop table todo_history;


CREATE TABLE todo_complete_history
(
    id int not null auto_increment primary key,
    todo text null,
    save_datetime datetime,
    status varchar(25) not null,
    author_id int not null,

    constraint FK_todo_list_todo_complete_status foreign key (status)
    references todo_status (status)
    on update cascade on delete no action,

    constraint FK_todo_history_complete_list_id foreign key (author_id)
    references todo_list (id)
    on update cascade on delete cascade
);


insert into todo_author (author) values ('jsc');
insert into todo_author (author) values ('kye');
insert into todo_author (author) values ('ljy');
insert into todo_author (author) values ('pjh');
insert into todo_author (author) values ('kjh');
insert into todo_author (author) values ('lsj');
insert into todo_author (author) values ('lsb');
insert into todo_author (author) values ('lsh');
insert into todo_author (author) values ('pjo');
insert into todo_author (author) values ('ksa');

insert into todo_status (status) values ('complete');
insert into todo_status (status) values ('inprogress');
insert into todo_status (status) values ('waiting');

select * from todo_history;

insert into todo_list (todo, save_datetime, deadline, status, author_id) VALUES('test 1222', '2022/12/10', '2030/01/22', 'inprogress', 1);

show triggers;
desc todo_history;
desc todo_complete_history;

CREATE TRIGGER tgr_after_insert_todo_list_table
    AFTER INSERT ON todo_list
    FOR EACH ROW # 각 행에 대해서 이벤트를 실행할 것인가
    BEGIN
        INSERT into todo_history (todo, save_datetime, deadline, todo_id) VALUES(NEW.todo, NOW(), NEW.deadline, NEW.id);
    end;

DROP TRIGGER tgr_after_insert_todo_list_table;

select * from todo_complete_history;

CREATE TRIGGER tgr_after_complete_todo_list_table
    AFTER UPDATE ON todo_list
    FOR EACH ROW
    BEGIN
        IF NEW.status = 'complete' THEN
        INSERT INTO todo_complete_history(todo, save_datetime, status, author_id) VALUES (OLD.todo, NOW(), NEW.status, OLD.id);
        END IF;
    End;

DROP TRIGGER tgr_after_complete_todo_list_table;
DROP TABLE todo_complete_history;

delete from todo_complete_history;   # 안에 있는 데이터만 지우는 것 delete / 통째로 다 지우는 것 drop
delete from todo_list;