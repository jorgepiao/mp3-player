
from tkinter import *
from tkinter import filedialog
import pygame

root = Tk()

root.title('MP3 Player')
root.geometry('500x400')

#- inicializar Pygame
pygame.mixer.init()

def agregar_cancion():
    cancion = filedialog.askopenfilename(initialdir='audio/', title='Elige una cancion', filetypes=(('Archivos mp3', '*.mp3'), ))
    # mi_label.config(text=cancion)

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
    # mi_label.config(text=cancion)

    #- cargar la cancion con pygame mixer
    pygame.mixer.music.load(cancion)
    #- tocar la cancion con pygame mixer
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()
    playlist_box.selection_clear(ACTIVE)


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



#- Crear playlist box
playlist_box = Listbox(root, bg='black', fg='green', width=60, selectbackground='green', selectforeground='black')
playlist_box.pack(pady=20)

#- Imagenes de los botones del control
atras_btn_img = PhotoImage(file='images/back50.png')
adelante_btn_img = PhotoImage(file='images/forward50.png')
play_btn_img = PhotoImage(file='images/play50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')

#- Crear frame de botones
control_frame = Frame(root)
control_frame.pack(pady=20)

#- Crear botones play/stop y demas
boton_atras = Button(control_frame, image=atras_btn_img, borderwidth=0)
boton_adelante = Button(control_frame, image=adelante_btn_img, borderwidth=0)
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


#- Label temporal
mi_label = Label(root, text='')
mi_label.pack(pady=20)




root.mainloop()

