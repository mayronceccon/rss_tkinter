#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String


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