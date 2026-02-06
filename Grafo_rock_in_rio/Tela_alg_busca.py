from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import numpy
from PIL import ImageTk, Image
import sqlite3
import Busca
import Busca_v

pastaApp=os.path.dirname(__file__)
root = Tk() #variavel do seu gosto, aqui ela recebe a tela que abre, mas temos que colocar num loop, se não ela abre e fecha rápido.
#Inserção da imagem usando o Tkinter.
"""
imgRock=PhotoImage(file=pastaApp+"\\Grafo_Rock_In_Rio.png")
l_rock=Label(root, image=imgRock)
l_rock.place(x=0.0,y=0)

imgRock1=PhotoImage(file=pastaApp+"\\marcacao-removebg-preview.png")
l_rock1=Label(root, image=imgRock1, highlightbackground='blue')
l_rock1.configure(background='blue')
l_rock1.place(x=345,y=214)
"""
#Inserção da imagem usando o Canvas.
canvas = Canvas(root,  width=1160, height=530,bd=0, highlightthickness=0)
canvas.place(x=0, y=0)
image = PhotoImage(file='Grafo_Rock_In_Rio ORIGINAL - Copia.png')
image_id0 = canvas.create_image(580,263, image=image)
image2 = PhotoImage(file='Bota2.png')



#FALTA TIRAR O ERRO QUE DA SE NÃO SELECIONAR NADA E USAR O BOTÃO EXCLUIR
class Funcs(): #Criando as funções
    #Métodos do banco conecta e desconecta
    def conecta_bd(self):
        self.conec = sqlite3.connect("buscar.bd")
        self.cursor = self.conec.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conec.close(); print("Desconectando ao banco de dados")
    #Método que insere imagens no grafo
    def montaTabelas(self):
        self.conecta_bd()
        #Criando tabela
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS buscar(
                cod INTEGER PRIMARY KEY,
                nome_metodo CHAR(50),
                caminho_metodo TEXT,
                caminho_custo INTEGER
            );
        """)
        #Dando o commit para validar a informação, seria tipo o execute.
        self.conec.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    # Select no banco
    def select_lista(self):
        #print(*self.listaCli.get_children())
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" 
        SELECT cod, nome_metodo, caminho_metodo, caminho_custo 
        FROM buscar
        ORDER BY cod;   
        """)#O "ASC" é em ordem alfabética. E tomar cuidado no SELECT da nossa VIEW, pois o número de selects tem que ser igual ao número de colunas que temos, então pegaremos até o cod.
        #Adicionando o SELECT para a tabela do frame_2.
        for i in lista:
            self.listaCli.insert("", END, values=i) #OBS: listaCli é o nosso - ttk.Treeview(tabela)
        self.desconecta_bd()
    # Deleta info no banco
    def deleta_info(self):

        self.listaCli.selection()

        for i in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(i, 'values')
            self.cod  = col1
        self.conecta_bd()
        try:
            self.cursor.execute("""DELETE FROM buscar WHERE cod = ? """, (self.cod))
            self.conec.commit()
            self.desconecta_bd()
            self.select_lista()
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um item da tabela!")

    # Método que insere imagens no grafo
    def monta_caminho(self, caminho):

        lista = caminho
        for i in lista:
            if (i=='MR'):
                self.image_id1 = canvas.create_image(368,233, image=image2)#MR
            elif (i=='B6'):
                self.image_id2 = canvas.create_image(262, 257, image=image2)  # B6
            elif (i=='CE'):
                self.image_id3 = canvas.create_image(289, 174, image=image2)  # CE
            elif (i=='RD'):
                self.image_id4 = canvas.create_image(191, 187, image=image2)  # RD
            elif (i=='MD'):
                self.image_id5 = canvas.create_image(47, 187, image=image2)  # MD
            elif (i=='C'):
                self.image_id6 = canvas.create_image(310, 141, image=image2)  # C
            elif (i=='EV'):
                self.image_id32 = canvas.create_image(952, 176, image=image2)  # EV
            elif (i=='AeB6'):
                self.image_id8 = canvas.create_image(81, 267, image=image2)  # AeB6
            elif (i=='AeB7'):
                self.image_id9 = canvas.create_image(122, 305, image=image2)  # AeB7
            elif (i=='B5'):
                self.image_id10 = canvas.create_image(146, 347, image=image2)  # B5
            elif (i=='DS'):
                self.image_id11 = canvas.create_image(357, 141, image=image2)  # DS
            elif (i=='B7'):
                self.image_id12 = canvas.create_image(404, 355, image=image2)  # B7
            elif (i=='AeB9'):
                self.image_id13 = canvas.create_image(524, 305, image=image2)  # AeB9
            elif (i=='RS'):
                self.image_id14 = canvas.create_image(524, 249, image=image2)  # RS
            elif (i=='AeB8'):
                self.image_id15 = canvas.create_image(546, 220, image=image2)  # AeB8
            elif (i=='B4'):
                self.image_id16 = canvas.create_image(431, 158, image=image2)  # B4
            elif (i=='AeB3'):
                self.image_id35 = canvas.create_image(860, 72, image=image2)  # AeB3
            elif (i=='AeB5'):
                self.image_id18 = canvas.create_image(499, 169, image=image2)  # AeB5
            elif (i=='T'):
                self.image_id19 = canvas.create_image(609, 119, image=image2)  # T
            elif (i=='AeB4'):
                self.image_id20 = canvas.create_image(568, 73, image=image2)  # AeB4
            elif (i=='RG'):
                self.image_id21 = canvas.create_image(689, 200, image=image2)  # RG
            elif (i=='LPO'):
                self.image_id22 = canvas.create_image(751, 278, image=image2)  # LPO
            elif (i=='GS'):
                self.image_id23 = canvas.create_image(688, 331, image=image2)  # GS
            elif (i=='L'):
                self.image_id24 = canvas.create_image(795, 342, image=image2)  # L
            elif (i=='XP'):
                self.image_id25 = canvas.create_image(729, 464, image=image2)  # XP
            elif (i=='E/S'):
                self.image_id26 = canvas.create_image(1140, 441, image=image2)  # E/S
            elif (i=='SD'):
                self.image_id27 = canvas.create_image(998, 318, image=image2)  # SD
            elif (i=='AeB1'):
                self.image_id28 = canvas.create_image(937, 301, image=image2)  # AeB1
            elif (i=='S'):
                self.image_id29 = canvas.create_image(887, 264, image=image2)  # S
            elif (i=='B1'):
                self.image_id30 = canvas.create_image(952, 218, image=image2)  # B1
            elif (i=='AeB2'):
                self.image_id31 = canvas.create_image(896, 191, image=image2)  # AeB2
            elif (i=='E'):
                self.image_id7 = canvas.create_image(18, 318, image=image2)  # E
            elif (i=='V'):
                self.image_id33 = canvas.create_image(913, 142, image=image2)  # V
            elif (i=='B2'):
                self.image_id34 = canvas.create_image(919, 89, image=image2)  # B2
            elif (i=='B3'):
                self.image_id17 = canvas.create_image(496, 118, image=image2)  # B3
            elif (i=='M'):
                self.image_id36 = canvas.create_image(728, 36, image=image2)  # M
    # Método que limpa as imagens do grafo
    def limpa_grafo(self):

        if(self.ultima_imgs == 1):messagebox.showinfo(title="ERRO", message="Não existe um caminho a ser excluido!")
        else:
            ult_caminho = self.ultima_imgs
            for i in ult_caminho:
                if(i=='MR'):canvas.delete(self.image_id1)
                elif(i=='B6'):canvas.delete(self.image_id2)
                elif(i=='CE'):canvas.delete(self.image_id3)
                elif(i=='RD'):canvas.delete(self.image_id4)
                elif(i=='MD'):canvas.delete(self.image_id5)
                elif(i=='C'):canvas.delete(self.image_id6)
                elif(i=='EV'):canvas.delete(self.image_id32)
                elif(i=='AeB6'):canvas.delete(self.image_id8)
                elif(i=='AeB7'):canvas.delete(self.image_id9)
                elif(i=='B5'):canvas.delete(self.image_id10)
                elif(i=='DS'):canvas.delete(self.image_id11)
                elif(i=='B7'):canvas.delete(self.image_id12)
                elif(i=='AeB9'):canvas.delete(self.image_id13)
                elif(i=='RS'):canvas.delete(self.image_id14)
                elif(i=='AeB8'):canvas.delete(self.image_id15)
                elif(i=='B4'):canvas.delete(self.image_id16)
                elif(i=='AeB3'):canvas.delete(self.image_id35)
                elif(i=='AeB5'):canvas.delete(self.image_id18)
                elif(i=='T'):canvas.delete(self.image_id19)
                elif(i=='AeB4'):canvas.delete(self.image_id20)
                elif(i=='RG'):canvas.delete(self.image_id21)
                elif(i=='LPO'):canvas.delete(self.image_id22)
                elif(i=='GS'):canvas.delete(self.image_id23)
                elif(i=='L'):canvas.delete(self.image_id24)
                elif(i=='XP'):canvas.delete(self.image_id25)
                elif(i=='E/S'):canvas.delete(self.image_id26)
                elif(i=='SD'):canvas.delete(self.image_id27)
                elif(i=='AeB1'):canvas.delete(self.image_id28)
                elif(i=='S'):canvas.delete(self.image_id29)
                elif(i=='B1'):canvas.delete(self.image_id30)
                elif(i=='AeB2'):canvas.delete(self.image_id31)
                elif(i=='E'):canvas.delete(self.image_id7)
                elif(i=='V'):canvas.delete(self.image_id33)
                elif(i=='B2'):canvas.delete(self.image_id34)
                elif(i=='B3'):canvas.delete(self.image_id17)
                elif(i=='M'):canvas.delete(self.image_id36)
    #Método verifica se está vazio
    """
    def ver_vazio(self):
        if (self.origem_entry.get()=="" or self.destino_entry.get()==""):
            messagebox.showinfo(title="ERRO", message="Preencha todos os campos")
            return 1
    """
    # Métodos de busca.
    def custo_uni(self):
        if (self.ultima_imgs != 1): self.limpa_grafo()

        object = Busca_v.busca()
        self.origem = self.cb_nos.get()
        self.destino = self.cb_nos2.get()
        lista, self.custo = object.custo_uniforme(self.origem, self.destino)
        self.ultima_imgs = lista
        self.monta_caminho(lista)
        self.nome = 'Custo Uniforme'
        if (lista == 'caminho não encontrado'):
            self.caminho = lista
        else:
            self.caminho = "-".join(lista)
        self.conecta_bd()
        print(self.caminho)
        self.cursor.execute(""" INSERT INTO buscar (nome_metodo, caminho_metodo, caminho_custo) VALUES (?,?,?)""", (self.nome, self.caminho, self.custo))
        self.conec.commit()
        self.desconecta_bd()
        self.select_lista()
    def greedi(self):
        if (self.ultima_imgs != 1): self.limpa_grafo()

        object = Busca_v.busca()
        self.origem = self.cb_nos.get()
        self.destino = self.cb_nos2.get()
        lista, self.custo = object.greedy(self.origem, self.destino)
        self.ultima_imgs = lista
        self.monta_caminho(lista)
        self.nome = 'Greedy'
        if (lista == 'caminho não encontrado'):
            self.caminho = lista
        else:
            self.caminho = "-".join(lista)
        self.conecta_bd()
        print(self.caminho)
        self.cursor.execute(""" INSERT INTO buscar (nome_metodo, caminho_metodo, caminho_custo) VALUES (?,?,?)""", (self.nome, self.caminho, self.custo))
        self.conec.commit()
        self.desconecta_bd()
        self.select_lista()
    def aestrela(self):
        if (self.ultima_imgs != 1): self.limpa_grafo()

        object = Busca_v.busca()
        self.origem = self.cb_nos.get()
        self.destino = self.cb_nos2.get()
        lista, self.custo = object.a_estrela(self.origem, self.destino)
        self.ultima_imgs = lista
        self.monta_caminho(lista)
        self.nome = 'Busca A*'
        if (lista == 'caminho não encontrado'):
            self.caminho = lista
        else:
            self.caminho = "-".join(lista)
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO buscar (nome_metodo, caminho_metodo, caminho_custo) VALUES (?,?,?)""", (self.nome, self.caminho, self.custo))
        self.conec.commit()
        self.desconecta_bd()
        self.select_lista()
    def ampli(self):
        if(self.ultima_imgs != 1): self.limpa_grafo()

        object = Busca.busca()
        self.origem = self.cb_nos.get()
        self.destino= self.cb_nos2.get()

        lista = object.amplitude(self.origem, self.destino)
        self.ultima_imgs = lista
        self.monta_caminho(lista)
        self.nome = 'Amplitude'
        if (lista == 'caminho não encontrado'):
            self.caminho = lista
        else:
            self.caminho = "-".join(lista)
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO buscar (nome_metodo, caminho_metodo) VALUES (?,?)""", (self.nome, self.caminho))
        self.conec.commit()
        self.desconecta_bd()
        self.select_lista()
    def prof(self):
        if (self.ultima_imgs != 1): self.limpa_grafo()

        object = Busca.busca()
        self.origem = self.cb_nos.get()
        self.destino = self.cb_nos2.get()

        lista = object.profundidade(self.origem, self.destino)
        self.ultima_imgs = lista
        self.monta_caminho(lista)
        self.nome = 'Profundidade'
        if (lista == 'caminho não encontrado'):
            self.caminho = lista
        else:
            self.caminho = "-".join(lista)
        self.conecta_bd()
        print(self.caminho)
        self.cursor.execute(""" INSERT INTO buscar (nome_metodo, caminho_metodo) VALUES (?,?)""", (self.nome, self.caminho))
        self.conec.commit()
        self.desconecta_bd()
        self.select_lista()
    def prof_lim(self):
        if (self.ultima_imgs != 1): self.limpa_grafo()
        if(self.limite_entry.get() == ''): messagebox.showinfo(title="ERRO", message="Preencha o campo limite")
        else:
            object = Busca.busca()
            self.origem = self.cb_nos.get()
            self.destino = self.cb_nos2.get()
            self.limite = self.limite_entry.get()

            lista = object.prof_limitada(self.origem, self.destino, getint(self.limite))
            self.ultima_imgs = lista
            self.monta_caminho(lista)
            self.nome = 'Profundidade Limitada'
            if(lista == 'caminho não encontrado'): self.caminho = lista
            else: self.caminho = "-".join(lista)
            self.conecta_bd()
            print(self.limite)
            self.cursor.execute(""" INSERT INTO buscar (nome_metodo, caminho_metodo) VALUES (?,?)""", (self.nome, self.caminho))
            self.conec.commit()
            self.desconecta_bd()
            self.select_lista()
    def aprof_iter(self):
        if (self.ultima_imgs != 1): self.limpa_grafo()

        object = Busca.busca()
        self.origem = self.cb_nos.get()
        self.destino = self.cb_nos2.get()
        self.limite = 36

        lista = object.aprof_iterativo(self.origem, self.destino, self.limite)
        self.ultima_imgs = lista
        self.monta_caminho(lista)
        self.nome = 'Aprofundamento Iterativo'
        if (lista == 'caminho não encontrado'):
            self.caminho = lista
        else:
            self.caminho = "-".join(lista)
        self.conecta_bd()
        print(self.caminho)
        self.cursor.execute(""" INSERT INTO buscar (nome_metodo, caminho_metodo) VALUES (?,?)""", (self.nome, self.caminho))
        self.conec.commit()
        self.desconecta_bd()
        self.select_lista()
    def bid(self):
        if (self.ultima_imgs != 1): self.limpa_grafo()

        object = Busca.busca()
        self.origem = self.cb_nos.get()
        self.destino = self.cb_nos2.get()

        lista = object.bidirecional(self.origem, self.destino)
        self.ultima_imgs = lista
        self.monta_caminho(lista)
        self.nome = 'Bidirecional'
        if (lista == 'caminho não encontrado'):
            self.caminho = lista
        else:
            self.caminho = "-".join(lista)
        self.conecta_bd()
        print(self.caminho)
        self.cursor.execute(""" INSERT INTO buscar (nome_metodo, caminho_metodo) VALUES (?,?)""", (self.nome, self.caminho))
        self.conec.commit()
        self.desconecta_bd()
        self.select_lista()




