#!/usr/bin/python
# -*- coding: utf-8 -*-

import feedparser
import urllib.request
from models.ModelProxy import *

class ModelUrlsRss:
    proxy = None
    def __init__(self):
        #model = ModelProxy()
        #config = model.getProxy()
        config = ''
        self.proxy = urllib.request.ProxyHandler({"http": config})

    def buscaResultados(self):
        url = 'http://www.r7.com//data/rss/tecnologiaCiencia.xml'
        feed = feedparser.parse(url, handlers=[self.proxy])
        return feed.entries