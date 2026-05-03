import flet as ft

def main(page: ft.Page):
    page.title = "Copiar Caminho de Arquivo"

    # 1. Função que trata o arquivo selecionado
    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files:
            # Obtém o caminho absoluto do arquivo
            file_path = e.files[0].path
            
            # 2. Copia o caminho para a área de transferência
            page.clipboard.set_value(file_path)
            
            # Mostra uma mensagem de confirmação
            snack = ft.SnackBar(ft.Text(f"Caminho copiado: {file_path}"))
            page.overlay.append(snack)
            snack.open = True
            page.update()

    # Configura o FilePicker
    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    # Interface
    page.add(
        ft.ElevatedButton(
            "Selecionar Arquivo e Copiar Caminho",
            icon=ft.icons.FOLDER_OPEN,
            on_click=lambda _: file_picker.pick_files()
        )
    )

ft.app(target=main)
