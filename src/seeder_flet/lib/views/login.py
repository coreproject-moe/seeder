import flet as ft

__all__ = ["login_view"]


def handle_login_click():
    pass


def login_view(page: ft.Page):
    return ft.Row(
        expand=True,
        controls=[
            ft.Column(
                [
                    ft.Text("Login to Continue", color=ft.colors.BLUE_100, size=20),
                    ft.TextField(
                        label="Username/Email address",
                        width=400,
                        height=50,
                        # hint_text="soraamamiya#4444",
                        border_color=ft.colors.TERTIARY,
                        focused_border_color=ft.colors.PRIMARY,
                        border_radius=10,
                        label_style=ft.TextStyle(color=ft.colors.BLUE_100),
                    ),
                    ft.TextField(
                        label="Password",
                        password=True,
                        can_reveal_password=True,
                        # hint_text="soraamamiya",
                        width=400,
                        height=50,
                        border_color=ft.colors.TERTIARY,
                        focused_border_color=ft.colors.PRIMARY,
                        border_radius=10,
                        label_style=ft.TextStyle(color=ft.colors.BLUE_100),
                    ),
                    ft.TextField(
                        label="Backend URL",
                        hint_text="backend.coreproject.moe",
                        width=400,
                        height=50,
                        border_color=ft.colors.TERTIARY,
                        focused_border_color=ft.colors.PRIMARY,
                        border_radius=10,
                        label_style=ft.TextStyle(color=ft.colors.BLUE_100),
                    ),
                    ft.FilledButton(
                        "Log in",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            color={ft.MaterialState.DEFAULT: ft.colors.BLUE_100},
                            bgcolor=ft.colors.TERTIARY,
                        ),
                        on_click=handle_login_click(),
                        height=40,
                        width=200,
                    ),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
    )
