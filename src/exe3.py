import asyncio

import flet
from flet import ThemeMode, View, AppBar, Colors, Button, TextField, Text, OutlinedButton, Column, Container, \
    CrossAxisAlignment


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.LIGHT # ou ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # funções
    def exibir_msg():
        text_marca.value = f"Marca: {input_marca.value}"
        text_cor.value = f"Cor: {input_cor.value}"
        text_preco.value = f"Preço: {input_preco.value}"
        text_quantidade.value = f"Quantidade: {input_quantidade.value}"

        tem_erro = False
        if input_marca.value:
            input_marca.error = None
        else:
            tem_erro = True
            input_marca.error = "Campo obrigatorio"

        tem_erro = False
        if input_cor.value:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatorio"

        tem_erro = False
        if input_preco.value:
            input_preco.error = None
        else:
            tem_erro = True
            input_preco.error = "Campo obrigatorio"

        tem_erro = False
        if input_quantidade.value:
            input_quantidade.error = None
        else:
            tem_erro = True
            input_quantidade.error = "Campo obrigatorio"


        if not(tem_erro):
            input_marca.value = ""
            input_cor.value = ""
            input_preco.value = ""
            input_quantidade.value = ""
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
                        title="Olá👉😌👈",
                        bgcolor=Colors.AMBER_200,
                    ),
                    Text("Preencha os campos"),
                    input_marca,
                    input_cor,
                    input_preco,
                    input_quantidade,
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
                        Container(
                            Column([
                                text_marca,
                                text_cor,
                                text_preco,
                                text_quantidade,
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=Colors.BLUE_200,
                            width= 1000,
                            padding=15,
                            border_radius=10
                        )

                    ]
                ),

            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)


    # Componentes
    input_marca = TextField(label="Digite a Marca do seu produto")
    text_marca = Text()
    text_cor = Text()
    text_preco = Text()
    text_quantidade = Text()
    btn_salvar = Button("Salvar", on_click=exibir_msg)
    input_cor = TextField(label="Digite a cor do produto")
    input_preco = TextField(label="Digite o preço do produto")
    input_quantidade = TextField(label="digite a quantidade de seu produto")


    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)