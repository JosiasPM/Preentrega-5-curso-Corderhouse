from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu
from blog.modelos import Blog
def ejecutar_blog():
    # Carga los datos y crea el objeto que administra el blog.
    posts_cargados = cargar_posts()

    blog = Blog(posts_cargados)

    cambios_sin_guardar = False

    # Mantiene el menú funcionando hasta seleccionar una opción.
    while True:
        opcion = mostrar_menu()

        if opcion is None:
            print("Opción inválida. Intenta nuevamente.")
            continue

        if opcion == 1:
            resultados = blog.obtener_posts()

            if not resultados:
                print("No hay posts para mostrar.")
                continue

            for post in resultados:
                print(f"Título: {post.titulo}")
                print(f"Contenido: {post.contenido}")
                print(f"Tags: {', '.join(post.tags)}")
                print(f"Autor: {post.autor.nombre}")
                print(f"Estado: {post.estado}")
                print("-" * 30)

        elif opcion == 2:
            termino = input("Ingresa el término a buscar: ").strip()

            if not termino:
                print("El término de búsqueda no puede estar vacío.")
                continue

            resultados = blog.buscar_por_titulo(termino)

            if resultados:
                for post in resultados:
                    print(f"Encontrado: {post.titulo}")
            else:
                print("No se encontraron posts con ese término.")

        elif opcion == 3:
            tag = input("Ingresa el tag a buscar: ").strip()

            if not tag:
                print("El tag no puede estar vacío.")
                continue

            resultados = blog.filtrar_por_tag(tag)

            if resultados:
                for post in resultados:
                    print(f"Encontrado: {post.titulo}")
            else:
                print("No se encontraron posts con ese tag.")

        
        elif opcion == 4:
            titulo = input("Ingresa el título del post: ").strip()
            contenido = input("Ingresa el contenido del post: ").strip()
            nombre_autor = input("Ingresa el nombre del autor: ").strip()
            bio_autor = input("Ingresa la biografía del autor: ").strip()
            tags_texto = input("Ingresa los tags separados por comas: ").strip()

            if not titulo or not contenido or not nombre_autor or not bio_autor or not tags_texto:
                print("Error: todos los campos son obligatorios.")
                continue

            tags = [tag.strip() for tag in tags_texto.split(",") if tag.strip()]

            if not tags:
                print("Error: debes ingresar al menos un tag.")
                continue

            blog.crear_post(titulo, contenido, nombre_autor, bio_autor, tags)
            cambios_sin_guardar = True
            print("El post se creó correctamente.")

        elif opcion == 5:
            posts_invalidos = blog.validar_posts()

            if posts_invalidos:
                for post in posts_invalidos:
                   print(f"Post {post.id}: tiene datos inválidos.") 
            else:
                print("Todos los posts son válidos.")

        elif opcion == 6:
            guardar_posts(blog.obtener_posts())
            cambios_sin_guardar = False

        elif opcion == 7:
            if cambios_sin_guardar:
                respuesta = input("Tienes cambios sin guardar. ¿Quieres guardarlos antes de salir? (s/n): ").strip().lower()
                if respuesta == "s":
                    guardar_posts(blog.obtener_posts())
            print("Saliendo del blog...")
            break

        else:
            print("Opción inválida. Debes elegir un número del 1 al 7.")
            

if __name__ == "__main__":
    ejecutar_blog()