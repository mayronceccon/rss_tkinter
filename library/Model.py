#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from library.Conexao import *


class Model(object):
    conn = None
    session = None
    def __init__(self):
        conexao = Conexao()
        self.conn = conexao.conn()
        Session = sessionmaker(bind=self.conn)
        self.session = Session()

    def salvar(self, data):
        self.session.add(data)
        self.session.commit()