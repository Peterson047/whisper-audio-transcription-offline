import streamlit as st
import whisper
import os

st.title("Transcrição Automática de Vídeo/Áudio com Whisper")

uploaded_file = st.file_uploader(
    "Selecione um vídeo ou áudio para transcrição",
    type=["mp4", "mp3", "wav", "m4a", "mpeg4"]
)

# Menu lateral com opções ajustadas
st.sidebar.title("Opções de Transcrição")

timestamp_option = st.sidebar.selectbox(
    "Exibir timestamps na transcrição?",
    ["Sim", "Não"]
)
add_timestamps = timestamp_option == "Sim"

model_name = st.sidebar.selectbox(
    "Modelo Whisper",
    ["tiny", "base", "small", "medium", "large"],
    index=2
)

language = st.sidebar.selectbox(
    "Idioma do áudio",
    ["auto", "pt", "en", "es", "fr", "de"],
    index=0,
    help="Defina o idioma do áudio para melhorar a transcrição (auto detecta automaticamente)."
)

if uploaded_file is not None:
    if uploaded_file.type.startswith("video"):
        st.video(uploaded_file)
    else:
        st.audio(uploaded_file)

    iniciar = st.button("Iniciar Transcrição")

    if iniciar:
        with open("temp_media", "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.info("Iniciando a transcrição, aguarde...")

        model = whisper.load_model(model_name)

        # Parâmetros para transcrição sem tradução
        options = {
            "language": None if language == "auto" else language,
            "task": "transcribe"
        }

        with st.spinner("Transcrevendo..."):
            result = model.transcribe("temp_media", **options)

        st.success("Transcrição concluída!")

        st.subheader("Preview da transcrição:")
        st.text_area("Transcrição", result["text"], height=200)

        if add_timestamps:
            texto_salvo = ""
            for seg in result["segments"]:
                start = seg["start"]
                end = seg["end"]
                text = seg["text"].strip()
                texto_salvo += f"[{start:.2f} --> {end:.2f}] {text}\n"
        else:
            texto_salvo = result["text"]

        st.download_button(
            label="Baixar transcrição",
            data=texto_salvo,
            file_name="transcription.txt",
            mime="text/plain"
        )

        os.remove("temp_media")
    else:
        st.warning("Clique em 'Iniciar Transcrição' para começar.")
else:
    st.info("Faça upload de um arquivo de áudio ou vídeo para iniciar.")
