show databases ; 

use classicmodels;

create trigger  trigger01

{BEFORE | AFTER} {INSERT | DELETE}

ON TABEL_NAME

FOR EACH ROW 

TRIGGER_BODY






use companyys;
select * from emp;

create table logtable (id int primary key auto_increment,action varchar (20),dt date);

delimiter $$
create trigger INSERT_trigger1 after insert on emp 
for each row
begin
  insert into logtable(action,dt) values("Record is inserted", now());
  
end $$
delimiter ;

select * from logtable;
insert into emp values(6,"gotay","malavali",9000,105);
select * from logtable;
select * from emp;






create table logTB (id int primary key auto_increment,action varchar (20),dt datetime);

delimiter $$
create trigger INSERT_trigger22 after insert on emp 
for each row
begin
  insert into logTB(action,dt) values("Record is inserted", now());
  
end $$
delimiter ;

select * from logTB;
insert into emp values(7,"manay","lolivali",5000,106);
select * from logTB;
select * from emp;





delimiter $$
create trigger delete_trigger1 after delete on emp 
for each row
begin
  insert into logtable(action,dt) values("Record is delete", now());
  
end $$
delimiter ;

delete from emp where empid=6;
delete from emp where empid=7;
select * from emp;




select * from emp;
desc emp;
desc empbkpss;
create table empbkpss(empid int primary key ,
emp_name varchar(20), emp_city varchar(20),emp_salary decimal(10,2),dept_code int);

select * from empbkpss;


delimiter $$
create trigger trigger0002 before delete on emp 
for each row 
begin
insert into empbkpss values(old.empid,old.emp_name,old.emp_city,old.emp_salary,old.dept_code);
end $$
delimiter ;

delete from emp where empid=6;
delete from emp where empid=7;
delete from emp where empid=5;

select*from empbkpss;

