#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from lib.menu import *
from models.urls_rss import *


class FormPrincipal:
    root = None

    def __init__(self):
        root = Tk()
        # configurações de janela
        root.title('RSS')
        root.geometry("1000x800")
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
        '''self.listbox = Listbox(self.root)
        self.listbox.grid(row=1, column=1)
        self.listbox.insert(END, "a list entry")
        for item in ["one", "two", "three"]:
            self.listbox.insert(END, item)'''

        tv = ttk.Treeview(self.root, selectmode="extended")
        tv['columns'] = ('titulo', 'url', 'publicacao')
        tv['displaycolumns'] = ('titulo', 'url', 'publicacao')

        tv.heading('titulo', text='Título')
        tv.heading('url', text='Link')
        tv.heading('publicacao', text='Publicação')

        tv.column('titulo', anchor='center', width=100)
        tv.column('url', anchor='center', width=100)
        tv.column('publicacao', anchor='center', width=20)
        scrollbar = Scrollbar(self.root)
        scrollbar.configure(command=tv.yview)

        tv.configure(yscrollcommand=scrollbar.set)

        tv.grid(sticky=(S, W, E))
        self.treeview = tv
        self.treeview.bind("<Double-1>", self.itemClicked)
        #self.treeview.grid(row=1, column=1, stick=E+W)
        self.treeview.pack()


        urlsRss = UrlsRss()
        urls = urlsRss.buscaResultados()

        cont = 0
        for post in urls:
            cont = cont + 1
            title = post.title
            link = post.link
            published = post.published
            self.treeview.insert('', 'end', None, values=(title, link, published))

        self.botao = ttk.Button(self.root, text='Enviar')
        self.botao['command'] = self.enviaDados
        #self.botao.grid(row=2, column=1, pady=5, padx=5, columnspan=4)
        self.botao.pack()

    def itemClicked(self, event):
        item = self.treeview.selection()[0]
        print("you clicked on", self.treeview.item(item, "text"))

    def enviaDados(self):
        print(self.campoNome.get())
        print(self.campoCpf.get())