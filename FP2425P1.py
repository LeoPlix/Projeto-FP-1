def eh_tabuleiro(tabuleiro):
    if not isinstance(tabuleiro,tuple):  #Verifica se é tuplo
        return False
    if not 2 <= len(tabuleiro) <= 100:  #Verifica se está dentro dos valores
        return False
    for i in range(len(tabuleiro)):
        if not isinstance(tabuleiro[i], tuple):  #Verifica se dentro do tuplo há exclusivamente outros tuplos
            return False
        if not 2 <= len(tabuleiro[i]) <= 100: #Verifica se o tamanho dos subtuplos está dentro dos valores
            return False
        if i > 0 and len(tabuleiro[i-1]) != len(tabuleiro[i]):  #Verifica se todos os tuplos têm o mesmo tamanho
            return False
        for j in range(len(tabuleiro[i])):
            if not isinstance(tabuleiro[i][j], int):  #Verifica se os elementos dos tuplos são inteiros
                return False
            if not -1 <= tabuleiro[i][j] <= 1:  #Verifica se os elementos dos tuplos estão dentro dos valores
                return False
    return True
    
def eh_posicao(posicao):
    return isinstance(posicao,int) and posicao > 0

def obtem_dimensao(tabuleiro):
    return (len(tabuleiro), len(tabuleiro[0]))

def obtem_valor(tabuleiro, posicao):
    linhas = (posicao - 1) // len(tabuleiro[0])   #Para determinar em que linha está (tem o -1 porque o indez começa em 0, não em 1)
    colunas = (posicao - 1) % len(tabuleiro[0])   #Para detrminar em que coluna está
    return tabuleiro[linhas][colunas]  

def obtem_coluna(tabuleiro, posicao):
    coluna = (posicao - 1) % len(tabuleiro[0])  # Caluclar o número da coluna
    tuplo = ()
    for i in range(len(tabuleiro)):
        tuplo += (i * len(tabuleiro[0]) + coluna + 1,)  # Calcular a posição e adicionar ao tuplo
    return tuplo

def obtem_linha(tabuleiro, posicao):
    linha = (posicao - 1) // len(tabuleiro[0])  
    tuplo = ()
    for i in range(1, len(tabuleiro[0]) + 1):
        tuplo += (linha * len(tabuleiro[0]) + i,)  # Calcular a posiçãp e adicionar ao tuplo
    return tuplo

def obtem_diagonais(tabuleiro, posicao):
    linhas = len(tabuleiro)
    if linhas > 0:
         colunas = len(tabuleiro[0])  #Garantir que não dá IndexError
    else:
        colunas = 0
    
    linha, coluna = (posicao - 1) // colunas, (posicao - 1) % colunas    #Ex.: linha = 1 e coluna = 2 para posicao = 5 de tabuleiro 2x3 (para o Index estar correto)
    diagonal, antidiagonal = (), ()
    i,j = linha,coluna
    
    # Sentido cima/esquerda (diagonal)
    while i >= 0 and j >= 0:
        diagonal += ((i * colunas + j + 1),)  
        i -= 1
        j -= 1
    
    # Sentido baixo/direita (diagonal)
    i, j = linha + 1, coluna + 1  #Para garantir que não acrescenta a variável posicao de novo
    while i < linhas and j < colunas:
        diagonal += ((i * colunas + j + 1),) 
        i += 1
        j += 1

    i, j = linha, coluna  # Refazer o processo mas com antidiagonais
    # Sentido cima/direita (antidiagonal)
    while i >= 0 and j < colunas:
        antidiagonal += ((i * colunas + j + 1),) 
        i -= 1
        j += 1
    
    # Sentido baixo/esquerda (antidiagonal)
    i, j = linha + 1, coluna - 1
    while i < linhas and j >= 0:
        antidiagonal += ((i * colunas + j + 1),)  
        i += 1
        j -= 1
    
    return (tuple(sorted(diagonal)), tuple(reversed(sorted(antidiagonal)))) #ordenar as diagonais e antidiagonais

def tabuleiro_para_str(tabuleiro):
    tab_desenho = ""
    contagem = 0
    for i in tabuleiro:
        tab_desenho += "+" + "---+"*(len(tabuleiro[0])-1)   #Desenhar cada linha do tabuleiro
        for j in i:
            if j == 1:
                tab_desenho = tab_desenho[:contagem] + "X" + tab_desenho[contagem+1:]  #Para colocar o X no sítio certo
                contagem += 4
            elif j == -1:
                tab_desenho = tab_desenho[:contagem] + "O" + tab_desenho[contagem+1:]   #Para colocar o O no sítio certo
                contagem += 4
            else:
                contagem += 4   #Para passar para a próxima posição
                
        if tabuleiro[len(tabuleiro)-1] != i:
            tab_desenho += "\n" + "|" + "   |"* (len(tabuleiro[0])-1) + "\n"   #Para desenhar as colunas
        contagem += 4*(len(tabuleiro[0])-1)   #Passar para a linha de baixo
    return tab_desenho

