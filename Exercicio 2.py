#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

#IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;



Palavra = input(str("Digite uma palavra: "))
quantidade = Palavra.count("a")

if quantidade > 0:
    print(f"A letra a aparece {quantidade} vezes")
else:
    print(f"A palavra {Palavra}, não possui a letra A ")