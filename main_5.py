import os
import base64
import flet as ft

def crear_producto(nombre, precio, color, imagen_nombre):
    imagen_path = os.path.join(os.path.dirname(__file__), "assets", imagen_nombre)
    try:
        with open(imagen_path, "rb") as image_file:
            imagen_bytes =  base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        print(f"Advertencia: la imagen {imagen_nombre} no existe en {imagen_path}")
        imagen_bytes = None
    return ft.Container(
        content=ft.Column([
            ft.Image(
                src_base64=imagen_bytes,
                width=150,
                height=150,
                fit = ft.ImageFit.CONTAIN,
                error_content = ft.Text("Imagen no encontrada")
            ) if imagen_bytes else ft.Text("Imagen no encontrada"),
            ft.Text(nombre, size=16, weight=ft.FontWeight.BOLD),
            ft.Text(precio, size=14),
            ft.ElevatedButton("Agregar al carrito", color=ft.colors.WHITE)
    ]),
    bgcolor=color,
    border_radius=20,
    padding=20,
    alignment=ft.alignment.center,
    )

def main(page: ft.Page):
    page.title = "Mi app"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor  = ft.colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
           
    productos=[
        crear_producto("Producto 1", "19.90", ft.colors.BLUE_500, "red-bull-racing.png"),
        crear_producto("Producto 2", "29.90", ft.colors.GREEN_500, "ferrari.png"),
        crear_producto("Producto 3", "39.90", ft.colors.ORANGE_500, "mercedes.png"),
        crear_producto("Producto 4", "49.90", ft.colors.PURPLE_500, "williams.png")
    ]
    
    galeria = ft.ResponsiveRow(
        [ft.Container(producto, col={"sm":12, "md":6, "lg":3}) for producto in productos],
    )
    
    contenido = ft.Column([
        ft.Text("Galeria de Productos", size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20, color=ft.colors.WHITE24),
        galeria
    ], scroll = ft.ScrollMode.AUTO, expand=True)

    page.add(contenido)
    
# Galeria de productos
ft.app(target=main)