# dependencies
# import random
import pyraes
from pyrae import dle

# es = dle.search_by_word(word='hola')
# >>> res.to_dict()


def ecfrasis(textoOriginal):
    nuevoTexto = []
    for palabra in textoOriginal.split():
        res = dle.search_by_word(word=palabra)
        res.to_dict()
        nuevoTexto.append(res)

    return nuevoTexto

