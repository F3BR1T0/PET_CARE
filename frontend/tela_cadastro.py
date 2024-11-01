import flet as ft
from partials.todos import obter_btn_style, obter_prev_button


def main(page: ft.Page):
    # Configurações da página
    page.title = "Cadastro"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#1B003A"  # Fundo roxo escuro para destaque neon

    # Logo reduzido com ajuste de efeito neon
    logo = ft.Image(
        src=r"assets/_IMG_PET_CARE/675ac9488896439ba6af16592ae468dc.png",
        fit=ft.ImageFit.CONTAIN,
        width=50,
        height=50,
    )

    # Título com efeito neon
    title = ft.Text(
        "Cadastros",
        size=36,
        weight=ft.FontWeight.BOLD,
        color="#DDA0DD",  # Roxo neon claro
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(shadow=ft.BoxShadow(
                color="#DDA0DD",
                blur_radius=10,
                offset=ft.Offset(0, 0)
            ),
        )
    )

    # Subtítulo com tom lilás neon
    subtitle = ft.Text(
        "Nesta tela você escolhe o seu tipo de perfil",
        size=18,
        color="#BB86FC",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=6,
                offset=ft.Offset(0, 0)
            ),
        )
    )

    # Botão "Cadastrar Usuário" com estilo neon
    sign_up_user = ft.ElevatedButton(
        text="Cadastrar Usuário",
        width=200,
        height=50,
        on_click=lambda e: print("Cadastrado Usuário"),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",
            color=ft.colors.WHITE,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            shadow_color="#8A2BE2",
            elevation=10,
        ),
        # animate=ft.Animation(duration=400, curve=ft.AnimationCurve.EASE_IN_OUT),
    )

    # Botão "Cadastrar Veterinário" com estilo neon
    sign_up_vet = ft.ElevatedButton(
        text="Cadastrar Veterinário",
        width=200,
        height=50,
        on_click=lambda e: print("Cadastrado Veterinário"),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",
            color=ft.colors.WHITE,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            shadow_color="#8A2BE2",
            elevation=10,
        ),
        # animate=ft.Animation(duration=400, curve=ft.AnimationCurve.EASE_IN_OUT),
    )

    # Fila para CPF e botão de cadastro de usuário
    row_sgnup_user = ft.Row(
        [
            ft.Text('CPF:', color="#BB86FC", size=16, weight=ft.FontWeight.BOLD),
            sign_up_user
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Fila para CRMV e botão de cadastro de veterinário
    row_sgnup_vet = ft.Row(
        [
            ft.Text('CRMV:', color="#BB86FC", size=16, weight=ft.FontWeight.BOLD),
            sign_up_vet
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Botão "Anterior" com efeito neon
    prev_button = obter_prev_button(140)
    prev_button.style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=12),
        bgcolor="#FF8A65",
        color=ft.colors.WHITE,
        shadow_color="#FF8A65",
        elevation=10,
    )

    # Layout principal com alinhamento
    page.add(
        ft.Column(
            [
                ft.Row(
                    controls=[
                        ft.Container(content=logo, alignment=ft.alignment.center, padding=ft.padding.only(right=10)),
                        title
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(subtitle, alignment=ft.alignment.center, padding=ft.padding.only(bottom=20)),
                row_sgnup_user,
                row_sgnup_vet,
                ft.Container(prev_button, padding=ft.padding.only(top=20))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
        )
    )


# Executando o app
ft.app(target=main, assets_dir='assets')
