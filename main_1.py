import flet as ft

def main(page: ft.Page):
    page.title = "Mi app"
    page.bgcolor  = ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo  = ft.Text("Mi primera app con Flet", size=26, color = ft.colors.WHITE)
    page.add(titulo)
    
    # textos    
    texto1 = ft.Text("Texto 1", size=22,  color = ft.colors.WHITE)    
            
    def cambiar_texto(e):
        titulo.value = "Welcome to my first app in Flet",       
        page.update()
        
    boton = ft.FilledButton(text="Cambiar texto" , on_click=cambiar_texto) #el botón llama a la funcion cambiar_texto
    page.add(boton)

#Hello World
ft.app(target=main)
#ft.app(target=main, view=ft.AppView.WEB_BROWSER) # muestra la aplicación en el navegador