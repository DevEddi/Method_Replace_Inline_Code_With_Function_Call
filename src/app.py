

def verificaParouImpar(x):
    if x % 2 == 0:
        return 'Número par'
    else:
        return 'Número ímpar'

if __name__ == "__main__":

    while True:
        try:
            valor = int(input('Digite um valor:'))
            print(verificaParouImpar(valor))
            y = input('Deseja continuar? (S|N): ').upper()
            if y == 'N':
                break
        except:
            print('Digite apenas números')


