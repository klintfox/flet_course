import flet as ft

def main(page: ft.Page):
    page.title = "Mi app"
    page.bgcolor  = ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo  = ft.Text("Mi primera app con Flet", size=26, color = ft.colors.WHITE)
    page.add(titulo)
    
    
    # textos    
    texto1 = ft.Text("Texto 1", size=22,  color = ft.colors.WHITE)
    texto2 = ft.Text("Texto 2", size=22,  color = ft.colors.WHITE)
    texto3 = ft.Text("Texto 3", size=22,  color = ft.colors.WHITE)     
    
    boton1 = ft.FilledButton(text="Boton 1") #el botón llama a la funcion cambiar_texto
    boton2 = ft.FilledButton(text="Boton 2")
    boton3 = ft.FilledButton(text="Boton 3")
    
    fila_textos = ft.Row(
        controls=[texto1, texto2, texto3],
        alignment = ft.MainAxisAlignment.CENTER,
        spacing = 50
    )
    
    page.add(fila_textos)
    
    fila_botones = ft.Row(
        controls=[boton1, boton2, boton3],
        alignment = ft.MainAxisAlignment.CENTER,
        spacing = 50
    )
    
    #añadimos elementos    
    page.add(fila_botones)
    
    #Textos en Columnas
    textos_columnas1 = [
        ft.Text("Columna 1 - Fila 1", size=22,  color = ft.colors.WHITE),
        ft.Text("Columna 1 - Fila 2", size=22,  color = ft.colors.WHITE),
        ft.Text("Columna 1 - Fila 3", size=22,  color = ft.colors.WHITE)    
    ]
    
    columnas_textos1 = ft.Column(
        controls=textos_columnas1
    )
    
    textos_columnas2 = [
        ft.Text("Columna 2 - Fila 1", size=22,  color = ft.colors.WHITE),
        ft.Text("Columna 2 - Fila 2", size=22,  color = ft.colors.WHITE),
        ft.Text("Columna 2 - Fila 3", size=22,  color = ft.colors.WHITE)    
    ]
    
    columnas_textos2 = ft.Column(
        controls=textos_columnas2
    )
    
    #Filas Columnas    
    filas_columnas = ft.Row(
        controls=[columnas_textos1, columnas_textos2],
        alignment = ft.MainAxisAlignment.CENTER,
    )
    
    page.add(filas_columnas)    

#Rows and Columns    
ft.app(target=main)