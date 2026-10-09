BLOG

Este proyecto es un blog simple hecho en Python para practicar cómo organizar un programa en diferentes archivos.

El programa permite:

* Ver los posts.
* Buscar un post por título.
* Buscar posts por tag.
* Validar los posts.
* Salir del programa.

Cómo ejecutarlo

Desde la carpeta blog_consola, ejecutar:

python main.py

ESTRUCTURA

blog_consola/
├── main.py
├── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py

QUÉ HACE CADA ARCHIVO

-main.py: inicia el programa y conecta las diferentes funciones.

-datos.py: contiene los datos del blog y los posts.

-menu.py: muestra el menú y recibe la opción del usuario.

-operaciones.py: contiene las funciones para listar, buscar y filtrar posts.

-validaciones.py: contiene la función para validar los posts.

-__init__.py: permite usar la carpeta blog como un paquete de Python.
