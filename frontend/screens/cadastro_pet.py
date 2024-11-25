import flet as ft
from datetime import datetime


def cadastro_pet(router):
    def go_back(e):
        router.go_back()

    def save_pet_data(e):
        print("Dados do pet salvos!")

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
        "CADASTRO - PET",
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

    # Campos de entrada para o pet
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

    dono_id_display = ft.TextField(
        value="ID do Dono: 654321",
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=250,
    )

    nome_field = ft.TextField(
        label="Nome do Pet",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
    )

    raca_field = ft.TextField(
        label="Raça do Pet",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
    )

    # Data de nascimento e idade do pet
    nascimento_field = ft.TextField(
        label="Data de Nascimento",
        read_only=True,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
    )

    idade_pet_display = ft.TextField(
        label="Idade do Pet (em anos)",
        read_only=True,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=170,
    )

    idade_humana_display = ft.TextField(
        label="Idade em Anos Humanos",
        read_only=True,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=170,
    )

    def atualizar_idade(data_nascimento):
        if data_nascimento:
            hoje = datetime.now()
            idade = hoje.year - data_nascimento.year - (
                (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
            )
            idade_pet_display.value = str(idade)
            idade_humana_display.value = str(idade * 7)
            router.page.update()

    date_picker_button = ft.IconButton(
        icon=ft.icons.CALENDAR_MONTH,
        icon_size=24,
        icon_color="#BB86FC",
        on_click=lambda e: router.page.open(
            ft.DatePicker(
                first_date=datetime(2000, 1, 1),
                last_date=datetime(2030, 12, 31),
                on_change=lambda e: (
                    setattr(nascimento_field, "value", e.control.value.strftime("%d/%m/%Y")),
                    atualizar_idade(e.control.value),
                ),
            )
        ),
    )

    # Outros campos de entrada
    altura_field = ft.TextField(
        label="Altura (em metros)",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
    )

    peso_field = ft.TextField(
        label="Peso (em kg)",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
    )

    tipo_pet_dropdown = ft.Dropdown(
        label="Tipo do Pet",
        options=[
            ft.dropdown.Option("Cachorro"),
            ft.dropdown.Option("Gato"),
            ft.dropdown.Option("Pássaro"),
            ft.dropdown.Option("Coelho"),
            ft.dropdown.Option("Outros"),
        ],
        width=350,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
    )

    observacoes_field = ft.TextField(
        label="Observações",
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
        on_click=save_pet_data,
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
            ft.Container(content=pet_id_display, alignment=ft.alignment.center, padding=ft.padding.only(bottom=5)),
            ft.Container(content=dono_id_display, alignment=ft.alignment.center, padding=ft.padding.only(bottom=15)),
            nome_field,
            raca_field,
            ft.Row(
                controls=[nascimento_field, date_picker_button],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[idade_pet_display, idade_humana_display],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            altura_field,
            peso_field,
            tipo_pet_dropdown,
            observacoes_field,
            ft.Row(
                controls=[back_button, save_button],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.alignment.top_center,
                spacing=20,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )
