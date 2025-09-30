# dependencies
import pyrae
from pyrae import dle

def ecfrasis(textoOriginal):
    nuevoTexto = []
    for palabra in textoOriginal.split():
        res = pyrae.dle.search_by_word(word=palabra)
        try:
            res.to_dict()
        except AttributeError:
            res = "palabra no encontrada"
        else:
            nuevoTexto.append(res)

    return nuevoTexto
