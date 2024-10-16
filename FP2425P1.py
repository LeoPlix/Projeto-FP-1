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
    if type(posicao) == int and 0 < posicao < 10000:  #10000 é o tamanho de uma matriz 100x100
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

"""
    Função que verifica se existem k peças consecutivas do mesmo jogador numa linha, coluna, diagonal ou antidiagonal.
    A função utiliza uma função auxiliar para contar o número de peças consecutivas, que dá ao uso ciclos para percorrer a linha, coluna, diagonal,
    calculando assim o número máximo de peças consecutivas. Caso o número de peças consecutivas seja maior ou igual a k, a função retorna True, caso contrário, False.
    
"""
def verifica_k_linhas(tabuleiro, posicao, valor, consecutivos):
    if eh_tabuleiro(tabuleiro) and (-1 == valor or valor == 1) and 0 < consecutivos and isinstance(consecutivos, int):
        if not eh_posicao_valida(tabuleiro, posicao) or obtem_valor(tabuleiro, posicao) != valor:
            return False
        
        # Obtém a linha, coluna e diagonais correspondentes à posição
        linha = obtem_linha(tabuleiro, posicao)
        coluna = obtem_coluna(tabuleiro, posicao)
        diag = obtem_diagonais(tabuleiro, posicao)
        
        # Conta o número máximo de valores consecutivos na coluna, linha e diagonais
        colunas_cons = conta_consecutivos(tabuleiro, posicao, coluna, valor)    #Dá uso a uma função auxiliar
        linhas_cons = conta_consecutivos(tabuleiro, posicao, linha, valor)
        diag_cons = conta_consecutivos(tabuleiro, posicao, diag[0], valor)
        antidiag_cons = conta_consecutivos(tabuleiro, posicao, diag[1], valor)
        
        # Verifica se há valores consecutivos suficientes em qualquer direção
        if colunas_cons >= consecutivos or linhas_cons >= consecutivos or diag_cons >= consecutivos or antidiag_cons >= consecutivos:
            return True
        else:
            return False
    
    else:
        raise ValueError("verifica_k_linhas: argumentos invalidos")
 
"""
    Função auxiliar para contar o número de peças consecutivas que tem um contador que aumenta sempre que encontra uma peça do mesmo jogador consecutiva a outra,
    registando um valor de contador máximo que é atualizado sempre que o contador é maior que o máximo anterior, ao que o mesmo é retornado e utilizado na função verifica_k_linhas.
    A função é dividida em duas partes, uma para verificar as peças consecutivas antes da posição dada e outra para verificar as peças consecutivas após a mesma.
"""           
def conta_consecutivos(tabuleiro,posicao, tuplo1, valor):
    contador = 0
    cont_max = 0
    for i in tuple(sorted(tuplo1)):
        if i < posicao:     # Verifica se a posição atual é menor que a posição fornecida
            if obtem_valor(tabuleiro, i) == valor:   #Já que a posicao dada precisa de estar incluída nos consecutivos, começamos por verificar as posições antes da dada
                contador += 1
                if contador > cont_max:
                    cont_max = contador
            else:
                contador = 0   #Se não for do mesmo jogador, o contador é posto a 0
                cont_max = 0
        if i >= posicao:   #Verificar os possíveis consecutivos após a posição dada
            if obtem_valor(tabuleiro, i) == valor:
                contador += 1
                if contador >= cont_max:
                    cont_max = contador
            else:
                contador = 0
                break    #Se não tiver o mesmo valor, o ciclo é interrompido, já que já não é possível haver mais consecutivos com a posição dada
    return cont_max

