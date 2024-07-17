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

alter table emp add dept_code varchar(20);

desc emp;


update emp set dept_code=102 where emp_city="karjat";
update emp set dept_code=103 where emp_city="dombivali";
update emp set dept_code=104 where emp_city="neral";

select *from emp;

update emp set dept_code=101 where empid=1;

update emp set dept_code=102 where empid=2;

update emp set dept_code=103 where empid=3;

update emp set dept_code=101 where empid=4;

update emp set dept_code=104 where empid=5;

select * from emp;

select emp_name,emp_city from emp where (emp_salary,deptcode) in ()

desc emp;

create table empbkp(empid int, empname varchar (20),empcity varchar(20),empdept varchar(20),salary decimal(10,2),deptcode int);
desc empbkp;
select * from empbkp;
insert into empbkp select * from emp where empid in (select empid from emp);



create table empbkup(empid int, empname varchar (20),empcity varchar(20),salary decimal(10,2),deptcode int);

desc empbkup;

insert into empbkup select * from emp where empid in (select empid from emp);

update empbkup set salary=salary*0.25 where dept_code in(select dept_code from emp where dept_code>102);

