from my_sqlalchemy import Employees, Departments, Session

session = Session()


# 修改表信息
q1 = session.query(Employees).filter(Employees.email=='123@qq.com')
q1 = q1.one()
print(q1)
q1.email = 'tom@qq.com'
session.commit()

