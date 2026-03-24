from cProfile import label

import flet
from flet import ThemeMode, Text, TextTheme, TextField, Button, OutlinedButton, Column, CrossAxisAlignment, \
    NumbersOnlyInputFilter, Container, Colors, FontWeight, MainAxisAlignment
from flet.controls import page
from flet.controls.border_radius import horizontal
from datetime import datetime
tempo = (datetime.now()).year


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    def salvar_nome():
        text.value = f"Bom dia {input_nome.value} {input_sobrenome.value}"
        page.update()

    def par_ou_impar():
        numero = int(num.value)
        if numero % 2 == 0:
            p = f"O número {numero} é PAR"
        else:
            p = f"O número {numero} é ÍMPAR"
        text_parimpar.value = f'seu numero é {p}'
        page.update()

    def idade():
        numero = int(input_idade.value)
        calculo = tempo - numero
        if calculo >= 18:
            i = f'conforme a sua idade {calculo} anos, você é maior de idade'
        else:
            i = f'Conforme a sua idade {calculo} anos, você é menor de idade'
        text_idade.value = i
        page.update()

    # Componentes
    text = Text("Ola digite seu nome")
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="sobrenome",)
    text_parimpar = Text("Digite um numero")
    text_idade = Text("Digite uma idadel")
    num = TextField(label='Verificar par ou impar')
    input_idade = TextField(label='Digite o ano de seu nascimento', hint_text="Ex:2000")
    btn_verificar_idade = OutlinedButton('Verificar idade', on_click=idade)
    btn_verificar = OutlinedButton("Par ou Impar", on_click=par_ou_impar)
    btn_salvar = OutlinedButton("Mostrar nome", on_click=salvar_nome)

    # Construção da tela

    page.add(
        Column(
            [
                Container(
                    Column(
                        [
                            Text("Atividade 1", weight=FontWeight.BOLD, size=24),
                            input_nome,
                            input_sobrenome,
                            btn_salvar,
                            text,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.BLUE_900,
                    padding=15,
                    border_radius=10

                ),

                Container(
                    Column(
                        [
                            Text("Atividade 2", weight=FontWeight.BOLD, size=24),
                            num,
                            btn_verificar,
                            text_parimpar,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.RED_900,
                    padding=15,
                    border_radius=10

                ),

                Container(
                    Column(
                        [
                            Text("Atividade 3", weight=FontWeight.BOLD, size=24),
                            input_idade,
                            btn_verificar_idade,
                            text_idade,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.GREEN_900,
                    padding=15,
                    border_radius=10

                )


            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )


flet.app(main)
