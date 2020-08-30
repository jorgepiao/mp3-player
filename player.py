
from tkinter import *

root = Tk()

root.title('MP3 Player')
root.geometry('500x400')


def agregar_cancion():
    pass

def agregar_varias_canciones():
    pass


#- Crear playlist box
playlist_box = Listbox(root, bg='black', fg='green', width=60)
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
boton_play = Button(control_frame, image=play_btn_img, borderwidth=0)
boton_pause = Button(control_frame, image=pause_btn_img, borderwidth=0)
boton_stop = Button(control_frame, image=stop_btn_img, borderwidth=0)

boton_atras.grid(row=0, column=0, padx=10)
boton_adelante.grid(row=0, column=1, padx=10)
boton_play.grid(row=0, column=2, padx=10)
boton_pause.grid(row=0, column=3, padx=10)
boton_stop.grid(row=0, column=4, padx=10)

#- Crear menu
mi_menu = Menu(root)
root.config(menu=mi_menu)

#- Crear menu para agregar canciones
agregar_cancion_menu = Menu(mi_menu, tearoff=0)
mi_menu.add_cascade(label='Agregar cancion', menu=agregar_cancion_menu)
#- Agregar una cancion a la playlist
agregar_cancion_menu.add_command(label='Agregar una cancion', command=agregar_cancion)
#- Agregar varias canciones a la playlist
agregar_cancion_menu.add_command(label='Agregar varias canciones', command=agregar_varias_canciones)

root.mainloop()

