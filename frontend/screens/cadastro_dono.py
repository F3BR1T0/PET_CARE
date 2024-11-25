import flet as ft


def cadastro_dono(router):
    def go_back(e):
        router.go_back()

    def save_data(e):
        print("Dados do dono salvos!")

    # Configurações da interface
    logo = ft.Container(
        content=ft.Image(
            src=r"..\_IMG_PET_CARE\675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.COVER,
            width=80,
            height=80,
        ),
        width=80,
        height=80,
        border_radius=40,
        border=ft.border.all(3, color="#BB86FC"),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

    title = ft.Text(
        "CADASTRO - DONO",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="#BB86FC",
        text_align=ft.TextAlign.LEFT,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=15,
                spread_radius=5,
                offset=ft.Offset(0, 0),
            )
        ),
    )

    header = ft.Row(
        controls=[logo, ft.Container(content=title, padding=ft.padding.only(left=15))],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Campos de entrada para dados do dono
    def create_text_field(label):
        return ft.TextField(
            label=label,
            text_align=ft.TextAlign.LEFT,
            color="#BB86FC",
            bgcolor="#1A1A2E",
            border_color="#BB86FC",
            border_radius=12,
            width=350,
        )

    nome_field = create_text_field("Nome")
    cpf_field = create_text_field("CPF")
    endereco_field = create_text_field("Endereço")
    telefone_field = create_text_field("Telefone")
    email_field = create_text_field("Email")

    # Botões
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

    save_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Text("Salvar", color="#FFFFFF"),
                ft.Icon(name="save", color="#FFFFFF"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
        on_click=save_data,
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
            ft.Container(content=header, alignment=ft.alignment.center, padding=ft.padding.all(20)),
            # Campos de entrada
            ft.Container(content=nome_field, padding=ft.padding.only(bottom=15)),
            ft.Container(content=cpf_field, padding=ft.padding.only(bottom=15)),
            ft.Container(content=endereco_field, padding=ft.padding.only(bottom=15)),
            ft.Container(content=telefone_field, padding=ft.padding.only(bottom=15)),
            ft.Container(content=email_field, padding=ft.padding.only(bottom=20)),
            # Botões
            ft.Row(controls=[back_button, save_button], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )
