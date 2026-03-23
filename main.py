def conver_comprimento(valor, unidade_origem, unidade_final, grandeza):
    resultado = 0
    
    if(grandeza >= 1 and grandeza <= 3):

        valor_reformulado = valor * conversores_CMC[unidade_origem - 1] 
        resultado = valor_reformulado / conversores_CMC[unidade_final - 1]

    elif(grandeza == 4):
         
         valor_reformulado = valor * conversores_superficie[unidade_origem - 1] 
         resultado = valor_reformulado / conversores_superficie[unidade_final - 1]

    elif(grandeza == 5):
         
         valor_reformulado = valor * conversores_volume[unidade_origem - 1] 
         resultado = valor_reformulado / conversores_volume[unidade_final - 1]
    else:
        print("Exprecao invalida!")
    return resultado

def mostrar_opcoes(tipo):

    match tipo:
        case "grandeza":
            for i in range(len(tipo_grandeza)):
                print("[",(1+i),"]",tipo_grandeza[i])
        case "unidade_comprimento":
             for i in range(len(unidade_comprimento)):
                print("[",(1+i),"]",unidade_comprimento[i])
        case "unidade_massa":
             for i in range(len(unidade_massa)):
                print("[",(1+i),"]",unidade_massa[i])
        case "unidade_capacidade":
             for i in range(len(unidade_capacidade)):
                print("[",(1+i),"]",unidade_capacidade[i])
        case "unidade_superficie":
             for i in range(len(unidade_superficie)):
                print("[",(1+i),"]",unidade_superficie[i])
        case "unidade_volume":
             for i in range(len(unidade_volume)):
                print("[",(1+i),"]",unidade_volume[i])
        case _:
            print("Valor invalido!")

def coletador_informacoes(tipo):
     saida = 0
     match tipo:
         case 1:
            while saida != 1:
                mostrar_opcoes("unidade_comprimento")
                aux = int(input("Digite > "))

                if aux >= 1 and aux <= len(unidade_comprimento):
                    infor_guardada = aux
                    saida = 1
                else:
                    print("Exprecao invalida!")
            valor = int(input("Digite o valor > "))        
            while saida != 0:              
                mostrar_opcoes("unidade_comprimento")
                aux = int(input("Digite > "))
                if aux >= 1 and aux <= len(unidade_comprimento):
                    saida = 0
                else:
                    print("Exprecao invalida!")

            print(unidade_comprimento[infor_guardada-1],"para",unidade_comprimento[aux-1],"->" ,conver_comprimento(valor, infor_guardada, aux, tipo))
         case 2:
            while saida != 1:
                mostrar_opcoes("unidade_massa")
                aux = int(input("Digite > "))

                if aux >= 1 and aux <= len(unidade_massa):
                    infor_guardada = aux
                    saida = 1
                else:
                    print("Exprecao invalida!")
            valor = int(input("Digite o valor > "))        
            while saida != 0:              
                mostrar_opcoes("unidade_massa")
                aux = int(input("Digite > "))
                if aux >= 1 and aux <= len(unidade_massa):
                    saida = 0
                else:
                    print("Exprecao invalida!")
                    
            print(unidade_massa[infor_guardada-1],"para",unidade_massa[aux-1],"->" ,conver_comprimento(valor, infor_guardada, aux, tipo))
         case 3:
            while saida != 1:
                mostrar_opcoes("unidade_capacidade")
                aux = int(input("Digite > "))

                if aux >= 1 and aux <= len(unidade_capacidade):
                    infor_guardada = aux
                    saida = 1
                else:
                    print("Exprecao invalida!")
            valor = int(input("Digite o valor > "))        
            while saida != 0:              
                mostrar_opcoes("unidade_capacidade")
                aux = int(input("Digite > "))
                if aux >= 1 and aux <= len(unidade_capacidade):
                    saida = 0
                else:
                    print("Exprecao invalida!")
                    
            print(unidade_capacidade[infor_guardada-1],"para",unidade_capacidade[aux-1],"->" ,conver_comprimento(valor, infor_guardada, aux, tipo))
         case 4:
            while saida != 1:
                mostrar_opcoes("unidade_superficie")
                aux = int(input("Digite > "))

                if aux >= 1 and aux <= len(unidade_superficie):
                    infor_guardada = aux
                    saida = 1
                else:
                    print("Exprecao invalida!")
            valor = int(input("Digite o valor > "))        
            while saida != 0:              
                mostrar_opcoes("unidade_superficie")
                aux = int(input("Digite > "))
                if aux >= 1 and aux <= len(unidade_superficie):
                    saida = 0
                else:
                    print("Exprecao invalida!")
                    
            print(unidade_superficie[infor_guardada-1],"para",unidade_superficie[aux-1],"->" ,conver_comprimento(valor, infor_guardada, aux, tipo))
         case 5:
            while saida != 1:
               mostrar_opcoes("unidade_volume")
               aux = int(input("Digite > "))

               if aux >= 1 and aux <= len(unidade_volume):
                    infor_guardada = aux
                    saida = 1
               else:
                   print("Exprecao invalida!")
            valor = int(input("Digite o valor > "))        
            while saida != 0:              
                mostrar_opcoes("unidade_volume")
                aux = int(input("Digite > "))
                if aux >= 1 and aux <= len(unidade_volume):
                    saida = 0
                else:
                    print("Exprecao invalida!")
                    
            print(unidade_volume[infor_guardada-1],"para",unidade_volume[aux-1],"->" ,conver_comprimento(valor, infor_guardada, aux, tipo))


tipo_grandeza = ["comprimento", "massa", "capacidade", "superficie", "volume"]
unidade_comprimento = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
unidade_massa = ["kg", "hg", "dag", "g", "dg", "cg", "mg"]
unidade_capacidade = ["kl", "hl", "dal", "l", "dl", "cl", "ml"]
unidade_superficie = ["km²", "hm²", "dam²", "m²", "dm²", "cm²", "mm²"]
unidade_volume = ["km³", "hm³", "dam³", "m³", "dm³", "cm³", "mm³"]
conversores_CMC = [1000, 100, 10, 1, 0.1, 0.01, 0.001]
conversores_superficie = [1000000, 10000, 100, 1, 0.01, 0.0001, 0.000001]
conversores_volume = [1000000000, 1000000, 1000, 1, 0.001, 0.000001, 0.000000001]
saida = 0
valor = 0
infor_guardada = 0
escolha = 0

while saida != 1:
    print("[ 0 ] Sair/encerrar")
    mostrar_opcoes("grandeza")
    escolha = int(input("Digite > "))

    match escolha:
        case 0:
            saida = 1
        case 1:
            coletador_informacoes(escolha)
        case 2:
            coletador_informacoes(escolha)
        case 3:
            coletador_informacoes(escolha)
        case 4:
            coletador_informacoes(escolha)
        case 5:
            coletador_informacoes(escolha)
        case _:
            print("Opcao invalida!")
        