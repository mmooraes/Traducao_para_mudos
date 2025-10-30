import PySimpleGUI
from falar import falar_texto #importado a função crianda no pasta falar.py

#(cores) da janela
PySimpleGUI.theme('LightGreen3')

"""
Aqui esta definido o Layout da janela, cada lista interna é uma linha
e B = Button (botão)
"""
layout = [
    [PySimpleGUI.Text('Selecione uma opção para comunicar: ')],

    [PySimpleGUI.Button('Olá', size=(20, 2)),
     PySimpleGUI.Button('Tudo bem?', size=(20, 2))],
    
    [PySimpleGUI.Button('Sim', size=(20, 2)),
     PySimpleGUI.Button('Não', size=(20, 2))],

    [PySimpleGUI.Button('Estou com fome', size=(20, 2)),
     PySimpleGUI.Button('Estou com cede', size=(20, 2))],
    
    [PySimpleGUI.Button('Quero ir ao banheiro', size=(20, 2)),
     PySimpleGUI.Button('Obrigado!', size=(20, 2))],

     [PySimpleGUI.Button('Sair', button_color=('white', 'red'), size=(10, 2))]
    ]

janela = PySimpleGUI.Window('Comunicador Digital v1.0', layout)

#Loop Principal do Aplicativo
while True:
    # Lê os eventos da janela (ex: qual botão foi clicado)
    evento, valores = janela.read()
    
    # Se o usuário fechar a janela ou clicar em "Sair"
    if evento == PySimpleGUI.WIN_CLOSED or evento == 'Sair':
        break
    
    # Se qualquer outro botão for clicado, o "evento"
    # será o próprio texto do botão.
    # Vamos usar esse texto para a nossa função de falar!
    if evento:
        print(f"Usuário clicou em: {evento}")
        falar_texto(evento)

# Fecha a janela ao sair do loop
janela.close()