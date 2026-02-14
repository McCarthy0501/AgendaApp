import database
import gui

def main():
    # 1. Aseguramos que la DB esté lista antes de abrir la ventana
    database.crear_tabla()
    
    # 2. Arrancamos la interfaz
    
    gui.inicializar_interfaz()

if __name__ == "__main__":
    main()