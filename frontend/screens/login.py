import flet as ft


def login(router):
    # Função para validar login
    def realizar_login(e):
        email = email_field.value
        senha = password_field.value

        if email == "admin" and senha == "admin":
            print("Login de administrador bem-sucedido!")
            router.navigate_to("tela_cadastro")  # Redireciona para tela_cadastro
        else:
            print("Credenciais inválidas.")

    # Interface da tela
    logo = ft.Container(
        content=ft.Image(
            src=r"..\_IMG_PET_CARE\675ac9488896439ba6af16592ae468dc.png",
            fit=ft.ImageFit.CONTAIN,
            width=300,
            height=300,
        ),
        width=300,
        height=300,
        border_radius=75,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

    title = ft.Text(
        "PET CARE",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="#BB86FC",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                color="#BB86FC",
                blur_radius=15,
                spread_radius=5,
                offset=ft.Offset(0, 0),
            )
        ),
    )

    email_field = ft.TextField(
        label="E-mail",
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
    )

    password_field = ft.TextField(
        label="Senha",
        password=True,
        text_align=ft.TextAlign.LEFT,
        color="#BB86FC",
        bgcolor="#1A1A2E",
        border_color="#BB86FC",
        border_radius=12,
        width=350,
    )

    recuperar_senha_link = ft.ElevatedButton(
        text="Esqueci minha senha",
        on_click=lambda e: print("Recuperação de senha acionada"),
        style=ft.ButtonStyle(
            color="#6C63FF",
            bgcolor="#00000000",
            text_style=ft.TextStyle(
                decoration=ft.TextDecoration.UNDERLINE,
            ),
        ),
    )

    login_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Text("Entrar", color="#FFFFFF"),
                ft.Icon(name="login", color="#FFFFFF"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
        on_click=realizar_login,  # Chama a função de validação
        width=180,
        height=45,
        style=ft.ButtonStyle(
            bgcolor="#6C63FF",
            shadow_color="#6C63FF",
            elevation=10,
            overlay_color=ft.colors.with_opacity(0.2, ft.colors.WHITE),
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    # Botão de "Voltar"
    back_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name="arrow_back", color="#FFFFFF"),
                ft.Text("Voltar", color="#FFFFFF"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
        on_click=lambda e: router.go_back(),
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
            logo,
            ft.Container(content=title, padding=ft.padding.only(top=20, bottom=40)),
            email_field,
            ft.Container(content=password_field, padding=ft.padding.only(top=10, bottom=5)),
            recuperar_senha_link,
            ft.Container(content=login_button, padding=ft.padding.only(top=20)),
            ft.Container(content=back_button, padding=ft.padding.only(top=20)),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )
