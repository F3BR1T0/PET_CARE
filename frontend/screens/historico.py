import flet as ft


def historico(router):
    def go_back(e):
        router.go_back()

    # Cabeçalho com logo e título
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
    )

    title = ft.Text(
        "HISTÓRICO",
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

    header = ft.Row(
        controls=[logo, title],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Campos de entrada para o ID do pet
    pet_id_field = ft.TextField(
        label="ID do Pet",
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=250,
    )

    nome_pet_display = ft.TextField(
        label="Nome do Pet",
        value="Exemplo: Rex",
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
    )

    # Listas de histórico
    datas_atendimento = ft.ListView(
        controls=[
            ft.Text("20/01/2023", text_align=ft.TextAlign.CENTER),
            ft.Text("15/03/2023", text_align=ft.TextAlign.CENTER),
            ft.Text("10/05/2023", text_align=ft.TextAlign.CENTER),
        ],
        spacing=10,
        padding=ft.padding.all(10),
        expand=True,
        height=100,
    )

    vacinas_list = ft.ListView(
        controls=[
            ft.Text("Vacina Anti-rábica - 20/01/2023", text_align=ft.TextAlign.CENTER),
            ft.Text("Vacina Polivalente - 15/03/2023", text_align=ft.TextAlign.CENTER),
        ],
        spacing=10,
        padding=ft.padding.all(10),
        expand=True,
        height=100,
    )

    consultas_list = ft.ListView(
        controls=[
            ft.Text("Consulta de rotina - 10/05/2023", text_align=ft.TextAlign.CENTER),
            ft.Text("Consulta com especialista - 20/06/2023", text_align=ft.TextAlign.CENTER),
        ],
        spacing=10,
        padding=ft.padding.all(10),
        expand=True,
        height=100,
    )

    cuidados_list = ft.ListView(
        controls=[
            ft.Text("Banho e Tosa - 05/04/2023", text_align=ft.TextAlign.CENTER),
            ft.Text("Higienização dos dentes - 25/07/2023", text_align=ft.TextAlign.CENTER),
        ],
        spacing=10,
        padding=ft.padding.all(10),
        expand=True,
        height=100,
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
        controls=[
            header,
            # Campos para ID do pet e nome
            ft.Container(content=pet_id_field, alignment=ft.alignment.center, padding=ft.padding.only(bottom=15)),
            ft.Container(content=nome_pet_display, alignment=ft.alignment.center, padding=ft.padding.only(bottom=20)),
            # Histórico de datas de atendimento
            ft.Text("Datas de Atendimento:", color="#BB86FC", size=16),
            datas_atendimento,
            # Histórico de vacinas
            ft.Text("Vacinas:", color="#BB86FC", size=16),
            vacinas_list,
            # Histórico de consultas
            ft.Text("Consultas:", color="#BB86FC", size=16),
            consultas_list,
            # Histórico de cuidados
            ft.Text("Cuidados:", color="#BB86FC", size=16),
            cuidados_list,
            # Botão "Voltar"
            ft.Container(content=back_button, alignment=ft.alignment.center, padding=ft.padding.only(top=20)),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )
