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
        text_nome.value = f"Bom dia: {input_nome.value}, Tudo Bem?"
        text_cpf.value = f"CPF: {input_cpf.value}"
        text_email.value = f"Email: {input_email.value}"
        text_salario.value = f"Salario: {input_salario.value}"

        tem_erro = False
        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio"

        tem_erro = False
        if input_cpf.value:
            input_cpf.error = None
        else:
            tem_erro = True
            input_cpf.error = "Campo obrigatorio"

        tem_erro = False
        if input_email.value:
            input_email.error = None
        else:
            tem_erro = True
            input_email.error = "Campo obrigatorio"

        tem_erro = False
        if input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = "Campo obrigatorio"


        if not(tem_erro):
            input_nome.value = ""
            input_cpf.value = ""
            input_email.value = ""
            input_salario.value = ""
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
                        title="Olá",
                        bgcolor=Colors.AMBER_200,
                    ),
                    Text("Preencha os campos"),
                    input_nome,
                    input_cpf,
                    input_email,
                    input_salario,
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
                        text_nome,
                        text_cpf,
                        text_email,
                        text_salario
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
    input_nome = TextField(label="Digite seu Nome")
    text_nome = Text()
    text_cpf = Text()
    text_email = Text()
    text_salario = Text()
    btn_salvar = Button("Salvar", on_click=exibir_msg)
    input_cpf = TextField(label="Digite um cpf")
    input_email = TextField(label="Digite seu email")
    input_salario = TextField(label="digite o valor do seu salario")

    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)