#Importacion de librerias
from tkinter import *
from PIL import Image, ImageTk

#Creacion de ventana
ventana = Tk()
ventana.title("Zapaisoft")
ventana.iconbitmap("iconon.ico")

#Creacion de frame 
frame1 = Frame(ventana, width=900, height=600)
frame1.pack ()

#Agregacion y posicionamiento de logo
Logo = Image.open("Logo.png")
ImagenRedimensionada = Logo.resize((100, 50))
imagen_tk = ImageTk.PhotoImage(ImagenRedimensionada)
label_imagen = Label(frame1, image=imagen_tk)
label_imagen.grid(row=1, column=1, padx=10, pady=10, sticky=W)

#Creacion y posicionamiento de etiquetas, entradas y botones
Label_Usuario = Label(frame1, text="Usuario", font=("Aharoni", 8,))
Label_Usuario.grid(row=2, column=1, sticky=SW, padx=10, pady=0)
Entrada_Usuario = Entry(frame1)
Entrada_Usuario.focus()
Entrada_Usuario.grid(row=3, column=1, sticky=W, padx=10, pady=0)

#Agregacion y posicionamiento de icono usuario
icoUser = Image.open("icoUser.ico")
icoUser = icoUser.resize((20, 20))
icoUser = ImageTk.PhotoImage(icoUser)
Label_icoUser = Label(frame1, image=icoUser)
Label_icoUser.grid(row=3, column=0, sticky=N, padx=1, pady=0)
Label_contraseña = Label(frame1, text="Contraseña", font=("Aharoni", 8,))
Label_contraseña.grid(row=4, column=1, sticky=W, padx=10, pady=0)
icoPassword = Image.open("icoPassword.ico")
icoPassword = icoPassword.resize((25, 25))
icoPassword = ImageTk.PhotoImage(icoPassword)
Label_icoPassword = Label(frame1, image=icoPassword)
Label_icoPassword.grid(row=5, column=0, sticky=NW, padx=1, pady=0)
Entrada_contraseña = Entry(frame1, show="*")
Entrada_contraseña.grid(row=5, column=1, sticky=W, padx=10, pady=0)
Boton_InicioSesion = Button(frame1, text="Iniciar Sesion", font=("Aharoni", 8,), bg="#2B00FF")
Boton_InicioSesion.grid(row=6, column=1, padx=10, pady=5)

ventana.mainloop()
