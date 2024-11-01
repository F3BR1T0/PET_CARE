import flet as ft
from partials.todos import obter_btn_style


def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "Splash"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#1B003A"  # Fundo roxo escuro para destaque neon

    # Configuração da imagem do logo
    logo = ft.Image(
        src=r"675ac9488896439ba6af16592ae468dc.png",
        fit=ft.ImageFit.CONTAIN,
        width=180,
        height=180,
    )

    # Texto principal com efeito neon
    title = ft.Text(
        "PET CARE",
        size=42,
        weight=ft.FontWeight.BOLD,
        color="#DDA0DD",  # Roxo neon claro
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(shadow=ft.BoxShadow(
            color="#DDA0DD",
            blur_radius=12,
            offset=ft.Offset(0, 0)
        ))
    )

    # Subtítulo com descrição e efeito de brilho
    subtitle = ft.Text(
        "Seu amigo em boas mãos",
        size=20,
        color="#BB86FC",  # Tom lilás neon para contraste
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=8,
                offset=ft.Offset(0, 0)
            )
        ),
    )

    # Botão "Próximo" com estilo neon
    next_button = ft.ElevatedButton(
        text="Próximo",
        width=150,
        height=45,
        on_click=lambda e: print("Próximo"),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",  # Tom roxo neon
            color=ft.colors.WHITE,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            shadow_color="#8A2BE2",
            elevation=10
        ),
        # animate=ft.Animation(duration=500, curve=ft.AnimationCurve.EASE_OUT),
    )

    # Layout com espaçamento e alinhamento
    splash_content = ft.Column(
        controls=[
            ft.Container(
                content=logo,
                alignment=ft.alignment.center,
                padding=ft.padding.only(bottom=20),
            ),
            title,
            subtitle,
            ft.Container(
                content=next_button,
                padding=ft.padding.only(top=30),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=8,
    )

    # Adicionando o layout à página
    page.add(splash_content)


# Executando o app
ft.app(target=main, assets_dir='..\_IMG_PET_CARE')
