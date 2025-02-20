import flet as ft
from flet import Colors


botoes = [
    {'operador': 'Clear', 'fonte': Colors.BLACK, 'fundo': '#ffca3a'},  #1 tom de lilas d1b3c4
    {'operador': '±', 'fonte': Colors.BLACK, 'fundo': '#ffca3a'},  #2 tom lilkas c19ee0
    {'operador': '%', 'fonte': Colors.BLACK, 'fundo': '#ffca3a'},  #3 tom de lilas cc92c2
    {'operador': '/', 'fonte': Colors.WHITE, 'fundo': '#5b058a'},  #2 tom de laranja ff8300
    {'operador': '7', 'fonte': Colors.WHITE, 'fundo': '#ff6604'},  #2 tom de roxo 5b058a
    {'operador': '8', 'fonte': Colors.WHITE, 'fundo': '#ff6604'},
    {'operador': '9', 'fonte': Colors.WHITE, 'fundo': '#ff6604'},
    {'operador': '*', 'fonte': Colors.WHITE, 'fundo': '#5b058a'},
    {'operador': '4', 'fonte': Colors.WHITE, 'fundo': '#ff6604'},
    {'operador': '5', 'fonte': Colors.WHITE, 'fundo': '#ff6604'},
    {'operador': '6', 'fonte': Colors.WHITE, 'fundo': '#ff6604'},
    {'operador': '-', 'fonte': Colors.WHITE, 'fundo': '#5b058a'},
    {'operador': '1', 'fonte': Colors.WHITE, 'fundo': '#ff6604'},
    {'operador': '2', 'fonte': Colors.WHITE, 'fundo': '#ff6604'},
    {'operador': '3', 'fonte': Colors.WHITE, 'fundo': '#ff6604'},
    {'operador': '+', 'fonte': Colors.WHITE, 'fundo': '#5b058a'},
    {'operador': '0', 'fonte': Colors.WHITE, 'fundo': '#ff6604'},
    {'operador': '.', 'fonte': Colors.WHITE, 'fundo': '#ff6604'},
    {'operador': '=', 'fonte': Colors.WHITE, 'fundo': '#5b058a'},
]
def main(page: ft.Page):
    page.bgcolor = '#cc92c2'
    page.window.resizable = False
    page.window.width = 270
    page.window.height = 380
    page.title = "Simão's Calculator"

    result = ft.Text(value = '0', color = Colors.BLACK, size = 21)
    

    def calculo(operador, value_atual):
        try:
            value = eval(value_atual)
            if operador == '%':
                value = value/100
            elif operador == '±':
                value = -value
        except:
            return 'Erro Matemático'
        return value
    

    def select(e):
        value_atual = result.value if result.value != '0' else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_atual + value
        elif value == 'Clear':
            value = '0'
        else:
            if value_atual and value_atual[-1] in ('/', '*', '-', '+', '.'):
                value_atual = value_atual[:-1]
            value = value_atual + value

            if value[-1] in ('=', '%', '±'):
                value = calculo(operador = value[-1], value_atual = value_atual)
        
        result.value = value
        result.update()

    display = ft.Row(
        width = 250,
        controls = [result],
        alignment = 'end'
    )

    botao = [ft.Container(
        content = ft.Text(value = botao['operador'], color = botao['fonte']),
        width = 50,
        height = 50,
        bgcolor = botao['fundo'],
        border_radius = 100,
        alignment = ft.alignment.center,
        on_click = select
      )  for botao in botoes]
    

    keyboard = ft.Row(
        width = 250,
        wrap = True,
        controls = botao,
        alignment = 'end'
    )
    page.add(display, keyboard)


ft.app(target = main, assets_dir="caminho/para/flet_client")