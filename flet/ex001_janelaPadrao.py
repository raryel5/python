import flet as ft

def main(page: ft.Page):
    page.window.width = 300
    page.window.height = 500
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(

    )


if __name__ == "__main__":
    ft.app(target=main)