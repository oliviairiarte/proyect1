from main2 import organizar_descargas
from generate_report import add_to_report
import tkinter as tk
from tkinter import filedialog, messagebox

# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("Organizador Pro v2.0")
ventana.geometry("400x200")

# 2. Función conectada
def seleccionar_y_limpiar():
    ruta = filedialog.askdirectory()
    
    if ruta:
        try:
            # --- AQUÍ CONECTAMOS CON TU LÓGICA ---
            # Ejecutamos la función que importamos de main2
            lista_info = organizar_descargas(ruta)
            
            # Guardamos en el CSV usando la función de tu otro módulo
            add_to_report(lista_info)
            
            # Calculamos cuántos archivos se movieron para avisar
            cantidad = len(lista_info)
            messagebox.showinfo("Éxito", f"Se organizaron {cantidad} archivos en: {ruta}")
            
        except Exception as e:
            # Si algo falla en el proceso, la GUI nos avisa sin cerrarse
            messagebox.showerror("Error", f"No se pudo completar la limpieza: {e}")
    else:
        messagebox.showwarning("Atención", "No seleccionaste ninguna carpeta")

# 3. Botón (puedes ponerle color para que destaque)
boton_limpiar = tk.Button(
    ventana, 
    text="Elegir Carpeta y Organizar", 
    command=seleccionar_y_limpiar,
    bg="#6FDE73", # Un verde bonito
    fg="white",   # Texto blanco
    font=("Arial", 10, "bold")
)
boton_limpiar.pack(pady=50)

# 4. Arrancar
ventana.mainloop()