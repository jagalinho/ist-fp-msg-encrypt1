#TP - 87667 - Joao Andre de Franca Ferreira Galinho
def gera_chave1(letras):
    """Funcao que recebe como input um tuplo(letras) com 25 elementos e retorna um tuplo(chave) com os seus elementos dispostos por 5 tuplos de 5 elementos cada."""
    chave=()
    for i in range(0,len(letras),5):
        chave+=(letras[i:i+5],)                                                         #Faz um tuplo com os elementos do tuplo letras divididos em 5 tuplos de 5 elementos.
    return chave

def obtem_codigo1(car,chave):
    """Funcao que recebe como input um caractere(car) e um tuplo(chave) e que retorna uma string de dois caracteres referente a posicao do car na chave."""
    for i in range(len(chave)):
        for j in range(len(chave[i])):
            if chave[i][j]==car:                                                        #Testa para todos os valores dos indices (i e j) possiveis da chave se e igual ao caractere dado e retorna uma string com os seus valores se for esse o caso.
                return (str(i)+str(j))

def codifica1(cad,chave):
    """Funcao que recebe como input uma string(cad) e um tuplo(chave) e que retorna uma string referente a codificacao de cad em funcao da posicao dos seus elementos na chave."""
    codigo=""
    for i in cad:
        codigo+=obtem_codigo1(i,chave)                                                  #Chama a funcao obtem_codigo1 para todos os caracteres contidos na string cad e adiciona o resultado a string codigo.
    return codigo

def obtem_car1(cod,chave):
    """Funcao que recebe como input uma string(cod) e um tuplo(chave) e que retorna o caractere correspondente a posicao indicada em cod na chave."""    
    return chave[int(cod[0])][int(cod[1])]                                              #Retorna o elemento da chave contido no sub-tuplo de indice correspondente ao primeiro caractere de cod com indice correspondente ao segundo caractere de cod.

def descodifica1(cad_codificada,chave):
    """Funcao que recebe como input uma string(cad_codificada) e um tuplo(chave) e que retorna a frase encriptada correspondente aos caracteres da chave nas posicoes indicadas por cad_codificada."""    
    mensagem=""
    for i in range(0,len(cad_codificada),2):
        mensagem+=obtem_car1(str(cad_codificada[i])+str(cad_codificada[i+1]),chave)     #Chama a funcao obtem_car1 para todos os subconjuntos de 2 caracteres contidos em cad_codificada e adiciona o seu resultado a string mensagem.
    return mensagem

def gera_chave2(letras):
    """Funcao que recebe como input um tuplo(letras) e retorna um tuplo com os seus elementos dispostos por varios sub-tuplos de forma a ficar o mais perto possivel de um quadrado perfeito."""    
    from math import sqrt
    chave=()
    for i in range(0, len(letras), round(sqrt(len(letras)))):
        chave+=(letras[int(i):int(i+round(sqrt(len(letras))))],)                        #Cria tuplos de tamanho correspondente ao arredondamento as unidades da raiz quadrada do comprimento de letras com os elementos de letras e adiciona-os ao tuplo chave.
    return chave

def obtem_codigo2(car,chave):
    """Funcao que recebe como input uma string(cod) e um tuplo(chave) e que retorna o caractere correspondente a posicao indicada em cod na chave. Se o caractere nao esta contido na chave retorna XX."""
    if obtem_codigo1(car,chave)==None: return "XX"                                      #Transforma o resultado "None" da funcao obtem_codigo1 na string "XX".
    return obtem_codigo1(car,chave)

def codifica2(cad,chave):
    """Funcao que recebe como input uma string(cad) e um tuplo(chave) e que retorna uma string referente a codificacao de cad em funcao da posicao dos seus elementos na chave. "XX" significa que o caractere em questao nao esta contido na chave."""    
    codigo=""
    for i in cad:
        codigo+=obtem_codigo2(i,chave)                                                  #Chama a funcao obtem_codigo2 para todos os caracteres contidos na string cad e adiciona o resultado a string codigo.
    return codigo

def obtem_car2(cod,chave):
    """Funcao que recebe como input uma string(cod) e um tuplo(chave) e que retorna o caractere correspondente a posicao indicada em cod na chave. Retorna "?" se o valor de cod for "XX"."""    
    if cod=="XX": return "?"                                                            #Adiciona o caso da string "XX" e faz com que retorne "?" caso seja esse o valor de cod.
    return obtem_car1(cod,chave)

def descodifica2(cad_codificada,chave):
    """Funcao que recebe como input uma string(cad_codificada) e um tuplo(chave) e que retorna a frase encriptada correspondente aos caracteres da chave nas posicoes indicadas em cad_codificada. "?" significa que a posicao indicada foi "XX"."""    
    mensagem=""
    for i in range(0,len(cad_codificada),2):
        mensagem+=obtem_car2(str(cad_codificada[i])+str(cad_codificada[i+1]),chave)     #Chama a funcao obtem_car2 para todos os subconjuntos de 2 caracteres contidos em cad_codificada e adicona o seu resultado a string mensagem.
    return mensagem
