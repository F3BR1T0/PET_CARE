import flet as ft


def tela_cadastro(router):
    # Funções de navegação
    def navigate_to_cadastro_dono(e):
        router.navigate_to("cadastro_dono")

    def navigate_to_cadastro_vet(e):
        router.navigate_to("cadastro_vet")

    def navigate_to_cadastro_pet(e):
        router.navigate_to("cadastro_pet")

    def navigate_to_ficha(e):
        router.navigate_to("ficha")

    def navigate_to_historico(e):
        router.navigate_to("historico")

    def go_back(e):
        router.go_back()

    # Logo
    logo = ft.Container(
        content=ft.Image(
            src=r"../_IMG_PET_CARE/675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.CONTAIN,
            width=50,
            height=50,
        ),
        width=50,
        height=50,
        border_radius=25,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        alignment=ft.alignment.center,
    )

    # Título
    title = ft.Text(
        "Cadastros",
        size=36,
        weight=ft.FontWeight.BOLD,
        color="#DDA0DD",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#DDA0DD",
                blur_radius=10,
                spread_radius=5,
                offset=ft.Offset(0, 0),
            )
        ),
    )

    # Subtítulo
    subtitle = ft.Text(
        "Escolha o tipo de cadastro ou consulta desejada",
        size=18,
        color="#BB86FC",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=6,
                spread_radius=3,
                offset=ft.Offset(0, 0),
            )
        ),
    )

    # Botões de navegação
    cadastro_dono_button = ft.ElevatedButton(
        text="Cadastro de Dono",
        width=250,
        height=50,
        on_click=navigate_to_cadastro_dono,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",
            color=ft.colors.WHITE,
            shadow_color="#8A2BE2",
            elevation=10,
        ),
    )

    cadastro_vet_button = ft.ElevatedButton(
        text="Cadastro de Veterinário",
        width=250,
        height=50,
        on_click=navigate_to_cadastro_vet,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",
            color=ft.colors.WHITE,
            shadow_color="#8A2BE2",
            elevation=10,
        ),
    )

    cadastro_pet_button = ft.ElevatedButton(
        text="Cadastro de Pet",
        width=250,
        height=50,
        on_click=navigate_to_cadastro_pet,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",
            color=ft.colors.WHITE,
            shadow_color="#8A2BE2",
            elevation=10,
        ),
    )

    ficha_button = ft.ElevatedButton(
        text="Ficha",
        width=250,
        height=50,
        on_click=navigate_to_ficha,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",
            color=ft.colors.WHITE,
            shadow_color="#8A2BE2",
            elevation=10,
        ),
    )

    historico_button = ft.ElevatedButton(
        text="Histórico",
        width=250,
        height=50,
        on_click=navigate_to_historico,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor="#8A2BE2",
            color=ft.colors.WHITE,
            shadow_color="#8A2BE2",
            elevation=10,
        ),
    )

    # Botão "Voltar"
    back_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name="arrow_back", color="#FFFFFF"),
                ft.Text("Voltar", color="#FFFFFF"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
        on_click=go_back,
        width=160,
        height=45,
        style=ft.ButtonStyle(
            bgcolor="#FF8A65",
            shadow_color="#FF8A65",
            elevation=10,
            overlay_color=ft.colors.with_opacity(0.2, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    # Layout principal
    return ft.Column(
        [
            ft.Row(controls=[logo, title], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(content=subtitle, alignment=ft.alignment.center, padding=ft.padding.only(bottom=20)),
            ft.Row([cadastro_dono_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Row([cadastro_vet_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Row([cadastro_pet_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Row([ficha_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Row([historico_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ft.Container(content=back_button, padding=ft.padding.only(top=30)),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
    )
