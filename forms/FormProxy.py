#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import ttk
from library.fields import *

class FormProxy:
    root = None
    def __init__(self):
        root = Tk()
        root.title('Proxy - RSS')
        root.resizable(width=False, height=False)
        root['pady'] = 10
        root['padx'] = 10
        self.montaCampos(root)
        root.mainloop()

    def montaCampos(self, root):
        self.labelDescricao = ttk.Label(root, text="Configuração de Proxy")
        self.labelDescricao['font'] = (None, '15','bold')
        self.labelDescricao.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

        self.labelHost = ttk.Label(root, text="Host:")
        self.labelHost.grid(row=2, column=1, pady=5, padx=5, stick=NW)

        self.campoHost = ttk.Entry(root)
        self.campoHost.focus_force()
        self.campoHost['width'] = 50
        self.campoHost.grid(row=2, column=2, pady=5, padx=5, stick=NW)

        self.labelPorta = ttk.Label(root, text="Porta:")
        self.labelPorta.grid(row=3, column=1, pady=5, padx=5, stick=NW)

        self.campoPorta = ttk.Entry(root)
        self.campoPorta['width'] = 20
        self.campoPorta.grid(row=3, column=2, pady=5, padx=5, stick=NW)

        self.labelUsuario = ttk.Label(root, text="Usuário:")
        self.labelUsuario.grid(row=4, column=1, pady=5, padx=5, stick=NW)

        self.campoUsuario = ttk.Entry(root)
        self.campoUsuario['width'] = 20
        self.campoUsuario.grid(row=4, column=2, pady=5, padx=5, stick=NW)

        self.labelSenha = ttk.Label(root, text="Senha:")
        self.labelSenha.grid(row=5, column=1, pady=5, padx=5, stick=NW)

        self.campoSenha = ttk.Entry(root)
        self.campoSenha['width'] = 20
        self.campoSenha['show'] = '*'
        self.campoSenha.grid(row=5, column=2, pady=5, padx=5, stick=NW)

        self.botao = ttk.Button(root, text='Salvar Dados')
        self.botao['command'] = self.enviaDados
        self.botao.grid(row=6, column=1, pady=5, padx=5, columnspan=2)

    def enviaDados(self):
        host = self.campoHost.get()
        porta = self.campoPorta.get()
        usuario = self.campoUsuario.get()
        senha = self.campoSenha.get()