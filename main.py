#Importacion de librerias
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from BD import *

colorfondo = "#26C6DA"
fondo = "#14213D"
#Creacion de ventana
class Login():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Zapaisoft")
        self.ventana.iconbitmap("iconon.ico")
        self.ventana.resizable(0,0)
        self.ventana.geometry("350x400+450+100")

        #Creacion de frames

        self.frame1 = Frame(self.ventana,bg=colorfondo)
        self.frame1.pack(fill='both', expand=True,)
        self.frame2 = Frame(self.ventana,bg= colorfondo)
        self.frame2.pack(fill='both', expand=True)

        # TITULO  
        
        Titulo = Label(self.frame1, text="Inicio de Sesion", font=("Aharoni" , 31), bg = colorfondo)
        Titulo.pack()

       # LOGO

        self.Logo = Image.open("iconon.ico")
        self.ImagenRedimensionada = self.Logo.resize((100, 100))
        self.imagen_tk = ImageTk.PhotoImage(self.ImagenRedimensionada)
        self.label_imagen = Label(self.frame1, image = self.imagen_tk)
        self.label_imagen.pack(pady = 10)

        #Creacion y posicionamiento de etiquetas, entradas y botones

        self.Label_Usuario = Label(self.frame2, text="Usuario: ", font=("Aharoni", 12), bg = colorfondo)
        self.Label_Usuario.grid(row = 1, column = 0, pady = 10, sticky = "nsew")
        self.Entrada_Usuario = Entry(self.frame2, width = 21)
        self.Entrada_Usuario.focus()
        self.Entrada_Usuario.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "nesw")
        
        self.Label_contrasena = Label(self.frame2, text="Contraseña: ", font=("Aharoni", 12,), bg = colorfondo)
        self.Label_contrasena.grid(row = 2, column = 0, sticky = "nesw", padx = 10, pady = 10)
        self.Entrada_contrasena = Entry(self.frame2, show="*", width=21)
        self.Entrada_contrasena.grid(row = 2, column = 1, sticky = 'nsew', padx = 10, pady = 10)

        self.Boton_InicioSesion = Button(self.frame2, text="Iniciar Sesion", font=("Aharoni", 15,), command = self.login)
        self.Boton_InicioSesion.grid(row = 3, column = 1, padx = 10, pady = 15, columnspan = 2, sticky = W)

        mainloop()

    # FUNCION QUE VERIFICA SI EL USUARIO Y CONTRASEÑA SON CORRECTAS PARA DAR PASO A LA SIGUIENTE PANTALLA

    def login(self):
      usuario = self.Entrada_Usuario.get()
      contrasena = self.Entrada_contrasena.get()
      if usuario == "edgar" and contrasena == "1234":
                messagebox.showinfo("Informacion", "Contrasena correcta")
                self.ventana.destroy()
                Eleccion()
      else: 
                messagebox.showinfo("Informacion", "Usuario o contraseña incorrectos")
               
               #Clase donde esta la ventana de Eleccion

class Eleccion:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Eleccion")
        self.ventana.iconbitmap("iconon.ico")
        self.ventana.geometry("700x500+300+100")
        self.ventana.resizable(False, False)

        # Frame principal para los botones horizontales
        self.frameBotones = Frame(self.ventana)
        self.frameBotones.pack(side=TOP, fill='both', expand=True)

        # Botón Venta (izquierda)
        self.botonVenta = Button(self.frameBotones, text="Venta", font=("Aharoni", 20), bg=colorfondo, width=15, height=13, cursor="pirate", command=self.Venta)
        self.botonVenta.pack(side=LEFT, fill="both", expand=True)

        # Botón Registrar (derecha)
        self.botonRegistro = Button(self.frameBotones, text="Registrar", font=("Aharoni", 20), bg="orange", width=15, height=13, cursor="hand2", command=self.Login_Registro)
        self.botonRegistro.pack(side=LEFT, fill="both", expand=True)

        # Frame para el botón de regresar abajo
        self.frameAbajo = Frame(self.ventana)
        self.frameAbajo.pack(side=BOTTOM, fill='x')

        self.botonRegresar = Button(self.frameAbajo, text="Regresar", font=("aharoni", 20), bg="grey", command=self.Regresar)
        self.botonRegresar.pack(fill='x')

        mainloop()

            # Funcion para regresar a la ventana de login

    def Regresar(self):
        self.ventana.destroy()
        Login()
        
        #Funcion para mostrar un messagebox para confirmar si quiere ir a la ventan de Venta

    def Venta(self):
          s=1+1

          #Funcion para mostrar un messagebox para confirmar si quiere ir a la ventana de registro

    def Login_Registro(self):
          Respuesta = messagebox.askyesno("Lechon", "Estas seguro que quieres ir a la ventana de Registro? ")
          if Respuesta == True:
            self.ventana.destroy()
            Login_Registro()
          else:
                print("1")

          ### Clase donde esta la ventana de inicio de sesion de la ventana de registro

class Login_Registro:
      def __init__(self):
           
            self.ventana = Tk()
            self.ventana.title("Zapaisoft")
            self.ventana.iconbitmap("iconon.ico")
            self.ventana.resizable(0,0)
            self.ventana.geometry("370x400+450+100")

        #Creacion de frames
            self.frame1 = Frame(self.ventana,bg=fondo)
            self.frame1.pack(fill='both', expand=True,)
            self.frame2 = Frame(self.ventana,bg= fondo)
            self.frame2.pack(fill='both', expand=True)

        # TITULO  
        
            Titulo = Label(self.frame1, text="Login Administrador", font=("Aharoni" , 31), bg = fondo, fg = "green")
            Titulo.pack()

       # LOGO

            self.Logo = Image.open("iconon.ico")
            self.ImagenRedimensionada = self.Logo.resize((100, 100))
            self.imagen_tk = ImageTk.PhotoImage(self.ImagenRedimensionada)
            self.label_imagen = Label(self.frame1, image = self.imagen_tk)
            self.label_imagen.pack(pady = 10)

        #Creacion y posicionamiento de etiquetas, entradas y botones

            self.Label_Usuario = Label(self.frame2, text="Administrador: ", font=("Aharoni", 12), bg = fondo, fg = "green")
            self.Label_Usuario.grid(row = 1, column = 0, pady = 10, sticky = "nsew")
            self.Entrada_Usuario = Entry(self.frame2, width = 21, fg = "green")
            self.Entrada_Usuario.focus()
            self.Entrada_Usuario.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "nesw")
        

            self.Label_contrasena = Label(self.frame2, text="Contraseña: ", font=("Aharoni", 12,), bg = fondo, fg = "green")
            self.Label_contrasena.grid(row = 2, column = 0, sticky = "nesw", padx = 10, pady = 10)
            self.Entrada_contrasena = Entry(self.frame2, show="*", width=21, fg = "green")
            self.Entrada_contrasena.grid(row = 2, column = 1, sticky = 'nsew', padx = 10, pady = 10)
            self.Boton_InicioSesion = Button(self.frame2, text="Iniciar Sesion", font=("Aharoni", 15,))
            self.Boton_InicioSesion.grid(row = 3, column = 1, padx = 10, pady = 15, columnspan = 2, sticky = W)

            mainloop()
            
      
Login()
