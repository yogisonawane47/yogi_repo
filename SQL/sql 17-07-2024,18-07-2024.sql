show databases;

use companyys;

select * from emp;

select emp_city from emp where emp_name="yogi" or emp_name="aswin";

select emp_name from emp where emp_city="kalyan" or emp_name="karjat";

select emp_name from emp where emp_city in (select emp_city from emp where emp_name in ("yogi","aswin"));


select emp_salary from emp where emp_name="yogi" or emp_name="aswin";

select emp_salary from emp where emp_salary <20000 or emp_salary<30000;

select emp_salary from emp where emp_salary < any(select emp_salary from emp where emp_name="yogi" or emp_name="aswin");

select emp_salary from emp where emp_salary > any(select emp_salary from emp where emp_name="yogi" or emp_name="aswin");

select emp_salary from emp where emp_salary < all(select emp_salary from emp where emp_name="yogi" or emp_name="aswin");

select emp_salary from emp where emp_salary > all(select emp_salary from emp where emp_name="yogi" or emp_name="aswin");



select*from emp;
select * from empbkup;
show tables;





select * from emp cross join empbkup;

select emp.emp_name,emp_city from emp cross join empbkup;

select * from empbkup;

create table department1 (deptcode int ,empdept varchar(20),empcity varchar(20));

insert into department1 values(101,"account","kalyan"),(102,"research","karjat"),(103,"sales","vangani"),(104,"operations","khopoli");

select * from department1;

select * from emp;

select emp.emp_name,department1.empcity from emp inner join department1 where emp.dept_code=department1.deptcode;

select * from emp  natural join department1;