def eh_posicao_valida(tabuleiro, posicao):
    return eh_posicao(posicao) and posicao <= len(tabuleiro)*len(tabuleiro[0])


def eh_posicao_livre(tabuleiro, posicao):
    if eh_tabuleiro(tabuleiro) and eh_posicao_valida(tabuleiro, posicao):
        return obtem_valor(tabuleiro, posicao) == 0
    else:
        raise ValueError("argumentos inválidos")

def obtem_posicoes_livres(tabuleiro):
    if not eh_tabuleiro(tabuleiro):
        raise ValueError("obtem_posicoes_livres: argumento invalido")
    else:
        livres = ()   #Tuplo para guardar as posições livres
        posicoes = 1
        for i in tabuleiro:
            for j in i:
                if eh_posicao_livre(tabuleiro, posicoes):
                    livres += (posicoes,)  #Adicionar a posição livre ao tuplo
                posicoes += 1
        return livres
    
def obtem_posicoes_jogador(tabuleiro, jogador):
    if eh_tabuleiro(tabuleiro) and isinstance(jogador,int) and -1 <= jogador <= 1:
        pos_jogador = ()  #Tuplo para guardar as posições do jogador
        posicoes = 1
        for i in tabuleiro:
            for j in i:
                if j == jogador:
                    pos_jogador += (posicoes,)   #Adicionar as posiçoes com o valor do jogador ao tuplo
                posicoes += 1
        return pos_jogador
    else:
        raise ValueError("obtem_posicoes_jogador: argumentos invalidos")
    
def obtem_posicoes_adjacentes(tabuleiro, posicao):
    if eh_tabuleiro(tabuleiro) and eh_posicao_valida(tabuleiro, posicao):
        num_linhas = len(tabuleiro)
        num_colunas = len(tabuleiro[0])
        linha = (posicao - 1) // num_colunas
        coluna = (posicao - 1) % num_colunas
        adjacentes = ()
        
        # Direções possíveis para encontrar as adjacências (horizontal, vertical e diagonal/antidiagonal)
        direcoes = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        
        for x, y in direcoes:
            nova_linha = linha + x
            nova_coluna = coluna + y
            # Verifica se a nova posição está dentro dos limites do tabuleiro
            if 0 <= nova_linha < num_linhas and 0 <= nova_coluna < num_colunas:
                adj_pos = nova_linha * num_colunas + nova_coluna + 1 
                adjacentes += (adj_pos, )
        
        # Retorna as posições adjacentes ordenadas
        return tuple(sorted(adjacentes))

    else:
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")

def ordena_posicoes_tabuleiro(tabuleiro, t):
    if eh_tabuleiro(tabuleiro) and isinstance(t, tuple):
        m, n = obtem_dimensao(tabuleiro)[0], obtem_dimensao(tabuleiro)[1]
        elem_central = (m//2) * n + (n//2) + 1
        
        def distancia_centro(centro, elemento):
            linha_centro = (centro - 1)//n
            coluna_centro = (centro - 1)%n
            linha_elemento = (elemento - 1) // n
            coluna_elemento = (elemento - 1) % n
            return max(abs(linha_elemento - linha_centro), abs(coluna_elemento - coluna_centro))
        
        distancias = ()
        for elemento in t:
            distancias += ((elemento, distancia_centro(elem_central, elemento)),)
            
        # Ordena por distância ao centro, e em caso de empate, por posição original
        distancias = sorted(distancias, key=lambda x: (x[1], x[0]))
        
        distancias_total = ()
        for elemento in distancias:
            distancias_total += (elemento[0],)
            
        return distancias_total
        
        #distancias = ()
        #for elemento in t:
            #distancias += ((elemento, distancia_centro(elem_central, elemento)),)
            
        #distancias = tuple(sorted(distancias, key=lambda x: (x[1], x[0])))
        
        #distancias_total = ()
        #for elemento in distancias:
            #distancias_total += (elemento[0],)
            
        #return distancias_total

    else:
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
        

        
def marca_posicao(tabuleiro, posicao, inteiro):
    if eh_tabuleiro(tabuleiro) and eh_posicao_livre(tabuleiro, posicao) and (inteiro == 1 or inteiro == -1):
        num_colunas = len(tabuleiro[0])
        linha = (posicao - 1) // num_colunas
        coluna = (posicao - 1) % num_colunas
    
        tab_marcado = ()  # Tuplo novo com o novo valor que queremos
        for i in range(len(tabuleiro)):  # Cria um novo tuplo de tabuleiro marcando a posição com o inteiro dado (jogador)
            nova_linha = ()
            for j in range(len(tabuleiro[i])):
                if i == linha and j == coluna:
                    nova_linha += (inteiro,)  # Marca a posição com o jogador
                else:
                    nova_linha += (tabuleiro[i][j],) # Mantém o valor original
            tab_marcado += (nova_linha,) # Adiciona a nova linha ao tuplo

        return tab_marcado
    
    else:
        raise ValueError('marca_posicao: argumentos invalidos')
    
def verifica_k_linhas(tabuleiro, posicao, valor, consecutivos):
    if eh_tabuleiro(tabuleiro) and (-1 == valor or valor == 1) and 0 < consecutivos and isinstance(consecutivos, int):
        if not eh_posicao_valida(tabuleiro, posicao) or obtem_valor(tabuleiro, posicao) != valor:
            return False
        
        linha = obtem_linha(tabuleiro, posicao)
        coluna = obtem_coluna(tabuleiro, posicao)
        diag = obtem_diagonais(tabuleiro, posicao)
        
        colunas_cons = conta_consecutivos(tabuleiro, posicao, coluna, valor)
        linhas_cons = conta_consecutivos(tabuleiro, posicao, linha, valor)
        diag_cons = conta_consecutivos(tabuleiro, posicao, diag[0], valor)
        antidiag_cons = conta_consecutivos(tabuleiro, posicao, diag[1], valor)
        
        if colunas_cons >= consecutivos or linhas_cons >= consecutivos or diag_cons >= consecutivos or antidiag_cons >= consecutivos:
            return True
        else:
            return False
    
    else:
        raise ValueError("verifica_k_linhas: argumentos invalidos")
 
"""Função auxiliar para contar o número de peças consecutivas"""           
def conta_consecutivos(tabuleiro,posicao, tuplo1, valor):
    contador = 0
    cons_max = 0
    for i in tuple(sorted(tuplo1)):
        if i < posicao:
            if obtem_valor(tabuleiro, i) == valor:
                contador += 1
                if contador > cons_max:
                    cons_max = contador
            else:
                contador = 0
                cons_max = 0
        if i >= posicao:
            if obtem_valor(tabuleiro, i) == valor:
                contador += 1
                if contador >= cons_max:
                    cons_max = contador
            else:
                contador = 0
                break
    return cons_max


def eh_fim_jogo(tabuleiro, consecutivos):
    if eh_tabuleiro(tabuleiro) and isinstance(consecutivos, int) and consecutivos > 0:
        cont_pos_livres = 0
        for i in range(1, len(tabuleiro)*len(tabuleiro[0])+1):
            if obtem_valor(tabuleiro, i) == 0:
                cont_pos_livres += 1
            
            else:  
                if verifica_k_linhas(tabuleiro, i, obtem_valor(tabuleiro, i), consecutivos):
                    return True
                    
        if cont_pos_livres == 0:
            return True

        return False
    else:
        raise ValueError("eh_fim_jogo: argumentos invalidos")

def escolhe_posicao_manual(tabuleiro):
    if eh_tabuleiro(tabuleiro):
        posicao = int(input("Turno do jogador. Escolha uma posicao livre: "))
        if eh_posicao_valida(tabuleiro, posicao):
            if eh_posicao_livre(tabuleiro, posicao):
                return posicao
            else:
                return escolhe_posicao_manual(tabuleiro)
        else:
            return escolhe_posicao_manual(tabuleiro)
    else:
        raise ValueError("escolhe_posicao_manual: argumento invalido")
    
def escolhe_posicao_auto(tabuleiro, valor, posicao, dificuldade):
    if eh_tabuleiro(tabuleiro) and isinstance(valor, int) and -1 <= valor <= 1 and eh_posicao_valida(tabuleiro,posicao) and dificuldade in ("facil", "normal", "dificil"):
        if eh_posicao_livre(tabuleiro, posicao):
            if dificuldade == "facil":
                return escolhe_posicao_auto_facil(tabuleiro, valor)
            #elif dificuldade == "normal":
                #return escolhe_posicao_auto_normal(tabuleiro, valor)
            #elif dificuldade == "dificil":
                #return escolhe_posicao_auto_dificil(tabuleiro, valor)
    else:
        raise ValueError("escolhe_posicao_auto: argumentos invalidos")
            
def escolhe_posicao_auto_facil(tabuleiro, valor):
    valor_simetrico = -1 if valor == 1 else 1
        
    for i in range(1, len(tabuleiro)*len(tabuleiro[0]) + 1):
        if obtem_valor(tabuleiro, i) == valor_simetrico:
            adjacentes = obtem_posicoes_adjacentes(tabuleiro, i)
            for adj in range(len(adjacentes) - 1):
                if adjacentes[adj] < i and adjacentes[adj + 1] > i:
                    return adjacentes[adj]
                
    for i in range(1, len(tabuleiro) + 1):
        if eh_posicao_livre(tabuleiro, i):
            return i

tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1))

print(escolhe_posicao_auto(tab, -1, 3, 'facil'))
print(verifica_k_linhas(tab, 6, -1, 7))
print(ordena_posicoes_tabuleiro(tab, tuple(range(1,13))))

        