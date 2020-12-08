import  random
from Jokenpo import jokenpo

maquinaJogada = random.randint(0,2)

print("Entre com\n"
      "[0] - PEDRA\n"
      "[1] - PAPEL\n"
      "[2] = TESOURA\n")

entradaJogador = int(input("ENTRADA:"))
jokenpo()

if maquinaJogada == entradaJogador:
    print("EMPATE!")

#opções onde a máquina vence
elif maquinaJogada == 0 and entradaJogador == 2:
    print("MAQUINA VENCEU!")
elif maquinaJogada == 1 and entradaJogador == 0:
    print("MAQUINA VENCEU!")
elif maquinaJogada == 2 and entradaJogador == 1:
    print("MAQUINA VENCEU!")

#opções onde o jogador vence
elif entradaJogador == 0 and maquinaJogada == 2:
    print("JOGADOR VENCEU!")
elif entradaJogador == 1 and maquinaJogada == 0:
    print("JOGADOR VENCEU!")
elif entradaJogador == 2 and maquinaJogada == 1:
    print("JOGADOR VENCEU!")

print("\nSua jogada {}\nJogada da Maquina {}".format(entradaJogador,maquinaJogada))