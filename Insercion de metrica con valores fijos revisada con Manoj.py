from zeus import client
import time

#conexion
conexion = client.ZeusClient('7caecc05', 'api.ciscozeus.io')

#metrica = '[{"timestamp": %d,"point":{"id":%d,"enganche": %d ,"gas": %d ,"ruido": %d ,"presion":%d,"temperatura":%d,"altura":%d,"oxigenacion":%d}}]'

# API expects the metric to be a list
metric_list =[]

timestamp=time.time()

identificador=00001

enganche=0

gas=30

ruido=48

presion=550

temperatura=41

altimetro=600

oxigenacion=15

data = {"timestamp": time.time(),"id": identificador, "enganche": enganche, "gas": gas, "ruido": ruido, "presion": presion, "temperatura": temperatura, "altura": altimetro, "oxigenacion": oxigenacion}
metric1 = { "point": data}

#metrica=metrica % (timestamp ,identificador , enganche , gas , ruido , presion , temperatura , altimetro ,oxigenacion )
metric_list.append(metric1)

# This works and the data can be retrieved as well. However, the problem with sending multiple columns of data is that 
# our current Zeus visualization cannot display it. It expects each metric (such as Insertvar) to have a single associated
# value.
print conexion.sendMetric("Insertar", metric_list)

#print eval(metrica)

print metric_list

raw_input()