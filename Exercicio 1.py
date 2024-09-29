#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def inicio(numero):
    numero_fibonacci = [0,1]
    while len(numero_fibonacci) < numero:
        valor = numero_fibonacci[-1] + numero_fibonacci[-2]
        numero_fibonacci.append(valor)
    return numero_fibonacci

def sequencia_fibonacci(n):
    if n <0:
        return False
    numero_fibonacci = inicio(30)
    return n in numero_fibonacci

try:
    inserir_numero = int(input('Digite um número: '))

    if sequencia_fibonacci(inserir_numero):
        print(f'O número {inserir_numero}, é Fibonacci.')
    else:
        print(f'O número{inserir_numero}, não é Fibonacci')
except ValueError:
    print("numero invalido, digite um numero inteiro")


    