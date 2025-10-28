import gtts
import pygame
import os
from io import BytesIO

#aqui iniciamos o pygame, ele é nescessario para reproduzir o audio
pygame.mixer.init() 

def falar_texto(texto, lingua='pt-br'):

    #area de conversão de texto em audio
    try:
        #Com o BytesIO foi criando um objeto de audio na memoria
        arquivo_mp3 = BytesIO()

        #Criação de audio utilizando Google TTS
        tts = gtts.gTTS(text=texto, lang=lingua)

        #Utilizado para salvar o objeto na memoria 
        tts.write_to_fp(arquivo_mp3)

        #"Rebobina" o arquivo em memória para o início
        arquivo_mp3.seek(0)

        # Carrega o áudio no mixer do pygame e tocar o áudio
        pygame.mixer.music.load(arquivo_mp3)
        pygame.mixer.music.play()

        #mensagem para caso houver erro
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        #tratamento de erro para caso não houver acesso a internet
    except Exception as e:
        print(f"Erro ao tentar falar {e}")
        
        #Teste
if __name__ == "__main__":
    print("Testando a função de fala...")
    falar_texto("Olá, isto é um teste.")
    falar_texto("Estou com sede.")
    print("Teste concluído.")