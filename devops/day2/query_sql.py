from my_sqlalchemy import Departments, Employees, Session

session = Session()

# # 查询所有
# query1 = session.query(Departments)
# for dep in query1:
#     print(dep)
#
# print("*" * 30)
#
# for obj in query1:
#     print('%s %s' % (obj.dep_id, obj.dep_name))

# # 查询某些列
# query2 = session.query(Employees.emp_name.label('姓名'), Employees.email.label('邮箱'))
# for item in query2:
#     print('%s'.center(15) % item.姓名 + '%s'.center(20) % item.邮箱)

# # 排序
# query3 = session.query(Employees.emp_name, Employees.email).order_by(Employees.emp_id)
# print(query3)
# for item in query3:
#     print('%s\t\t%s' % (item.emp_name, item.email))

# # 取切片
# query4 = session.query(Departments).order_by(Departments.dep_id)[2:5]
# for item in query4:
#     print('%s\t\t%s' % (item.dep_id,item.dep_name))

# # 过滤(相当于where)
# query5 = session.query(Employees.emp_name, Employees.email).filter(Employees.emp_id > 3).filter(Employees.dep_id==2)
# for name, email in query5:
#     print('%s\t\t%s' % (name, email))

# all(),one(),first(),scalar()用法
# query6 = session.query(Employees)
# print(query6.all())
# print(query6.first())
# print(query6.count())
# query7 = query6.filter(Employees.emp_id==2)
# print(query7.one())
# print(query7.scalar())

# # 多表查询
# query8 = session.query(Employees.emp_name,Departments.dep_name).join(Departments, Employees.dep_id==Departments.dep_id)
# print(query8.all())

test = session.query(Employees).filter(Employees.emp_id ==10).scalar()
if test:
    print('yes')
else:
    print('no')
























