#!/usr/bin/python
# -*- coding: utf-8 -*-

from forms.FormProxy import *

class MenuPrincipal:
    root = None
    def __init__(self, root):
        self.root = root

        menubar = Menu(root)
        #File
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # Configurações
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Configurar Proxy", command=self.configureProxy)
        menubar.add_cascade(label="Configurações", menu=helpmenu)

        #Edit
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.donothing)
        editmenu.add_command(label="Copy", command=self.donothing)
        editmenu.add_command(label="Paste", command=self.donothing)
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)

        #Help
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        root.config(menu=menubar)

    def donothing(self):
        print("Abrir")

    def configureProxy(self):
        FormProxy()