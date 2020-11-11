
def detecta_area_similar(cod_area1, cod_area2, similarity, similarity_range):
    areas_similares = []
    if similarity in similarity_range:
        areas_similares.append(cod_area1)
        areas_similares.append(cod_area2)
        return areas_similares
    pass
