import flet as ft


def main(page: ft.Page):
    # Definindo o layout da página
    page.title = "Pet CARE"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.PURPLE
    # Criando os widgets da interface
    logo = ft.Image(
        src=r"..\_IMG_PET_CARE\675ac9488896439ba6af16592ae468dc.png",
        fit=ft.ImageFit.COVER,
        width=200,
        height=200,
    )

    title = ft.Text("PET CARE", size=40, weight=ft.FontWeight.BOLD)

    subtitle = ft.Text("Seu amigo em boas mãos", size=20)

    btn_style = ft.ButtonStyle(
        color={ft.ControlState.DEFAULT: ft.colors.WHITE, ft.ControlState.HOVERED: ft.colors.PURPLE},
        bgcolor={ft.ControlState.DEFAULT: ft.colors.PURPLE, ft.ControlState.HOVERED: ft.colors.WHITE},
    )

    next_button = ft.ElevatedButton("Próximo", on_click=lambda e: print("Próximo"), style=btn_style)

    # Adicionando ao layout
    page.add(
        ft.Column(
            [
                ft.Container(content=logo, alignment=ft.alignment.center),
                title,
                subtitle,
                next_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


# Executando o app
ft.app(target=main, assets_dir='assets')
