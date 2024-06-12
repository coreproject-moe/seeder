import flet as ft


def main(page: ft.Page):
    page.title = "Flet counter example"

    page.fonts = {
        "Kokoro": "fonts/Kokoro/Regular.ttf",
        "Kokoro-Medium": "fonts/Kokoro/Medium.ttf",
        "Kokoro-Bold": "fonts/Kokoro/Bold.ttf",
    }
    page.theme = ft.Theme(
        font_family="Kokoro",
        color_scheme=ft.ColorScheme(
            secondary="#03020c"
        )
    )

    page.add(ft.Text("coreproject", color=ft.colors.BLUE_100))
    page.bgcolor = ft.colors.SECONDARY

    page.update()


if __name__ == "__main__":
    ft.app(main, assets_dir="assets/")
