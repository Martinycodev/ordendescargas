import os
import shutil

route_downloads = "E:\\Downloads\\"
text_extensions = ('.txt', '.doc', '.docx', 'pptx', '.odf', '.docm', '.pdf', '.odt')
video_extensions = ('.mov', '.mp4', '.avi', '.mkv', '.mkv', '.flv', '.wmv','.mpeg')
audio_extensions = ('.mp3', '.wma', '.wav', '.flac','.sesx','.pkf')
photo_extensions = ('.jpg', '.png', 'jpeg', '.gif', '.tiff', '.psd', '.bmp', '.ico', '.svg','.ai','.eps')
compressed_extensions = ('.zip', '.rar', '.rar5', '.7z', '.ace', '.gz')
executable_extensions = ('.exe', '.msi')

def order(file, extension):

    for ext in text_extensions:

        if extension == ext:
            shutil.move(route_downloads + file, route_downloads + 'Documentos')

    for ext in video_extensions:

        if extension == ext:
            shutil.move(route_downloads + file, route_downloads + 'Videos')

    for ext in audio_extensions:

        if extension == ext:
            shutil.move(route_downloads + file, route_downloads + 'Audios')

    for ext in photo_extensions:

        if extension == ext:
            shutil.move(route_downloads + file, route_downloads + 'Imagenes')

    for ext in compressed_extensions:

        if extension == ext:
            shutil.move(route_downloads + file, route_downloads + 'Comprimidos')

    for ext in executable_extensions:

        if extension == ext:
            shutil.move(route_downloads + file, route_downloads + 'Ejecutables')

    if extension != '':
        try:
            shutil.move(route_downloads + file, route_downloads + 'Otros')

        except:
            pass


def main():

    print('Iniciando\n')

    for file in os.listdir(route_downloads):
        try:
            nombre_archivo, ext = os.path.splitext(file)
            order(file, ext)

        except:
            print('No se puedo mover '+nombre_archivo+' {}\n'.format(file))


    print('Proceso terminado')

if __name__ == '__main__':  
    main()