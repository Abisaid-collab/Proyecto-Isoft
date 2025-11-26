from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
import BD

# ============================
#       CLASES DE PANTALLAS
# ============================

class LoginScreen(Screen):
    def do_login(self):
        usuario = self.ids.usuario.text
        contra = self.ids.contra.text

        if BD.comparar_contra(usuario, contra) or BD.comparar_Admin(usuario, contra):
            self.manager.current = "menu"
        else:
            self.ids.mensaje.text = "Usuario o contraseña incorrectos"


class MenuScreen(Screen):
    pass


class AgregarScreen(Screen):
    def agregar(self):
        tabla = self.ids.tabla.text
        idp = self.ids.idp.text
        sexo = self.ids.sexo.text
        talla = self.ids.talla.text
        color = self.ids.color.text
        material = self.ids.material.text
        tipo = self.ids.tipo.text
        precio = self.ids.precio.text
        stock = self.ids.stock.text

        if not all([tabla, idp, sexo, talla, color, material, tipo, precio, stock]):
            self.ids.mensaje.text = "Faltan datos"
            return

        msg = BD.agregar_nuevo_zapato(tabla, idp, sexo, talla, color, material, tipo, precio, stock)
        self.ids.mensaje.text = msg


class ModificarScreen(Screen):
    def buscar(self):
        tabla = self.ids.tabla.text
        idp = self.ids.idp.text

        precio = BD.buscar_precio(tabla, idp)
        if precio == "":
            self.ids.mensaje.text = "Producto no encontrado"
        else:
            self.ids.precio.text = str(precio)
            self.ids.mensaje.text = "Precio encontrado"

    def modificar(self):
        tabla = self.ids.tabla.text
        idp = self.ids.idp.text
        precio = self.ids.precio.text

        if not all([tabla, idp, precio]):
            self.ids.mensaje.text = "Faltan datos"
            return

        msg = BD.Modificar_Precio(tabla, idp, precio)
        self.ids.mensaje.text = msg


class EliminarScreen(Screen):
    def eliminar(self):
        tabla = self.ids.tabla.text
        idp = self.ids.idp.text

        if not all([tabla, idp]):
            self.ids.mensaje.text = "Faltan datos"
            return

        msg = BD.Eliminar_Zapato(tabla, idp)
        self.ids.mensaje.text = msg


class BuscarScreen(Screen):
    precio = StringProperty("")

    def buscar(self):
        tabla = self.ids.tabla.text
        idp = self.ids.idp.text
        
        res = BD.buscar_precio(tabla, idp)
        if res == "":
            self.precio = "Producto no encontrado"
        else:
            self.precio = f"Precio: {res}"


# ============================
#            KV
# ============================

kv = """
#:import Factory kivy.factory.Factory

<LabelTitle@Label>:
    font_size: 32
    bold: True
    size_hint_y: None
    height: 60

<LabelSub@Label>:
    font_size: 20
    size_hint_y: None
    height: 40

<Input@TextInput>:
    size_hint_y: None
    height: 45
    multiline: False

<ButtonMain@Button>:
    size_hint_y: None
    height: 50

ScreenManager:
    LoginScreen:
    MenuScreen:
    AgregarScreen:
    ModificarScreen:
    EliminarScreen:
    BuscarScreen:

<LoginScreen>:
    name: "login"
    BoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 10

        LabelTitle:
            text: "Login"

        Input:
            id: usuario
            hint_text: "Usuario"

        Input:
            id: contra
            hint_text: "Contraseña"
            password: True

        ButtonMain:
            text: "Ingresar"
            on_release: root.do_login()

        LabelSub:
            id: mensaje
            text: ""

<MenuScreen>:
    name: "menu"
    BoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 10

        LabelTitle:
            text: "Menú Principal"

        ButtonMain:
            text: "Agregar Producto"
            on_release: app.root.current = "agregar"

        ButtonMain:
            text: "Modificar Precio"
            on_release: app.root.current = "modificar"

        ButtonMain:
            text: "Eliminar Producto"
            on_release: app.root.current = "eliminar"

        ButtonMain:
            text: "Buscar Precio"
            on_release: app.root.current = "buscar"

        ButtonMain:
            text: "Salir"
            on_release: app.root.current = "login"

<AgregarScreen>:
    name: "agregar"
    BoxLayout:
        orientation: "vertical"
        padding: 15
        spacing: 8

        LabelTitle:
            text: "Agregar Producto"

        Input:
            id: tabla
            hint_text: "Tabla (ejemplo: VANS)"

        Input:
            id: idp
            hint_text: "ID del producto"

        Input:
            id: sexo
            hint_text: "Sexo"

        Input:
            id: talla
            hint_text: "Talla"

        Input:
            id: color
            hint_text: "Color"

        Input:
            id: material
            hint_text: "Material"

        Input:
            id: tipo
            hint_text: "Tipo"

        Input:
            id: precio
            hint_text: "Precio"

        Input:
            id: stock
            hint_text: "Stock"

        ButtonMain:
            text: "Agregar"
            on_release: root.agregar()

        LabelSub:
            id: mensaje
            text: ""

        ButtonMain:
            text: "Regresar"
            on_release: app.root.current = "menu"

<ModificarScreen>:
    name: "modificar"
    BoxLayout:
        orientation: "vertical"
        padding: 15
        spacing: 8

        LabelTitle:
            text: "Modificar Precio"

        Input:
            id: tabla
            hint_text: "Tabla"

        Input:
            id: idp
            hint_text: "ID del producto"

        ButtonMain:
            text: "Buscar precio"
            on_release: root.buscar()

        Input:
            id: precio
            hint_text: "Nuevo precio"

        ButtonMain:
            text: "Modificar"
            on_release: root.modificar()

        LabelSub:
            id: mensaje
            text: ""

        ButtonMain:
            text: "Regresar"
            on_release: app.root.current = "menu"

<EliminarScreen>:
    name: "eliminar"
    BoxLayout:
        orientation: "vertical"
        padding: 15
        spacing: 8

        LabelTitle:
            text: "Eliminar Producto"

        Input:
            id: tabla
            hint_text: "Tabla"

        Input:
            id: idp
            hint_text: "ID del producto"

        ButtonMain:
            text: "Eliminar"
            on_release: root.eliminar()

        LabelSub:
            id: mensaje
            text: ""

        ButtonMain:
            text: "Regresar"
            on_release: app.root.current = "menu"

<BuscarScreen>:
    name: "buscar"
    BoxLayout:
        orientation: "vertical"
        padding: 15
        spacing: 8

        LabelTitle:
            text: "Buscar Precio"

        Input:
            id: tabla
            hint_text: "Tabla"

        Input:
            id: idp
            hint_text: "ID del producto"

        ButtonMain:
            text: "Buscar"
            on_release: root.buscar()

        LabelSub:
            text: root.precio

        ButtonMain:
            text: "Regresar"
            on_release: app.root.current = "menu"
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(kv)

MainApp().run()
