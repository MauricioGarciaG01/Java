class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai = pai
        self.estado = estado
        self.valor1 = valor1
        self.valor2 = valor2
        self.anterior = anterior
        self.proximo = proximo


class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, st, v1, v2, p):
        novo_no = No(p, st, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, st, v1, v2, p):

        novo_no = No(p, st, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
        self.tail = novo_no

    # INSERE NO FIM DA LISTA
    def inserePos_X(self, s, v1, v2, p):

        # se lista estiver vazia
        if self.head is None:
            self.inserePrimeiro(s, v1, v2, p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break

            if atual == self.head:
                self.inserePrimeiro(s, v1, v2, p)
            else:
                if atual is None:
                    self.insereUltimo(s, v1, v2, p)
                else:
                    novo_no = No(p, s, v1, v2, None, None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    # RETORNA O PRIMEIRO DA LISTA
    def primeiro(self):
        return self.head

    # RETORNA O ÚLTIMO DA LISTA
    def ultimo(self):
        return self.tail

    # VERIFICA SE LISTA ESTÁ VAZIA
    def vazio(self):
        if self.head is None:
            return True
        else:
            return False

    # EXIBE O CONTEÚDO DA LISTA
    def exibeLista(self):

        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.estado)
            temp.append(aux.valor1)
            temp.append(aux.valor2)
            str.append(temp)
            aux = aux.proximo

        return str

    # EXIBE O CAMINHO ENCONTRADO
    def exibeCaminho(self):

        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        caminho = caminho[::-1]
        return caminho

    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL)
    def exibeCaminho1(self, valor):

        atual = self.head
        while atual.estado != valor:
            atual = atual.proximo

        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho

    def exibeCaminho2(self, s, v1):

        atual = self.tail

        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior

        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho


class busca(object):

    # BUSCA CUSTO UNIFORM
    def custo_uniforme(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeCaminho2(atual.estado, atual.valor1)
                # print(l2.exibeLista())
                # print(l1.exibeLista())
                return caminho, atual.valor2

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]
                v1 = v2

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= v1:
                            flag1 = False
                        else:
                            visitado[j][1] = v1
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)

        return "Caminho não encontrado"
    #BUSCA COM O GREEDY
    def greedy(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeCaminho2(atual.estado, atual.valor1)
                # print(l2.exibeLista())
                # print(l1.exibeLista())
                return caminho, atual.valor2

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]
                v1 = h[nos.index(destino)][i]

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= v1:
                            flag1 = False
                        else:
                            visitado[j][1] = v1
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)

        return "Caminho não encontrado"

    #BUSCA COM O ESTRELA
    def a_estrela(self, inicio, fim):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeCaminho2(atual.estado, atual.valor1)
                # print(l2.exibeLista())
                # print(l1.exibeLista())
                return caminho, atual.valor2

            ind = nos.index(atual.estado)
            for i in range(len(grafo[ind])):
                novo = grafo[ind][i][0]

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + grafo[ind][i][1]
                v1 = h[nos.index(destino)][i] + v2

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= v1:
                            flag1 = False
                        else:
                            visitado[j][1] = v1
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo, v1, v2, atual)
                    l2.inserePos_X(novo, v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)

        return "Caminho não encontrado"

"""
********************************************************************
                     PROBLEMA: MAPA DO ROCK IN RIO
********************************************************************
"""
nos = ["E/S","XP","SD","AeB1","S","B1","EV","AeB2","V","B2","AeB3","M",
       "AeB4","T","B3","AeB5","B4","DS","C","CE","RD","MD","AeB6","E",
       "AeB7","B5","B6","MR","AeB8","RS","AeB9","B7","RG","LPO","GS","L"]

grafo = [
            [["XP",350],["SD",250]],#E/S(Entrada e saída)
            [["E/S",350]],#XP(Game Experience)
            [["E/S",250],["AeB1",50]],#SD(Street Dance)
            [["SD",50],["S",52]],#AeB1(Alimentos e Bebidas 1)
            [["AeB1",52],["L",71],["LPO",71],["B1",55]],#S(Sunset)
            [["S",55],["EV",20]],#B1(Banheiros 1)
            [["B1",20],["AeB2",30]],#EV(Entrada/Saída VIP)
            [["EV",30],["V",10]],#AeB2(Alimentos e Bebidas 2)
            [["AeB2",10],["B2",30]],#V(Área VIP)
            [["V",30],["AeB3",30]],#B2(Banheiros 2)
            [["B2",30],["M",115]],#AeB3(Alimentos e Bebidas 3)
            [["AeB3",115],["AeB4",150]],#M(Mundo)
            [["M",150],["T",60],["B3",65]],#AeB4(Alimentos e Bebidas 4)
            [["AeB4",60]],#T(Tirolesa)
            [["AeB5",65],["B4",65],["AeB4",65]],#B3(Banheiros 3)
            [["B3",65],["B4",65]],#AeB5(Alimentos e Bebidas 5)
            [["B3",65],["AeB5",65],["DS",66],["MR",80]],#B4
            [["B4",66],["C",20]],#DS(Digital Stage)
            [["DS",20],["CE",15]],#C(Capela
            [["C",15],["RD",30]],#CE(Caixa Eletrônico)
            [["CE",30],["MR",80],["MD",100]],#RD(Rock District)
            [["RD",100],["AeB6",8],["E",17]],#MD(Mega Drop)
            [["MD",8],["E",30],["AeB7",70]],#AeB6(Alimentos e Bebidas 6)
            [["MD",17],["AeB6",30],["AeB7",56]],#E(Eletronica)
            [["AeB6",70],["E",56],["B5",15],["B6",75]],#AeB7(Alimentos e Bebidas 7)
            [["AeB7",15]],#B5(Banheiros 5)
            [["AeB7",75],["MR",50]],#B6(Banheiros 6)
            [["B6",50],["AeB8",89],["RD",80],["B4",80]],#MR(Montanha Russa)
            [["MR",89],["RS",100],["RG",56]],#AeB8(Alimentos e Bebidas 8)
            [["AeB8",100],["AeB9",8]],#RS(Rock Street África)
            [["B7",30],["RS",8]],#AeB9(Alimentos e Bebidas 9)
            [["AeB9",30]],#B7(Banheiros 7)
            [["AeB8",56],["LPO",57]],#RG(Roda Gigante)
            [["RG",57],["GS",65],["L",62],["S",71]],#LPO(Loja de Produtos Oficiais)
            [["LPO",65],["L",60]],#GS(Gourmet Square)
            [["GS",60],["LPO",62],["S",71]]#L(Lounge)
        ]

# PROGRAMA PRINCIPAL

sol = busca()
caminho = []

h = []

for i in range(len(nos)):
    linha=[]
    for j in range(len(nos)):
        if i == j:
            v = 0
        else:
            c,v = sol.custo_uniforme(nos[i], nos[j])
        linha.append(v*0.9)
    h.append(linha)

print(h)


origem = "E/S"
destino = "M"

caminho, custo = sol.custo_uniforme(origem, destino)
print("\nCusto Unfirme:", caminho)
print("Custo do caminho:", custo)

caminho, custo = sol.greedy(origem, destino)
print("\nCusto Unfirme:", caminho)
print("Custo do caminho:", custo)

caminho, custo = sol.a_estrela(origem, destino)
print("\nCusto Unfirme:", caminho)
print("Custo do caminho:", custo)