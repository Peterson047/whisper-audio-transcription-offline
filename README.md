# Whisper Audio Transcription Offline

Este projeto oferece um script Python para realizar transcrições de áudio e vídeo de forma offline, utilizando o poderoso modelo [Whisper da OpenAI](https://openai.com/research/whisper). A principal vantagem é garantir a privacidade dos seus dados e não depender de serviços online ou APIs pagas.

## 📺 Tutorial em Vídeo

Este projeto foi desenvolvido e explicado em uma série de vídeos no YouTube. Assista à playlist completa para um guia passo a passo detalhado, desde a configuração do ambiente até a execução do script.

[▶️ **Assista à Playlist Completa no YouTube**](https://www.youtube.com/playlist?list=PLRP7YsIqo0BI3CF6h6fAlJYO00VzqlVHi)

## ✨ Funcionalidades

* **Transcrição Offline:** Processe seus arquivos localmente, sem a necessidade de enviar dados para a nuvem.
* **Alta Precisão:** Utiliza um dos modelos de reconhecimento de fala mais avançados do mercado.
* **Suporte a Diversos Formatos:** Transcreve tanto arquivos de áudio quanto de vídeo.
* **Saída em .txt:** Gera um arquivo de texto simples (`.txt`) com a transcrição completa e timestamps.
* **Aceleração por GPU:** Suporte para processamento com placas de vídeo NVIDIA (CUDA) para uma transcrição muito mais rápida.

## ⚙️ Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados:

* [Python 3.8+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)
* (Opcional, mas recomendado) Uma GPU NVIDIA com [CUDA](https://developer.nvidia.com/cuda-downloads) instalado para aceleração de hardware.

## 🚀 Instalação e Configuração

Siga os passos abaixo para configurar o ambiente e instalar as dependências do projeto.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Peterson047/whisper-audio-transcription-offline.git
    ```

2.  **Acesse a pasta do projeto:**
    ```bash
    cd whisper-audio-transcription-offline
    ```

3.  **Crie e ative um ambiente virtual (Virtual Environment):**
    ```bash
    # Crie o ambiente
    python -m venv venv

    # Ative o ambiente
    # No Windows:
    venv\Scripts\activate
    # No Linux/macOS:
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## 🎧 Como Usar

1.  **Adicione seu arquivo:**
    Coloque o seu arquivo de áudio ou vídeo (ex: `meu_video.mp4`) na pasta raiz do projeto.

2.  **Configure o script:**
    Abra o arquivo `main.py` em um editor de texto e altere o valor da variável `video_path` para o nome do seu arquivo:
    ```python
    # ...
    # --- Configurações ---
    video_path = "meu_video.mp4"  # <-- Altere aqui para o nome do seu arquivo
    output_txt = "transcricao.txt"
    # ...
    ```

3.  **Execute o script:**
    Com o ambiente virtual ainda ativado, execute o seguinte comando no terminal:
    ```bash
    python main.py
    ```

4.  **Verifique o resultado:**
    Aguarde o processamento. Ao final, um arquivo chamado `transcricao.txt` será criado na pasta do projeto com a transcrição completa.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Feito com ❤️ por [Peterson Alves](https://github.com/Peterson047)
