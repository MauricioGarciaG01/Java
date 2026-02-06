from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk() #variavel do seu gosto, aqui ela recebe a tela que abre, mas temos que colocar num loop, se não ela abre e fecha rápido.

class Funcs(): #Criando as funções dos botões
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.tel_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def conecta_bd(self):
        self.conec = sqlite3.connect("clientes.bd")
        self.cursor = self.conec.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conec.close(); print("Desconectando ao banco de dados")
    def montaTabelas(self):
        self.conecta_bd()
        #Criando tabela
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS clientes(
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        #Dando o commit para validar a informação, seria tipo o execute.
        self.conec.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def add_cliente(self):
        #self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.tel = self.tel_entry.get()
        self.cidade = self.cidade_entry.get()
        self.conecta_bd()
        #INSERT
        #Programando para poder inserir os valores, colocamos "?" para inserir ao digitar, já que não sabemos o que vai ser inserido.
        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade) VALUES (?, ?, ?)""", (self.nome, self.tel, self.cidade))#o cod vai ser inserido auto
        self.conec.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    #SELECT - agora é pra exibir os dados.
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" 
        SELECT cod, nome_cliente, telefone, cidade 
        FROM clientes
        ORDER BY cod;   
        """)#O "ASC" é em ordem alfabética. E tomar cuidado no SELECT da nossa VIEW, pois o número de selects tem que ser igual ao número de colunas que temos, então pegaremos até o cod.
        #Adicionando o SELECT para a tabela do frame_2.
        for i in lista:
            self.listaCli.insert("", END, values=i) #OBS: listaCli é o nosso - ttk.Treeview(tabela)
        self.desconecta_bd()

class application(Funcs): #Nos parametros tem que dizer que ele vai usar as funções da nossa classe "Funcs".
    def __init__(self):
        self.root = root
        self.tela()# chama o método criado abaixo para o título.
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background= 'lightblue')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
    def frames_da_tela(self):
        #frame 1
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness=2)
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        #frame 2
        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self):
        #Botão Limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Novo
        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botão Apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        #Criação do label e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        # Criação do label e entrada do nome
        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        # Criação do label e entrada do telefone
        self.lb_tel = Label(self.frame_1, text='Telefone', bg='#dfe3ee', fg='#107db2')
        self.lb_tel.place(relx=0.05, rely=0.6)

        self.tel_entry = Entry(self.frame_1)
        self.tel_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        # Criação do label e entrada da cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1, relief='groove')
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    def lista_frame2(self):
        #Criando e definindo nome para as colunas
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")
        #Definindo tamanho para as colunas
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)#Para o tamanho dividir as colunas por 500, pois o espaço da tabela é sempre um número próximo de 500, por isso se somarmos o tam das colunas da 500.
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)
        #Definindo a posição para a tabela
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        #Criando a barra de rolagem
        self.scroolLista = Scrollbar(self.frame_2, orient="vertical")
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)

application() #chama o método que exibe tela.