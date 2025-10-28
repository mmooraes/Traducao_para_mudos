#pip install PySimpleGUI 
#Documentação: https://pypi.org/project/PySimpleGUI
#Utilidade: Utlizado para criar a janela de botoes de forma simples


"""Atualização 1.0: 

Foi detectado um erro de instação da bliblioteca no App.py, para correção siga o passo a passo:

Passo 1: Desinstale a versão atual. Copie e cole este comando abaixo e aperte Enter. Ele vai perguntar "Proceed (Y/n)?", digite Y e aperte Enter.
Comando: python -m pip uninstall PySimpleGUI

Passo 2: Limpe o cache do pip (para garantir) Este comando abaixo limpa qualquer versão antiga que esteja guardada.
Comando: python -m pip cache purge

Passo 3: Instale a versão correta do servidor privado Este é o comando mais importante. Ele força a instalação da versão mais recente, buscando no novo endereço (--extra-index-url).
Comando: python -m pip install --force-reinstall --extra-index-url https://PySimpleGUI.net/install PySimpleGU
"""


#pip install gTTS
#Documentação: https://pypi.org/project/gTTS
#Utilidade: Google Text-to-Speech, para criar o áudio

#pip install pygame
#Documentação: https://pypi.org/project/pygame
#Utilidade: para tocar o áudio .mp3 que o gTTS vai criar