#Chamada dos métodos
class application(Funcs):
    def __init__(self):
        self.ultima_imgs = 1
        self.root = root
        self.tela()# chama o método criado abaixo para o título.
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.widgets_frame3()
        self.montaTabelas()
        self.select_lista()
        root.mainloop()
    def tela(self):
        self.root.title("Grafo Rock in Rio")
        self.root.iconbitmap('rock.ico') #Basta jogar o caminho da imagem aqui para setar um icone
        #command=root.quit -- Sai da aplicação
        self.root.configure(background= 'lightblue')
        #self.root.geometry("1100x700")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
    def frames_da_tela(self):
        #frame 1
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness=2)
        self.frame_1.place(relx= 0.85, rely=0.001, relwidth=0.15, relheight=0.69)
        #frame 2
        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.001, rely=0.69, relwidth=0.85, relheight=0.31)
        # frame 3
        self.frame_3 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_3.place(relx=0.85, rely=0.69, relwidth=0.15, relheight=0.31)
        # frame 4
        #self.frame_4 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        #self.frame_4.place(relx=0.02, rely=0.49, relwidth=0.80, relheight=0.20)
    def widgets_frame1(self):
        #Botão Custo Uniforme
        self.bt_uniforme = Button(self.frame_1, text='Custo Uniforme', command=self.custo_uni)
        self.bt_uniforme.place(relx=0.02, rely=0.05, relwidth=0.95, relheight=0.04)

        # Botão Greedy
        self.bt_greedy = Button(self.frame_1, text='Greedy', command=self.greedi)
        self.bt_greedy.place(relx=0.02, rely=0.12, relwidth=0.95, relheight=0.04)

        # Botão A*
        self.bt_aestrela = Button(self.frame_1, text='Busca A*', command=self.aestrela)
        self.bt_aestrela.place(relx=0.02, rely=0.19, relwidth=0.95, relheight=0.04)

        # Botão Amplitude
        self.bt_ampli = Button(self.frame_1, text='Amplitude', command=self.ampli)
        self.bt_ampli.place(relx=0.02, rely=0.26, relwidth=0.95, relheight=0.04)

        # Botão Profundidade
        self.bt_prof = Button(self.frame_1, text='Profundidade', command=self.prof)
        self.bt_prof.place(relx=0.02, rely=0.33, relwidth=0.95, relheight=0.04)

        # Botão Profundidade Limitada
        self.bt_proflim = Button(self.frame_1, text='Profundidade Limitada', command=self.prof_lim)
        self.bt_proflim.place(relx=0.02, rely=0.40, relwidth=0.95, relheight=0.04)

        # Botão Aprofundamento Iterativo
        self.bt_aprofit = Button(self.frame_1, text='Aprofundamento Iterativo', command=self.aprof_iter)
        self.bt_aprofit.place(relx=0.02, rely=0.47, relwidth=0.95, relheight=0.04)

        # Botão Bidirecional
        self.bt_bidi = Button(self.frame_1, text='Bidirecional', command=self.bid)
        self.bt_bidi.place(relx=0.02, rely=0.54, relwidth=0.95, relheight=0.04)

        # Botão Excluir
        self.bt_excluir = Button(self.frame_1, text='Excluir Registro', command=self.deleta_info)
        self.bt_excluir.place(relx=0.02, rely=0.70, relwidth=0.95, relheight=0.04)

        # Botão Limpa Img
        self.bt_limpar = Button(self.frame_1, text='Limpar Imagens', command=self.limpa_grafo)
        self.bt_limpar.place(relx=0.02, rely=0.84, relwidth=0.95, relheight=0.04)

        # Botão Finalizar
        self.bt_finalizar = Button(self.frame_1, text='Finalizar Aplicação', command=self.root.quit)
        self.bt_finalizar.place(relx=0.02, rely=0.77, relwidth=0.95, relheight=0.04)
    def lista_frame2(self):
        #Criando e definindo nome para as colunas
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Método")
        self.listaCli.heading("#3", text="Caminho")
        self.listaCli.heading("#4", text="Custo Caminho")

        #Definindo tamanho para as colunas
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=10)#Para o tamanho dividir as colunas por 500, pois o espaço da tabela é sempre um número próximo de 500, por isso se somarmos o tam das colunas da 500.
        self.listaCli.column("#2", width=125)
        self.listaCli.column("#3", width=345)
        self.listaCli.column("#4", width=20)

        #Definindo a posição para a tabela
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        #Criando a barra de rolagem
        self.scroolLista = Scrollbar(self.frame_2, orient="vertical")
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
    def widgets_frame3(self):
        # Criação do label e entrada da Origem

        self.lb_origem = Label(self.frame_3, text='Origem', bg='#dfe3ee', fg='#107db2')
        self.lb_origem.place(relx=0.35, rely=0.001)
        #Criando um combobox (campo com os valores dentro já)
        listaNos = ['XP', 'M', 'AeB3', 'B2', 'V', 'AeB2', 'EV', 'B1', 'S', 'AeB1', 'SD', 'E/S','AeB4','B3','AeB5','T','B4','DS','C','CE','RD','MD','E','AeB6','AeB7','B5','B6','MR','AeB8','RS','AeB9','B7','RG','LPO','GS','L']
        self.cb_nos = ttk.Combobox(self.frame_3, values=listaNos)
        self.cb_nos.set('XP')
        self.cb_nos.place(relx=0.30, rely=0.16, relwidth=0.40)
        """
        self.origem_entry = Entry(self.frame_3)
        self.origem_entry.place(relx=0.30, rely=0.16, relwidth=0.40)
        """

        # Criação do label e entrada do Destino
        self.lb_destino = Label(self.frame_3, text='Destino', bg='#dfe3ee', fg='#107db2')
        self.lb_destino.place(relx=0.35, rely=0.31)
        self.cb_nos2 = ttk.Combobox(self.frame_3, values=listaNos)
        self.cb_nos2.set('E/S')
        self.cb_nos2.place(relx=0.30, rely=0.49, relwidth=0.40)
        '''
        self.destino_entry = Entry(self.frame_3)
        self.destino_entry.place(relx=0.30, rely=0.49, relwidth=0.40)
        '''
        # Criação do label e entrada do Destino
        self.lb_limite = Label(self.frame_3, text='Limite', bg='#dfe3ee', fg='#107db2')
        self.lb_limite.place(relx=0.35, rely=0.68)

        self.limite_entry = Entry(self.frame_3)
        self.limite_entry.place(relx=0.30, rely=0.84, relwidth=0.40)



#PRINCIPAL
application()