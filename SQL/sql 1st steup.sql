show databases;
desc empn;
desc stud_details;
alter table stud_details add courseid int,add course_name varchar(20);
desc stud_details;
alter table stud_details rename to stud;
desc stud;
alter table stud modify column address varchar(100) after studroll;
desc stud;

alter table stud add primary key (studroll);

show tables;
desc stud;

alter table stud drop primary key;
desc stud;

alter table stud add primary key (studroll);
desc stud;

create table course(cid int,cname varchar(20),studroll int);

alter table course add constraint stud_fix foreign key(studroll)
references stud(studroll);

desc course;


create database companyys;

use companyys;

create table product_details(prod_id int primary key,prod_name 
varchar(20),prod_cat varchar(20),prod_price decimal(10,2));

desc product_details;

insert into product_details values(1,"mobile","electronics",20000);

insert into product_details values(2,"sofaset","furniture",25000);

insert into product_details values(3,"refrigerator","electronics",30000);

insert into product_details values(4,"cooker","kitchen applinces",2000);

insert into product_details values(5,"bat","sports acupment",2000);

insert into product_details values(6,"chair","furniture",3000);

insert into product_details values(7,"sofaset","furniture",25000);

select*from product_details;

select prod_name,prod_price from product_details;

select 4+4;

select 4+5 as result;

select distinct prod_name from product_details;

select * from product_details where prod_cat="electronics";

select * from product_details where prod_price<10000;

select * from product_details where prod_price>10000;

select distinct prod_name,prod_name,prod_cat,prod_price
 from product_details where prod_price<10000;

select * from product_details where prod_cat="electronics" and prod_price>25000;

select 125-120 as "result";

select 2*4 as "result";

select *  from product_details;

select prod_price-1000 as "discount" from product_details;

select prod_price-1000 as "discount" from product_details where prod_name="mobile";

select * from product_details;

select * from product_details where prod_cat="electronics" or prod_price>20000;

select * from product_details where  prod_price between 1000 and 3000;

select * from product_details where  prod_price not between 1000 and 3000;

select * from product_details where  prod_name in ('mobile','sofaset');

select * from product_details where  prod_name not in ('mobile','sofaset');

select * from product_details where prod_cat like 'e%';

select * from product_details where prod_name like 'mobil_';

select * from product_details order by prod_price;

select * from product_details order by prod_name;

select * from product_details limit 5;

select * from product_details limit 4;

select * from product_details limit 2,5; 

show databases;  

show tables;

use companyys;

show create table product_details;

help contents;

select * from product_details;

insert into product_details values(8,null,null,2000);

select prod_name,prod_price from product_details where prod_name is null;

select prod_name,prod_price from product_details where prod_name=null;

select prod_name,prod_price from product_details where prod_name is not null;

select * from product_details;


select prod_name,prod_cat,
case
	when prod_price>=20000 then "10% discount"
	when prod_price>=20000 then "5% discount"
    when prod_price>=3000 then "2% discount"
     when prod_price>=2000 then "2% discount"
    else prod_price
end as 'discount'
from product_details;


select min(prod_price) from product_details;

select max(prod_price) from product_details;

select avg(prod_price) from product_details;


create table emp(empid int primary key , emp_name varchar(20), emp_city varchar (20), emp_salary decimal(10,2));

alter table emp add contact varchar (20);

desc emp;

alter table emp add emp_design bigint after emp_name;

desc emp;





