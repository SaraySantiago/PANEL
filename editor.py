import tkinter as tk
from tkinter import messagebox
import os

# Ruta del archivo a editar
archivo_path = "/home/panel/cosa.txt"

# Función para cargar el contenido del archivo
def cargar_archivo():
    try:
        if os.path.exists(archivo_path):
            with open(archivo_path, "r") as archivo:
                contenido = archivo.read()
                text_area.delete(1.0, tk.END)  # Borra el contenido actual
                text_area.insert(tk.END, contenido)  # Inserta el contenido del archivo
        else:
            messagebox.showwarning("Advertencia", f"El archivo '{archivo_path}' no existe.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al abrir el archivo: {e}")

# Función para guardar el contenido en el archivo
def guardar_archivo():
    try:
        contenido = text_area.get(1.0, tk.END).strip()
        if contenido == "":
            messagebox.showwarning("Advertencia", "El contenido está vacío, no se guardará nada.")
            return

        with open(archivo_path, "w") as archivo:
            archivo.write(contenido)
        messagebox.showinfo("Éxito", "Archivo guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al guardar el archivo: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Editor de texto")
ventana.geometry("600x400")

# Crear un marco para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10, fill=tk.X)

# Botones para cargar y guardar archivo
boton_abrir = tk.Button(frame_botones, text="Cargar archivo", command=cargar_archivo)
boton_abrir.pack(side=tk.LEFT, padx=10)

boton_guardar = tk.Button(frame_botones, text="Guardar archivo", command=guardar_archivo)
boton_guardar.pack(side=tk.LEFT, padx=10)

# Crear un canvas para el área de texto y el scrollbar
canvas = tk.Canvas(ventana, bg="#f0f0f0")  # Fondo gris claro para el canvas
canvas.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

# Crear un marco para el área de texto dentro del canvas
frame_texto = tk.Frame(canvas, bg="#f0f0f0")  # Fondo gris claro para el marco de texto
canvas.create_window((0, 0), window=frame_texto, anchor="nw")

# Crear el área de texto en el marco con fondo grisáceo
text_area = tk.Text(frame_texto, wrap=tk.WORD, width=60, height=15, bg="#d3d3d3", fg="black", font=("Arial", 10))
text_area.pack(padx=10, pady=10)

# Configurar el scrollbar con el canvas
canvas.configure(yscrollcommand=scrollbar.set)
frame_texto.bind(
    "<Configure>", 
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Cargar el archivo al inicio
cargar_archivo()

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
