"""
    Função que prevê todos os erros ou exceções que podem existir no tabuleiro dado, returnando False se existir algum
    erro e impossibilitando assim a execução do programa.
    
"""

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
    
"""
    Funções básicas que verificam se a posição dada é válida e a dimensão m x n do tabuleiro.   
    
"""
def eh_posicao(posicao):
    if isinstance(posicao,int) and 0 < posicao < 10000:  #10000 é o tamanho de uma matriz 100x100
        return True
    else:
        return False

def obtem_dimensao(tabuleiro):
    return (len(tabuleiro), len(tabuleiro[0]))

"""
    Funções de obtenção de valores, colunas, linhas e diagonais/antidiagonais de uma posição dada.
    
"""
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

"""
    Função mais complexa de obtenção de diagonais e antidiagonais de uma posição dada. Esta função é dividida em duas partes, a parte do
    cálculo das diagonais e a parte do cálculo das antidiagonais, que são feitas em simultâneo a partir de whiles que percorrem
    a extensão toda do tabuleiro e adicionam as posições ao tuplo correspondente. No final, recorre-se ao método sorted para ordenar a diagonal e
    às antidionais, para além do sorted, utiliza-se o método reversed para inverter a ordem dos elementos e estar no sentido certo.
    
"""
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

"""
    Função que desenha o tabuleiro, colocando os valores de X e O nas posições corretas e desenhando as linhas e colunas do tabuleiro. 
    A mesma é feita através de um ciclo for que percorre o tabuleiro e vai desenhando o jogo conforme o tabuleiro fornecido, ao que se
    encontrar os valores de 1 e -1, coloca-se X e O respetivamente, e caso contrário, deixa-se como estava originalmente.
    
""" 
def tabuleiro_para_str(tabuleiro):
    tab_desenho = ""
    tab_desenho_final = ""
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
                

        tab_desenho += "\n" + "|" + "   |"* (len(tabuleiro[0])-1) + "\n"    #Para desenhar as colunas
        contagem += 4*(len(tabuleiro[0])-1)   #Passar para a linha de baixo
        
    tab_desenho_final = tab_desenho[:len(tab_desenho)-4*(len(tabuleiro[0])-1)-3]  #Para desenhar a última linha do tabuleiro
    return tab_desenho_final

"""
    Funções auxiliares básicas para uma melhor abstração procedimental do código
    
"""
def eh_posicao_valida(tabuleiro, posicao):
    if not eh_tabuleiro(tabuleiro) or not isinstance(posicao, int):
        raise ValueError("eh_posicao_valida: argumentos invalidos")
    return eh_posicao(posicao) and posicao <= len(tabuleiro)*len(tabuleiro[0])


def eh_posicao_livre(tabuleiro, posicao):
    if eh_tabuleiro(tabuleiro) and eh_posicao_valida(tabuleiro, posicao):
        return obtem_valor(tabuleiro, posicao) == 0
    else:
        raise ValueError("eh_posicao_livre: argumentos invalidos")

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
    if eh_tabuleiro(tabuleiro) and isinstance(jogador,int) and jogador in (-1,1):
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
    
"""
    Função que cria um tuplo com as posições adjacentes à posição dada, ordenadas por ordem crescente.
    De modo a fazer isso, a função converte a posição linear em coordenadas (linha, coluna), define direções possíveis,
    calcula novas posições e verifica se estas estão dentro dos limites do tabuleiro. Caso estejam, adiciona-as ao tuplo das adjacentes.
    
"""
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

