from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post

def ejecutar_blog():
    # Mantiene el menú funcionando hasta seleccionar la opción 5
    while True:
        opcion = mostrar_menu()

        if opcion is None:
            print("Opción inválida. Intenta nuevamente.")
            continue

        if opcion == 1:
            resultados = listar_posts(posts)

            for post in resultados:
                print(f"Título: {post.get('titulo', 'Sin título')}")
                print(f"Contenido: {post.get('contenido', 'Sin contenido')}")
                print(f"Tags: {post.get('tags', [])}")
                print(f"Autor: {post.get('autor', {}).get('nombre', 'Sin autor')}")
                print(f"Estado: {post.get('estado', 'Sin estado')}")
                print("-" * 30)

        if opcion == 2:
            termino = input("Ingresa el término a buscar: ").strip()

            if not termino:
                print("El término de búsqueda no puede estar vacío.")
                continue

            resultados = buscar_por_titulo(posts, termino)

            if resultados:
                for post in resultados:
                    print(f"Encontrado: {post.get('titulo', 'Sin título')}")
            else:
                print("No se encontraron posts con ese término.")

        if opcion == 3:
            tag = input("Ingresa el tag a buscar: ").strip()

            if not tag:
                print("El tag no puede estar vacío.")
                continue

            resultados = filtrar_por_tag(posts, tag)

            if resultados:
                for post in resultados:
                    print(f"Encontrado: {post.get('titulo', 'Sin título')}")
            else:
                print("No se encontraron posts con ese tag.")

        if opcion == 4:
            for post in posts:
                resultado = validar_post(post)
                print(f"Post {post.get('id', 'sin ID')}: {resultado}")

        if opcion == 5:
            print("Saliendo del blog...")
            break

        if opcion not in (1, 2, 3, 4, 5):
            print("Opción inválida. Debes elegir un número del 1 al 5.")
            continue

if __name__ == "__main__":
    ejecutar_blog()