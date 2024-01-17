# Write your MySQL query statement below

with rk as  (
select 
    d.name as Department,   
    e.name as Employee, 
    e.salary as Salary ,
    DENSE_RANK() over (partition by d.id order by e.salary desc) as r
    from Employee e
    inner join Department d 
    on d.id=e.departmentId
) select Department,
Employee,
Salary from rk 
where r<=3