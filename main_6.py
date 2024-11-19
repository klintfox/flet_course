import flet as ft
from openpyxl import Workbook
from datetime import datetime

def main(page: ft.Page):
    page.title = "Mi app"
    page.bgcolor  = ft.colors.BLUE_GREY_800
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo  = ft.Text("Datatable en Flet con Excel", size=26, color = ft.colors.WHITE)
    
    data_table = ft.DataTable(
        bgcolor=ft.colors.BLUE_GREY_700,
        border= ft.border.all(2, ft.colors.BLUE_GREY_200), #width=2
        border_radius=10,
        vertical_lines=ft.BorderSide(3, ft.colors.BLUE_GREY_200), #borde linas verticales
        horizontal_lines=ft.BorderSide(1, ft.colors.BLUE_GREY_400),
        columns =[
            ft.DataColumn(ft.Text("ID", color = ft.colors.BLUE_GREY_200)),
            ft.DataColumn(ft.Text("Nombre", color = ft.colors.BLUE_GREY_200)),
            ft.DataColumn(ft.Text("Edad", color = ft.colors.BLUE_GREY_200)),
        ],
        rows = []
    )        
    
    def agregar_fila(e):
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(len(data_table.rows) + 1 ), color=ft.colors.WHITE)),
                ft.DataCell(ft.Text(nombre_input.value, color=ft.colors.WHITE)),
                ft.DataCell(ft.Text(edad_input.value, color=ft.colors.WHITE)),
            ]
        )
        data_table.rows.append(nueva_fila)
        nombre_input.value  = ""
        edad_input.value = ""
        page.update()
        
    def guardar_excel(e):
        wb = Workbook()
        ws = wb.active
        ws.title = "BBDD"
        ws.append(["ID", "Nombre", "Edad"])
        for row in data_table.rows:
                ws.append([cell.content.value for cell in row.cells])
                
                fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
                nombre_archivo = f"{fecha_hora}_datos_tabla.xlsx"
                
                wb.save(nombre_archivo)
        
        snack_bar = ft.SnackBar(content=ft.Text(f"Datos guardados en {nombre_archivo}"))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()
                
        
    nombre_input = ft.TextField(label="Nombre" , bgcolor =ft.colors.BLUE_700, color = ft.colors.WHITE)
    edad_input = ft.TextField(label="Edad" , bgcolor =ft.colors.BLUE_700, color = ft.colors.WHITE)
    agregar_boton = ft.ElevatedButton("Agregar", on_click=agregar_fila, color = ft.colors.WHITE,
                                      bgcolor= ft.colors.BLUE)
    guardar_boton = ft.ElevatedButton("Guardar", on_click=guardar_excel, color = ft.colors.WHITE,
                                      bgcolor=ft.colors.GREEN)
    
    
    input_container = ft.Row(
        controls=[nombre_input, edad_input,agregar_boton,guardar_boton],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    page.add(titulo,data_table, input_container)
    
# Datatable
ft.app(target=main)