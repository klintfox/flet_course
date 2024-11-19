import flet as ft
import random

def main(page: ft.Page):
    page.bgcolor  = ft.colors.BLUE_GREY_800
    page.title = "Juego de adivinanzas"
    page.theme_mode = ft.ThemeMode.DARK    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER    
    titulo  = ft.Text("Cards, Divider and Vertical Divider", size=30, weight=ft.FontWeight.BOLD)
    
    page.add(titulo)
    
# Cards, Divider, Vertical Divider
ft.app(target=main)