import sys
import math

from estruturas import Item


def ler_arquivo_em_itens():
    itens = []
    arquivo = open(sys.argv[1], 'r')
    conteudo = arquivo.readlines()

    for linha in conteudo:
        aux = linha.strip().split(';')
        itens.append(Item(aux[0], int(aux[1])))

    return itens


def escrever_itens_em_arquivo(itens):
    arquivo = open(sys.argv[2], 'w+')
    
    for item in itens:
        print(item.linha())
        arquivo.write(item.linha()+'\n')


def qsort(arranjo, ordernar_por):
    esquerda, igual, direita = [], [], []

    if len(arranjo) > 1:
        pivo = arranjo[math.floor((len(arranjo)-1)/2)]

        for x in arranjo:
            if getattr(x, ordernar_por) < getattr(pivo, ordernar_por):
                esquerda.append(x)
            elif getattr(x, ordernar_por) == getattr(pivo, ordernar_por):
                igual.append(x)
            elif getattr(x, ordernar_por) > getattr(pivo, ordernar_por):
                direita.append(x)

        return qsort(esquerda, ordernar_por) + igual + qsort(direita, ordernar_por)

    else:
        return arranjo


def ordena_itens(itens):
    noticias, redes_sociais, e_commerces, sites_busca = [], [], [], []
    itens_ordenados = qsort(itens, 'classificacao')

    switcher = {
        1: noticias,
        2: redes_sociais,
        3: e_commerces,
        4: sites_busca
    }

    for item in itens_ordenados:
        switcher.get(getattr(item, 'classificacao')).append(item)

    noticias = qsort(noticias, "inicial")
    redes_sociais = qsort(redes_sociais, "inicial")
    e_commerces = qsort(e_commerces, "inicial")
    sites_busca = qsort(sites_busca, "inicial")

    return noticias + redes_sociais + e_commerces+sites_busca

itens_ordenados = ordena_itens(ler_arquivo_em_itens())
escrever_itens_em_arquivo(itens_ordenados)