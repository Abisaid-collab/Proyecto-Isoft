#Importacion de librerias
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
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
      comparacion = comparar_contra(usuario,contrasena)
      if comparacion:
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
            self.ventana.iconbitmap("iconon.ico")
            self.ventana.resizable(1,1)
            self.ventana.geometry("370x470+450+100")

        #Creacion de frames
            self.frame1 = Frame(self.ventana,bg=fondo)
            self.frame1.pack(fill='both', expand=True)
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
            self.Boton_Regresar = Button(self.frame2, text = " Regresar ",font=("Aharoni", 12,), command = self.Regresar)
            self.Boton_Regresar.grid(row = 3, column = 0)
            self.Boton_InicioSesion = Button(self.frame2, text="Iniciar Sesion", font=("Aharoni", 15,), command = self.login)
            self.Boton_InicioSesion.grid(row = 3, column = 1, padx = 10, pady = 15, columnspan = 2, sticky = W)
    
      def login(self):
            usuario = self.Entrada_Usuario.get()
            contrasena = self.Entrada_contrasena.get()
            comparacion = comparar_Admin(usuario,contrasena)
            if comparacion:
                messagebox.showinfo("Informacion", "Contrasena correcta")
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
            self.ventana.iconbitmap("iconon.ico")
            self.ventana.config(bg = fondo)

#  Creacion de frames

            self.frame1 = Frame(self.ventana, bg = fondo)
            self.frame1.pack(fill='both', expand=True)
            self.frame2 = Frame(self.ventana, bg = fondo)
            self.frame2.pack(fill='both', expand=True)

#LOGO

            self.Logo = Image.open("iconon.ico")
            self.ImagenRedimensionada = self.Logo.resize((100, 100))
            self.imagen_tk = ImageTk.PhotoImage(self.ImagenRedimensionada)
            self.label_imagen = Label(self.frame1, image = self.imagen_tk)
            self.label_imagen.pack(pady = 15)
            
            # Creacion de labels,listas y entradas

            self.Label_IDProducto = Label(self.frame2, text = " ID: ", font = ("Aharoni", 18),bg = fondo, fg = "white")
            self.Label_Marca = Label(self.frame2, text = "Marca: " ,font = ("Aharoni", 18), bg = fondo, fg = "white")
            self.Label_Sexo = Label(self.frame2, text = "Sexo: " ,font = ("Aharoni", 18), bg = fondo, fg = "white")
            self.Label_Talla = Label(self.frame2, text = "Talla: " ,font = ("Aharoni", 18), bg = fondo, fg = "white")
            self.Label_Color = Label(self.frame2, text = "Color: " ,font = ("Aharoni", 18), bg = fondo, fg = "white")
            self.Label_Material = Label(self.frame2, text = "Material: " ,font = ("Aharoni", 18), bg = fondo, fg = "white")
            self.Label_Tipo = Label(self.frame2, text = "Tipo: " ,font = ("Aharoni", 18), bg = fondo, fg = "white")
            self.Label_Precio = Label(self.frame2, text = "Precio: " ,font = ("Aharoni", 18), bg = fondo, fg = "white")
            self.Label_Stock = Label(self.frame2, text = "Stock: " ,font = ("Aharoni", 18), bg = fondo, fg = "white")

            self.ListaMarca = ["Nike", "Adidas", "Converse", "Puma", "Skechers","VANS"]
            self.ListaSexo = ["Masculino", "Femenino"]
            self.ListaMaterial = ["Sintetico", "Cuero", "Plastico"]
            self.ListaTipo = ["Tenis", "Zapato", "Sandalia", "Bota", "Zapatilla"]

            self.MarcaV = StringVar()
            self.SexoV  = StringVar()
            self.TallaV = IntVar()
            self.MaterialV = StringVar()
            self.TipoV = StringVar()
            
            
            self.Entrada_IDproducto = Entry(self.frame2, cursor = "hand2" )
            self.Entrada_Marca = OptionMenu(self.frame2, self.MarcaV, *self.ListaMarca)
            self.MarcaV.set("Seleccione la Marca")
            self.Entrada_Sexo = OptionMenu(self.frame2, self.SexoV, *self.ListaSexo)
            self.SexoV.set("Seleccione el Sexo")
            self.Entrada_Talla = Spinbox(self.frame2, textvariable  = self.TallaV, from_=0, to = 10, increment = 1, font = ("Aharoni",8))
            self.Entrada_Color = Entry(self.frame2,cursor = "ibeam")
            self.Entrada_Material = OptionMenu(self.frame2,self.MaterialV, *self.ListaMaterial)
            self.MaterialV.set("Eliga el material")
            self.Entrada_Tipo = OptionMenu(self.frame2,self.TipoV, *self.ListaTipo)
            self.TipoV.set("Eliga el Tipo")
            self.Entrada_Precio = Entry(self.frame2, cursor = "ibeam" )
            self.Entrada_Stock = Entry(self.frame2, cursor = "ibeam")

            self.Botonregistro = Button(self.frame2, text = "Registrar", font = ("Aharoni", 16), command = lambda: self.Agregar(self.MarcaV.get(),self.Entrada_IDproducto.get(),self.SexoV.get(),self.TallaV.get(),self.Entrada_Color.get(),self.MaterialV.get(),self.TipoV.get(),self.Entrada_Precio.get(),self.Entrada_Stock.get()))
            self.BotonActualizar =Button(self.frame2, text = "Actualizar", font = ("Aharoni", 16), command = lambda: self.Modificar(self.MarcaV.get(),self.Entrada_IDproducto.get(),self.Entrada_Precio.get()))
            self.BotonEliminar =Button(self.frame2, text = "Eliminar", font = ("Aharoni", 16), command = lambda: self.Eliminar(self.MarcaV.get(),self.Entrada_IDproducto.get()) )

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
            self.Botonregistro.grid(row  = 10, column = 1, columnspan = 1, sticky = NSEW, pady=8, padx = 2)
            self.BotonActualizar.grid(row  = 10, column = 2, columnspan = 1, sticky = NSEW, pady=8, padx = 2)
            self.BotonEliminar.grid(row  = 10, column = 3, columnspan = 1, sticky = NSEW, pady=8, padx = 2)

      def Agregar(self,tabla,id,sexo,talla,color,material,tipo,precio,stock):
            msg = agregar_nuevo_zapato(tabla,id,sexo,talla,color,material,tipo,precio,stock)
            messagebox.showinfo("Informacion",msg)
            

      def Eliminar(self,tabla,id):
            msg = Eliminar_Zapato(tabla,id)
            messagebox.showinfo("Informacion",msg)
            mainloop ()

      def Modificar(self,tabla,id,precio):
            msg = Modificar_Precio(tabla,id,precio)
            messagebox.showinfo("Informacion",msg)


Login()
