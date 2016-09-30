#!/usr/bin/python
# -*- coding: utf-8 -*-

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
    timestamp = Column(DateTime, default=func.now())

    def __repr__(self):
        return "%s(cpf=%r, cnpj= %r)" % (
            self.__class__.__name__, self.cpf,
            self.__class__.__name__, self.cnpj
        )

class T1Foo(TBase, Base):
    __tablename__ = 'pessoas'
    cpf = Column(String(11))

class T2Foo(TBase, Base):
    __tablename__ = 'empresas'
    cnpj = Column(String(14))



engine = create_engine('sqlite:///rss.db', echo=False)

Base.metadata.create_all(engine)

sess = sessionmaker(engine)()

sess.add_all([T1Foo(cpf='07785679908'), T1Foo(cpf='98989898'), T2Foo(cnpj='9898996598659'),
             T1Foo(cpf='98958989')])
sess.commit()

print(sess.query(T1Foo).all())
print(sess.query(T2Foo).all())