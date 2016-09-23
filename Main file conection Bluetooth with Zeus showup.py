#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import os
import time
import serial
import datetime
from zeus import client
import json

#archivo=open("metricas.txt","w")
#for linea in archivo:
#    continue
#prueba=open("probando.txt","w")

#conexion
conexion = client.ZeusClient('7caecc05', 'api.ciscozeus.io')

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
    #archivo=open("metricas.txt","r+")
    #for linea in archivo:
    #    continue

    #metrica = '[{"point":{"timestamp": %d,"id":%d,"seguro": %d ,"colgado":%d ,"gas": %d ,"ruido": %d ,"presion":%d,"temperatura":%d,"altura":%d,"oxigenacion":%d}}]'

    #timestamp de la hora del sistema
    timestamp= time.time()

    getSerialValue = arduinoPort.readline()

    listaSenales=getSerialValue.strip().split("*")

    #id*e1*E2*UV(entero)*R(ruido)*PAS(presion)*TEMP(temperatura)*ALT(altura)
    # ["id","E1 (seguro)","E2 (Colgado o no)","Gas","Ruido","Presion","Temperatura","Altura","Oxigenacion"]

    identificador=int(listaSenales[0])
    metid= [{ "point": {"timestamp":timestamp, "value": identificador}}]
    
    seguro=int(listaSenales[1])
    metseguro= [{"point": {"timestamp":timestamp ,"value": seguro}}]

    colgado=int(listaSenales[2])
    metcolgado= [{"point": {"timestamp":timestamp ,"value": colgado}}]

    uv=int(listaSenales[3])
    metuv= [ {"point": {"timestamp":timestamp, "value": uv}}]

    ruido=int(listaSenales[4])
    metruido= [{ "point": {"timestamp":timestamp,"value": ruido}}]

    presion=int(listaSenales[5])
    metpresion= [ {"point": {"timestamp":timestamp, "value": presion}}]

    temperatura=float(listaSenales[6])
    mettemperatura= [{"point": {"timestamp":timestamp, "value": temperatura}}]

    altimetro=float(listaSenales[7])
    metaltimetro= [ {"point": {"timestamp":timestamp, "value": altimetro}}]

    #oxigenacion=float(listaSenales[8])
    #metoxigenacion= [{ "point": {"timestamp":timestamp, "value": oxigenacion}}]

    #metrica=metrica % (timestamp ,identificador ,seguro ,colgado , gas , ruido , presion , temperatura , altimetro ,oxigenacion )
    #data_string= json.dumps(eval(metrica))
    #metrica2=eval(metrica)
    #cadena=str(int(timestamp))+';'+str(identificador)+';'+str(seguro)+';'+str(colgado)+';'+str(gas)+';'+str(ruido)+';'+str(presion)+';'+str(temperatura)+';'+str(altimetro)+';'+str(oxigenacion)+'\n'
    #print type(str(eval(metrica)))
    #prueba.write(str(eval(metrica)))
    #archivo.write(cadena)
    #archivo.close()


    conexion.sendMetric("Harnes2.0.identificador", metid)
    conexion.sendMetric("Harnes2.0.seguro", metseguro)
    conexion.sendMetric("Harnes2.0.colgado", metcolgado)
    conexion.sendMetric("Harnes2.0.gas", metuv)
    conexion.sendMetric("Harnes2.0.ruido", metruido)
    conexion.sendMetric("Harnes2.0.presion", metpresion)
    conexion.sendMetric("Harnes2.0.temperatura", mettemperatura)
    conexion.sendMetric("Harnes2.0.altimetro", metaltimetro)
    #conexion.sendMetric("Harnes2.0.oxigenacion", metoxigenacion)

    print listaSenales
    #print "-------------------------------------------------------------------------------"



    #print conexion.getMetricNames(metric_name="Device", limit=10)
    #print (metrica)





    time.sleep(1)



# Cerrando puerto serial
arduinoPort.close()