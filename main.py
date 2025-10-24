#Archivo Main
#Importacion de librerias
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk as kt
from BD import *
import sys, os



def ruta_recurso(relative_path):
    """Devuelve la ruta correcta para archivos dentro o fuera del exe."""
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base_path, relative_path)

color = "#EB6C10"
fondo = "#292929"
#Creacion de ventana
class Login():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Zapaisoft")
        icon_path = ruta_recurso("iconon.ico")
        self.ventana.iconbitmap(ruta_recurso("iconon.ico"))
        self.ventana.resizable(0,0)
        self.ventana.geometry("350x400+450+100")

        #Creacion de frames

        self.frame1 = Frame(self.ventana, bg = fondo)
        self.frame1.pack(fill='both', expand=True,)
        self.frame2 = Frame(self.ventana ,bg = fondo)
        self.frame2.pack(fill='both', expand=True)

        # TITULO  
        
        Titulo = Label(self.frame1, text="Inicio de Sesion", font=("Times New Roman" , 31), bg = fondo, fg = color)
        Titulo.pack()

       # LOGO

        self.Logo = Image.open(ruta_recurso("iconon.ico"))
        self.ImagenRedimensionada = self.Logo.resize((100, 100))
        self.imagen_tk = ImageTk.PhotoImage(self.ImagenRedimensionada)
        self.label_imagen = Label(self.frame1, image = self.imagen_tk)
        self.label_imagen.pack(pady = 10)

        #Creacion y posicionamiento de etiquetas, entradas y botones

        self.Label_Usuario = Label(self.frame2, text="Usuario: ", font=("Times New Roman", 15 ), bg = fondo, fg = color)
        self.Label_Usuario.grid(row = 1, column = 0, pady = 10, sticky = "e",padx = 5)
        self.Entrada_Usuario = Entry(self.frame2, width = 21)
        self.Entrada_Usuario.focus()
        self.Entrada_Usuario.grid(row = 1, column = 1, padx = 5, pady = 10, sticky = "w")
        
        self.Label_contrasena = Label(self.frame2, text="Contraseña: ", font=("Times New Roman", 15), bg = fondo, fg = color)
        self.Label_contrasena.grid(row = 2, column = 0, sticky = "w", padx = 5, pady = 10)
        self.Entrada_contrasena = Entry(self.frame2, show="*", width=21)
        self.Entrada_contrasena.grid(row = 2, column = 1, sticky = "w", padx = 5, pady = 10)

        self.Boton_InicioSesion = Button(self.frame2, text="Iniciar Sesion", command = self.login, font = ("New Times Roman", 15))
        self.Boton_InicioSesion.grid(row = 3, column = 1, padx = 1, pady = 15, columnspan = 2, sticky = "w")
        self.ventana.bind('<Return>', lambda event= None: self.Boton_InicioSesion.invoke())
        mainloop()

    # FUNCION QUE VERIFICA SI EL USUARIO Y CONTRASEÑA SON CORRECTAS PARA DAR PASO A LA SIGUIENTE PANTALLA

    def login(self):
      usuario = self.Entrada_Usuario.get()
      contrasena = self.Entrada_contrasena.get()
      comparacion = comparar_contra(usuario,contrasena)
      if comparacion:
                self.ventana.destroy()
                Eleccion()
      else: 
                messagebox.showinfo("Informacion", "Usuario o contraseña incorrectos")
               
               
    #Clase donde esta la ventana de Eleccion

