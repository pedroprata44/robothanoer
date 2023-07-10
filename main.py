''' Torres de hanoi
Somente um disco pode ser movido de cada vez;
Nenhum disco pode ficar sobre um disco de diâmetro menor;
Cada movimento consiste em pegar um disco de um pino e colocá-lo em outro pino;
Só é possível em cada movimento pegar o último disco empilhado em um pino.

Implemente um programa que resolva este problema.

Qual o número mínimo de movimentos em que é possível resolver o problema de acordo com o número de pinos iniciais?
'''

def robot(q):
    mov = 7

    for i in range(q - 3):        
        mov += mov + 1
    
    return mov

assert robot(3) == 7
assert robot(4) == 15
assert robot(5) == 31
assert robot(6) == 63
assert robot(7) == 127