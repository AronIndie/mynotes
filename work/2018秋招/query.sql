show databases;
use test;

-- select id,
-- 	RANK() OVER (order by id) as rank,
-- 	count(0)
-- 	from pingduoduo1;

drop table pinduoduo2;
create table pinduoduo2(
	id int,
    name char(10),
    gender char(2),
    month char(10))
    ;


insert into pinduoduo2 values ('1', 'A', 'm', '2017-06') ,('2', 'B', 'f', '2017-06'), ('3', 'B', 'm', '2017-07');

select * from pinduoduo2;

update
       pinduoduo2 as p1
       join pinduoduo2 as p2
       on (
          p1.gender = 'm' and p2.gender = 'f'
          or
          p1.gender = 'f' and p2.gender = 'm'
          )
          set p1.gender = p2.gender
       where p1.month = '2017-06';


create table pinduoduo3(
	uid char(8) not null,
    gid char(10) not null,
    star int);

insert into pinduoduo3 values ('u0', 'g0', 2), ('u0', 'g1', 4), ('u1', 'g0', 3), ('u1', 'g1', 1);

select * from pinduoduo3;


select luid, ruid,
       l.g0 * r.g0 + l.g1 * r.g1 as 'inner'
       from
       (select a.uid as luid, sum(case when a.gid='g0' then a.star else null end) as 'g0',
              sum(case when a.gid='g1' then a.star else null end) as 'g1'
              from pinduoduo3 a group by a.uid) l
       ,
       (select b.uid as ruid, sum(case when b.gid='g0' then b.star else null end) as 'g0',
               sum(case when b.gid='g1' then b.star else null end) as 'g1'
               from pinduoduo3 b group by b.uid) r;


-- 其他尝试，这里需要用到反射的技巧，可惜不会
select uid, group_concat(distinct  concat('sum(case when gid="', gid, '" then star else null end) as "', gid, '"'))
       from pinduoduo3 group by uid;


select t.star from pinduoduo3 as t;



-- 拼多多2019提前批笔试




