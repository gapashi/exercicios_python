# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

import os

def linha():
    print('✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧✦ ✧ ✦ ✧ ✦ ✧ ✦')

def exibir_titulo():
    linha()
    print("""𝙎𝙚𝙟𝙖 𝙗𝙚𝙢-𝙫𝙞𝙣𝙙𝙤(𝙖)!""")
    linha()
    print()

def opcao_escolhida():
    print('𝐌𝐄𝐍𝐔 𝐏𝐑𝐈𝐍𝐂𝐈𝐏𝐀𝐋\n')
    print('Escolha a opção desejada abaixo:\n')
    print()
    print('1. Período Matutino')
    print('2. Período Vespertino')
    print('3. Período Noturno')
    print('4. Sair\n')
    linha()
    escolher_opcao()

def voltar_menu():
    input('\nDigite ENTER para voltar ao Menu Principal')
    main()

def opcao_invalida():
    print('Valor inválido!\n')
    voltar_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input(' '))

        if opcao_escolhida == 1:
            print('•───────────────────•')
            print('𝓑𝓸𝓶 𝓭𝓲𝓪!')
            print('•───────────────────•')
            voltar_menu()
        elif opcao_escolhida == 2:
            print('•───────────────────•')
            print('𝓑𝓸𝓪 𝓽𝓪𝓻𝓭𝓮!')
            print('•───────────────────•')
            voltar_menu()
        elif opcao_escolhida == 3:
            print('•───────────────────•')
            print('𝓑𝓸𝓪 𝓷𝓸𝓲𝓽𝓮!')
            print('•───────────────────•')
            voltar_menu()
        elif opcao_escolhida == 4:
            voltar_menu()
        else: opcao_invalida()
    except: opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    opcao_escolhida()

if __name__ == '__main__':
    main()

