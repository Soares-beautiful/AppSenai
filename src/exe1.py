import asyncio

import flet
from flet import ThemeMode, View, AppBar, Colors, Button, TextField, Text, OutlinedButton


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.LIGHT # ou ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # funções
    def exibir_msg():
        text_msg.value = f"Bom dia: {input_nome.value}, Tudo Bem?"
        input_nome.value = ""
        navegar("/tela_msg")

    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Primeira página",
                        bgcolor=Colors.AMBER_200,
                    ),
                    Text("Digite seu nome para receber uma msg"),
                    input_nome,
                    btn_salvar
                ]
            )
        )
        if page.route == "/tela_msg":
            page.views.append(
                View(
                    route="/tela_msg",
                    controls=[
                        flet.AppBar(
                            title="Segunda página"
                        ),
                        text_msg
                    ]
                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)


    # Componentes
    input_nome = TextField(label="Nome")
    text_msg = Text()
    btn_salvar = Button("Salvar", on_click=exibir_msg)

    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)