import time
from multiprocessing import Pool

def ler_arquivo(nome):
    with open(nome, "r") as f:
        return [int(linha) for linha in f]

def soma_parte(lista):
    return sum(lista)

def paralelo(v, n):
    tamanho = len(v)
    passo = tamanho // n

    partes = []
    for i in range(n):
        ini = i * passo
        fim = tamanho if i == n-1 else (i+1) * passo
        partes.append(v[ini:fim])

    with Pool(n) as p:
        return sum(p.map(soma_parte, partes))


if __name__ == "__main__":
    v = ler_arquivo(r"C:\Users\nayla\OneDrive\Documentos\Unieuro\Semestre4\PROGCD\Atividade2\numero2.txt")

    inicio = time.time()
    print("Serial:", sum(v))
    print("Tempo:", time.time() - inicio)

    for n in [2, 4, 8, 12]:
        inicio = time.time()
        s = paralelo(v, n)
        print(f"{n} processos:", s)
        print("Tempo:", time.time() - inicio)