
from tkinter import *

root = Tk()

root.title('MP3 Player')
root.geometry('500x400')

#- crear playlist box
playlist_box = Listbox(root, bg='black', fg='green', width=60)
playlist_box.pack(pady=20)

#- crear frame de botones
control_frame = Frame(root)
control_frame.pack(pady=20)

#- crear botones play/stop y demas
boton_atras = Button(control_frame, text='Atras')
boton_adelante = Button(control_frame, text='Adelante')
boton_play = Button(control_frame, text='Play')
boton_pause = Button(control_frame, text='Pause')
boton_stop = Button(control_frame, text='Stop')

boton_atras.grid(row=0, column=0, padx=10)
boton_adelante.grid(row=0, column=1, padx=10)
boton_play.grid(row=0, column=2, padx=10)
boton_pause.grid(row=0, column=3, padx=10)
boton_stop.grid(row=0, column=4, padx=10)




root.mainloop()

