from my_sqlalchemy import Departments, Employees, Salary, Session

session = Session()

# # 单条写入数据
xs = Departments(dep_id=6, dep_name='销售部')
session.add(xs)
session.commit()
# session.close()

# # 多条数据插入
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qs = Departments(dep_id=4, dep_name='测试部')
# fn = Departments(dep_name='财务部')
# session.add_all([ops, dev, qs, fn])
# session.commit()
# session.close()

# tom = Employees(emp_id=1, emp_name='tom', email='123@163.com', dep_id=2)
# kenji = Employees(emp_id=2, emp_name='kenji', email='abcde@163.com', dep_id=3)
# lucy = Employees(emp_id=3, emp_name='lucy', email='rejldf@163.com', dep_id=1)
# wgs = Employees(emp_id=4, emp_name='王国率', email='opooe@163.com', dep_id=4)
# by = Employees(emp_name='百余', email='qqlldd@163.com', dep_id=5)
# cy = Employees(emp_name='曹禺', email='lelel@163.com', dep_id=2)
# sz = Employees(emp_name='孙政', email='haah@163.com', dep_id=3)
# ydl = Employees(emp_name='因地理', email='ydi@163.com', dep_id=4)
# wyl = Employees(emp_name='网与来', email='fjldfldl@163.com', dep_id=5)

# session.add_all([tom, kenji, lucy, wgs, by, cy, sz, ydl, wyl])
# session.commit()
# session.close()

