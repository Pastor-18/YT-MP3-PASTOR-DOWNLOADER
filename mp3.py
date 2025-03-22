import streamlit as st
import yt_dlp
import os

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")
    
    return filename

st.title("YouTube MP3 Downloader")

url = st.text_input("Introduce la URL del video de YouTube:")

if st.button("Descargar MP3"):
    if url:
        with st.spinner("Descargando y convirtiendo..."):
            try:
                file_path = download_audio(url)
                st.success("¡Descarga completada!")
                with open(file_path, "rb") as file:
                    st.download_button(
                        label="Descargar MP3",
                        data=file,
                        file_name=os.path.basename(file_path),
                        mime="audio/mp3"
                    )
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Por favor, introduce una URL válida.")
