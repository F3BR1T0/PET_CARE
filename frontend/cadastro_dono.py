import flet as ft


def main(page: ft.Page):
    # Configurações da página
    page.title = "Cadastro - Dono"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = "#0D0028"  # Fundo ainda mais escuro para destacar o tema neon

    # Imagem circular do cabeçalho
    logo = ft.Container(
        content=ft.Image(
            src=r"675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.COVER,
            width=60,
            height=60,
        ),
        width=60,
        height=60,
        border_radius=30,  # Tornando a imagem circular
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

    # Título com efeito neon
    title = ft.Text(
        "CADASTRO - DONO",
        size=24,
        weight=ft.FontWeight.BOLD,
        color="#E0BBE4",  # Roxo neon claro
        text_align=ft.TextAlign.LEFT,
        style=ft.TextStyle(shadow=ft.BoxShadow(
            color="#E0BBE4",
            blur_radius=10,
            offset=ft.Offset(0, 0)
        ),
        )
    )

    # Cabeçalho com imagem e título alinhados
    header = ft.Row(
        controls=[
            logo,
            ft.Container(content=title, padding=ft.padding.only(left=10))  # Espaçamento entre imagem e título
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0
    )

    # Botão para inserir foto do usuário com ícone à esquerda
    insert_photo_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name="photo_camera", color=ft.colors.WHITE),  # Ícone de câmera
                ft.Text("Inserir Foto", color=ft.colors.WHITE)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5
        ),
        on_click=lambda e: print("Foto inserida"),
        width=180,
        height=40,
        style=ft.ButtonStyle(
            bgcolor="#8A2BE2",  # Roxo neon
            shadow_color="#8A2BE2",
            elevation=8,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    # Campo para exibir o ID do usuário dentro de um TextField desabilitado
    user_id_display = ft.TextField(
        value="ID do Usuário: 123456",  # Exemplo de ID
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        color="#BB86FC",  # Lilás neon para contraste
        bgcolor="#0D0028",
        border_color="#BB86FC",
        border_radius=10,
        width=200
    )

    # Campos de texto adicionais para Nome, CPF, Endereço, Telefone e Email
    nome_field = ft.TextField(
        label="Nome",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#0D0028",
        border_color="#BB86FC",
        border_radius=10,
        width=300
    )

    cpf_field = ft.TextField(
        label="CPF",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#0D0028",
        border_color="#BB86FC",
        border_radius=10,
        width=300
    )

    endereco_field = ft.TextField(
        label="Endereço",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#0D0028",
        border_color="#BB86FC",
        border_radius=10,
        width=300
    )

    telefone_field = ft.TextField(
        label="Telefone",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#0D0028",
        border_color="#BB86FC",
        border_radius=10,
        width=300
    )

    email_field = ft.TextField(
        label="Email",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#0D0028",
        border_color="#BB86FC",
        border_radius=10,
        width=300
    )

    # Botões de "Voltar" e "Prosseguir" com ícones
    back_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name="arrow_back", color="#FFFFFF"),  # Ícone de seta para a esquerda
                ft.Text("Voltar", color="#FFFFFF")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5
        ),
        on_click=lambda e: print("Voltar clicado"),
        width=140,
        height=40,
        style=ft.ButtonStyle(
            bgcolor="#FF8A65",  # Laranja neon mais claro
            shadow_color="#FF8A65",
            elevation=8,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    next_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Text("Prosseguir", color="#FFFFFF"),
                ft.Icon(name="arrow_forward", color="#FFFFFF")  # Ícone de seta para a direita
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5
        ),
        on_click=lambda e: print("Prosseguir clicado"),
        width=140,
        height=40,
        style=ft.ButtonStyle(
            bgcolor="#8A2BE2",  # Roxo neon mais claro
            shadow_color="#8A2BE2",
            elevation=8,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    # Layout principal
    page.add(
        ft.Column(
            controls=[
                # Cabeçalho
                ft.Container(
                    content=header,
                    alignment=ft.alignment.center,
                    padding=ft.padding.all(20)
                ),
                # Inserir Foto e ID do Usuário
                ft.Container(
                    content=insert_photo_button,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=20, bottom=10)
                ),
                ft.Container(
                    content=user_id_display,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(bottom=10)
                ),
                # Campos de texto adicionais
                ft.Container(content=nome_field, padding=ft.padding.only(bottom=10)),
                ft.Container(content=cpf_field, padding=ft.padding.only(bottom=10)),
                ft.Container(content=endereco_field, padding=ft.padding.only(bottom=10)),
                ft.Container(content=telefone_field, padding=ft.padding.only(bottom=10)),
                ft.Container(content=email_field, padding=ft.padding.only(bottom=20)),
                # Botões de navegação
                ft.Row(
                    controls=[back_button, next_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


# Executando o app
ft.app(target=main, assets_dir='..\_IMG_PET_CARE')
