import flet as ft
import random

def main(page: ft.Page):
    page.title = "Mi app"
    page.bgcolor  = ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo  = ft.Text("Tabs", size=26, color = ft.colors.WHITE)
    
    
    def generar_tareas():
        tareas = [
            "Levantarse","Tomar Desayuno","Estudiar","Tomar Agua","Cocinar",
            "Almorzar", "Leer", "Merendar"
        ]
        return random.sample(tareas,4)
    
    lista_tareas = ft.ListView(spacing=20, padding=20)
    
    def actualizar_tareas():
        lista_tareas.controls.clear()
        for tarea in generar_tareas():
            lista_tareas.controls.append(ft.Text(tarea, color=ft.colors.WHITE))
        page.update()

    actualizar_tareas()
    
    # Contenido para la pestaña Tareas
    boton_actualizar = ft.ElevatedButton("Actualizar tarea", on_click=lambda _:actualizar_tareas())
    contenido_tareas = ft.Column([lista_tareas, boton_actualizar])
    
    # Contenido para la pestaña Perfil
    campo_nombre = ft.TextField(label="Nombre", bgcolor=ft.colors.BLUE_GREY_700)
    campo_email = ft.TextField(label="Email", bgcolor=ft.colors.BLUE_GREY_700)
    boton_guardar = ft.ElevatedButton("Guardar Perfil")
    contenido_perfil = ft.Column([campo_nombre, campo_email, boton_guardar])
    
    # Contenido Settings
    switch_notificaciones = ft.Switch(label="Notificaciones",value=True)
    slider_volumen = ft.Slider(min=0, max=100, divisions=10, label="Volumen")
    contenido_config = ft.Column([switch_notificaciones, slider_volumen])
    
    # Tabs
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Tareas", icon=ft.icons.LIST_ALT, content=contenido_tareas),
            ft.Tab(text="Tareas", icon=ft.icons.PERSON, content=contenido_perfil),
            ft.Tab(text="Tareas", icon=ft.icons.SETTINGS, content=contenido_config),
        ],
        expand=1
    )
    
    page.add(titulo, tabs)

# Tabs 
ft.app(target=main)