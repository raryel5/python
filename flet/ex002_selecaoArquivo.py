import flet as ft
# from flet import FilePickerUploadEvent
# para rodar em tempo real a aplicação:
# flet run nome.py

def main(page: ft.Page):
    page.window.width = 350
    page.window.height = 600
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    def get_file(e):
        if e.files:
            caminho.value = f"{e.files[0].path}"
            caminho.update()

    file = ft.FilePicker(
        on_result= get_file
    )

    page.overlay.append(file) # importante

    caminho = ft.TextField(
        width = 220,
        height = 60,
        border_radius = 16,
        border_width= 2,
        border_color= ft.Colors.BLACK_87,
        cursor_color= ft.Colors.RED
    )

    botao = ft.IconButton(
        icon= ft.Icons.FILE_OPEN,
        icon_color= ft.Colors.RED,
        on_click= lambda _: file.pick_files()
    )

    page.add(
        ft.Row(
            [caminho, botao],
            alignment= ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == "__main__":
    ft.app(target=main)