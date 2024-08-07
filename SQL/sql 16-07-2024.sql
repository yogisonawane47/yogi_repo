create database companyeee;

use companyeee;

create table empolye (deptno int primary key,dname varchar(15),loc varchar(15));

insert into empolye values(10,"accounting","new york"),(20,"research","dallas"),
(30,"sales","chicago"),(40,"operations","boston");

create table empo(empno int primary key,empname varchar(20),job varchar (20), mgr int, hirdate date, sal decimal(10,2),deptno int,foreign key(deptno) references empolye(deptno));

select * from empolye;

select * from empo;

insert into empo values (1,"riya","manager",209,"2022-04-03",6000,0,10);


