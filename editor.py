import tkinter as tk
from tkinter import filedialog, messagebox

# Función para cargar el contenido del archivo seleccionado
def cargar_archivo():
    archivo_path = filedialog.askopenfilename(initialdir="/home/panel", title="Abrir archivo", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if archivo_path:
        try:
            with open(archivo_path, "r") as archivo:
                contenido = archivo.read()
                text_area.delete(1.0, tk.END)  # Borra el contenido actual
                text_area.insert(tk.END, contenido)  # Inserta el contenido del archivo
            ventana.title(f"Editor de texto - {archivo_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al abrir el archivo: {e}")

# Función para guardar el contenido del área de texto en el archivo actual
def guardar_archivo():
    try:
        contenido = text_area.get(1.0, tk.END).strip()
        if contenido == "":
            messagebox.showwarning("Advertencia", "El contenido está vacío, no se guardará nada.")
            return

        with open("/home/panel /cosa.txt", "w") as archivo:
            archivo.write(contenido)
        messagebox.showinfo("Éxito", "Archivo guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al guardar el archivo: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Editor de texto")
ventana.geometry("600x400")

# Crear el área de texto para editar el archivo
text_area = tk.Text(ventana, wrap=tk.WORD, width=60, height=20)
text_area.pack(padx=10, pady=10)

# Crear los botones de cargar y guardar
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_abrir = tk.Button(frame_botones, text="Abrir archivo", command=cargar_archivo)
boton_abrir.grid(row=0, column=0, padx=10)

boton_guardar = tk.Button(frame_botones, text="Guardar archivo", command=guardar_archivo)
boton_guardar.grid(row=0, column=1, padx=10)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
