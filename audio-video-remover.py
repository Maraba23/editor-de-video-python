import tkinter as tk
from tkinter import filedialog, simpledialog
from moviepy.editor import VideoFileClip
import os

# Função para remover o áudio do vídeo
def remover_audio_video(caminho_video, nome_saida):
    video = VideoFileClip(caminho_video)
    video_sem_audio = video.without_audio()
    
    if not os.path.exists('videos'):
        os.makedirs('videos')
    
    caminho_saida = os.path.join('videos', nome_saida)
    video_sem_audio.write_videofile(caminho_saida)

def selecionar_arquivo_video():
    root = tk.Tk()
    root.withdraw() # Fechar a janela principal
    arquivo = filedialog.askopenfilename(title="Selecione o vídeo", filetypes=[("Arquivos de vídeo", "*.mp4 *.avi *.mov")])
    return arquivo

def interface_usuario():
    caminho_video = selecionar_arquivo_video()
    
    if caminho_video:
        nome_saida = simpledialog.askstring("Nome do Arquivo de Saída", "Insira o nome do arquivo de saída (sem extensão):")
        if nome_saida:
            nome_saida += ".mp4"  # Garantir que o arquivo tenha a extensão .mp4
            remover_audio_video(caminho_video, nome_saida)
            tk.messagebox.showinfo("Concluído", f"O vídeo sem áudio foi salvo com sucesso em 'videos/' como {nome_saida}.")

if __name__ == "__main__":
    interface_usuario()
