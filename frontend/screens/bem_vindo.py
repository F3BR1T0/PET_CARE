import flet as ft


def bem_vindo(router):
    def navigate_to_login(e):
        router.navigate_to("login")

    def navigate_to_cadastro(e):
        router.navigate_to("cadastro")

    # Configuração do layout
    logo = ft.Container(
        content=ft.Image(
            src=r"..\_IMG_PET_CARE\675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.CONTAIN,
            width=300,
            height=300,
        ),
        width=300,
        height=300,
        border_radius=75,
        alignment=ft.alignment.center,
    )

    title = ft.Text("PET CARE", size=40, weight=ft.FontWeight.BOLD, color="#DDA0DD")
    subtitle = ft.Text("BEM-VINDO!", size=20, color="#BB86FC")
    sign_up_button = ft.ElevatedButton("Cadastrar", on_click=navigate_to_cadastro)
    sign_in_button = ft.ElevatedButton("Login", on_click=navigate_to_login)

    return ft.Column(
        controls=[
            logo,
            title,
            subtitle,
            sign_up_button,
            sign_in_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
