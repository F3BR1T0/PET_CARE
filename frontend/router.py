from flet import Page, MainAxisAlignment, CrossAxisAlignment

class Router:
    def __init__(self, page: Page):
        self.page = page
        self.routes = {}
        self.history = []
        self.page.horizontal_alignment = MainAxisAlignment.CENTER
        self.page.vertical_alignment = CrossAxisAlignment.CENTER

    def register_route(self, name, screen_function):
        self.routes[name] = screen_function

    def navigate_to(self, route_name, *args, **kwargs):
        if route_name not in self.routes:
            raise ValueError(f"Rota '{route_name}' não está registrada.")

        # Adicione a tela atual à pilha apenas se houver conteúdo
        if self.page.controls:
            self.history.append(self.page.controls[-1])  # Adiciona a tela atual à pilha

        self.page.controls.clear()  # Limpa os controles da página
        self.page.controls.append(self.routes[route_name](self, *args, **kwargs))  # Renderiza a nova tela
        self.page.update()

    def go_back(self):
        if self.history:
            previous_screen = self.history.pop()  # Remove a última tela da pilha
            self.page.controls.clear()
            self.page.controls.append(previous_screen)  # Renderiza a tela anterior
            self.page.update()
        else:
            print("Nenhuma tela no histórico para voltar.")
