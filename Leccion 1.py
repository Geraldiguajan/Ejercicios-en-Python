import tkinter as tk
from tkinter import messagebox
class Alumno:
    def __init__(self, dni, apellidos, nombre, nota):
        self.dni = dni
        self.apellidos = apellidos
        self.nombre = nombre
        self.nota = nota
        self.calificacion = self.calcular_calificacion()

    def calcular_calificacion(self):
        """Calcula la calificación a partir de la nota"""
        if self.nota < 5:
            return "SS"
        elif 5 <= self.nota < 7:
            return "AP"
        elif 7 <= self.nota < 9:
            return "NT"
        elif self.nota >= 9:
            return "SB"
    
    def __str__(self):
        return f"{self.dni} {self.apellidos}, {self.nombre} {self.nota} {self.calificacion}"

class GestionCalificaciones:
    def __init__(self):
        self.alumnos = {}

    def agregar_alumno(self, dni, apellidos, nombre, nota):
        if dni in self.alumnos:
            return "Alumno con ese DNI ya existe."
        self.alumnos[dni] = Alumno(dni, apellidos, nombre, nota)
        return "Alumno agregado correctamente."
    
    def eliminar_alumno(self, dni):
        if dni not in self.alumnos:
            return "Alumno no encontrado."
        del self.alumnos[dni]
        return "Alumno eliminado correctamente."

    def consultar_alumno(self, dni):
        if dni not in self.alumnos:
            return "Alumno no encontrado."
        alumno = self.alumnos[dni]
        return f"{alumno.dni} {alumno.apellidos}, {alumno.nombre} {alumno.nota} {alumno.calificacion}"

    def modificar_nota(self, dni, nueva_nota):
        if dni not in self.alumnos:
            return "Alumno no encontrado."
        self.alumnos[dni].nota = nueva_nota
        self.alumnos[dni].calificacion = self.alumnos[dni].calcular_calificacion()
        return "Nota modificada correctamente."

    def mostrar_alumnos(self):
        if not self.alumnos:
            return "No hay alumnos registrados."
        return "\n".join(str(alumno) for alumno in self.alumnos.values())

    def mostrar_alumnos_suspensos(self):
        suspensos = [str(alumno) for alumno in self.alumnos.values() if alumno.calificacion == "SS"]
        if not suspensos:
            return "No hay alumnos suspensos."
        return "\n".join(suspensos)

    def mostrar_alumnos_aprobados(self):
        aprobados = [str(alumno) for alumno in self.alumnos.values() if alumno.calificacion in ["AP", "NT", "SB"]]
        if not aprobados:
            return "No hay alumnos aprobados."
        return "\n".join(aprobados)

    def mostrar_candidatos_MH(self):
        candidatos = [str(alumno) for alumno in self.alumnos.values() if alumno.nota == 10]
        if not candidatos:
            return "No hay candidatos a MH."
        return "\n".join(candidatos)


def actualizar_interfaz():
    texto = gestion.mostrar_alumnos()
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, texto)

def agregar_alumno():
    dni = entry_dni.get()
    apellidos = entry_apellidos.get()
    nombre = entry_nombre.get()
    try:
        nota = float(entry_nota.get())
        resultado = gestion.agregar_alumno(dni, apellidos, nombre, nota)
        messagebox.showinfo("Resultado", resultado)
        actualizar_interfaz()
    except ValueError:
        messagebox.showerror("Error", "La nota debe ser un número válido.")

def eliminar_alumno():
    dni = entry_dni.get()
    resultado = gestion.eliminar_alumno(dni)
    messagebox.showinfo("Resultado", resultado)
    actualizar_interfaz()

def consultar_alumno():
    dni = entry_dni.get()
    resultado = gestion.consultar_alumno(dni)
    messagebox.showinfo("Resultado", resultado)

def modificar_nota():
    dni = entry_dni.get()
    try:
        nueva_nota = float(entry_nota.get())
        resultado = gestion.modificar_nota(dni, nueva_nota)
        messagebox.showinfo("Resultado", resultado)
        actualizar_interfaz()
    except ValueError:
        messagebox.showerror("Error", "La nota debe ser un número válido.")

def mostrar_suspensos():
    texto = gestion.mostrar_alumnos_suspensos()
    messagebox.showinfo("Alumnos Suspensos", texto)

def mostrar_aprobados():
    texto = gestion.mostrar_alumnos_aprobados()
    messagebox.showinfo("Alumnos Aprobados", texto)

def mostrar_candidatos_MH():
    texto = gestion.mostrar_candidatos_MH()
    messagebox.showinfo("Candidatos a MH", texto)


ventana = tk.Tk()
ventana.title("Gestión de Calificaciones de Alumnos")
gestion = GestionCalificaciones()

label_dni = tk.Label(ventana, text="DNI:")
label_dni.grid(row=0, column=0)
entry_dni = tk.Entry(ventana)
entry_dni.grid(row=0, column=1)

label_apellidos = tk.Label(ventana, text="Apellidos:")
label_apellidos.grid(row=1, column=0)
entry_apellidos = tk.Entry(ventana)
entry_apellidos.grid(row=1, column=1)

label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=2, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=2, column=1)

label_nota = tk.Label(ventana, text="Nota:")
label_nota.grid(row=3, column=0)
entry_nota = tk.Entry(ventana)
entry_nota.grid(row=3, column=1)


btn_agregar = tk.Button(ventana, text="Agregar Alumno", command=agregar_alumno)
btn_agregar.grid(row=4, column=0)

btn_eliminar = tk.Button(ventana, text="Eliminar Alumno", command=eliminar_alumno)
btn_eliminar.grid(row=4, column=1)

btn_consultar = tk.Button(ventana, text="Consultar Alumno", command=consultar_alumno)
btn_consultar.grid(row=6, column=0)

btn_modificar = tk.Button(ventana, text="Modificar Nota", command=modificar_nota)
btn_modificar.grid(row=6, column=1)

btn_suspensos = tk.Button(ventana, text="Mostrar Suspensos", command=mostrar_suspensos)
btn_suspensos.grid(row=8, column=0)

btn_aprobados = tk.Button(ventana, text="Mostrar Aprobados", command=mostrar_aprobados)
btn_aprobados.grid(row=8, column=1)

btn_candidatos_MH = tk.Button(ventana, text="Mostrar Candidatos MH", command=mostrar_candidatos_MH)
btn_candidatos_MH.grid(row=9, column=0, columnspan=2)


text_output = tk.Text(ventana, height=10, width=50)
text_output.grid(row=10, column=0, columnspan=2)


ventana.mainloop()
