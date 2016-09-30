from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TBase(object):
    """Base class is a 'mixin'.

    Guidelines for declarative mixins is at:

    http://www.sqlalchemy.org/docs/orm/extensions/declarative.html#mixin-classes

    """
    id = Column(Integer, primary_key=True)
    data = Column(String(50))

    def __repr__(self):
        return "%s(data=%r)" % (
            self.__class__.__name__, self.data
        )

class T1Foo(TBase, Base):
    __tablename__ = 't1'

class T2Foo(TBase, Base):
    __tablename__ = 't2'

    timestamp = Column(DateTime, default=func.now())

engine = create_engine('sqlite://', echo=True)

Base.metadata.create_all(engine)

sess = sessionmaker(engine)()

sess.add_all([T1Foo(data='t1'), T1Foo(data='t2'), T2Foo(data='t3'),
             T1Foo(data='t4')])

print sess.query(T1Foo).all()
print sess.query(T2Foo).all()