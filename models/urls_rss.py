#!/usr/bin/python
# -*- coding: utf-8 -*-

import feedparser
import urllib.request

class UrlsRss:
    proxy = None
    def __init__(self):
        self.proxy = urllib.request.ProxyHandler({"http": "user:senha@192.168.0.1:3128"})

    def buscaResultados(self):
        url = 'http://www.r7.com//data/rss/tecnologiaCiencia.xml'
        feed = feedparser.parse(url, handlers=[self.proxy])
        return feed.entries