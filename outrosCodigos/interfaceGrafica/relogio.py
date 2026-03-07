import flet as ft
# print('ola, mundo')

def main(page:ft.Page):
    page.window.width = 800
    page.window.max_width = 800
    page.window.min_width = 800
    page.window.height = 500
    page.window.max_height = 500
    page.window.min_heidth = 500
    page.window.top = 500
    page.window.left = 250
    page.window.title_bar_hidden = False
    page.padding = 0

    stack_main = ft.Stack(
        expand = True,
        controls = [
            ft.WindowDragArea(expand=True, content=ft.Container(bgcolor='white'))
        ]
    )

    page.update(stack_main)

if __name__ == '__main__':
    ft.app(target=main)
    