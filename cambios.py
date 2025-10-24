        def Modificar(self, tabla, id, precio):

        emergente = Toplevel(self.ventana)
        emergente.title("Modificar Producto")
        emergente.geometry("300x200")
        emergente.grab_set()  

        Label(emergente, text="ID del producto:").pack(pady=5)
        entrada_Id = Entry(emergente)
        entrada_Id.insert(0, id)  
        entrada_Id.pack(pady=5)

        Label(emergente, text="Nuevo precio:").pack(pady=5)
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