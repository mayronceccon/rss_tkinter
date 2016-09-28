#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper, relation
from library.Model import Model

class Proxy(object):
    def __repr__(self):
        host = self.host
        porta = self.porta
        usuario = self.usuario
        senha = self.senha
        return """host : %s, porta : %d, usuario : %s, senha : %s""" % (host, porta, usuario, senha)

class ModelProxy(Model):
    def __init__(self):
        super(ModelProxy, self).__init__()
        self.criarTabela()

    def criarTabela(self):
        metadata = MetaData()
        tabela_proxy = Table('proxy', metadata,
            Column('id', Integer, primary_key=True),
            Column('host', String),
            Column('porta', Integer),
            Column('usuario', String),
            Column('senha', String)
        )
        metadata.create_all(self.conn)
        mapper(Proxy, tabela_proxy)

    def getOne(self):
        row = self.session.query(Proxy).filter().first()
        return row

    def update(self, id, dados):
        stmt = self.session.update(Proxy).where(Proxy.id == 5).values(dados)
        self.session.commit()

    def getProxy(self):
        config = None
        row = self.getOne()
        if row != None:
            host = row.host
            porta = row.porta
            usuario = row.usuario
            senha = row.senha
            if len(usuario) > 0 and len(senha) > 0 and porta > 0 and len(host) > 0:
                config = """%s:%s@%s:%d""" % (usuario, senha, host, porta)
            elif porta > 0 and len(host) > 0:
                config = """%s:%d""" % (host, porta)

        return config
