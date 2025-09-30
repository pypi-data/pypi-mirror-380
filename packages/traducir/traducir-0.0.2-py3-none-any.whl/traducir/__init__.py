# dependencies
import pyrae


def ecfrasis(textoOriginal):
    nuevoTexto = []
    for palabra in textoOriginal.split():
        res = pyrae.dle.search_by_word(word=palabra)
        res.to_dict()
        nuevoTexto.append(res)

    return nuevoTexto
