import os
import pandas as pd
from ftplib import FTP
from ftplib import all_errors
from subprocess import call
from time import time
from datetime import datetime
import socket
import json



xen = "192.168.196.105"
xen_user = "archivo"
xen_pass = "archivo01"

stratus = "192.168.196.139"
stratus_user = "movie"
stratus_pass = ""



json_data=open("conf.json").read()

data = json.loads(json_data)
print(data['user'])


stratus_coprobation = "V:\\media\\RECUP DATA\\"
is_v_maped = False
if(not os.path.exists(stratus_coprobation)):
	print("No está mapeado el desino")
	print("Mapeando unidad")
	return_code = call(["net","use","V:","\\\\192.168.196.139\\v","/user:GVAdmin","adminGV!"], shell=True)  
	#print(return_code)
	if(return_code == 0):
		print("La unidad de Stratus fue mapeada correctamente!! :)")
		

# archivo_down = input("¿Cuál es el nombre del material?: ")
# carpeta = input("¿Cuál es la carpeta?: ")

archivo_down = "CADENA PERPETUA MOCHOMO_DF004ENF.gxf"
carpeta = "Noticias"

tmp_path = "tmp"
os.chdir(tmp_path)

# archivo_down = "AMLO SOBRE ALIANZAS-BIT_DF003S2K.gxf"
# carpeta = "Noticias"


destino = "RECUP DATA"

download_success = False

if(os.path.exists(archivo_down)):
	print("El archivo: "+ archivo_down+" ya fue descargado, comprobando existencia remota.")
	if os.path.exists(stratus_coprobation+archivo_down.replace(".gxf",".cmf")):
		print("Ya existe el archivo en Stratus")
else:
	print("Descargando.")
	tiempo_inicial = time() 
	# ftp = FTP(xen)
	# print(ftp.login(xen_user,xen_pass))
	# ftp.cwd(carpeta)
	# # ftp.retrlines('LIST')
	# print("Descargando: "+archivo_down)
	

	# # filelist = []
	# # ftp.retrlines('LIST',filelist.append)
	# # print(filelist)
	# # for item in filelist:
	# # 	if(archivo_down in item):
	# # 		print("El archivo existe")
	# # 		break
	# # 	else:
	# # 		print("El archivo ",archivo_down," no existe en el origen.")
	# try:
	# 	# print('RETR \''+archivo_down+'\'')
	# 	ftp.retrbinary('RETR '+archivo_down, open(archivo_down, 'wb').write)
	# 	download_success = True
	# except all_errors as e:
	# 	print(e)
	
	# ftp.quit()
	# print( archivo_down + " listo para ingestar.")

	# if(download_success):
	# 	print("Ingestar")
	# 	ftp = FTP(stratus)
	# 	print(ftp.login(stratus_user,stratus_pass))
	# 	ftp.cwd(destino)
		
	# 	print("Ingestando: "+archivo_down)
	# 	ftp.storbinary('STOR '+archivo_down, open(archivo_down, 'rb'))
	# 	ftp.quit()
	# 	print( archivo_down + " listo.")
	# 	os.remove(archivo_down)
	# else:
	# 	print("No Ingestar")

	

	tiempo_final = time()
	tiempo_ejecucion = tiempo_final - tiempo_inicial


	# print("Tardó: " , tiempo_ejecucion,"s")
	m, s = divmod(tiempo_ejecucion, 60)
	h, m = divmod(m, 60)
	restore_time = "%02d:%02d:%02d" % (h, m, s)
	print ("Tardó:",restore_time)

	origin = xen+"\\"+carpeta+"\\"+archivo_down
	destination = stratus + "\\"+ destino +"\\"+archivo_down.split(".")[0]
	ip = socket.gethostbyname(socket.gethostname())
	date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
	print(date)
	data = [origin,destination,ip,data['user'],restore_time,date]
	print(data)


	


	# #Append
	# last_row = len(df)

	# df.loc[last_row] = data
	# print(df)

	# df.to_csv('restore_datax.csv',sep=',')

	key = input("Presiona cualquier tecla para salir.")

