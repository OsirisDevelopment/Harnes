#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import os
import time
import serial
import datetime
from zeus import client
import json

archivo=open("metricas.txt","w")
#for linea in archivo:
#    continue
#prueba=open("probando.txt","w")

#conexion
#conexion = client.ZeusClient('7caecc05', 'api.ciscozeus.io')

#Para uso interno de while
flag=True

# Iniciando conexion serial
arduinoPort = serial.Serial('COM8', 9600, timeout=1)
flagCharacter = 'k'



# Retardo para establecer la conexion serial
time.sleep(1.8)
arduinoPort.write(flagCharacter)

#archivo.write('timestamp ; id ; enganche : gas : ruido : presion : temperatura : altura : oxigenacion\n')

while flag:
    archivo=open("metricas.txt","r+")
    for linea in archivo:
        continue

    metrica = '[{"timestamp": %d,"point":{"id":%d,"seguro": %d ,"colgado":%d ,"gas": %d ,"ruido": %d ,"presion":%d,"temperatura":%d,"altura":%d,"oxigenacion":%d}}]'

    #timestamp de la hora del sistema
    timestamp= time.time()

    getSerialValue = arduinoPort.readline()

    listaSenales=getSerialValue.strip().split("*")
    # ["id","E1 (seguro)","E2 (Colgado o no)","Gas","Ruido","Presion","Temperatura","Altura","Oxigenacion"]


    identificador=int(listaSenales[0])
    seguro=int(listaSenales[1])
    colgado=int(listaSenales[2])
    gas=int(listaSenales[3])
    ruido=int(listaSenales[4])
    presion=int(listaSenales[5])
    temperatura=float(listaSenales[6])
    altimetro=float(listaSenales[7])
    oxigenacion=float(listaSenales[8])


    metrica=metrica % (timestamp ,identificador ,seguro ,colgado , gas , ruido , presion , temperatura , altimetro ,oxigenacion )
    #data_string= json.dumps(eval(metrica))
    #metrica2=eval(metrica)
    cadena=str(int(timestamp))+';'+str(identificador)+';'+str(seguro)+';'+str(colgado)+';'+str(gas)+';'+str(ruido)+';'+str(presion)+';'+str(temperatura)+';'+str(altimetro)+';'+str(oxigenacion)+'\n'
    #print type(str(eval(metrica)))
    #prueba.write(str(eval(metrica)))
    archivo.write(cadena)
    archivo.close()


    #conexion.sendMetric("Device",eval(metrica))
    #print conexion.getMetricNames(metric_name="Device", limit=10)
    print (metrica)

    





    time.sleep(1)



# Cerrando puerto serial
arduinoPort.close()