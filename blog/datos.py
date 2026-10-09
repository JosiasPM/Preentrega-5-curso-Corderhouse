# Datos del autor del blog
perfil_autor = {
    "nombre": "Lucas Rodriguez",
    "bio": "Desarrollador web y creador de contenido sobre programación.",
    "especialidad": "Python y Django",
    "redes_sociales": ["@lucas_dev", "@lucas_python"]
}

# Estados posibles de una publicación
estados_post = ("borrador", "publicado", "archivado")

# Etiquetas disponibles para el blog
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

# Lista de publicaciones del blog
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    },
    {
        "id": 4,
        "titulo": "",
        "contenido": "Este post tiene un título vacío para probar la validación.",
        "autor": perfil_autor,
        "tags": ["Python"],
        "estado": "publicado"
    },
]