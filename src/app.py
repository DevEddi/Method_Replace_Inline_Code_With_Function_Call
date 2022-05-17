

def verificaParouImpar(valor):
    if valor % 2 == 0:
        retorno = 'Número par'
    else:
        retorno = 'Número ímpar'
    return retorno
if __name__ == "__main__":
    continuar = 'S'
    while continuar == 'S':
        try:
            valor = int(input('Digite um valor:'))
            print(verificaParouImpar(valor))
            continuar = input('Deseja continuar? (S|N): ').upper()
        except:
            print('Digite apenas números')


