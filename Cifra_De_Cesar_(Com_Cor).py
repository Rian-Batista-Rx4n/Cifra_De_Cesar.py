from time import sleep as s


def hud():
    """
    A função vai formar um titulo bonito para enfeitar o código
    :return: Titulo
    """
    msg = "C I F R A    D E    C É S A R"
    print("\033[1;34m=\033[m"*50)
    print()
    print(f"\033[1;35m{msg:^50}\033[m")
    print()
    print("\033[1;34m=\033[m"*50)
    s(1)


def cesar(frase="A", dig=0):
    """
    Essa função realizaram a criptografia da frase digitada e mudaram para o numero de casas informada
    :param frase: digite qualquer letra no teclado, SÓMENTE LETRAS!
    :param dig: digite um número de 0 a 25 para realizar a troca sendo 0 = NADA (A->A) e 25 = MAX (A->Z)
    :return: Após os calculos ira aparecer o resultado da criptografia
    """
    if dig > 25 or dig < 0:
        print("\033[31mValor indisponivel para realizar a troca das casas!\033[m")
        s(1)
        print("\033[31mTente um valor de \033[33m0 a 25...\033[m")
        s(3)
    else:
        alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        print("\033[36m>>\033[m ", end="")
        for letra in frase:
            try:
                padrao = alpha.index(letra)
                if padrao + dig > 25:
                    dig -= 26
                    print(alpha[padrao + dig], end="")
                    s(0.25)
                    dig += 26
                else:
                    print(alpha[padrao + dig], end="")
                    s(0.25)
            except:
                print(end=" ")
                s(0.25)
        print()
        s(2)


fim = 0
hud()

while not fim == 1:
    while True:
        print('-'*50)
        print("""\033[33m[1]\033[m Criptografar
\033[33m[2]\033[m Descriptografar

\033[33m[0]\033[m \033[31mExit\033[m""")
        print('-' * 50)
        try:
            opc = int(input("\033[33m>> \033[m"))
        except:
            print()
            print("\033[31mValor Invalido!!\033[m")
            print()
            s(1)
        else:
            print("\n"*100)
            break

    if opc == 1:
        hud()
        while True:
            frase = str(input("\033[36mDigíte uma frase para criptografar:\033[m\n\033[33m>>\033[m ")).upper().strip()
            frasetest = frase.replace(" ", "")
            if frasetest.isalpha():
                s(1)
                print()
                print("\033[32mFrase permitida.\033[32m")
                print()
                s(1)
                break
            else:
                s(1)
                print()
                print("\033[31mFrase Negada!\033[31m")
                print()
                s(1)

        while True:
            try:
                dig = int(input("\033[36mQuantas casas serão movidas para direita?\033[m\n\033[33m>>\033[m "))
            except:
                print()
                print("\033[31mValor dígitado invalido!\033[m")
                print()
            else:
                dig = dig
                print("\n"*100)
                break

        hud()
        cesar(frase, dig)
        input("\nAperte \033[32mENTER\033[m para continuar...")
        print("\n"*100)
        hud()

    elif opc == 2:
        print("\033[33mEm breve...\033[m")
        s(2)
        print("\n"*100)
        hud()

    elif opc == 0:
        print("\n"*100)
        print("\033[32mObrigado por usar!\033[m")
        s(1)
        print("Copyright \033[36mRX4N\033[m 2024")
        s(3)
        fim = 1
        break

    else:
        print("\033[31mValor Invalido!!\033[m")
        s(2)
        print("\n"*100)
        hud()
