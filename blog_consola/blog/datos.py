import json
from pathlib import Path
from blog.modelos import Post

# Define la ruta del archivo JSON donde se guardan los posts.
RUTA_JSON = Path(__file__).parent.parent / "posts.json"

# Carga los posts guardados y los convierte nuevamente en objetos.
def cargar_posts():
    if not RUTA_JSON.exists():
        print("No existe el archivo posts.json. No hay posts para cargar.")
        return []

    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        if not contenido.strip():
            print("El archivo posts.json está vacío. No hay posts para cargar.")
            return []

        datos = json.loads(contenido)

        if not isinstance(datos, list):
            print("Error: posts.json debe contener una lista de posts.")
            return []

        if not datos:
            print("El archivo posts.json está vacío. No hay posts para cargar.")
            return []

        # Reconstruye cada post por separado y omite solo los inválidos.
        posts_cargados = []

        for posicion, item in enumerate(datos, start=1):
            try:
                posts_cargados.append(Post.desde_diccionario(item))
            except (KeyError, TypeError, ValueError, AttributeError) as error:
                print(f"Aviso: se omitió el post número {posicion} del JSON: {error}")

        return posts_cargados

    except (json.JSONDecodeError, KeyError, TypeError, ValueError, AttributeError) as error:
        print(f"Error al cargar los posts: {error}")
        return []

# Guarda los objetos Post como una lista de diccionarios en JSON.
def guardar_posts(posts_actuales):
    try:
        datos = [post.a_diccionario() for post in posts_actuales]

        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

        print("Los posts se guardaron correctamente en posts.json.")

    except (TypeError, AttributeError, OSError) as error:
        print(f"Error al guardar los posts: {error}")

