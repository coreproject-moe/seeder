import flet as ft


def custom_appbar(**extra_properties: ft.AppBar | None) -> ft.AppBar:
    appbar = ft.AppBar(
        title=ft.Image(src="/icons/logo.png", height=25),
        center_title=True,
        bgcolor="#03020c",
        **extra_properties,
    )

    return appbar
