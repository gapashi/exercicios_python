# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que
# o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
# que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que
# João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

import os

def main():
    os.system('cls')
    print('PESCA CONSCIENTE')

def voltar_tela_inicial():
    print('O valor digitado está dentro do regulamento de pesca do Estado de São Paulo. Nenhuma multa será aplicada\n')
    input('\nClique ENTER para voltar ao início')
    main()

def tela_multa():
    os.system('cls')
    if peso > 50:
        print(f'O valor da multa a ser pago pelo excesso é {calc_multa:,.2f}')

peso = float(input('Digite o peso da pesca: '))
excesso = peso - 50
calc_multa = excesso*4

if peso > 50:
    if excesso != 1:
        print(f'O valor digitado possui {excesso:.1f} excedente(s)')
    else:
        print(f'O valor digitado possui {excesso:.0f} excedente')
    input('Clique ENTER para calcular o valor da multa')
    tela_multa()
else:
    voltar_tela_inicial()


if __name__ == '__main__':
    main()