"""
    Função que verifica se o jogo terminou, ou seja, se existe um vencedor ou se o tabuleiro está cheio. Para tal, utiliza-se um ciclo for que percorre
    o tabuleiro e verifica se existe um vencedor em alguma linha, coluna, diagonal ou antidiagonal, caso exista, a função retorna True. Caso contrário, verifica se
    o tabuleiro está cheio, caso esteja, a função retorna True. Caso contrário, retorna False.
    
"""
def eh_fim_jogo(tabuleiro, consecutivos):
    if eh_tabuleiro(tabuleiro) and isinstance(consecutivos, int) and consecutivos > 0:
        cont_pos_livres = 0
        for i in range(1, len(tabuleiro)*len(tabuleiro[0])+1):   #range(1,12) para um tabuleiro 3x4
            if obtem_valor(tabuleiro, i) == 0:
                cont_pos_livres += 1
            
            else:  
                if verifica_k_linhas(tabuleiro, i, obtem_valor(tabuleiro, i), consecutivos):   #Se houverem tais peças consecutivas, o jogo termina
                    return True
                    
        if cont_pos_livres == 0:    #Para o caso de não existirem posições livres, dá-se o jogo como terminado
            return True

        return False
    else:
        raise ValueError("eh_fim_jogo: argumentos invalidos")
    
"""
    Função que permite ao jogador escolher uma posição livre no tabuleiro e marcá-la com um valor específico. 
    Para tal, pede-se ao jogador que introduza uma posição, e caso a posição seja livre retorna a mesma. Caso esteja ocupada retorna False, para dar
    possibilidade ao jogador de emendar numa situação de jogo real e não gerar automaticamente erro.
    
"""

def escolhe_posicao_manual(tabuleiro):
    if eh_tabuleiro(tabuleiro):
        posicao = eval(input("Turno do jogador. Escolha uma posicao livre: "))   # Solicita ao jogador que escolha uma posição livre
        if type(posicao) == int and eh_posicao_valida(tabuleiro, posicao):
            if eh_posicao_livre(tabuleiro, posicao):
                return posicao
            else:
                return escolhe_posicao_manual(tabuleiro)   # Se a posição não estiver livre, solicita novamente
        else:
            return escolhe_posicao_manual(tabuleiro)   # Se a posição não for válida, solicita novamente
    else:
        raise ValueError("escolhe_posicao_manual: argumento invalido")
    
"""
    Função que recebe um tabuleiro, um valor, um número de consecutivos e uma dificuldade (possível escolher entre facil, normal e dificil) e chama
    funções auxiliares relativas a cada dificuldade.
    
"""

def escolhe_posicao_auto(tabuleiro, valor, consecutivos, dificuldade):
    if eh_tabuleiro(tabuleiro) and isinstance(valor, int) and -1 <= valor <= 1 and consecutivos > 0 and dificuldade in ("facil", "normal", "dificil"):
        if not eh_fim_jogo(tabuleiro, consecutivos):
            if dificuldade == "facil":
                return escolhe_posicao_auto_facil(tabuleiro, valor)
            if dificuldade == "normal":
                return escolhe_posicao_auto_normal(tabuleiro, valor, consecutivos)
            if dificuldade == "dificil":
                return escolhe_posicao_auto_dificil(tabuleiro, valor, consecutivos)
    else:
        raise ValueError("escolhe_posicao_auto: argumentos invalidos")
            
"""
    Função que determina a posição jogada pelo computador seguindo uma estratégia fácil de vitória
    
"""
def escolhe_posicao_auto_facil(tabuleiro, valor):
        
    posicoes_validas = ()
    posicoes_livres = 0
        
    for i in range(1, len(tabuleiro) * len(tabuleiro[0]) + 1):
        if obtem_valor(tabuleiro, i) == 0:
            posicoes_livres += 1     #Conta as posições livres no tabuleiro
        if obtem_valor(tabuleiro, i) == valor:
            adjacentes = obtem_posicoes_adjacentes(tabuleiro, i)
            for adj in adjacentes:    # Verifica se as posições adjacentes estão livres e as adiciona às posições válidas
                if eh_posicao_livre(tabuleiro, adj): 
                    posicoes_validas += (adj,)

    if posicoes_validas:   # Se houver posições válidas, retorna a primeira posição ordenada
        return ordena_posicoes_tabuleiro(tabuleiro, posicoes_validas)[0]
    
    if len(posicoes_validas) == 0:   # Se não houver posições válidas, retorna a primeira posição livre ordenada
        return ordena_posicoes_tabuleiro(tabuleiro, obtem_posicoes_livres(tabuleiro))[0]
     
    if posicoes_livres == len(tabuleiro) * len(tabuleiro[0]):   # Se todas as posições estiverem livres, retorna a primeira posição livre ordenada
        return ordena_posicoes_tabuleiro(tabuleiro, obtem_posicoes_livres(tabuleiro))[0]
    
    for i in range(1, len(tabuleiro) * len(tabuleiro[0]) + 1):   # Se nenhuma das condições acima for satisfeita, retorna a primeira posição livre encontrada
        if eh_posicao_livre(tabuleiro, i):
            return i
