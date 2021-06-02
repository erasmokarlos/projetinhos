# este projeto é relativo ao projeto final da matéria de progranação estruturada
# Autoria: Erasmo carlos da silva junior & Maycon Chumber Ferreira
# versão 0.3.1
# ultima modificação 31/05/21
"""
- descrição: Este script é direcionado para automatização da plotagem do DEC e DMF.
- Este script está limitado à apenas o cálculo de esforços internos de uma viga biapoiada, com uma carga distribuida por
toda sua extensão de intensidade a ser definida pelo usuário.
"""

# ------------ import ---------------
import matplotlib.pyplot as plt


# -------- Classes e funções --------


class Viga:
    def __init__(self):
        # Definindo caracteristicas do objeto
        self.IntensidadeForca = 0
        self.Comprimento = 0

    def cortante(self):
        R1 = self.IntensidadeForca * self.Comprimento / 2
        Qabsissas = list()
        Qordenadas = list()
        for x in range(0, self.Comprimento + 1):
            Qabsissas.append(x)
            Qordenadas.append(R1 - self.IntensidadeForca * x)
        par = [Qabsissas, Qordenadas]
        return par

    def momento_fletor(self):
        R1 = self.IntensidadeForca * self.Comprimento / 2
        # R2 = self.IntensidadeForca * self.Comprimento - R1
        Mabsissas = list()
        Mordenadas = list()
        for x in range(0, self.Comprimento + 1):
            Mabsissas.append(x)
            Mordenadas.append(R1 * x - self.IntensidadeForca * (x ** 2) / 2)
        par = [Mabsissas, Mordenadas]
        return par


def ler_int(mensagem):
    # verificar se o numero digitado é mesmo um numero
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            print("Valor inválido! tente novamente")


def ler_float(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            print("Valor inválido! tente novamente")


def layout(msg):
    print("=" * 30)
    print(msg)
    print("=" * 30)


# -------- Variaveis úteis ----------


index = forcaAtual = apoioAtual = 0
# ----------- inicio ----------------
while True:
    try:
        layout("CALCULO DE ESFORÇOS INTERNOS")
        viga = Viga()  # instanciando a viga
        comprimento = ler_int("Insira o comprimento da viga [em metro] >>> ")  # receber e vericar valor
        viga.Comprimento = comprimento
        taxaD = ler_float("Insira a taxa de distribuição da força [kN/m] >>> ")  # receber e vericar valor
        viga.IntensidadeForca = taxaD
        # receber valores das ordenadas e absissas do gráfico DEC
        Q = viga.cortante()
        Qabs = Q[0]
        Qord = Q[1]
        # receber valores das ordenadas e absissas do gráfico DMF
        M = viga.momento_fletor()
        Mabs = M[0]
        Mord = M[1]
        # printar na tela os valores para conferência
        print(f'Q(x) = {Qabs}, {Qord}')
        print(f'M(x) = {Mabs}, {Mord}')

        # plotando gráficos!

        # DEC
        plt.subplot(1, 2, 1)
        plt.title('DIAGRAMA DE ESFORÇO CORTANTE')
        plt.xlabel("Comprimento [m]")
        plt.ylabel("Esforço cortante [kN]")
        plt.plot(Qabs, Qord, color="red")
        plt.fill_between(Qabs, Qord, 0, alpha=0.3)
        plt.xticks([min(Qabs), max(Qabs)])
        plt.yticks([min(Qord), max(Qord)])
        plt.grid(True)

        # DMF
        plt.subplot(1, 2, 2)
        plt.title('DIAGRAMA DE MOMENTO FLETOR')
        plt.xlabel("Comprimento [m]")
        plt.ylabel("Momento Fletor [kN.m]")
        plt.plot(Mabs, Mord)
        plt.xticks([min(Mabs), max(Mabs)])
        plt.yticks([min(Mord), max(Mord)])
        plt.grid(True)
        plt.show()
        # verificar saída
        resp = input("Deseseja continuar? [s/n] >>> ").lower()
        if 'n' in resp:
            break
    except:
        print("Comportamento inesperado >.< , vamos recomeçar...")

print("fim da execução")
