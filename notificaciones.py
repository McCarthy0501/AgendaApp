from CTkMessagebox import CTkMessagebox

def mensaje_exito(titulo, mensaje):
    CTkMessagebox(title=titulo, message=mensaje, icon="check", option_1="Aceptar")

def mensaje_error(titulo, mensaje):
    CTkMessagebox(title=titulo, message=mensaje, icon="cancel", option_1="Entendido")