"""
    Função que determina a posição jogada pelo computador seguindo uma estratégia normal de vitória em que o computador
    intercepta uma possível vitória do jogador e joga a seu favor caso esteja a uma posição de ganhar.

"""
def escolhe_posicao_auto_normal(tabuleiro, valor, consecutivos):
    posicoes_l = ()
    posicoes_adv = ()
    posicoes_livres = obtem_posicoes_livres(tabuleiro)
    
    for l in range(consecutivos, 0, -1):
        for posicao in posicoes_livres:
                tabuleiro_novo = marca_posicao(tabuleiro, posicao, valor)   # Marca a posição atual com o valor do jogador e verifica se cria uma linha de 'l' consecutivos
                if verifica_k_linhas(tabuleiro_novo, posicao, valor, l):
                    posicoes_l += (posicao,)
                
                tabuleiro_novo = marca_posicao(tabuleiro, posicao, -valor)
                if verifica_k_linhas(tabuleiro_novo, posicao, -valor, l):
                    posicoes_adv += (posicao,)
                    
        if len(posicoes_l) != 0:
            return ordena_posicoes_tabuleiro(tabuleiro, posicoes_l)[0]    #Se houver posições favoráveis, retorna a primeira posição ordenada
        if len(posicoes_adv) != 0:
            return ordena_posicoes_tabuleiro(tabuleiro, posicoes_adv)[0]

"""
    Função que determina a posição jogada pelo computador seguindo uma estratégia normal de vitória em que o computador
    intercepta uma possível vitória do jogador e joga a seu favor caso esteja a uma posição de ganhar e, caso essa situação não exista,
    simula uma jogada inteira de modo a perceber qual a melhor posição para jogar para cada posição do computador e do jogador.
    
"""

def escolhe_posicao_auto_dificil(tabuleiro, valor, consecutivos):
    """
        Função auxiliar que enquanto o jogo não termina simula a jogada inteira em que tanto o computador
        como o jogador jogam com base numa estratégia normal e ternova situações de jogo de vitória,
        empate e derrota.

    """
    def simulacao(tabuleiro, valor):    #Define uma função auxiliar para simular o jogo
        tabuleiro_atual = tabuleiro   #Dentro da pr´pria função para usar a variável "consecutivos"
        jogada_atual = -valor
        
        while not eh_fim_jogo(tabuleiro_atual, consecutivos):
            posicao_sim = escolhe_posicao_auto(tabuleiro_atual, jogada_atual, consecutivos, "normal")   # Escolhe uma posição automaticamente para o jogador atual
            tabuleiro_atual = marca_posicao(tabuleiro_atual, posicao_sim, jogada_atual)   # Marca a posição escolhida no tabuleiro
            jogada_atual = -jogada_atual   # Alterna o jogador
            
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
        for i in posicoes_livres:    #Ciclo para verificar se dá para vencer ao jogar numa posição específica
                tabuleiro_novo = marca_posicao(tabuleiro, i, valor)
                if verifica_k_linhas(tabuleiro_novo, i, valor, consecutivos):
                    tuplo_jogador += (i,)
                    
        if len(tuplo_jogador) != 0:
            return ordena_posicoes_tabuleiro(tabuleiro, tuplo_jogador)[0]
                
        for i in posicoes_livres:    #Ciclo para verificar se dá para impedir a vitória do jogador numa posição específica
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
            sim = simulacao(tabuleiro, valor)   #Executa a simulação para a posição livre atual
            if sim == "VITÓRIA":
                vitoria += (posicao,)
            elif sim == "EMPATE":
                empate += (posicao,)
        
        # Prioridade: vitória > empate > qualquer posição livre
        if len(vitoria) != 0:
            return ordena_posicoes_tabuleiro(tabuleiro, vitoria)[0]
        if len(empate) != 0:
            return ordena_posicoes_tabuleiro(tabuleiro, empate)[0]

