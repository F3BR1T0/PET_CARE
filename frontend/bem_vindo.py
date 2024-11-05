import flet as ft
from partials.todos import obter_btn_style, obter_prev_button


def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "Bem Vindo!"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#1B003A"  # Fundo escuro para destacar o neon

    # Configuração da imagem do logo
    logo = ft.Image(
        src=r"675ac9488896439ba6af16592ae468dc.png",
        fit=ft.ImageFit.CONTAIN,
        width=150,
        height=150,
    )

    # Título com estilo neon
    title = ft.Text(
        "PET CARE",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#DDA0DD",  # Roxo neon claro
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(shadow=ft.BoxShadow(
                color="#DDA0DD",
                blur_radius=12,
                offset=ft.Offset(0, 0)
            ),
        )
    )

    # Subtítulo com efeito neon
    subtitle = ft.Text(
        "BEM-VINDO!".upper(),
        size=20,
        color="#BB86FC",  # Lilás neon para contraste
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=8,
                offset=ft.Offset(0, 0)
            ),
        )
    )

    # Botão de "Cadastrar" com estilo neon
    sign_up_button = ft.ElevatedButton(
        text="Cadastrar",
        width=200,
        height=50,
        on_click=lambda e: print("Cadastrado"),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",  # Roxo neon
            color=ft.colors.WHITE,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            shadow_color="#8A2BE2",
            elevation=10,
        ),
        # animate=ft.Animation(duration=400, curve=ft.AnimationCurve.EASE_IN_OUT),
    )

    # Botão de "Login" com estilo neon
    sign_in_button = ft.ElevatedButton(
        text="Login",
        width=200,
        height=50,
        on_click=lambda e: print("Logado"),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",  # Roxo neon
            color=ft.colors.WHITE,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            shadow_color="#8A2BE2",
            elevation=10,
        ),
        # animate=ft.Animation(duration=400, curve=ft.AnimationCurve.EASE_IN_OUT),
    )

    # Botão "Anterior" com ajuste ao estilo neon
    prev_button = obter_prev_button()
    prev_button.style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=12),
        bgcolor="#FF8A65",
        color=ft.colors.WHITE,
        shadow_color="#FF8A65",
        elevation=10,
    )

    # Layout com espaçamento e alinhamento
    page.add(
        ft.Column(
            [
                subtitle,
                ft.Container(content=logo, alignment=ft.alignment.center, padding=ft.padding.only(bottom=20)),
                title,
                ft.Container(content=sign_up_button, padding=ft.padding.only(top=30)),
                ft.Container(content=sign_in_button, padding=ft.padding.only(top=10)),
                ft.Container(content=prev_button, padding=ft.padding.only(top=30))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
        )
    )


# Executando o app
ft.app(target=main, assets_dir='..\_IMG_PET_CARE')
