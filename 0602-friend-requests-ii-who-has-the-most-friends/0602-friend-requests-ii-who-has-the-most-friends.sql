# Write your MySQL query statement below
with total as(
    select requester_id as id,count(*) as tot from RequestAccepted group by requester_id
    union all
    select accepter_id as id,count(*) as tot from RequestAccepted group by accepter_id
)
select id,sum(tot) as num from total group by id order by num desc limit 1;