"""
    Função que, dado um tabuleiro e um tuplo de posições, ordena as posições de acordo com a distância ao centro do tabuleiro.
    Começa por calcular a posição central do tabuleiro, e de seguida, calcula a distância de cada posição ao centro com recurso
    a uma função auxiliar.  Após isso, cria-se tuplos (posição, distância ao centro da respeitva posição) e 
    usa-se uma função lambda para organizar os mesmos por distância ao centro e, em caso de empate, por posição original.
    No fim, faz-se um novo tuplo apenas com as distâncias ao centro, por fim ordenadas.
    
"""
def ordena_posicoes_tabuleiro(tabuleiro, t):
    if eh_tabuleiro(tabuleiro) and isinstance(t, tuple):
        for i in range(len(t)-1):
            if not isinstance(t[i], int):      # Verifica se todos os elementos de t são inteiros
                raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
            
        m, n = obtem_dimensao(tabuleiro)[0], obtem_dimensao(tabuleiro)[1]
        elem_central = (m//2) * n + (n//2) + 1     # Calcula a posição central do tabuleiro
        
        # Função para calcular a distância de um elemento ao centro
        def distancia_centro(centro, elemento):
            linha_centro = (centro - 1)//n
            coluna_centro = (centro - 1)%n
            linha_elemento = (elemento - 1) // n
            coluna_elemento = (elemento - 1) % n
            return max(abs(linha_elemento - linha_centro), abs(coluna_elemento - coluna_centro))
        
        distancias = ()
        for elemento in t:
            distancias += ((elemento, distancia_centro(elem_central, elemento)),)  # Faz um tuplo com a posição e a sua respeitva distância ao centro
            
        # Ordena por distância ao centro, e em caso de empate, por posição original
        distancias = sorted(distancias, key=lambda x: (x[1], x[0]))
        
        # Extrai os elementos ordenados
        distancias_total = ()
        for elemento in distancias:
            distancias_total += (elemento[0],)

        return distancias_total

    else:
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
        
"""
    Função que marca uma posição com um inteiro, que representa o jogador que marcou a posição. Ela cria um novo tabuleiro,
    ao que o mesmo é composto por todos os elementos do tabuleiro original, exceto na posição dada, que é substituída
    pelo inteiro correspondente ao valor do jogador
    
"""      
def marca_posicao(tabuleiro, posicao, inteiro):
    if eh_tabuleiro(tabuleiro) and inteiro in (-1, 1) and eh_posicao_valida(tabuleiro, posicao):
        if eh_posicao_livre(tabuleiro, posicao):
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
 
"""
    Função auxiliar para contar o número de peças consecutivas
    
"""           
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
        posicao = eval(input("Turno do jogador. Escolha uma posicao livre: "))
        if isinstance(posicao, int) and eh_posicao_valida(tabuleiro, posicao):
            if eh_posicao_livre(tabuleiro, posicao):
                return posicao
            else:
                return escolhe_posicao_manual(tabuleiro)
        else:
            return escolhe_posicao_manual(tabuleiro)
    else:
        raise ValueError("escolhe_posicao_manual: argumento invalido")
    
def escolhe_posicao_auto(tabuleiro, valor, consecutivos, dificuldade):
    if eh_tabuleiro(tabuleiro) and isinstance(valor, int) and -1 <= valor <= 1 and consecutivos > 0 and dificuldade in ("facil", "normal", "dificil"):
        if not eh_fim_jogo(tabuleiro, consecutivos):
            if dificuldade == "facil":
                return escolhe_posicao_auto_facil(tabuleiro, valor, consecutivos)
            if dificuldade == "normal":
                return escolhe_posicao_auto_normal(tabuleiro, valor, consecutivos)
            if dificuldade == "dificil":
                return escolhe_posicao_auto_dificil(tabuleiro, valor, consecutivos)
    else:
        raise ValueError("escolhe_posicao_auto: argumentos invalidos")
            
def escolhe_posicao_auto_facil(tabuleiro, valor, consecutivos):
        
    posicoes_validas = ()
    posicoes_livres = 0
        
    for i in range(1, len(tabuleiro) * len(tabuleiro[0]) + 1):
        if obtem_valor(tabuleiro, i) == 0:
            posicoes_livres += 1
        if obtem_valor(tabuleiro, i) == valor:
            adjacentes = obtem_posicoes_adjacentes(tabuleiro, i)
            for adj in adjacentes:
                if eh_posicao_livre(tabuleiro, adj): 
                    posicoes_validas += (adj,)

    if posicoes_validas:
        return ordena_posicoes_tabuleiro(tabuleiro, posicoes_validas)[0]
    
    if len(posicoes_validas) == 0:
        return ordena_posicoes_tabuleiro(tabuleiro, obtem_posicoes_livres(tabuleiro))[0]
    
    if posicoes_livres == len(tabuleiro) * len(tabuleiro[0]):
        return ordena_posicoes_tabuleiro(tabuleiro, obtem_posicoes_livres(tabuleiro))[0]
    
    for i in range(1, len(tabuleiro) * len(tabuleiro[0]) + 1):
        if eh_posicao_livre(tabuleiro, i):
            return i

def escolhe_posicao_auto_normal(tabuleiro, valor, consecutivos):
    posicoes_l = ()
    posicoes_adv = ()
    posicoes_livres = obtem_posicoes_livres(tabuleiro)
    
    for l in range(consecutivos, 0, -1):
        for posicao in posicoes_livres:
            tabuleiro_novo = marca_posicao(tabuleiro, posicao, valor)
            if verifica_k_linhas(tabuleiro_novo, posicao, valor, l):
                posicoes_l += (posicao,)
            
            tabuleiro_novo = marca_posicao(tabuleiro, posicao, -valor)
            if verifica_k_linhas(tabuleiro_novo, posicao, -valor, l):
                posicoes_adv += (posicao,)
        if len(posicoes_l) != 0:
            return ordena_posicoes_tabuleiro(tabuleiro, posicoes_l)[0]
        if len(posicoes_adv) != 0:
            return ordena_posicoes_tabuleiro(tabuleiro, posicoes_adv)[0]


def escolhe_posicao_auto_dificil(tabuleiro, valor, consecutivos):
    
    def simulacao(tabuleiro, valor):
        tabuleiro_atual = tabuleiro
        jogada_atual = -valor
        posicao_passada = 0
        
        while not eh_fim_jogo(tabuleiro_atual, consecutivos):
            posicao_sim = escolhe_posicao_auto(tabuleiro_atual, jogada_atual, consecutivos, "normal")
            tabuleiro_atual = marca_posicao(tabuleiro_atual, posicao_sim, jogada_atual)
            jogada_atual = -jogada_atual
            
            if len(obtem_posicoes_livres(tabuleiro_atual)) == 0:
                return "EMPATE"
            if verifica_k_linhas(tabuleiro_atual, posicao_sim, valor, consecutivos):
                return "VITÓRIA"
            if verifica_k_linhas(tabuleiro_atual, posicao_sim, -valor, consecutivos):
                return "DERROTA"
            
    tuplo_jogador = ()
    tuplo_adv = ()
    posicoes_livres = obtem_posicoes_livres(tabuleiro)
    
    if not eh_fim_jogo(tabuleiro, consecutivos):
        for i in posicoes_livres:
                tabuleiro_novo = marca_posicao(tabuleiro, i, valor)
                if verifica_k_linhas(tabuleiro_novo, i, valor, consecutivos):
                    tuplo_jogador += (i,)
                    
        if len(tuplo_jogador) != 0:
            return ordena_posicoes_tabuleiro(tabuleiro, tuplo_jogador)[0]
                
        for i in posicoes_livres:
                tabuleiro_novo = marca_posicao(tabuleiro, i, -valor)
                print(tabuleiro_novo)
                if verifica_k_linhas(tabuleiro_novo, i, -valor, consecutivos):
                    tuplo_adv += (i,)
                    
        if len(tuplo_adv) != 0:
            return ordena_posicoes_tabuleiro(tabuleiro, tuplo_adv)[0]
                
        vitoria = ()
        empate = ()

        for posicao in posicoes_livres:
            tabuleiro_novo = marca_posicao(tabuleiro, posicao, valor)
            sim = simulacao(tabuleiro, valor)
            if sim == "VITÓRIA":
                vitoria += (posicao,)
            elif sim == "EMPATE":
                empate += (posicao,)
        print(empate)
        
        # Prioridade: vitória > empate > qualquer posição livre
        if len(vitoria) != 0:
            return ordena_posicoes_tabuleiro(tabuleiro, vitoria)[0]
        if len(empate) != 0:
            return ordena_posicoes_tabuleiro(tabuleiro, empate)[0]
       
       
def jogo_mnk(tuplo, valor, dificuldade):
    if len(tuplo) == 3 and isinstance(valor, int) and valor in (-1,1) and dificuldade in ("facil", "normal", "dificil"):
        linhas_tabuleiro = tuplo[0]
        colunas_tabuleiro = tuplo[1]
        tabuleiro = ((0,) * colunas_tabuleiro,) * linhas_tabuleiro
        tabuleiro_atual = tabuleiro
        tabuleiro_desenho = tabuleiro_para_str(tabuleiro_atual)
        
        if valor == 1:
            print(f"Bem-vindo ao JOGO MNK.\nO jogador joga com \'X\'\n{tabuleiro_desenho}\n")
        else:
            posicao_maquina = escolhe_posicao_auto(tabuleiro, valor, tuplo[2], dificuldade)
            print(posicao_maquina)
            tabuleiro_atual = marca_posicao(tabuleiro, posicao_maquina, -valor)
            print(f"Bem-vindo ao JOGO MNK.\nO jogador joga com \'O\'\n{tabuleiro_desenho}\n")

        return resto_mnk(tabuleiro_atual, valor, dificuldade)
    
def resto_mnk(tabuleiro, valor, dificuldade):
    while not eh_fim_jogo(tabuleiro, 3):
        jogada_humana = escolhe_posicao_manual(tabuleiro)
        tabuleiro = marca_posicao(tabuleiro, jogada_humana, valor)
        print(tabuleiro_para_str(tabuleiro))
        
        if verifica_k_linhas(tabuleiro, jogada_humana, valor, 3):
            return "Vitória"
        
        if eh_fim_jogo(tabuleiro, 3):
            break
        
        # Jogada da máquina
        jogada_maquina = escolhe_posicao_auto(tabuleiro, -valor, 3, dificuldade)
        tabuleiro = marca_posicao(tabuleiro, jogada_maquina, -valor)
        print(f"Turno do computador ({dificuldade})")
        print(tabuleiro_para_str(tabuleiro))
        
        if verifica_k_linhas(tabuleiro, jogada_maquina, -valor, 3):
            return "Derrota"
        
        if eh_fim_jogo(tabuleiro, 3):
            break
    
    return "Empate"
