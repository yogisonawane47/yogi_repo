select * from companyeee.new_view;

use classicmodels;

delimiter $$
create procedure new_proc1()
begin
select * from users;
select * from city;
end $$

delimiter ;
call new_proc1;



select * from users;

delimiter $$
create procedure proc_88(out result int)
begin
select max(userage) into result from users;
end $$
delimiter $$
call proc_88(@result);
select @result;


delimiter //
create procedure proc_10(inout var1 int, var2 int)
begin
select userage into var1 from users where userage-var2;
end//
delimiter ; 

call proc_10(@var1,26);
select @var1;



delimiter //
create procedure proc22(in normal_price decimal(10,2),out disc_price decimal(10,2))
begin
 if (normal_price>500)  then 
						set disc_price=normal_price*.8;
          elseif(normal_price>100) then
						set disc_price=normal_price*9;
		  else
						set disc_price=normal_price;
                        end if;
end //
delimiter ;

call proc22(400,@disc_price);
select @disc_price;





desc customers;

delimiter &&
create procedure proc80(in pCustomerNumber int,out pShipping varchar(20))
begin
declare cutomer_country VARCHAR(20);
SELECT country into cutomer_country from  customers
where customerNumber= pCustomerNumber;

case cutomer_country
when 'USA' then 
	set pShipping='2 day shipping';
when 'canada' then 
	set pShipping='3 day shipping';
else
	set pShipping='5 day shipping';
end case;
end &&
delimiter ; 


call proc80(360,@pShipping);
select @pShipping;



syntax:
while expression do 
	statement 
end while    


delimiter $$
create procedure proc_while1(OUT st varchar(20))
begin
declare i int; 
set i=1;
set st= " ";
while i<=10 do 
set st=concat(st,i,",");
set i=i+1;
end while;
end $$
delimiter ; 

call proc_while(@st);
select @st;







delimiter $$
create function fun12(name varchar(20))
returns varchar(50)
deterministic
begin
 declare output varchar(20);
 set output=concat("Hello",name,"!");
 return output;
end $$
delimiter ;

select fun12("yogi")'message';



delimiter $$
create function cf6(creditlim double)
returns varchar(50)
deterministic
begin
declare cutomerlevel varchar(20);
if creditlim>500000 then 
set  cutomerlevel="platinum";
elseif  creditlim<=500000 and creditlim>=100000 then 
    set  cutomerlevel="dimond";
elseif creditlim<=100000 and creditlim>=50000 then 
set  cutomerlevel="gold";
elseif creditlim<=50000 and  creditlim>=10000 then 
set  cutomerlevel="silver";
else 
set  cutomerlevel="bronz";
end if;
return  cutomerlevel;
end $$
delimiter ; 

select cf6(100000);

 
