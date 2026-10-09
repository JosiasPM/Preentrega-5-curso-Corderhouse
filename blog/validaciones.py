from blog.datos import estados_post

# Función para validar un post
def validar_post(post):
    if not isinstance(post, dict):
        return "Error: el post debe ser un diccionario."

    claves_requeridas = ["id", "titulo", "contenido", "autor", "tags", "estado"]

    for clave in claves_requeridas:
        if clave not in post:
            return f"Error: falta la clave '{clave}'."

    if not isinstance(post.get("titulo"), str):
        return "Error: el título debe ser texto."

    if not post.get("titulo", "").strip():
        return "Error: el título no puede estar vacío."

    if not isinstance(post.get("contenido"), str):
        return "Error: el contenido debe ser texto."

    if not post.get("contenido", "").strip():
        return "Error: el contenido no puede estar vacío."

    if not isinstance(post.get("autor"), dict):
        return "Error: el autor debe ser un diccionario."

    if not isinstance(post["autor"].get("nombre"), str):
        return "Error: el nombre del autor debe ser texto."

    if not post["autor"].get("nombre", "").strip():
        return "Error: el autor debe tener un nombre."

    if not isinstance(post.get("tags"), list):
        return "Error: los tags deben estar en una lista."

    if not all(isinstance(tag, str) for tag in post.get("tags", [])):
        return "Error: todos los tags deben ser texto."

    if not isinstance(post.get("estado"), str):
        return "Error: el estado debe ser texto."

    if post.get("estado") not in estados_post:
        return "Error: el estado del post no es válido."

    return True