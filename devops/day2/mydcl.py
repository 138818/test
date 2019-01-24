import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='tedu.cn', db='nsd1808', charset='utf8')
cursor = conn.cursor()

# # 部门表
# create_dep = 'create table departments(dep_id int, dep_name varchar(20), primary key (dep_id))'
# cursor.execute(create_dep)

# # 员工表
# create_employess = """create table employess(
# emp_id int, emp_name varchar(20) not null, gender varchar(6), birth_date date, email varchar(50), dep_id int,
# primary key (emp_id), foreign key (dep_id) references departments(dep_id))"""
# cursor.execute(create_employess)

# # 工资表
# create_salary = """create table salary(auto_id int, date date, emp_id int, basic int, awards int,
# primary key(auto_id), foreign key(emp_id) references employess(emp_id))"""
# cursor.execute(create_salary)

# insert1 = 'insert into departments values(%s, %s)'
# # 单列插入
# cursor.execute(insert1, (1, 'HR'))
# # 插入多列
# deps = [(2, '运维'), (3, '开发'), (4, '测试')]
# cursor.executemany(insert1, deps)
# data = [(5, '行政'), (6, '财务'), (7, '市场')]
# cursor.executemany(insert1, data)
# # 插入到数据库(对数据有改变的操作需要commit)
# conn.commit()

# # 查询数据
# sql1 = 'select * from departments order by dep_id asc'
# cursor.execute(sql1)
# result1 = cursor.fetchone()
# print(result1)
# result2 = cursor.fetchmany(2)
# print(result2)
# result3 = cursor.fetchall()
# print(result3)

# # 游标使用
# sql1 = 'select * from departments order by dep_id asc'
# cursor.execute(sql1)
# cursor.scroll(1, mode='absolute')
# print(cursor.fetchone())
# cursor.scroll(2, mode='relative')
# print(cursor.fetchone())

# # 修改,删除表信息
# update = 'update departments set dep_name=%s where dep_name=%s'
# cursor.execute(update, ('人事部', 'HR'))
# delete = 'delete from departments where dep_id=%s'
# cursor.execute(delete, (7,))
# conn.commit()

data = 'select * from departments'
cursor.execute(data)
print(cursor.fetchall())



cursor.close()
conn.close()


