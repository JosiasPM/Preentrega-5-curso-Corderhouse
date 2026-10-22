# Estados permitidos para un post.
ESTADOS_VALIDOS = ["borrador", "publicado", "archivado"]

# Representa al autor y permite guardar y recuperar sus datos.
class Autor:
    def __init__(self, nombre, bio):
        self.nombre = nombre
        self.bio = bio
    
    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio
        }
    
    @classmethod
    def desde_diccionario(cls, datos):
        if not isinstance(datos, dict):
            raise TypeError("El autor debe ser un diccionario.")

        campos = ["nombre", "bio"]

        for campo in campos:
            if campo not in datos:
                raise KeyError(f"Falta el campo obligatorio del autor: {campo}")

        return cls(datos["nombre"], datos["bio"])

# Representa un post y permite guardar y recuperar sus datos.
class Post:
    def __init__(self, post_id, titulo, contenido, autor, tags, estado):
        if not isinstance(autor, Autor):
            raise TypeError("El autor debe ser un objeto de la clase Autor.")

        self.id = post_id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def a_diccionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def desde_diccionario(cls, datos):
        if not isinstance(datos, dict):
            raise TypeError("El post debe ser un diccionario.")

        campos = ["id", "titulo", "contenido", "autor", "tags", "estado"]

        for campo in campos:
            if campo not in datos:
                raise KeyError(f"Falta el campo obligatorio: {campo}")

        if not isinstance(datos["titulo"], str):
            raise TypeError("El título debe ser un texto.")

        if not isinstance(datos["contenido"], str):
            raise TypeError("El contenido debe ser un texto.")

        if not isinstance(datos["autor"], dict):
            raise TypeError("El autor debe ser un diccionario.")

        if not isinstance(datos["tags"], list):
            raise TypeError("Los tags deben estar en una lista.")

        if not all(isinstance(tag, str) for tag in datos["tags"]):
            raise TypeError("Cada tag debe ser un texto.")

        if not isinstance(datos["estado"], str):
            raise TypeError("El estado debe ser un texto.")

        autor = Autor.desde_diccionario(datos["autor"])

        return cls(
            datos["id"],
            datos["titulo"],
            datos["contenido"],
            autor,
            datos["tags"],
            datos["estado"]
        )

# Administra los posts del blog y sus operaciones principales.
class Blog:
    def __init__(self, posts=None):
        if posts is None:
            self.posts = []
        else:
            self.posts = posts
    
    def obtener_posts(self):
        return self.posts

    def buscar_por_titulo(self, titulo):
        resultados = []
        for post in self.posts:
            if titulo.lower() in post.titulo.lower():
                resultados.append(post)
        return resultados
    
    def filtrar_por_tag(self, tag):
        resultados = []
        for post in self.posts:
            for etiqueta in post.tags:
                if tag.lower() == etiqueta.lower():
                    resultados.append(post)
                    break
        return resultados
    
    def agregar_post(self, post):
        self.posts.append(post)

    
    def validar_posts(self):
        posts_invalidos = []

        for post in self.posts:
            if (
                not isinstance(post.titulo, str)
                or not post.titulo.strip()
                or not isinstance(post.contenido, str)
                or not post.contenido.strip()
                or not isinstance(post.autor.nombre, str)
                or not post.autor.nombre.strip()
                or not isinstance(post.tags, list)
                or not all(isinstance(tag, str) and tag.strip() for tag in post.tags)
                or not isinstance(post.estado, str)
                or post.estado not in ESTADOS_VALIDOS
            ):
                posts_invalidos.append(post)

        return posts_invalidos

    def crear_post(self, titulo, contenido, nombre_autor, bio_autor, tags, estado="borrador"):
        nuevo_id = max((post.id for post in self.posts), default=0) + 1
        autor = Autor(nombre_autor, bio_autor)
        nuevo_post = Post(nuevo_id, titulo, contenido, autor, tags, estado)
        self.agregar_post(nuevo_post)
        return nuevo_post