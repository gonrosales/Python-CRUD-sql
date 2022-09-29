from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import re

conexion = sqlite3.connect("dbgp.db")

tabla=conexion.cursor()
tabla.execute (""" CREATE TABLE IF NOT EXISTS pacientes (id INTEGER PRIMARY KEY AUTOINCREMENT, 
          'Nombre y apellido'TEXT NOT NULL,
            edad INTEGER,dni INTEGER,observaciones TEXT NOT NULL) """)
conexion.commit() #guardar los cambios
tabla.close()


ventana = Tk()
ventana.title("Proyecto Final")
ventana.config(bg="bisque2")
ventana.geometry("1100x700")


# TITULO

titulo = Label(ventana, text="Registro de pacientes",
               bg="bisque2", fg="#112731", font=("calibri", 40))
titulo.place(x=80, y=17)

# CONTENEDOR 1

contenedor1 = Frame(ventana)
contenedor1.config(width=250, height=550, bg="linen")
contenedor1.place(x=50, y=100)


# CONTENEDOR 2

contenedor2 = Frame(ventana)
contenedor2.config(width=700, height=550, bg="peachpuff2")
contenedor2.place(x=350, y=100)


registro = Label(contenedor2, text="Registro",
                 bg="peachpuff2", font=("calibri", 20))
registro.place(x=250, y=10)

id = Label(contenedor2, text="ID",
               bg="peachpuff2", font=("calibri", 18))
id.place(x=30, y=60)

eid = Entry(contenedor2, width=31, font=("calibri", 18))
eid.place(x=300, y=60)

nombre = Label(contenedor2, text="Nombre y apellido",
               bg="peachpuff2", font=("calibri", 18))
nombre.place(x=30, y=120)

enombre = Entry(contenedor2, width=31, font=("calibri", 18))
enombre.place(x=300, y=120)

edad = Label(contenedor2, text="Edad", bg="peachpuff2", font=("calibri", 18))
edad.place(x=30, y=170)

eedad = Entry(contenedor2, width=31, font=("calibri", 18))
eedad.place(x=300, y=170)

dni = Label(contenedor2, text="DNI", bg="peachpuff2", font=("calibri", 18))
dni.place(x=30, y=220)

edni = Entry(contenedor2, width=31, font=("calibri", 18))
edni.place(x=300, y=220)

observaciones = Label(contenedor2, text="Observaciones:",
                      bg="peachpuff2", font=("calibri", 18))
observaciones.place(x=30, y=260)

eobservaciones = Entry(contenedor2, width=50,font=("calibri", 18))
eobservaciones.place(x=30, y=310)


def guardar():
        print("guardado exitoso")
        datos = (enombre.get(), eedad.get(), edni.get(), eobservaciones.get())
        tabla = conexion.cursor()
        tabla.execute("INSERT INTO pacientes('Nombre y apellido', edad, dni, observaciones) VALUES(?,?,?,?)", datos)
        conexion.commit() #para que se quede guardado
        tabla.close()
        messagebox.showinfo("Registro de pacientes",
                                "Paciente guardado exitosamente.")

def eliminar(): 
    #if (eid.get()==" "):        # si en el entry de id no hay nada , entonces tira un error.
     #   messagebox.showinfo("mensaje","para eliminar,primero debe buscar un paciente")
    #else:
        eliminarId=eid.get()
        tabla= conexion.cursor()
        tabla.execute("DELETE FROM pacientes WHERE id=?",eliminarId)
        conexion.commit() #para que se quede guardado
        tabla.close
        messagebox.showinfo("Registro de pacientes","Eliminacion exitosa")


def modificar():
    datos=(enombre.get(),eedad.get(),edni.get(),eobservaciones.get(),eid.get())
    tabla= conexion.cursor()
    tabla.execute("UPDATE pacientes SET 'Nombre y Apellido' =?,edad=?,dni=?,observaciones=? WHERE id = ?",datos)
    conexion.commit()
    tabla.close
    messagebox.showinfo("Registro de pacientes","Modificacion exitosa")


def buscar():
    buscarId = eid.get()
    tabla = conexion.cursor()
    tabla.execute("SELECT * FROM pacientes WHERE id= ?", buscarId)
    conexion.commit()
    datos = tabla.fetchall()
    tabla.close
    for dato in datos :
        eid.delete(0,END)
        eid.insert(END,dato[0])
        enombre.delete(0,END)
        enombre.insert(END,dato[1])
        eedad.delete(0,END)
        eedad.insert(END,dato[2])
        edni.delete(0,END)
        edni.insert(END,dato[3])
        eobservaciones.delete(0,END)
        eobservaciones.insert(END,dato[4])




# CONTENEDOR 3

contenedor3=Frame(ventana)
contenedor3.config(width = 700, height = 500, bg = "rosybrown2")


contactanos=Label(contenedor3, text = "Contactanos",
                  font = ("calibri", 23), bg = "rosybrown2")
contactanos.place(x = 100, y = 50)

mail=Text(contenedor3, width = 45, height = 10, font = ("calibri", 18))
mail.place(x = 100, y = 100)

enviarmail=Button(contenedor3, text = "Enviar Mail", font = ("calibri", 18))
enviarmail.place(x = 520, y = 410)


# FUNCIONES

def fboton1():

    contenedor2.place(x = 350, y = 100)#darle posicion al contenedor 2 para que aparezca.(el q tiene el formulario)
    contenedor3.place_forget()         #olvidar la posicion del contenedor 3 por si estaba posicionado ahi.


def fboton2():
    contenedor3.place(x = 350, y = 100)
    contenedor2.place_forget()


# BOTONES

boton1=Button(contenedor1, text = "Registros", width = 10, height = 2,
              bg = "floral white", font = ("calibri", 20), command = fboton1)
boton1.place(x = 50, y = 50)

boton2=Button(contenedor1, text = "Contactanos", width = 10, height = 2,
              bg = "floral white", font = ("calibri", 20), command = fboton2)
boton2.place(x = 50, y = 350)

bGuardar=Button(contenedor2, text = "Guardar",
                font = ("calibri", 16), command = guardar)
bGuardar.place(x = 30, y = 490)

bBuscar = Button(contenedor2, text = "Buscar",font=("calibri",16),command=buscar)
bBuscar.place(x = 208, y =490)


bEliminar = Button(contenedor2, text="Eliminar",
                 font=("calibri", 16), command=eliminar)
bEliminar.place(x=565, y=490)

bModificar = Button(contenedor2, text="Modificar",
                 font=("calibri", 16), command=modificar)
bModificar.place(x=386, y=490)




ventana.mainloop()
