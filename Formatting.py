import customtkinter
import os
import sys
import sqlparse
import tkinter
import json

from datetime import datetime
from PIL import Image
from tkinter import Frame, END, filedialog as fd, Scrollbar, Text

# Programa: Formatting
# Versão: 1.0.00
# Descrição: Formatação expressões SQL e JSON
# Data Inicio: 21/10/2023
# Data Revisão: 19/11/2023
# Autor: Eduardo Gomes Júnior

Caminho = os.path.dirname(os.path.realpath(__file__))
Historico = os.path.abspath(".")+'\\Histórico\\'

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# Função: resource_path
# Descrição: Obtem o caminho absoluto do aplicativo


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS + '\\img\\'
    except Exception:
        base_path = f'{Caminho}\\Icones\\'

    return os.path.join(base_path, relative_path)

# Classe: Formatting
# Descrição: Classe principal


class Formatting(Frame):

    def __init__(self, t1=None):

        self.t1 = customtkinter.CTk()
        Frame.__init__(self, t1)
        height = self.t1.winfo_screenheight()
        width = self.t1.winfo_screenwidth()
        self.t1.geometry(str('{0}x{0}+0+0').format(width, height))
        self.t1.protocol("WM_DELETE_WINDOW", self.t1.destroy)
        self.t1.title("Formatting - 1.0.00")
        self.t1.iconbitmap(resource_path("format_shapes.ico"))

        FrameOpcs = customtkinter.CTkFrame(self.t1)

        # Carrega icones usados
        self.ico_find = customtkinter.CTkImage(Image.open(resource_path("find.png")))
        self.ico_cle = customtkinter.CTkImage(Image.open(resource_path("clear.png")))
        self.ico_sql = customtkinter.CTkImage(Image.open(resource_path("sql.png")))
        self.ico_json = customtkinter.CTkImage(Image.open(resource_path("json.png")))
        self.ico_his = customtkinter.CTkImage(Image.open(resource_path("json.png")))
        self.ico_fec = customtkinter.CTkImage(Image.open(resource_path("Cancelar.png")))

        self.label = customtkinter.CTkLabel(FrameOpcs,
                                            text='Localizar:',
                                            font=("Consolas", 15))
        self.label.pack(side='left')

        self.edit1 = customtkinter.CTkEntry(FrameOpcs,
                                            width=300,
                                            state=tkinter.DISABLED)
        self.edit1.pack(side='left', fill='both', expand=1, padx=10)
        self.edit1.focus_set()

        # Função: Pesquisa
        # Descrição: Pesquisa palavras nos quadros

        def Pesquisa():

            self.textoAtu.tag_remove('found', '1.0', END)
            self.textoFor.tag_remove('found', '1.0', END)

            sAtu = self.edit1.get()
            sFor = self.edit1.get()

            if sAtu:
                idx = '1.0'

                while 1:

                    idx = self.textoAtu.search(sAtu,
                                               idx,
                                               nocase=1,
                                               stopindex='end')

                    if not idx:
                        break

                    lastidx = '%s+%dc' % (idx, len(sAtu))
                    self.textoAtu.tag_add('found', idx, lastidx)
                    idx = lastidx

            if sFor:
                idxf = '1.0'

                while 1:

                    idxf = self.textoFor.search(sFor,
                                                idxf,
                                                nocase=1,
                                                stopindex='end')

                    if not idxf:
                        break

                    lastidx = '%s+%dc' % (idxf, len(sFor))
                    self.textoFor.tag_add('found', idxf, lastidx)
                    idxf = lastidx

                self.textoAtu.tag_config('found', foreground='red')
                self.textoFor.tag_config('found', foreground='red')

                self.edit1.focus_set()

        self.butt1 = customtkinter.CTkButton(FrameOpcs,
                                             image=self.ico_find,
                                             text='Localizar',
                                             hover_color="gray25",
                                             command=Pesquisa,
                                             state=tkinter.DISABLED)

        self.butt2 = customtkinter.CTkButton(FrameOpcs,
                                             image=self.ico_cle,
                                             text='Limpar',
                                             fg_color="#CCAC00",
                                             hover_color="gray25",
                                             command=self.clearFomt,
                                             state=tkinter.DISABLED)

        self.butt3 = customtkinter.CTkButton(FrameOpcs,
                                             image=self.ico_sql,
                                             text='SQL',
                                             fg_color="#228B22",
                                             hover_color="gray25",
                                             command=lambda opcao="sql": self.formtExp(opcao),
                                             state=tkinter.DISABLED)

        self.butt4 = customtkinter.CTkButton(FrameOpcs,
                                             image=self.ico_json,
                                             text='JSON',
                                             fg_color="#d99e63",
                                             hover_color="gray25",
                                             command=lambda opcao="json": self.formtExp(opcao),
                                             state=tkinter.DISABLED)

        self.butt5 = customtkinter.CTkButton(FrameOpcs,
                                             image=self.ico_his,
                                             text='Historico',
                                             fg_color="#863c53",
                                             command=self.AbreHistor,
                                             hover_color="gray25",
                                             state=tkinter.DISABLED)

        self.butt6 = customtkinter.CTkButton(FrameOpcs,
                                             image=self.ico_fec,
                                             text='Fechar',
                                             fg_color="#FF0000",
                                             command=self.t1.destroy,
                                             hover_color="gray25")

        if os.path.exists(Historico) is True:
            self.butt5.configure(state=tkinter.NORMAL)

        self.butt1.pack(side='right', padx=10, after=self.edit1)
        self.butt2.pack(side='right', padx=10, before=self.butt1)
        self.butt3.pack(side='right', padx=10, before=self.butt2)
        self.butt4.pack(side='right', padx=10, before=self.butt3)
        self.butt5.pack(side='right', padx=10, before=self.butt4)
        self.butt6.pack(side='right', padx=10, before=self.butt5)

        FrameOpcs.pack(side='top', fill='both', padx=5, pady=5)

        FrameOpcs2 = customtkinter.CTkFrame(self.t1)
        FrameOpcs2.pack(side='top', fill='both', padx=5, pady=5)

        self.lblText1 = customtkinter.CTkLabel(FrameOpcs2,
                                               text='Expressão Original:',
                                               font=("Consolas", 15))
        self.lblText1.pack(side='left', fill='x', padx=5, pady=5, expand=1)

        self.lblText2 = customtkinter.CTkLabel(FrameOpcs2,
                                               text='Expressão Formatada:',
                                               font=("Consolas", 15),
                                               text_color="#3e79b4")
        self.lblText2.pack(side='right', fill='both', padx=5, pady=5, expand=1)

        FrameOpcs3 = customtkinter.CTkFrame(self.t1)
        FrameOpcs3.pack(side='bottom', fill='both', padx=5, pady=5, expand=1)

        self.scrollVer = Scrollbar(FrameOpcs3, orient="vertical")
        self.scrollVer.pack(side="right", fill='y', padx=10, pady=10)

        self.scrollHor = Scrollbar(FrameOpcs3, orient="horizontal")
        self.scrollHor.pack(side="bottom", fill='both', padx=10, pady=10)

        self.textoAtu = Text(FrameOpcs3,
                             font=("Consolas", 18),
                             width=4,
                             height=4,
                             yscrollcomman=self.scrollVer.set,
                             xscrollcomman=self.scrollHor.set,
                             bg="#323232",
                             fg="white",
                             cursor="arrow",
                             blockcursor=True)

        self.textoFor = Text(FrameOpcs3,
                             font=("Consolas", 18),
                             width=4,
                             height=4,
                             yscrollcomman=self.scrollVer.set,
                             xscrollcomman=self.scrollHor.set,
                             bg="#323232",
                             fg="#3e79b4",
                             cursor="arrow",
                             blockcursor=True)

        self.textoAtu.pack(side='left',
                           fill='both',
                           expand=1,
                           padx=10,
                           pady=10)

        self.textoFor.pack(side='right',
                           fill='both',
                           expand=1,
                           padx=10,
                           pady=10)

        # Eventos
        self.textoAtu.bind("<KeyRelease>", self.eventotextoAtu)

        # Barras de rolagem
        self.scrollVer.config(command=self.multiple_yview)
        self.scrollHor.config(command=self.multiple_xview)

        self.t1.mainloop()

    # Função: clearFomt
    # Descrição: Limpa/apaga quadros

    def clearFomt(self):
        self.textoAtu.delete("0.0", "end")
        self.textoFor.delete("0.0", "end")

    # Função: multiple_yview
    # Descrição: Scrool BAR VERTICAL para ambos os quadros

    def multiple_yview(self, *args):
        self.textoAtu.yview(*args)
        self.textoFor.yview(*args)

    # Função: multiple_xview
    # Descrição: Scrool BAR HORIZONTAL para ambos os quadros

    def multiple_xview(self, *args):
        self.textoAtu.xview(*args)
        self.textoFor.xview(*args)

    # Função: eventotextoAtu
    # Descrição: Trata eventos do quadro txtAtuNu

    def eventotextoAtu(self, event):

        textoAtu = self.textoAtu.get(1.0, END)

        LinhasAtu = 0
        qtdLinhasAtu = textoAtu.split("\n")

        for i in qtdLinhasAtu:
            if i:
                LinhasAtu += 1

        if LinhasAtu > 0:
            self.edit1.configure(state=tkinter.NORMAL)
            self.butt1.configure(state=tkinter.NORMAL)
            self.butt2.configure(state=tkinter.NORMAL)
            self.butt3.configure(state=tkinter.NORMAL)
            self.butt4.configure(state=tkinter.NORMAL)
        else:
            self.edit1.configure(state=tkinter.DISABLED)
            self.butt1.configure(state=tkinter.DISABLED)
            self.butt2.configure(state=tkinter.DISABLED)
            self.butt3.configure(state=tkinter.DISABLED)
            self.butt4.configure(state=tkinter.DISABLED)

    # Função: formtExp
    # Descrição: Formata expressão SQL ou JSON

    def formtExp(self, opcao):

        if os.path.exists(Historico) is False:
            os.makedirs(Historico)

        self.textoAtu.tag_remove('errojon', '1.0', END)

        dtHrAtual = datetime.now()

        dtHrAtual_text = dtHrAtual.strftime("%Y-%m-%d-%H%M%S")

        self.butt5.configure(state=tkinter.NORMAL)

        self.textoFor.delete("0.0", "end")

        textoAtu = self.textoAtu.get(1.0, END)

        if opcao == "sql":

            textoSQL = sqlparse.format(textoAtu,
                                       reindent=True,
                                       keyword_case='upper')

            self.textoFor.insert("0.0", textoSQL)
        else:

            json_formatted_str = ""

            try:
                json_object = json.loads(textoAtu)
                json_formatted_str = json.dumps(json_object, indent=2)
                self.textoFor.insert("0.0", json_formatted_str)
            except json.JSONDecodeError as errojson:
                self.textoFor.insert(END, "Inconsistência: \n")
                self.textoFor.insert(END, f"Erro: {errojson.msg} \n")
                self.textoFor.insert(END, f"Linha: '{errojson.lineno} \n")
                self.textoFor.insert(END, f"Coluna: '{errojson.colno}")

                linhaErroI = f'{str(errojson.lineno)}.0'
                linhaErroF = f'{str(errojson.lineno+1)}.0'

                self.textoAtu.tag_add('errojon', linhaErroI, linhaErroF)
                self.textoAtu.tag_config('errojon',
                                         background='yellow',
                                         foreground='black')

        with open(f"{Historico +'//' +dtHrAtual_text}."+opcao, "w") as arquivo:
            if opcao == "sql":
                arquivo.write(textoSQL)
            else:
                arquivo.write(json_formatted_str)

        arquivo.close()

    # Função: AbreHistor
    # Descrição: Abre pasta de históricos

    def AbreHistor(self):

        filetypes = (
            ('Arquivos SQL', ' *.sql'),
            ('Arquivos JSON', '*.json'),
            ('Todos Arquivos', '*.*'),
        )

        filenames = fd.askopenfilenames(
            title='Histórico',
            initialdir=Historico,
            filetypes=filetypes)

        with open(filenames[0], 'r', errors="ignore") as file:
            self.AbreHist = file.read()
            file.close()

        self.textoAtu.delete("0.0", "end")
        self.textoFor.delete("0.0", "end")
        self.textoAtu.insert('1.0', self.AbreHist)


Formatting()
