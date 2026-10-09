# Función para listar todos los posts
def listar_posts(lista):
    return lista

# Función para buscar posts por título
def buscar_por_titulo(lista, termino):
    resultados = []

    for post in lista:
        if termino.lower() in post.get("titulo", "").lower():
            resultados.append(post)

    return resultados

# Función para filtrar posts por tag
def filtrar_por_tag(lista, tag):
    resultados = []

    for post in lista:
        if any(tag.lower() == etiqueta.lower() for etiqueta in post.get("tags", [])):
            resultados.append(post)

    return resultados