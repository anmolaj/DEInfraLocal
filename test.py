""""
Table 1: id, name
- 1, a
- 2, b
- 3, c

Table 2: id, name
- 1, a
- 4, d
- 5, e
"""

"""
t.id t1.n t2.id t2.n
1 a 1 a
2 b N N
3 c N N
N N 4 d
N N 5 e

"""

"""
OP
- 2, b
- 3, c
- 4, d
- 5, e
"""

"""
SQL

Select * from table1
where id not in (Select id from table2)
Union
Select * from table2
where id not in (Select id from table1)


Using Joins:

Select coalesce(t1.id,t2.id) as id, coalesce(t1.name,t2.name) as name from 
table1 t1 full outer join table2 as t2
On (ta.id= t2.id)
where t1.id is None or t2.id is None
"""

"""
Spark SQL
t1 = 100MB 100 files
t2 100MB 1 file

spark.read(t1) = 100 tasks (executor 100 cores)

read(t2) = 1 task = increase?
Shuffle -> Stage
t2 (ids) 
shufle data t1 id
t2 ids 

Sort Merge Join 

"""