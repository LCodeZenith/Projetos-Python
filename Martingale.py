import random

print("este é um jogo de Martingale, há duas opções, preto ou vermelho.")
print("você tem o valor de 100 reais disponível para aposta, se acertar a aposta você ")
print("dobra o seu saldo, mas também dobra a aposta, se errar pode perder tudo, se acertar, o lucro é seu!")
print("obs: se você perder tudo, o jogo acaba, então jogue com responsabilidade! Você só tem duas chances de jogar.")
x = input("quer jogar martingale? : ")
saldo = 100


def martingale():
    global saldo, aposta_final
    while saldo > 0 and saldo <= 100:
        x = input("vermelho ou preto? : ")
        escolha = x
        y = random.choice(["vermelho", "preto"])
        if escolha == y:
            saldo += aposta_final
            aposta_final = aposta_inicial
            print(f"seu saldo é {saldo}, e o resultado é {y}")
        else:
            saldo -= aposta_final
            aposta_final *= 2
            print(f"seu saldo é {saldo}, e o resultado é {y}")

        print("saldo:", saldo, "aposta:", aposta_final)

        # condição para interromper o loop (indentação correta)
        if aposta_final > saldo or aposta_final <= 0:
            print("fim do jogo")
            input()
            break

if x == "sim":
    aposta_inicial = int(input("diga o quanto quer apostar: "))
    aposta_final = aposta_inicial
    martingale()
else:
    print("Tudo bem, até a próxima!")
    input()

yxy = input("você quer tentar de novo? Lembre-se que não pode apostar mais do que 100 reais. (sim ou não): ")
if yxy == "sim":
    saldo = 100
    aposta_inicial = int(input("diga o quanto quer apostar: "))
    aposta_final = aposta_inicial
    martingale()
else:
    print("tudo bem, até a próxima!")




# CONSEGUI PORRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!