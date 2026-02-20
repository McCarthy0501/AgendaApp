from notificaciones import mensaje_exito,mensaje_error

#funcion de validar datos
def validar_campos(**datos):
    
    for campo , valor in datos.items():
        #print(f"{campo}")

        if valor.strip() == "":
            return False,mensaje_error("Algo Salio Mal","Los Campos del Formulario no deben quedar Vacios")

        #validacion de la cedula
        if campo.lower() == "cedula":
            if not valor.isdigit():
                return False,mensaje_error("Algo Salio Mal",f"El Campos de {campo} debe ser Numerico ")
            if len(valor)<5:
                return False,mensaje_error("Algo Salio Mal",f"El campo {campo} debe tener mas de 5 Caracteres Numericos")

        #validacion de los textos quita espacionn en blanco y se asegura que sea texto y no numeros
        if campo.lower() in ["nombre","apellido"]:
            if len(valor.strip())<2 or  not valor.replace(" ","").isalpha():
                return False,mensaje_error("Algo Salio Mal",f"El Campo {campo} debe tener mas de 2 caracteres y deben ser caracteres de texto  ")
               
        
        #validacion de la direccion y pais
        if campo.lower() in ["direccion","pais"]:
            if len(valor.strip())<3 or  not valor.replace(" ","").isalpha():
                return False,mensaje_error("Algo Salio Mal",f"El Campo {campo} debe tener mas de 2 caracteres y deben ser caracteres de texto  ")
        



    return True,"Todo en orden"



#boton de guardado de formualrio
def guardar_datos(ventana):
     # 1. Recolectas la información
    nom = ventana.entry_nombre.get()
    ape = ventana.entry_apellido.get()
    ced = ventana.entry_cedula.get()
    dire = ventana.entry_direccion.get()
    pais = ventana.entry_pais.get()

        # 2. Validamos que no estén vacíos con una funcion del modulo logic
    exito,mensaje=validar_campos(
            nombre=nom,
            apellido=ape,
            cedula=ced,
            direccion=dire,
            pais=pais

        )

        #mensaje de error
    if not exito:
            mensaje_error("Algo salio Mal","Error al Guardar el Contacto")
            return

        

        # 3. Mandas la información al búnker (database.py)
    import database
    database.insertar_contacto(nom, ape, ced, dire, pais)
        
   
    ventana.destroy()





