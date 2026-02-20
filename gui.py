import customtkinter as ctk
from logic import guardar_datos
from notificaciones import mensaje_exito,mensaje_error

#colores de la interfaz
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class VentanaRegistro(ctk.CTkToplevel):
    def __init__(self, master, *args, **kwargs):
        # 1. Pasamos el 'master' (la ventana principal) explícitamente
        super().__init__(master, *args, **kwargs)
        
        self.title("Agenda de Registros")
        self.geometry("450x550")
        
        # 2. Obligamos a la ventana a saltar al frente
        self.attributes("-topmost", True)
        self.focus() # Le da el foco para que puedas escribir de una
        
        # --- TÍTULO ---
        self.label_tit = ctk.CTkLabel(self, text="DATOS DE LA PERSONA", font=("Roboto", 20, "bold"))
        self.label_tit.pack(pady=20)

        # --- CAMPOS (Asegúrate de que digan 'self' al principio) ---
        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombres", width=300)
        self.entry_nombre.pack(pady=10)
        
        self.entry_apellido = ctk.CTkEntry(self, placeholder_text="Apellidos", width=300)
        self.entry_apellido.pack(pady=10)

        self.entry_cedula = ctk.CTkEntry(self, placeholder_text="Cédula", width=300)
        self.entry_cedula.pack(pady=10)

        self.entry_direccion = ctk.CTkEntry(self, placeholder_text="DIRECCION", width=300)
        self.entry_direccion.pack(pady=10)

        self.entry_pais = ctk.CTkEntry(self, placeholder_text="PAIS", width=300)
        self.entry_pais.pack(pady=10)



        self.btn_guardar = ctk.CTkButton(self, text="GUARDAR", fg_color="green", command=lambda:guardar_datos(self))
        self.btn_guardar.pack(pady=30)




#eliminar contacto 
class VentanaEliminacion(ctk.CTkToplevel):
    def __init__(self, master, *args, **kwargs):
        # 1. Pasamos el 'master' (la ventana principal) explícitamente
        super().__init__(master, *args, **kwargs)
        
        self.title("Agenda de Registros")
        self.geometry("450x550")
        
        # 2. Obligamos a la ventana a saltar al frente
        self.attributes("-topmost", True)
        self.focus() # Le da el foco para que puedas escribir de una
        
        # --- TÍTULO ---
        self.label_tit = ctk.CTkLabel(self, text="Eliminar Contacto", font=("Roboto", 20, "bold"))
        self.label_tit.pack(pady=20)

            # --- DENTRO DE TU CLASE VentanaEliminacion ---

        # 1. Obtenemos la lista de la base de datos
        import database
        datos = database.obtener_contactos()

        opciones = [] #creo una lsita vacia 

        for i in datos: #recorro la consulda de la base de datos y ordeno los datos traidos
            formato= f'{i[0]}  {i[1]}  V- {i[2]}'
            opciones.append(formato) #agg los datos en la lista vacia 
        
        #mensaje de error
        if not opciones:
            opciones=['no hay contactos para borrar']

      # 3. Agregar el Select (OptionMenu)
        self.label_sel = ctk.CTkLabel(self, text="Seleccione el contacto a eliminar:", font=("Roboto", 14))
        self.label_sel.pack(pady=10)


        #el select donde se muestran los contactos guardados
        self.select_eliminar = ctk.CTkOptionMenu(
            self, 
            values=opciones, #pasamos la lista con los contactos
            width=300
        )
        self.select_eliminar.pack(pady=15)

        # 4. Botón de acción
        self.btn_confirmar = ctk.CTkButton(
            self, 
            text="Eliminar de la Base de Datos",
            fg_color="#A82424", # Rojo oscuro para advertencia
            command=self.confirmar_proceso #funcion de borrar el contacto  aun en proceso
        )
        self.btn_confirmar.pack(pady=20)


#confirmacion de la operacion de borrado
    def confirmar_proceso(self):
        seleccion = self.select_eliminar.get()
        
        if seleccion == 'No hay contactos para borrar':
            return

        try:
            # 1. Extraemos la cédula
            # Buscamos lo que está entre (V-)
            cedula_a_borrar = seleccion.split("V-")[1].replace(" ", "")
            
            
            # 2. Llamamos a tu función de database.py
            import database
            database.borrar_Contacto_Por_Cedula(cedula_a_borrar)
            
            # 3. Refrescamos la ventana principal (el master)
            self.master.mostrar_contactos()
            
            # 4. Cerramos la ventana de eliminación
            self.destroy()
            
        except Exception as e:
            print(f"Error al procesar el borrado: {e}")
            




#ventana principal
class AgendaApp (ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("S.I.P - Sistema de Control")
        self.attributes('-zoomed', True) #para que la ventana de la app se ajuste a la resulucion del pc

        # 1. Título
        self.label_titulo = ctk.CTkLabel(self, text="SISTEMA DE CONTROL ", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        # 2. Frame de Controles (Donde está tu botón)
        self.frame_controles = ctk.CTkFrame(self)
        self.frame_controles.pack(pady=10, padx=20, fill="x")

        self.btn_probar = ctk.CTkButton(self.frame_controles, text="Agregar Nuevo Contacto", command=self.agregar_contacto)
        self.btn_probar.pack(side="left", padx=20, pady=10)

        self.btn_refrescar = ctk.CTkButton(self.frame_controles, text="Actualizar Lista", command=self.mostrar_contactos, fg_color="gray")
        self.btn_refrescar.pack(side="left", padx=10)

        self.btn_refrescar = ctk.CTkButton(self.frame_controles, text="Eliminar contacto", command=self.eliminar_contacto, fg_color="red")
        self.btn_refrescar.pack(side="left", padx=10)

        self.btn_refrescar = ctk.CTkButton(self.frame_controles, text="Modificar contacto", command=self.modificar_contacto, fg_color="violet")
        self.btn_refrescar.pack(side="left", padx=10)

        # 3. ÁREA DE LISTADO (donde se muestran los contactos)
        # Aquí es donde se van a mostrar los contactos
        self.frame_lista = ctk.CTkScrollableFrame(self, width=1500, height=1100, label_text="PERSONAS REGISTRADAS")
        self.frame_lista.pack(pady=20, padx=20)

        # Cargar los datos automáticamente al abrir
        self.mostrar_contactos()

    def agregar_contacto(self):
        # Tu función de siempre que abre la ventana emergente
        VentanaRegistro(self)

    def mostrar_contactos(self):
        # A. Limpiar la lista actual para no repetir nombres al refrescar
        for widget in self.frame_lista.winfo_children():
            widget.destroy()

        # B. Traer los datos de la base de datos
        import database
        datos = database.obtener_contactos()

        # C. Crear una "fila" por cada funcionario
        for persona in datos:
            nombre_completo = f"Nombre : {persona[0]} | Apellido : {persona[1]} | "
            info_detallada = f"Cédula de Identidad V-{persona[2]}  |  Direccion: {persona[3]}  |  Pais: {persona[4]}"
            mensaje_exito("Proceso Realizado con exito ","Contactos actualizados")
            
            
            # Creamos un pequeño frame para cada contacto para que se vea ordenado
            fila = ctk.CTkFrame(self.frame_lista)
            fila.pack(fill="x", pady=5, padx=5)

            label_nom = ctk.CTkLabel(fila, text=nombre_completo, font=("Roboto", 14, "bold"), width=200, anchor="w")
            label_nom.pack(side="left", padx=10)

            label_info = ctk.CTkLabel(fila, text=info_detallada, font=("Roboto", 14, "bold"), width=200, anchor="w")
            label_info.pack(side="left", padx=20)
    
    #boton de eliminar
    def eliminar_contacto(self):
        VentanaEliminacion(self)
    #boton de modificar
    def modificar_contacto(self):
        print("Modificando...")

def inicializar_interfaz():
    #iniciamos la ventana
    app=AgendaApp()
    app.mainloop()



if __name__ == "__main__":
    inicializar_interfaz()