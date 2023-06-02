import os
import PySimpleGUI as sg
from pytube import YouTube

sg.theme('DefaultNoMoreNagging')

layout = [
    [sg.Text('Insira a URL do vídeo do YouTube:')],
    [sg.Input(key='-URL-', size=(50, 1))],
    [sg.Button('Download')]
]

window = sg.Window('Baixar Vídeo do YouTube', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Download':
        url = values['-URL-']
        try:
            video = YouTube(url)
            titulo = video.title

            caminho_salvar = os.path.join(os.path.expanduser("~"), "Videos")
            if not os.path.exists(caminho_salvar):
                os.makedirs(caminho_salvar)

            stream = video.streams.get_highest_resolution()
            stream.download(output_path=caminho_salvar)

            sg.popup(f'O vídeo "{titulo}" foi baixado com sucesso!', title='Download Concluído')
        except Exception as e:
            sg.popup_error(f'Ocorreu um erro durante o download:\n{str(e)}', title='Erro')

window.close()