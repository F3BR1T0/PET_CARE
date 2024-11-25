import flet as ft


def splash(router):
    def navigate_to_bem_vindo(e):
        router.navigate_to("bem_vindo")

    # Configuração da imagem do logo
    logo = ft.Container(
        content=ft.Image(
            src=r"..\_IMG_PET_CARE\675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.CONTAIN,
            width=400,
            height=400,
        ),
        width=400,
        height=400,
        border_radius=200,
        alignment=ft.alignment.center,
        padding=ft.padding.only(bottom=20),
    )

    # Título "PET CARE" com efeito neon
    title = ft.Text(
        "PET CARE",
        size=42,
        weight=ft.FontWeight.BOLD,
        color="#DDA0DD",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#DDA0DD",
                blur_radius=12,
                spread_radius=5,
                offset=ft.Offset(0, 0),
            )
        ),
    )

    # Subtítulo com descrição e efeito de brilho
    subtitle = ft.Text(
        "Seu amigo em boas mãos",
        size=20,
        color="#BB86FC",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=8,
                spread_radius=3,
                offset=ft.Offset(0, 0),
            )
        ),
    )

    # Botão "Próximo" com ação de navegação
    next_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Text("Prosseguir", color="#FFFFFF"),
                ft.Icon(name="arrow_forward", color="#FFFFFF"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
        on_click=navigate_to_bem_vindo,
        width=160,
        height=45,
        style=ft.ButtonStyle(
            bgcolor="#6C63FF",
            shadow_color="#6C63FF",
            elevation=10,
            overlay_color=ft.colors.with_opacity(0.2, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    # Layout principal
    return ft.Column(
        controls=[
            logo,
            title,
            subtitle,
            ft.Container(content=next_button, padding=ft.padding.only(top=30)),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )
