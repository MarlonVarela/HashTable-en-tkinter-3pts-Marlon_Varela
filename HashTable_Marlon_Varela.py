import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    ciudad = entry_ciudad.get()
    if not nombre or not edad or not ciudad:
        messagebox.showerror("Error", "Ingrese todos los datos.")
        return
    HashTable[nombre] = {"edad": edad, "ciudad": ciudad}
    messagebox.showinfo(" ", "Datos guardados con éxito.")
    
def mostrar_datos():
    nombre = entry_nombre.get()
    if nombre in HashTable:
        edad = HashTable[nombre]["edad"]
        ciudad = HashTable[nombre]["ciudad"]
        messagebox.showinfo("Datos", f"Nombre: {nombre}\nEdad: {edad}\nCiudad: {ciudad}")
    else:
        messagebox.showerror("Error", "No se encontraron datos para el nombre ingresado.")

root = tk.Tk()
root.title("HashTable en Tkinter")
root.geometry("280x260")
HashTable = {}

label1 = tk.Label(root, text="Ingrese los datos que se le piden")
label1.pack()

labelinv = tk.Label(root, text=" ")
labelinv.pack()

label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()

label_edad = tk.Label(root, text="Edad:")
label_edad.pack()

label_ciudad = tk.Label(root, text="Ciudad:")
label_ciudad.pack()

entry_nombre = tk.Entry(root)
entry_nombre.pack()

entry_edad = tk.Entry(root)
entry_edad.pack()

entry_ciudad = tk.Entry(root)
entry_ciudad.pack()

labelinv = tk.Label(root, text=" ")
labelinv.pack()

btn_guardar = tk.Button(root, text="Guardar", command = guardar_datos)
btn_guardar.pack()

btn_mostrar = tk.Button(root, text="Mostrar", command = mostrar_datos)
btn_mostrar.pack()

root.mainloop()
