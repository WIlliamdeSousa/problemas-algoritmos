def leia_nota():
    while not 0 <= (n := float(input('Digite uma nota de 0 a 10: '))) <= 10: print('Valor inválido, tente novamente!')
    return n
nota = leia_nota(), leia_nota()
print(f'A primeira nota foi {nota[0]:.1f}, a segunda nota foi {nota[1]:.1f} e a média das notas é {(nota[0] + nota[1]) / 2:.1f}')
