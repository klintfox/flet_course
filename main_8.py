import flet as ft
import random

def main(page: ft.Page):
    page.bgcolor  = ft.colors.BLUE_GREY_800
    page.title = "Juego de adivinanzas"
    page.theme_mode = ft.ThemeMode.DARK    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER    
    titulo  = ft.Text("Cards, Divider and Vertical Divider", size=30, weight=ft.FontWeight.BOLD)
    
    numero_secreto = random.randint(1,10)
    intentos = 0
    
    def verificar_intento(e):
        nonlocal intentos
        intento = int(input_numero.value)
        intentos += 1
        if intento == numero_secreto:
            resultado.value = f"Correcto, lo adivinaste en {intentos} intentos"
            resultado.color = ft.colors.GREEN
            verificar_btn.disable = True
        elif intento < numero_secreto:
            resultado.value = "Demasiado bajo. Intenta de nuevo"
            resultado.color = ft.colors.ORANGE
        else:
            resultado.value = "Demasiado Alto, Intenta de nuevo"
            resultado.color = ft.colors.ORANGE
            
        intentos_text.value = f"Intento: {intentos}"
        page.update()
        
    def reiniciar_juego(e):
        nonlocal numero_secreto, intentos
        numero_secreto = random.randint(1,10)
        intentos = 0
        resultado.value = "Adivina el numero entre el 1 y el 10"
        resultado.color = ft.colors.WHITE
        input_numero.value = ""
        intentos_text.value = "Intentos 0"
        verificar_btn.disabled = False
        page.update()
        
    titulo_juego = ft.Text("Juego de Adivinanzas", size=20, weight=ft.FontWeight.BOLD)
    input_numero = ft.TextField(label="Tu intento", width=100)
    verificar_btn = ft.ElevatedButton("Verificr", on_click=verificar_intento)
    resultado = ft.Text("Adivina el número  entre 1 y 10")
    intentos_text = ft.Text("Intentos 0")
    btn_reiniciar = ft.ElevatedButton("Reiniciar juego", on_click=reiniciar_juego)
    
    divider_simple = ft.Divider(height=1, color=ft.colors.BLUE_200)
    divider_vertical = ft.VerticalDivider(width=1, color=ft.colors.BLUE_200) #si es vertical tiene width
    
    card1  = ft.Card(
        content=ft.Container(
            content= ft.Column([titulo_juego, input_numero, verificar_btn, resultado, intentos_text, btn_reiniciar],
                               alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            padding=10
        ),
        width=300,
        height=400
    )
    
    def cambiar_tema(e):
        print("MODO: " , page.theme_mode)
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT  
            page.bgcolor = ft.colors.BLUE_GREY_100
            tema_btn.text = "Modo Oscuro"
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = ft.colors.BLUE_GREY_800
            tema_btn.text = "Modo Claro"
        page.update()
    
    titulo_tema = ft.Text("Cambiar Tema", size=20,  weight=ft.FontWeight.BOLD)
    tema_btn = ft.ElevatedButton("Modo Claro", on_click=cambiar_tema)
    
    columna_tema = ft.Column([titulo_tema, tema_btn],
                             alignment=ft.MainAxisAlignment.CENTER, spacing=20)
    
    card2 = ft.Card(
        content=ft.Container(
            content=columna_tema,
            padding=10
        ),
        width=200,
        height=150
    )
    
    layaout = ft.Row([
        card1, divider_vertical, card2
    ], alignment=ft.MainAxisAlignment.CENTER)
    
    divider_final = ft.Divider(height=1, color=ft.colors.BLUE_200)
    
    page.add(titulo, divider_simple, layaout, divider_final)
    
# Cards, Divider, Vertical Divider
ft.app(target=main)