class Eleccion:
    def __init__(self):

            self.ventana = Tk()
            self.ventana.title("Eleccion")
            self.ventana.iconbitmap(ruta_recurso("iconon.ico"))
            self.ventana.geometry("700x500+300+100")
            self.ventana.resizable(False, False)

            self.ImagenV = Image.open(ruta_recurso("Venta.ico"))
            self.ImagenRedimensionada = self.ImagenV.resize((100, 100))
            self.Imagen_Venta = ImageTk.PhotoImage(self.ImagenRedimensionada)

            self.ImagenR = Image.open(ruta_recurso("Registritio.ico"))
            self.ImagenRedimensionad = self.ImagenR.resize((100, 100))
            self.Imagen_Registro = ImageTk.PhotoImage(self.ImagenRedimensionad)
           

        # Frame principal para los botones horizontales
            self.frameBotones = Frame(self.ventana)
            self.frameBotones.pack(side=TOP, fill='both', expand=True)

        # Botón Venta (izquierda)
            self.botonVenta = Button(self.frameBotones, image = self.Imagen_Venta, bg=fondo, width=15, height=13, cursor="hand2", command=self.Venta)
            self.botonVenta.pack(side=LEFT, fill="both", expand=True)

        # Botón Registrar (derecha)
            self.botonRegistro = Button(self.frameBotones,image = self.Imagen_Registro, bg="orange", width = 15, height = 13, cursor = "hand2", command=self.Login_Registro)
            self.botonRegistro.pack(side=LEFT, fill="both", expand=True)

        # Frame para el botón de regresar abajo
            self.frameAbajo = Frame(self.ventana)
            self.frameAbajo.pack(side=BOTTOM, fill='x')

            self.botonRegresar = Button(self.frameAbajo, text="Regresar", font=("Times New Roman", 20), bg="grey", command=self.Regresar)
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
          Respuesta = messagebox.askyesno("Eleccion", "Estas seguro que quieres ir a la ventana de Registro? ")
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
            self.ventana.iconbitmap(ruta_recurso("iconon.ico"))
            self.ventana.resizable(1,1)
            self.ventana.geometry("370x470+450+100")

        #Creacion de frames
            self.frame1 = Frame(self.ventana,bg=fondo)
            self.frame1.pack(fill='both', expand=True)
            self.frame2 = Frame(self.ventana,bg= fondo)
            self.frame2.pack(fill='both', expand=True)

        # TITULO  
        
            Titulo = Label(self.frame1, text="Login Administrador", font=("Times New Roman" , 31), bg = fondo, fg = color)
            Titulo.pack()

       # LOGO

            self.Logo = Image.open(ruta_recurso("iconon.ico"))
            self.ImagenRedimensionada = self.Logo.resize((100, 100))
            self.imagen_tk = ImageTk.PhotoImage(self.ImagenRedimensionada)
            self.label_imagen = Label(self.frame1, image = self.imagen_tk)
            self.label_imagen.pack(pady = 10)

        #Creacion y posicionamiento de etiquetas, entradas y botones

            self.Label_Usuario = Label(self.frame2, text="Administrador: ", font=("Times New Roman", 12), bg = fondo, fg = color)
            self.Label_Usuario.grid(row = 1, column = 0, pady = 10,padx = 5 ,sticky = "e")
            self.Entrada_Admin = Entry(self.frame2, width = 21, fg = "green")
            self.Entrada_Admin.focus()
            self.Entrada_Admin.grid(row = 1, column = 1, padx = 5, pady = 10, sticky = "e")
        

            self.Label_contrasena = Label(self.frame2, text="Contraseña: ", font=("Times New Roman", 12,), bg = fondo, fg = color)
            self.Label_contrasena.grid(row = 2, column = 0, sticky = "e", padx = 5, pady = 10)
            self.Entrada_contrasena = Entry(self.frame2, show="*", width=21, fg = "green")
            self.Entrada_contrasena.grid(row = 2, column = 1, sticky = 'e', padx = 5, pady = 10)
            self.Boton_InicioSesion = Button(self.frame2, text="Iniciar Sesion", font=("Times New Roman", 15,), command = self.login)
            self.Boton_InicioSesion.grid(row = 3, column = 1, padx = 10, pady = 15, columnspan = 2, sticky = W)
            
            self.Boton_Regresar = Button(self.frame2, text = " Regresar ",font=("Times New Roman", 12,), command = self.Regresar)
            self.Boton_Regresar.grid(row = 4, column = 1)  
            
            
      def login(self):
            usuario = self.Entrada_Admin.get()
            contrasena = self.Entrada_contrasena.get()
            comparacion = comparar_Admin(usuario,contrasena)
            if comparacion:
                self.ventana.destroy()
                Registro()
            else: 
                messagebox.showinfo("Informacion", "Usuario o contraseña incorrectos")

            #Funcion de regresar

      def Regresar(self):
            self.ventana.destroy()
            Eleccion()
        
        #Funcion de Registrar admin

#Clase de registro

class Registro:
      def __init__(self):
            
            #Creacion de ventana

            self.ventana = Tk()
            self.ventana.title("Registro")
            self.ventana.iconbitmap(ruta_recurso("iconon.ico"))
            self.ventana.config(bg = fondo)