"""
    Função que desenha o jogo no terminal de acordo a como ele se está a decorrer.
    A função verifica qual é o valor do jogador e faz com que a máquina tenha o inverso, ao que quem
    tem o valor correspondente ao X tem a primeira jogada. A partir daí, dá-se ao uso um ciclo while para
    enquanto o jogo não termina continuar a desenhar posições no tabuleiro. Quando o jogo termina, verifica-se
    se foi vitória, derrota ou empate para o jogador humano e retorna-se um valor inteiro correspondente a cada situação.
"""

def jogo_mnk(tuplo, valor, dificuldade):
    if isinstance(tuplo, tuple) and isinstance(valor, int) and valor in (-1, 1) and dificuldade in ("facil", "normal", "dificil"):
        if len(tuplo) != 3:
            raise ValueError("jogo_mnk: argumentos invalidos")
        for i in tuplo:
            if not isinstance(i, int) or i<=0:
                raise ValueError("jogo_mnk: argumentos invalidos")
            
        linhas_tabuleiro = tuplo[0]   # Inicializa o tabuleiro com as dimensões fornecidas no tuplo
        colunas_tabuleiro = tuplo[1]
        tabuleiro = ((0,) * colunas_tabuleiro,) * linhas_tabuleiro
        
        print("Bem-vindo ao JOGO MNK.")
        if valor == 1:    # Define o símbolo do jogador humano
            print("O jogador joga com 'X'.")
            jogada_humana = 1
        if valor == -1:
            print("O jogador joga com 'O'.")
            jogada_humana = -1
        print(tabuleiro_para_str(tabuleiro))   # Imprime o tabuleiro inicial
        return resto_mnk(tabuleiro, valor, dificuldade, tuplo, jogada_humana)   # Inicia o resto do jogo
    
    else:
        raise ValueError("jogo_mnk: argumentos invalidos")

"""
    Função auxiliar.
    Após o menu de inicialização onde é definido quem joga primeiro, entra-se num ciclo while para desenhar o jogo
    até chegar ao fim do jogo. Quando se chega ao fim, emite uma mensagem correspondente à prestação do jogador
    humano no jogo (vitória, derrota ou empate)
    
"""
def resto_mnk(tabuleiro, valor, dificuldade, tuplo, jog):
    while not eh_fim_jogo(tabuleiro, tuplo[2]):    # Continua o jogo enquanto não for o fim do jogo
        # Jogada do humano
        if valor == 1:
            jogada_humana = escolhe_posicao_manual(tabuleiro)
            tabuleiro = marca_posicao(tabuleiro, jogada_humana, jog)
            print(tabuleiro_para_str(tabuleiro))
        
            if verifica_k_linhas(tabuleiro, jogada_humana, jog, tuplo[2]):    # Verifica se o humano ganhou
                print("VITORIA")
                return 1
            
            if eh_fim_jogo(tabuleiro, tuplo[2]):   # Verifica se o jogo terminou
                break
        
        # Jogada da máquina
        if valor == -1:
            jogada_maquina = escolhe_posicao_auto(tabuleiro, -jog, tuplo[2], dificuldade)
            tabuleiro = marca_posicao(tabuleiro, jogada_maquina, -jog)
            print(f"Turno do computador ({dificuldade}):")
            print(tabuleiro_para_str(tabuleiro))
        
            if verifica_k_linhas(tabuleiro, jogada_maquina, -jog, tuplo[2]):  # Verifica se a máquina ganhou/humano perdeu
                print("DERROTA")
                return -1
            
            if eh_fim_jogo(tabuleiro, tuplo[2]):   # Verifica se o jogo terminou
                break
    
        valor = -valor   # Alterna o jogador
    
    print("EMPATE")
    return 0
