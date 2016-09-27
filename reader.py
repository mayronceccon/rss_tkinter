#!/usr/bin/python
# -*- coding: utf-8 -*-

import feedparser
import urllib.request
from sqlalchemy import create_engine

mostrar = True
engine = create_engine('sqlite:///rss.db', echo = mostrar) 

#https://jucacrispim.wordpress.com/2009/12/07/pequena-introducao-ao-sqlalchemy/

proxy = urllib.request.ProxyHandler({"http":"mayron.ceccon:M@yron151290@192.168.0.1:3128"})

url = 'http://www.r7.com//data/rss/tecnologiaCiencia.xml'
feed = feedparser.parse(url, handlers = [proxy])

for post in feed.entries:
   title = post.title
   link = post.link
   published = post.published
   #summary = post.summary
   rss = "Titulo %s - %s" % (title, link)
   
   print(rss)