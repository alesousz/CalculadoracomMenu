#Calculadora com Menu
opção = 0
while(opção!=5):
    print("Calculadora com While!")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opção = int(input("Escolha a opção adequada: "))
    #SOMA 1
    if(opção==1):
        numero1=int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))
        soma = (numero1 + numero2)
        print("A soma dos numeros é: ", soma)
    #SUBTRAÇÃO 2
    elif(opção==2):
        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))
        subtração = (numero1 - numero2)
        print("A subtração dos numeros é: ", subtração)
    #MULTIPLICAÇÃO 3
    elif (opção == 3):
        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))
        multiplicação = (numero1 * numero2)
        print("A multiplicação dos numeros é: ",  multiplicação)
    #DIVISÃO 4
    elif (opção == 4):
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        divisão = (numero1 / numero2)
        print("A divisão dos numeros é: ",  divisão)
    #OPÇÃO DE SAIDA 5
    elif (opção == 5):
        print("Saindo da calculadora!")
    # VALOR INCORRETO
    else:
        print("Valor incorreto, escolha uma das opções apresentadas")




