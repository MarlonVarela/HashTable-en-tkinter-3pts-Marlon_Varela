import tkinter as tk

def agregar_persona():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    ciudad = entry_ciudad.get()
    
    hashtable[nombre] = {
        "edad": edad,
        "ciudad": ciudad
    }
    
    # Actualizar la lista de personas
    actualizar_lista_personas()

    entry_nombre.delete(0,tk.END)
    entry_edad.delete(0,tk.END)
    entry_ciudad.delete(0,tk.END)

def actualizar_lista_personas():
    lista_personas.delete(0, tk.END)
    for nombre in hashtable:
        edad = hashtable[nombre]["edad"]
        ciudad = hashtable[nombre]["ciudad"]
        lista_personas.insert(tk.END, f"Nombre: {nombre} | Edad: {edad} años | Ciudad: {ciudad}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Hashtable en Tkinter")
#ventana.geometry("400x400")

# Crear el hashtable
hashtable = {}

# Widgets de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack()

entry_edad = tk.Entry(ventana)
entry_edad.pack()

label_ciudad = tk.Label(ventana, text="Ciudad:")
label_ciudad.pack()

entry_ciudad = tk.Entry(ventana)
entry_ciudad.pack()

# Botón para agregar persona
boton_agregar = tk.Button(ventana, text="Agregar Persona", command=agregar_persona)
boton_agregar.pack()

# Lista para mostrar las personas ingresadas
lista_personas = tk.Listbox(ventana, width=60, height=10)
lista_personas.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
