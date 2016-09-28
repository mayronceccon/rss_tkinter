#!/usr/bin/python
# -*- coding: utf-8 -*-

from library.Menu import *
from models.ModelUrlsRss import *


class FormPrincipal:
    root = None

    def __init__(self):
        root = Tk()
        # configurações de janela
        root.title('RSS')
        root.geometry("800x600")
        root['pady'] = 10
        root['padx'] = 10
        root.resizable(width=False, height=False)
        # root.maxsize(width=1000, height=800)
        # root.minsize(width=1000, height=800)

        # MENU
        MenuPrincipal(root)
        # MENU

        self.root = root
        self.montaCampos()

        root.mainloop()

    def montaCampos(self):
        tv = ttk.Treeview(self.root, selectmode="extended", show='headings', height="26", padding=10)
        tv['columns'] = ('publicacao', 'titulo', 'url')

        tv.heading('publicacao', text='Publicação')
        tv.heading('titulo', text='Título')
        tv.heading('url', text='Link')

        tv.column('publicacao', anchor='center', width=100)
        tv.column('titulo', width=100, minwidth=100)
        tv.column('url', width=100, minwidth=100)
        tv.grid(sticky=(N,E,S,W))

        self.treeview = tv
        self.treeview.bind("<Double-1>", self.itemClicked)
        self.treeview.grid()

        urlsRss = ModelUrlsRss()
        urls = urlsRss.buscaResultados()
        cont = 0
        for post in urls:
            cont = cont + 1
            title = post.title
            link = post.link
            published = post.published

            self.treeview.insert('', 'end', text=cont, values=(published, title, link))

        self.root.grid_columnconfigure(0, weight=1)

    def itemClicked(self, event):
        item = self.treeview.selection()[0]
        print("you clicked on", self.treeview.item(item, "text"))