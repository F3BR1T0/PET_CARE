import flet as ft
from datetime import datetime


def ficha(router):
    def go_back(e):
        router.go_back()

    def save_ficha_data(e):
        print("Ficha do pet salva!")

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
        "FICHA",
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

    # Campos de entrada para a ficha
    pet_id_display = ft.TextField(
        value="ID do Pet: 123456",
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=250,
    )

    nome_pet_field = ft.TextField(
        label="Nome do Pet",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
    )

    consulta_date_field = ft.TextField(
        label="Data da Consulta",
        read_only=True,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
    )

    def atualizar_data(e):
        if e.control.value:
            consulta_date_field.value = e.control.value.strftime("%d/%m/%Y")
            router.page.update()

    date_picker_button = ft.IconButton(
        icon=ft.icons.CALENDAR_MONTH,
        icon_size=24,
        icon_color="#BB86FC",
        on_click=lambda e: router.page.open(
            ft.DatePicker(
                first_date=datetime(2020, 1, 1),
                last_date=datetime(2030, 12, 31),
                on_change=atualizar_data,
            )
        ),
    )

    medicamentos_field = ft.TextField(
        label="Descrição dos Medicamentos",
        multiline=True,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
        height=150,
    )

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
        on_click=save_ficha_data,
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
            header,
            ft.Container(content=pet_id_display, alignment=ft.alignment.center, padding=ft.padding.only(bottom=15)),
            nome_pet_field,
            ft.Row(
                controls=[consulta_date_field, date_picker_button],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Container(content=medicamentos_field, padding=ft.padding.only(top=15, bottom=15)),
            ft.Row(
                controls=[back_button, save_button],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )
