from zeus import client
import time

#conexion
conexion = client.ZeusClient('7caecc05', 'api.ciscozeus.io')

#metrica = '[{"timestamp": %d,"point":{"id":%d,"enganche": %d ,"gas": %d ,"ruido": %d ,"presion":%d,"temperatura":%d,"altura":%d,"oxigenacion":%d}}]'

timestamp=time.time()

for i in range(1000):

	identificador=00001

	metid= [{ "point": {"timestamp":timestamp, "value": identificador}}]

	enganche=i
	metenganche= [{"point": {"timestamp":timestamp ,"value": enganche}}]

	gas=i*10
	metgas= [ {"point": {"timestamp":timestamp, "value": gas}}]

	ruido=i*5
	metruido= [{ "point": {"timestamp":timestamp,"value": ruido}}]

	presion=i*2
	metpresion= [ {"point": {"timestamp":timestamp, "value": presion}}]

	temperatura=i*3
	mettemperatura= [{"point": {"timestamp":timestamp, "value": temperatura}}]

	altimetro=i*7
	metaltimetro= [ {"point": {"timestamp":timestamp, "value": altimetro}}]

	oxigenacion=i*8
	metoxigenacion= [{ "point": {"timestamp":timestamp, "value": oxigenacion}}]


#metrica=metrica % (timestamp ,identificador , enganche , gas , ruido , presion , temperatura , altimetro ,oxigenacion )

# Keeping one value per metric allows Zeus visualization to graph the data. Also, another quirk is that the column name
# must be "value" for visualizatin to work.
	print conexion.sendMetric("Insertar.identificador", metid)
	conexion.sendMetric("Insertar.enganche", metenganche)
	conexion.sendMetric("Insertar.gas", metgas)
	conexion.sendMetric("Insertar.ruido", metruido)
	conexion.sendMetric("Insertar.presion", metpresion)
	conexion.sendMetric("Insertar.temperatura", mettemperatura)
	conexion.sendMetric("Insertar.altimetro", metaltimetro)
	conexion.sendMetric("Insertar.oxigenacion", metoxigenacion)

#print eval(metrica)
#raw_input()