#  Creacion de frames

            self.frame1 = Frame(self.ventana, bg = "#424242")
            self.frame1.pack(fill='both', expand=True)
            self.frame2 = Frame(self.ventana, bg = fondo)
            self.frame2.pack(fill='both', expand=True)

#LOGO

            self.Logo = Image.open(ruta_recurso("iconon.ico"))
            self.ImagenRedimensionada = self.Logo.resize((100, 100))
            self.imagen_tk = ImageTk.PhotoImage(self.ImagenRedimensionada)
            self.label_imagen = Label(self.frame1, image = self.imagen_tk)
            self.label_imagen.pack(pady = 15,padx = 5, side = LEFT)

            self.Titulo = Label(self.frame1, text = "Registro", font = ("Times New Roman", 36), bg = "#424242", fg = color,)
            self.Titulo.pack(padx = 5, pady=35)
            
            # Creacion de labels,listas y entradas

            self.Label_IDProducto = Label(self.frame2, text = " ID: ", font = ("Times New Roman", 18),bg = fondo, fg = color)
            self.Label_Marca = Label(self.frame2, text = "Marca: " ,font = ("Times New Roman", 18), bg = fondo, fg = color)
            self.Label_Sexo = Label(self.frame2, text = "Sexo: " ,font = ("Times New Roman", 18), bg = fondo, fg = color)
            self.Label_Talla = Label(self.frame2, text = "Talla: " ,font = ("Times New Roman", 18), bg = fondo, fg = color)
            self.Label_Color = Label(self.frame2, text = "Color: " ,font = ("Times New Roman", 18), bg = fondo, fg = color)
            self.Label_Material = Label(self.frame2, text = "Material: " ,font = ("Times New Roman", 18), bg = fondo, fg = color)
            self.Label_Tipo = Label(self.frame2, text = "Tipo: " ,font = ("Times New Roman", 18), bg = fondo, fg = color)
            self.Label_Precio = Label(self.frame2, text = "Precio: " ,font = ("Times New Roman", 18), bg = fondo, fg = color)
            self.Label_Stock = Label(self.frame2, text = "Stock: " ,font = ("Times New Roman", 18), bg = fondo, fg = color)

            self.ListaMarca = ["Nike", "Adidas", "Converse", "Puma", "Skechers","VANS"]
            self.ListaSexo = ["Masculino", "Femenino"]
            self.ListaMaterial = ["Sintetico", "Cuero", "Plastico"]
            self.ListaTipo = ["Tenis", "Zapato", "Sandalia", "Bota", "Zapatilla"]

            self.MarcaV = StringVar()
            self.SexoV  = StringVar()
            self.TallaV = IntVar()
            self.MaterialV = StringVar()
            self.TipoV = StringVar()
            
            
            self.Entrada_IDproducto = Entry(self.frame2, cursor = "ibeam" ,width = 20)
            self.Entrada_Marca = OptionMenu(self.frame2, self.MarcaV, *self.ListaMarca)
            self.MarcaV.set("Nike")
            self.Entrada_Sexo = OptionMenu(self.frame2, self.SexoV, *self.ListaSexo)
            self.SexoV.set("Seleccione el sexo")
            self.Entrada_Talla = Spinbox(self.frame2, textvariable  = self.TallaV, from_=0, to = 10, increment = 1, font = ("Times New Roman",8))
            self.Entrada_Color = Entry(self.frame2,cursor = "ibeam", width = 20)
            self.Entrada_Material = OptionMenu(self.frame2,self.MaterialV, *self.ListaMaterial)
            self.MaterialV.set("Eliga el material")
            self.Entrada_Tipo = OptionMenu(self.frame2,self.TipoV, *self.ListaTipo)
            self.TipoV.set("Eliga el Tipo")
            self.Entrada_Precio = Entry(self.frame2, cursor = "ibeam", width = 20 )
            self.Entrada_Stock = Entry(self.frame2, cursor = "ibeam", width = 20)

            self.Botonregistro = Button(self.frame2, text = "Registrar", font = ("Times New Roman", 20),bg = "green", command = lambda: self.Agregar(self.MarcaV.get(),self.Entrada_IDproducto.get(),self.SexoV.get(),self.TallaV.get(),self.Entrada_Color.get(),self.MaterialV.get(),self.TipoV.get(),self.Entrada_Precio.get(),self.Entrada_Stock.get()))
            self.BotonActualizar =Button(self.frame2, text = "Actualizar", font = ("Times New Roman", 20),bg = "yellow", command = lambda: self.Modificar(self.MarcaV.get(),self.Entrada_IDproducto.get(),self.Entrada_Precio.get()))
            self.BotonEliminar =Button(self.frame2, text = "Eliminar", font = ("Times New Roman", 20),bg = "red", command = lambda: self.Eliminar(self.MarcaV.get(),self.Entrada_IDproducto.get()) )

            #Posicionamiento

            self.Label_IDProducto.grid(row = 1, column = 1, pady = 8,padx = 10, sticky = E)
            self.Label_Marca.grid(row = 2, column = 1, pady = 8,padx = 10, sticky = E)
            self.Label_Sexo.grid(row = 3, column = 1, pady = 8,padx = 10, sticky = E)
            self.Label_Talla.grid(row = 4, column = 1, pady = 8,padx = 10, sticky = E)
            self.Label_Color.grid(row = 5, column = 1, pady = 8,padx = 10, sticky = E)
            self.Label_Material.grid(row = 1, column = 3, pady = 8,padx = 10, sticky = E)
            self.Label_Tipo.grid(row = 2, column = 3, pady = 8,padx = 10, sticky = E)
            self.Label_Precio.grid(row = 3, column = 3, pady = 8,padx = 10, sticky = E)
            self.Label_Stock.grid(row = 4, column = 3, pady = 8,padx = 10, sticky = E)


            self.Entrada_IDproducto.grid(row = 1, column = 2, pady=8, padx = 10)
            self.Entrada_Marca.grid(row = 2, column = 2, pady=8, padx = 10)
            self.Entrada_Sexo.grid(row = 3, column = 2, pady=8, padx = 10)
            self.Entrada_Talla.grid(row = 4, column = 2, pady=8, padx = 10)
            self.Entrada_Color.grid(row = 5, column = 2, pady=8, padx = 10)
            self.Entrada_Material.grid(row = 1, column = 4, pady=8, padx = 10)
            self.Entrada_Tipo.grid(row = 2, column = 4, pady=8, padx = 10)
            self.Entrada_Precio.grid(row = 3, column = 4, pady=8, padx = 10)
            self.Entrada_Stock.grid(row = 4, column = 4, pady=8, padx = 10)
            self.Botonregistro.grid(row  = 10, column = 1, columnspan = 1, sticky = W, pady=5, padx = 5)
            self.BotonActualizar.grid(row  = 10, column = 2, columnspan = 2, pady=5, padx = 2)
            self.BotonEliminar.grid(row  = 10, column = 4, columnspan = 1, sticky = E, pady=5, padx = 5)

      def Agregar(self,tabla,id,sexo,talla,color,material,tipo,precio,stock):
            msg = agregar_nuevo_zapato(tabla,id,sexo,talla,color,material,tipo,precio,stock)
            messagebox.showinfo("Informacion",msg)
            

      def Eliminar(self,tabla,id):
            msg = Eliminar_Zapato(tabla,id)
            messagebox.showinfo("Informacion",msg)
            mainloop ()

      def Modificar(self, tabla, id, precio):

        emergente = Toplevel(self.ventana, bg = fondo)
        emergente.title("Modificar Producto")
        emergente.geometry("300x200")
        emergente.grab_set()  

        Label(emergente, text="ID del producto:", fg = color, bg = fondo).pack(pady=5)
        entrada_Id = Entry(emergente)
        entrada_Id.insert(0, id)  
        entrada_Id.pack(pady=5)

        Label(emergente, text="Nuevo precio:", bg = fondo, fg = color).pack(pady=5)
        entrada_precio = Entry(emergente)
        precio_actual = buscar_precio(tabla,entrada_Id.get())
        entrada_precio.insert(0,precio_actual)
        entrada_precio.pack(pady=5)

        def modificar():
            nuevo_id = entrada_Id.get()
            nuevo_precio = entrada_precio.get()

            msg = Modificar_Precio(tabla, nuevo_id, nuevo_precio)
            messagebox.showinfo("Información", msg)

            emergente.destroy()  # Cierra la ventana emergente

        Button(emergente, text="Actualizar", command=modificar).pack(pady=10)


Login()
