from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Enum, Boolean


engine = create_engine('mysql+pymysql://wjy:123qqq...A@192.168.1.2/shopping?charset=utf8', encoding='utf8')
# self.engine = create_engine('mysql+pymysql://wjy:123qqq...A@192.168.1.2/shopping?charset=utf8', encoding='utf8', echo=Ture)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    u_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    password = Column(String(100), nullable=False)
    states = Column(Boolean, nullable=False)

class Goods(Base):
    __tablename__ = 'goods'
    g_id = Column(Integer, primary_key=True)
    g_name = Column(String(20), nullable=False)
    g_price = Column(Float, nullable=False)
    g_number = Column(Integer)
    states = Column(Boolean, nullable=False)

class VipUser(Base):
    __tablename__ = 'vipUser'
    v_id = Column(Integer, primary_key=True)
    v_name = Column(String(20), nullable=False)
    telphone = Column(String(11), nullable=False)
    birthday = Column(String(10))

# class Ticket(self.Base):
#     id = Column(Integer, primary_key=True)
#     v_id = Column(Integer)
#     datetime = Column(DateTime)

if __name__ == '__main__':
    Base.metadata.create_all(engine)