from Tkinter import *
import time
import datetime


def invertirarchivo(nombrearchivo):
	archivo=open(nombrearchivo,"r")
	nuevo=open("archivoinvertido.txt","w")
	lista=list()
	for linea in archivo:
		lista.append(linea)
	lista.reverse()
	for elemento in lista:
		nuevo.write(elemento)

	archivo.close()
	nuevo.close()


def leerarchivo(nombrearchivo):
	lista.delete(0,END)
	archivo=open(nombrearchivo,"r")
	for linea in archivo:
		listaSenales=linea.strip().split(";")
		fecha=datetime.datetime.fromtimestamp(int(listaSenales[0])).strftime('%Y-%m-%d %H:%M:%S')
		#print fecha

		listaauxiliar=listaSenales[1::]
		cadena= str(fecha)
		auxiliar=""
		for elemento in listaauxiliar:
			if len(elemento)==1:
				auxiliar += (" | "+ elemento.center(12))
			elif len(elemento)==2:
				auxiliar += (" | "+ elemento.center(11))
			elif len(elemento)==3:
				auxiliar += (" | "+ elemento.center(10))
			elif len(elemento)%2==0:
				auxiliar += (" | "+ elemento.center(10))
			else:
				auxiliar += (" | "+ elemento.center(9))

		final=cadena+auxiliar
		print final


		lista.insert(END,final)




#root=Tk()
flag=True
c=0
f=Frame(height=95, width=95,cursor="target")
f.pack(padx=0,pady=0)

#Creacion del titulo
titulo= Label(f,text = "Realtime Monitoring", font=("Arial",15))
titulo.pack(padx=0, pady=0)

#Creacion del logo
logoimg= PhotoImage(file="logohiway.gif")
etiquetalogo=Label(f,image =logoimg)
etiquetalogo.pack(padx=50, pady=10)

titulo= Label(f,text = "         FECHA              |       ID       |   LOCK   | ENGAGE |   GAS   |   RUIDO   | PRESION |   TEMP   | ALTURA |   OXIGENO   | ", font=("Arial",8))
titulo.pack(padx=0, pady=0)




lista=Listbox(f,height=50,width=95)
lista.pack(side=BOTTOM, fill=BOTH, expand=1)
#lista.insert(END,"fecha")

while flag:
	#lista.delete(0,END)
	#print "bien"
	#lista.insert(END,"fecha")

	#for i in range(1):
	#		lista.insert(END,"")

	invertirarchivo("metricas.txt")
	leerarchivo("archivoinvertido.txt")
	#lista.delete(0,END)

	#b = Button(f, text="Delete",
    #       command=lambda lista=lista: lista.delete(ANCHOR))

	time.sleep(5)
	#flag=int(raw_input("Ingrese Opcion: "))

	#lista.delete(0,END)

	
	
	a=raw_input('presione una tecla')