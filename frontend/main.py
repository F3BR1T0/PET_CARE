from flet import Page
from router import Router
from screens.splash import splash
from screens.bem_vindo import bem_vindo
from screens.login import login
from screens.cadastro_dono import cadastro_dono
from screens.cadastro_pet import cadastro_pet
from screens.cadastro_vet import cadastro_vet
from screens.ficha import ficha
from screens.historico import historico
from screens.tela_cadastro import tela_cadastro


def main(page: Page):
    page.title = "PET CARE - Navegação Modular"
    router = Router(page)

    # Registro das rotas
    router.register_route("splash", splash)
    router.register_route("bem_vindo", bem_vindo)
    router.register_route("login", login)
    router.register_route("cadastro_dono", cadastro_dono)
    router.register_route("cadastro_pet", cadastro_pet)
    router.register_route("cadastro_vet", cadastro_vet)
    router.register_route("ficha", ficha)
    router.register_route("historico", historico)
    router.register_route("tela_cadastro", tela_cadastro)

    # Tela inicial
    router.navigate_to("splash")


# Executa o app
if __name__ == "__main__":
    import flet
    flet.app(target=main)
