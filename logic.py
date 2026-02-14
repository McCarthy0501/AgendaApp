

#funcion de validar datos
def validar_campos(**datos):
    
    for campo , valor in datos.items():
        #print(f"{campo}")

        if valor.strip() == "":
            return False,f"Falta el campo {campo}"

        #validacion de la cedula
        if campo.lower() == "cedula":
            if not valor.isdigit():
                return False,f"el campo {campo} debe ser numerico "
            if len(valor)<5:
                return False,f"cedula demasiado corta"

        #validacion de los textos quita espacionn en blanco y se asegura que sea texto y no numeros
        if campo.lower() in ["nombre","apellido"]:
            if len(valor.strip())<2 or  not valor.replace(" ","").isalpha():
                return False,f"el valor del campo {campo} debe tener mas de 2 caracteres y deben ser caracteres de texto  "
        
        #validacion de la direccion y pais
        if campo.lower() in ["direccion","pais"]:
            if len(valor.strip())<3 or  not valor.replace(" ","").isalpha():
                return False,f"el valor del campo {campo} debe tener mas de 2 caracteres y deben ser caracteres de texto  "
        



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
            print(f'{mensaje}')
            return

        

        # 3. Mandas la información al búnker (database.py)
    import database
    database.insertar_contacto(nom, ape, ced, dire, pais)
        
        # 4. AHORA SÍ, cierras la ventana
    print("Guardado. Cerrando formulario...")
    ventana.destroy()
