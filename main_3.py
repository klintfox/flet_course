import flet as ft

def main(page: ft.Page):
    page.title = "Mi app"
    page.bgcolor  = ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo  = ft.Text("Lista de tareas", size=26, color = ft.colors.WHITE)
    page.add(titulo)
    
    def agregar_tarea(e):
        if campo_tarea.value:
            tarea = ft.ListTile(title= ft.Text(campo_tarea.value),
                                leading=ft.Checkbox(on_change=seleccionar_tarea))
            tareas.append(tarea)
            campo_tarea.value = ""
            actualizar_lista()
            
    def seleccionar_tarea(e):
        seleccionadas = [t.title.value for t in tareas if t.leading.value]
        tareas_seleccionadas.value =  "Tareas seleccionadas: " + ", ".join(seleccionadas)
        page.update()
    
    def actualizar_lista():
        listar_tareas.controls.clear()
        listar_tareas.controls.extend(tareas)
        page.update()
        
    
    campo_tarea = ft.TextField(hint_text="Escriba la nueva tarea")
    boton_tarea= ft.FilledButton(text="Agregar Tarea", on_click=agregar_tarea)    
    listar_tareas = ft.ListView(expand=1, spacing=3) #expand = 1 utiliza todo el espacio si cambio a 1 se va a adaptando al tamaño
    
    tareas = []
    tareas_seleccionadas = ft.Text("", size=20, weight=ft.FontWeight.BOLD)
    
    page.add(campo_tarea, boton_tarea, listar_tareas, tareas_seleccionadas)
    
#ListView
ft.app(target=main)