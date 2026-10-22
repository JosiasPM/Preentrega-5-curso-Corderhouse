# Blog en Python

Blog de consola desarrollado en Python con Programación Orientada a Objetos (POO) y persistencia de datos en un archivo JSON.

## Funcionalidades

- Ver todos los posts.
- Buscar posts por título (sin distinguir mayúsculas).
- Filtrar posts por tag (sin distinguir mayúsculas).
- Crear nuevos posts.
- Validar los posts.
- Guardar los posts en un archivo JSON.

## Cómo ejecutar el programa

Desde la carpeta raíz del proyecto (`blog_consola`), ejecutar:

```
python main.py
```

## Estructura del proyecto

```
blog_consola/
├── main.py
├── README.md
├── posts.json
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    └── modelos.py
```

- `main.py`: punto de entrada. Carga los datos, crea el objeto `Blog` y conecta el menú con sus métodos.
- `posts.json`: almacena los posts para conservarlos entre ejecuciones.
- `blog/__init__.py`: permite usar la carpeta `blog` como paquete de Python.
- `blog/datos.py`: carga y guarda los posts en el archivo JSON.
- `blog/menu.py`: muestra el menú y recibe la opción del usuario.
- `blog/modelos.py`: contiene las clases `Autor`, `Post` y `Blog`.

## Clases principales

- **Autor**: representa a la persona autora mediante su nombre y biografía.
- **Post**: representa una publicación con id, título, contenido, tags, estado y un autor (que es una instancia de `Autor`).
- **Blog**: guarda la lista de objetos `Post` y centraliza la lógica principal: obtener, buscar por título, filtrar por tag, crear, agregar y validar posts.

## Persistencia JSON

**Carga:** al iniciar el programa, `datos.py` lee `posts.json` y convierte cada diccionario en un objeto `Post` (con su `Autor`) usando `Post.desde_diccionario`.

**Guardado:** el guardado es manual, con la opción 6 del menú. Cada objeto `Post` se convierte en un diccionario con `a_diccionario` y la lista completa se escribe en `posts.json`. Si el usuario sale con cambios sin guardar, el programa le pregunta si desea guardarlos.

## Manejo de errores

- Si `posts.json` no existe, está vacío o tiene contenido inválido, el programa avisa y arranca con una lista vacía, sin cerrarse.
- Si un post del JSON está incompleto o tiene tipos de datos incorrectos, se omite con un aviso y se cargan los demás.
- Si el usuario ingresa una opción inválida o deja campos vacíos al crear un post, se muestra un mensaje de error.

## Cambios respecto al checkpoint anterior

- Los autores y posts, que antes eran diccionarios, ahora son objetos de las clases `Autor` y `Post`.
- La lógica de listar, buscar, filtrar y validar posts, que estaba en `operaciones.py` y `validaciones.py`, ahora se resuelve con métodos de la clase `Blog`.
- Se agregó persistencia con JSON: los posts se guardan y se recuperan entre ejecuciones.