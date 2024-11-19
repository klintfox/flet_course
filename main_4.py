import flet as ft

def main(page: ft.Page):
    page.title = "Mi app"
    page.bgcolor  = ft.colors.BLUE_GREY_800
    page.padding = 20
    page.theme_mode = "light"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo  = ft.Text("Lista de tareas", size=26, color = ft.colors.WHITE)
    page.add(titulo)
    
    
    
    def add_note(e):
        new_note = create_note("Nueva nota")
        grid.controls.append(new_note)
        page.update()
    
    def delete_note(note):
        grid.controls.remove(note)
        page.update()    
    
    def create_note(text):
        note_content = ft.TextField(value=text, multiline=True,
                                    bgcolor=ft.colors.BLUE_GREY_200)
        note = ft.Container(
            content= ft.Column([note_content,  ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _:delete_note(note))]),
            width=200,
            height=200,
            bgcolor=ft.colors.BLUE_GREY_400,
            border_radius=10,
            padding=10        
        )
        return note
        
    grid = ft.GridView(
        expand=True, 
        max_extent=200,
        child_aspect_ratio=1,
        spacing=10, #espacio vertical
        run_spacing=10 #espacio horizontal
        #horizontal=False # Si cambia a True los spacios se invierten
    )
        
    notes = [
        "Mi primera nota",
        "Mi segunda nota",
        "Mi tercera nota"
    ]
    
    for note in notes:
        grid.controls.append(create_note(note))
        
    page.add(
        ft.Row([
                ft.Text("Mis notas adehsivas", size=24, weight="bold",
                        color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.ADD, on_click=add_note, icon_color=ft.colors.WHITE)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), grid
    )
    

#Tablero de notas - Grid
ft.app(target=main)