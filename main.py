#
# Autor: Daniel Luis
# Data de criação: 27/10/2022

from PySimpleGUI import PySimpleGUI as sg

op_novo = "Novo"
op_abrir = "Abrir"
op_salva = "Salvar"
op_salvar_como = "Salvar como"
op_config = "Configurações"
op_sair = "Sair"

# Menu de opções
menu = (
    ["Arquivo", [
        op_novo,
        op_abrir,
        op_salva,
        op_salvar_como,
        op_config,
        op_sair
        ]],
    ["Editar", ["Cortar", "Copiar", "Colar"]],
)

layout = [
    [sg.MenuBar(menu)],
    [sg.Multiline(
        font=("Consolas", 23),
        background_color='grey23',
        text_color="white",
        key="_Local_texto"
    )]
]

janela = sg.Window(
    "Bloco de Notas",
    layout=layout,
    size=(900, 500),
    margins=(0, 0),
    resizable=True,
)

janela.read(timeout=1)
janela["_Local_texto"].expand(expand_x=True, expand_y=True)


# Abrir um arquivo que já existe
def abrir_arquivo():
    try:
        filename: str = sg.popup_get_file("Open File", no_window=True)

    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "r") as f:
            janela["_Local_texto"].update(value=f.read())
    return filename


# Loop da janela
while True:
    eventos, values = janela.read()

    if eventos in (None, "Sair"):
        janela.close()
        break

    if eventos in (op_abrir):
        filename = abrir_arquivo()

# Fim
