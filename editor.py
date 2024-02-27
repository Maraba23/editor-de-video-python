from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

# Caminho para sua imagem e música
caminho_imagem = 'image/imagem.png'
caminho_musica = 'audio/musica.mp3'

# Carregar a imagem como um clipe de vídeo estático
clip_imagem = ImageClip(caminho_imagem)

# Carregar o áudio
clip_audio = AudioFileClip(caminho_musica)

# Definir a duração do clipe de imagem para corresponder à duração do áudio
clip_imagem = clip_imagem.set_duration(clip_audio.duration)

# Definir o clipe de áudio no clipe de imagem
video_final = clip_imagem.set_audio(clip_audio)

# Escrever o resultado em um arquivo .mp4
video_final.write_videofile("videos/video_final.mp4", fps=24)
