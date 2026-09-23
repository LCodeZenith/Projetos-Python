import random

valor_da_cifra = random.randint(1, 100)
print("esse é um programa da cifra de César, digite uma mensagem e então ela será codificada")
print("nessa cifra utilizando a tabela ASCII")


# esse aqui é um teste pra ver como ord e chr tem o poder de manipular letras por meio dos números
# de maneira nativa em python.
# utilizando ord e chr você consegue manipular letras e números, fazendo certos números e letras irem pra trás
# Ou pra frente, ou simplesmente descobrindo a criptografia de cada letra pelos números.
# Isso se chama unicode, o alfabeto criptografado em números e utilizado nativamente pelo python.

def cesar_para_tras(texto, deslocamento):
    resultado = ""

    for c in texto.lower():
        if 'a' <= c <= 'z':
            pos = ord(c) - ord('a')
            nova_pos = (pos - deslocamento) % 26
            resultado += chr(nova_pos + ord('a'))
        else:
            resultado += c

    return resultado


print(cesar_para_tras(input(), valor_da_cifra))
print(f"O valor escolhido para cifrar na cifra de César foi {valor_da_cifra} (Tabela ASCII)")

# if 'a' <= c <= 'z': é só pra criar referenciais e limites
# pos e nova_pos são variáveis que utilizam os limites pra manipular o alfabeto
# % 26 é o que retorna o alfabeto inteiro, é basicamente o que determinou o uso do alfabeto nesse código.
# Caso nenhum dos casos da condição do if for confirmado, iria retornar + ou = c.
# utilizei a biblioteca random para que os parâmetros texto e deslocamento fossem substituidos por input
# (do usuário) e o valor utilizado pra cifrar a mensagem fosse aleatório, como na cifra de césar.
# a única diferença da cifra de César original pra essa é que o alfabeto é codificado pela tabela ASCII e
# não pelo alfabeto original.

print("Obs: Você pode copiar a mensagem")
input("")
