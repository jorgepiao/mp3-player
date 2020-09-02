
from tkinter import *
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()

root.title('MP3 Player')
root.geometry('500x400')

#- inicializar Pygame
pygame.mixer.init()


#- Funcion para el tiempo de reproduccion
def tiempo_reproduccion():
    #- obtener el tiempo actual de la cancion
    tiempo_actual = pygame.mixer.music.get_pos() / 1000
    #- formato de tiempo (minutos y segundos)
    formato_tiempo = time.strftime('%M:%S', time.gmtime(tiempo_actual))

    #- obtener la ruta de la cancion
    cancion = playlist_box.get(ACTIVE)
    cancion = f'C:/Users/AMD A6/Desktop/proys/mp3-player_python/audio/{cancion}.mp3'

    #- duracion de la cancion
    mut_cancion = MP3(cancion)
    global duracion_cancion
    duracion_cancion = mut_cancion.info.length
    #- formato de tiempo
    formato_duracion_cancion = time.strftime('%M:%S', time.gmtime(duracion_cancion))

    #- mostrar el tiempo en la barra de estado
    if tiempo_actual >= 0:
        barra_estado.config(text=f'Tiempo transcurrido: {formato_tiempo} de {formato_duracion_cancion}  ')
    #- loop para el tiempo por segundo
    barra_estado.after(1000, tiempo_reproduccion)


def agregar_cancion():
    cancion = filedialog.askopenfilename(initialdir='audio/', title='Elige una cancion', filetypes=(('Archivos mp3', '*.mp3'), ))
    # etiqueta.config(text=cancion)

    #- Nombre de la cancion sin la ruta
    cancion = cancion.replace('C:/Users/AMD A6/Desktop/proys/mp3-player_python/audio/', '')
    cancion = cancion.replace('.mp3', '')

    #- Agregar cancion al final de la playlist
    playlist_box.insert(END, cancion)


def agregar_varias_canciones():
    canciones = filedialog.askopenfilename(initialdir='audio/', title='Elige una cancion', filetypes=(('Archivos mp3', '*.mp3'), ))

    for cancion in canciones:
        #- Nombre de la cancion sin la ruta
        cancion = cancion.replace('C:/Users/AMD A6/Desktop/proys/mp3-player_python/audio/', '')
        cancion = cancion.replace('.mp3', '')

        #- Agregar cancion al final de la playlist
        playlist_box.insert(END, cancion)


def borrar_cancion():
    playlist_box.delete(ANCHOR)


def borrar_todas_canciones():
    playlist_box.delete(0, END)


def play():
    #- obtener la ruta de la cancion
    cancion = playlist_box.get(ACTIVE)
    cancion = f'C:/Users/AMD A6/Desktop/proys/mp3-player_python/audio/{cancion}.mp3'
    # etiqueta.config(text=cancion)

    #- cargar la cancion con pygame mixer
    pygame.mixer.music.load(cancion)
    #- tocar la cancion con pygame mixer
    pygame.mixer.music.play(loops=0)

    #- tiempo de reproduccion de la cancion
    tiempo_reproduccion()


def stop():
    pygame.mixer.music.stop()
    playlist_box.selection_clear(ACTIVE)

    barra_estado.config(text='')


def siguiente_cancion():
    #- numero (indice) de la cancion
    siguiente = playlist_box.curselection()
    siguiente = siguiente[0] + 1

    #- titulo de la cancion
    cancion = playlist_box.get(siguiente)
    cancion = f'C:/Users/AMD A6/Desktop/proys/mp3-player_python/audio/{cancion}.mp3'
    #- cargar la cancion con pygame mixer
    pygame.mixer.music.load(cancion)
    #- tocar la cancion con pygame mixer
    pygame.mixer.music.play(loops=0)

    #- barra de seleccion
    playlist_box.selection_clear(0, END)
    playlist_box.activate(siguiente)
    playlist_box.selection_set(siguiente, last=None)


