#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine


class Conexao:
    engine = None
    def __init__(self):
        self.engine = create_engine('sqlite:///rss.db')

    def conn(self):
        return self.engine