import tkinter as tk
from tkinter import filedialog, simpledialog
from moviepy.editor import ImageClip, AudioFileClip
import os

# Função para criar vídeo
def criar_video(caminho_imagem, caminho_musica, nome_saida, volume=2.0):
    clip_imagem = ImageClip(caminho_imagem)
    clip_audio = AudioFileClip(caminho_musica).volumex(volume)
    clip_imagem = clip_imagem.set_duration(clip_audio.duration)
    video_final = clip_imagem.set_audio(clip_audio)
    
    # Certifique-se de que a pasta videos/ existe
    if not os.path.exists('videos'):
        os.makedirs('videos')
    
    caminho_saida = os.path.join('videos', nome_saida)
    video_final.write_videofile(caminho_saida, fps=24)

# Função para selecionar arquivo
def selecionar_arquivo(tipo):
    root = tk.Tk()
    root.withdraw() # Fechar a janela principal
    if tipo == 'imagem':
        arquivo = filedialog.askopenfilename(title="Selecione a imagem",
                                             filetypes=[("Arquivos PNG", "*.png")])
    elif tipo == 'musica':
        arquivo = filedialog.askopenfilename(title="Selecione a música",
                                             filetypes=[("Arquivos MP3", "*.mp3")])
    return arquivo

# Interface principal
def interface_usuario():
    caminho_imagem = selecionar_arquivo('imagem')
    if not caminho_imagem:
        return
    caminho_musica = selecionar_arquivo('musica')
    if not caminho_musica:
        return
    
    # Pedir ao usuário o nome do arquivo de saída
    nome_saida = simpledialog.askstring("Nome do Arquivo de Saída", "Insira o nome do arquivo de saída (sem extensão):")
    if nome_saida:
        nome_saida += ".mp4"  # Garantir que o arquivo tenha a extensão .mp4
        criar_video(caminho_imagem, caminho_musica, nome_saida)
        tk.messagebox.showinfo("Concluído", "O vídeo foi salvo com sucesso em 'videos/'")

if __name__ == "__main__":
    interface_usuario()