def anterior_cancion():
    #- numero (indice) de la cancion
    anterior = playlist_box.curselection()
    anterior = anterior[0] - 1

    #- titulo de la cancion
    cancion = playlist_box.get(anterior)
    cancion = f'C:/Users/AMD A6/Desktop/proys/mp3-player_python/audio/{cancion}.mp3'
    #- cargar la cancion con pygame mixer
    pygame.mixer.music.load(cancion)
    #- tocar la cancion con pygame mixer
    pygame.mixer.music.play(loops=0)

    #- barra de seleccion
    playlist_box.selection_clear(0, END)
    playlist_box.activate(anterior)
    playlist_box.selection_set(anterior, last=None)


global pausado
pausado = False

def pause(esta_pausado):
    global pausado
    pausado = esta_pausado

    if pausado:
        pygame.mixer.music.unpause()
        pausado = False
    else:
        pygame.mixer.music.pause()
        pausado = True


def volumen(x):
    pygame.mixer.music.set_volume(volumen_barra.get())


#- Crear main frame
main_frame = Frame(root)
main_frame.pack(pady=20)

#- Crear playlist box
playlist_box = Listbox(main_frame, bg='black', fg='green', width=60, selectbackground='green', selectforeground='black')
playlist_box.grid(row=0, column=0)

#- Crear el marco para la barra de volumen
volumen_frame = LabelFrame(main_frame, text='Volumen')
volumen_frame.grid(row=0, column=1, padx=20)

#- Crear barra de volumen
volumen_barra = ttk.Scale(volumen_frame, from_=0, to=1, orient=VERTICAL, length=125, value=1, command=volumen)
volumen_barra.pack(pady=10)

#- Imagenes de los botones del control
atras_btn_img = PhotoImage(file='images/back50.png')
adelante_btn_img = PhotoImage(file='images/forward50.png')
play_btn_img = PhotoImage(file='images/play50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')

#- Crear frame de botones
control_frame = Frame(main_frame)
control_frame.grid(row=1, column=0, pady=20)

#- Crear botones play/stop y demas
boton_atras = Button(control_frame, image=atras_btn_img, borderwidth=0, command=anterior_cancion)
boton_adelante = Button(control_frame, image=adelante_btn_img, borderwidth=0, command=siguiente_cancion)
boton_play = Button(control_frame, image=play_btn_img, borderwidth=0, command=play)
boton_pause = Button(control_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(pausado))
boton_stop = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop)

boton_atras.grid(row=0, column=0, padx=10)
boton_adelante.grid(row=0, column=1, padx=10)
boton_play.grid(row=0, column=2, padx=10)
boton_pause.grid(row=0, column=3, padx=10)
boton_stop.grid(row=0, column=4, padx=10)

#- Crear menu
mi_menu = Menu(root)
root.config(menu=mi_menu)

#- Crear menu para agregar canciones a la playlist
agregar_cancion_menu = Menu(mi_menu, tearoff=0)
mi_menu.add_cascade(label='Agregar cancion', menu=agregar_cancion_menu)
#- Agregar una cancion a la playlist
agregar_cancion_menu.add_command(label='Agregar una cancion', command=agregar_cancion)
#- Agregar varias canciones a la playlist
agregar_cancion_menu.add_command(label='Agregar varias canciones', command=agregar_varias_canciones)

#- Crear menu para borrar canciones de la playlist
borrar_cancion_menu = Menu(mi_menu, tearoff=0)
mi_menu.add_cascade(label='Borrar cancion', menu=borrar_cancion_menu)
borrar_cancion_menu.add_command(label='Borrar una cancion', command=borrar_cancion)
borrar_cancion_menu.add_command(label='Borrar todas las canciones', command=borrar_todas_canciones)

#- Barra de estado
barra_estado = Label(root, text='nada', bd=1, relief=GROOVE, anchor=E)
barra_estado.pack(fill=X, side=BOTTOM, ipady=2)


#- Label temporal
etiqueta = Label(root, text='')
etiqueta.pack(pady=20)



root.mainloop()

