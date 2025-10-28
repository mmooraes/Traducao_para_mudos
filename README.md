# 💻 Projeto: In

![Status do Projeto](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)

Uma aplicação de desktop em Python que atua como uma Prancha de Comunicação Aumentativa e Alternativa (CAA), desenvolvida para auxiliar pessoas com dificuldades de fala a se comunicarem através de frases pré-definidas que são convertidas em voz.

---

> **⚠️ Nota Importante:**
> Antes de qualquer coisa, tire um print screen (captura de tela) do seu aplicativo funcionando e coloque aqui. Um README com imagens é 10x mais profissional.
> 
> ![Imagem do App](aqui_vai_o_link_da_sua_imagem.png)
> 
> (Para fazer isso no GitHub, você pode simplesmente arrastar e soltar a imagem na caixa de texto enquanto edita o README).

---

## 🎯 Sobre o Projeto

Este projeto foi inspirado na ideia de usar a tecnologia para criar soluções de acessibilidade. O objetivo é fornecer uma ferramenta digital, simples e de fácil acesso, que permita a usuários não-verbais ou com dificuldades de fala expressar necessidades básicas, pensamentos e sentimentos de forma rápida e intuitiva, usando um computador.

A aplicação utiliza a biblioteca `PySimpleGUI` para criar uma interface amigável com botões e `gTTS` (Google Text-to-Speech) para gerar uma voz natural em português do Brasil.

## ✨ Funcionalidades

* **Interface Gráfica Simples:** Uma janela com botões grandes e claros para fácil seleção.
* **Comunicação Instantânea:** Ao clicar em um botão, a frase correspondente é falada imediatamente.
* **Voz em Português-BR:** Utiliza a API do Google para uma síntese de voz clara e natural.
* **Frases Essenciais:** Inclui um conjunto básico de frases para comunicação (ex: "Olá", "Estou com fome", "Estou com sede", "Banheiro").

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias:

* **Python 3:** Linguagem principal do projeto.
* **PySimpleGUI:** Para a criação da interface gráfica (GUI).
* **gTTS (Google Text-to-Speech):** Para converter o texto dos botões em áudio.
* **pygame (módulo mixer):** Para reproduzir os arquivos de áudio .mp3 gerados.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o projeto em sua máquina local.

**1. Clone o Repositório**
```bash
git clone [https://github.com/SEU-USUARIO/NOME-DO-SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-SEU-REPOSITORIO.git)
cd NOME-DO-SEU-REPOSITORIO
