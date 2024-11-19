import flet as ft
import time

def main(page: ft.Page):    
    page.title = "Simulador de Descarga"
    page.bgcolor  = ft.colors.BLUE_GREY_800    
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER      
    
    titulo  = ft.Text("Simulador de Descarga", size=24, color = ft.colors.WHITE)
    archivos  = ft.Text("Selecciona archivo para descargar", size=16, color = ft.colors.WHITE)
    file_list = ft.Column([
        ft.Checkbox(label="Documento pdf (2.5 MB)", value=False),
        ft.Checkbox(label="Imagen.jpg (1.2 MB)", value=False),
        ft.Checkbox(label="Video.map (20 MB)", value=False),
        ft.Checkbox(label="Archivo.zip (10 MB)", value=False)
    ])
    
    def simular_descarga(e):
        archivos_seleccionados = [checkbox for checkbox in file_list.controls if checkbox.value]
        if not archivos_seleccionados:
            status_text.value = "Por favor, selecciona un archivo."
            page.update()
            return
        progress_bar.value = 0
        progress_ring.value = 0
        page.update()
        
        total_size = sum([float(archivo.label.split("(")[1].split(" MB")[0]) for archivo in archivos_seleccionados])
        downloaded = 0
        for archivo in archivos_seleccionados:
            file_size = float(archivo.label.split("(")[1].split(" MB")[0])
            status_text.value = f"Descarga {archivo.label}..."
            
            for _ in range(10):
                time.sleep(0.2)
                downloaded += file_size/ 10
                progress = min(downloaded / total_size, 1) # 1 es el maximo
                progress_bar.value = progress
                progress_ring.value = progress
                page.update()

        # Se actualiza el valor y mensaje
        progress_bar.value = 1
        progress_ring.value = 1
        status_text.value = "Descarga Completada"
        page.update()
        
        #Reinicia a cero despues de 1 segundo
        time.sleep(1)
        progress_bar.value = 0
        progress_ring.value = 0
        status_text.value = ""
        for checkbox in file_list.controls:
            checkbox.value = False
        page.update()
    
    contenedor = ft.Container(content=file_list, padding=20)
    
    progress_bar = ft.ProgressBar(width=400, color="amber", bgcolor="#263238", value=0 )
    progress_ring = ft.ProgressRing(stroke_width=5, color="amber", value=0)
    fila = ft.Row([progress_bar, progress_ring, ], alignment=ft.MainAxisAlignment.CENTER)
    status_text = ft.Text("", color=ft.colors.WHITE)
    boton_descarga = ft.ElevatedButton("Iniciar Descarga", on_click=simular_descarga, bgcolor=ft.colors.AMBER, color=ft.colors.BLACK)
    
    page.add(titulo, archivos, contenedor, fila, status_text, boton_descarga)
    
# Simulador de descargas
ft.app(target=main)