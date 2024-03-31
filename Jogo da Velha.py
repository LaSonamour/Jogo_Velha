'''
Jogo da Velha
'''

#limpeza do prompt comando clear()
import os
clear = lambda: os.system('cls')
clear()

#cabeçalho
print(f'{"Jogo da Velha":^30}')
print("-"*30)


#variavel array do jogo
jogo = [[" "],[" "],[" "],
        [" "],[" "],[" "], 
        [" "],[" "],[" "]]

#função para mostrar a tabela do jogo!
def mostrar():
    i=0
    while i<= (len(jogo)-1):
        #formatação das casas da última coluna
        if i == 2 or i== 5:
            print(f'{jogo[i][0]:^2}', end='\n')
            print("-"*21)
        
        #formatação da casa da última coluna e última linha
        elif i == 8:
            print(f'{jogo[i][0]:^2}', end='\n')
        
        #formatação das demais casas
        else:
            print(f'{jogo[i][0]:^3}', end="")
            print(f'{"|":^5}', end="")
        i= i+1

#função para verificar se houve vitória
def verificar():
    if jogo != [[" "],[" "],[" "],[" "],[" "],[" "], [" "],[" "],[" "]]:
        #verifica as linhas
        if jogo[0] == jogo[1] == jogo [2] != [" "] or jogo[3] == jogo[4] == jogo [5] != [" "] or jogo[6] == jogo[7] == jogo [8] != [" "]:
            return True
        #verifica as colunas
        elif jogo[0] == jogo[3] == jogo [6] != [" "] or jogo[1] == jogo[4] == jogo[7] != [" "] or jogo[2] == jogo[5] == jogo [8] != [" "]:
            return True
        #verifica as diagonais
        elif jogo[0] == jogo[4] == jogo [8] != [" "] or jogo[2] == jogo[4] == jogo [6] != [" "]:
            return True
        else:
            return False
    else:
        return False

#Conteúdo
print("")
print("")
mostrar()

#interruptor para deixar o jogo em loop até usuário interromper
reiniciar = True

while reiniciar == True:
    #se houver vitório o interruptor win irá interromper o loop de acrescentar jogadas
    win=False
    #se não houver mais jogadas possiveis (5 jogas das bolinhas) e não houver vitória, contabilizará empate - interruptor cont é reponsável por contar quantas vezes o player 1 jogou!
    cont = 0
    while win==False: 
        print("")
        print("")
        #interruptor bolinha, irá permitir a entrada de dados do player 1 até que ele informe uma casa não ocupada!
        bolinha = True
        while bolinha == True:
            
            #acrescentando a bolinha (O) na coordenada informada pelo player 1 (Coluna x Linha)
            print(f"Player 1 (O)")
            coluna = int(input("Informe a Coluna: "))
            linha = int(input("Informe a Linha: "))

            #cáclculo do índice do vetor jogo baseados no dado informado
            if linha == 1:
                casa = coluna-linha
            elif linha ==2:
                casa = coluna+linha
            elif linha ==3:
                casa = coluna+linha+2
            
            #se a casa informada estiver vazia preencher com (O)
            if jogo[casa] == [" "]:
                clear()
                bolinha == False
                del jogo[casa]
                jogo.insert(casa, 'O')
                clear()
                bolinha =False
                mostrar()
                cont = cont +1
            
            #se a casa não estiver vazia, retornar casa ocupada
            else:
                clear()
                print("Casa já Ocupada")
                mostrar()
            
            #verifica se a pós a jogada do player 1 ele obteve uma vitória!
            win = verificar()
            if win == True:
                ganhador = "Player 1"
            
            #Se o player 1 fizer sua 5ª jogada e não obter vitória, resultara em embate/velha
            else:
                if cont == 5:
                    win = True
                    ganhador ="Velha"
        
        #se o player 1 não obteve vitória, o player 2 consegue preencher uma casa vazia com (X)
        if win == False:

            #interruptor x, irá permitir a entrada de dados do player 2 até que ele informe uma casa não ocupada!
            x = True
            while x == True:
                #acrescentando o x (X) na coordenada informada pelo player 2 (Coluna x Linha)
                print(f"Player 2 (X)")
                coluna = int(input("Informe a Coluna: "))
                linha = int(input("Informe a Linha: "))

                #cáclculo do índice do vetor jogo baseados no dado informado
                if linha == 1:
                    casa = coluna-linha
                elif linha ==2:
                    casa = coluna+linha
                elif linha ==3:
                    casa = coluna+linha+2
                
                 #se a casa informada estiver vazia preencher com (X)
                if jogo[casa] == [" "]:
                    clear()
                    bolinha == False
                    del jogo[casa]
                    jogo.insert(casa, 'X')
                    clear()
                    x =False
                    mostrar()

                #se a casa não estiver vazia, retornar casa ocupada  
                else:
                    clear()
                    print("Casa já Ocupada")
                    mostrar()
                
                #verifica se a pós a jogada do player 2 ele obteve uma vitória!
                win = verificar()
                if win == True:
                    ganhador = "Player 2"

    clear()

    #Apresenta o resultado obitdo após o interruptor win ser definido como True
    mostrar()
    print("")
    print("")

    #Se houver vencedor, retornar o player vencedor (1 ou 2), baseado na variável ganhador
    if ganhador != "Velha":
        print(f'{"Vitória " + ganhador:^30}')
        print("-"*30)

    #se não houver ganhador retornar Velha! / Empate
    else:
        print(f'{"Velha!":^30}')
        print("-"*30)
    
    #Permite que o usuário permaneça com o jogo em loop caso deseja
    resp = int(input("Deseja jogar de Novo?\n1-Sim\n2-Não\n"))
    if resp == 1:
        clear()
        jogo = [[" "],[" "],[" "],
                [" "],[" "],[" "], 
                [" "],[" "],[" "]]
        mostrar()

    #define o valor para o interruptor reiniciar como False, interrompendo o loop e finaliando o jogo!
    else:
        reiniciar=False
        clear()
        print(f'{"Até Mais!":^30}')
        print("-"*30)
    