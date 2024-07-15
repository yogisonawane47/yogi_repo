
create database companyys;

use companyys;
create table emp(empid int primary key , emp_name varchar(20), emp_city varchar (20), emp_salary decimal(10,2));
insert into emp values(1,"yogi","kalyan",20000),(2,"aswin","karjat",30000),(3,"kalpesh","Dombivali",35000),(4,"rupesh","kalyan",40000);

select * from emp;
select concat(emp_name,"working in",emp_city) as "emp_working dept" from emp;

select upper(emp_name) as "emp_name" from emp;

select lower(emp_name) as "emp_name" from emp;

select length(emp_name) as "total_length" from emp;

select char_length(emp_name) as "total_length" from emp;

select substring(emp_name,1,3) from emp;

select substring(emp_name,2,4) from emp;

select reverse(emp_name) from emp;

select round(3.146788,2);

select round(3.144788,2);


select ceil(4.3);

select floor(4.8);

select abs(-24);

select abs(24);

select power(3,3);

select current_date;

select current_time;

select curdate();

select current_timestamp;

select datediff("2024-07-15","2024-05-20");

select timestampdiff(year,"2004-11-15",curdate());

select timestampdiff(year,"2004-11-15",curdate());

select timestampdiff(year,"2004-11-15",curdate()) as "current age";

select * from emp;

select * from emp where emp_name="aswin";

select * from emp where emp_name!="aswin";

select * from emp where emp_name<>"aswin";

select * from emp where emp_salary>20000;

select * from emp where emp_salary<20000;

select max(emp_salary) from emp;

select min(emp_salary) from emp;

select avg(emp_salary) from emp;

select count(*) from emp;

select sum() from emp;


select * from emp;

select emp_city,count(*) from emp group by emp_city;

select*from emp;

insert into emp values(5,"shekhar","neral","10000");

select*from emp;

select emp_salary,count(*) from emp group by emp_salary having emp_salary>20000;

select emp_salary,count(*) as "Total dept" from emp group by emp_salary having emp_salary>20000;

select emp_city,sum(emp_salary) from emp group by emp_city;

