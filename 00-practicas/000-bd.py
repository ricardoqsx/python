# instrucciones para lograr una conexion 
# desde python a una base de datos oracle
# esto en linux, caso concreto Bookworm

# descargar el paquete instant client para tu sistema

# en el caso de linux, lo logre descargando el paquete
# basico, creando un directorio en /opt/oracle, 
# moviendo el .zip a esta ubicacion y descomprimiendo

# luego instalar el paquete libaio1
# Si no hay ningún otro software de Oracle en la máquina que se verá afectado, 
# agregue permanentemente Instant Client a la ruta del enlace de tiempo de ejecución. 
# Por ejemplo, con sudo o como usuario root:

# sudo sh -c "echo /opt/oracle/instantclient_21_1 > /etc/ld.so.conf.d/oracle-instantclient.conf"
# sudo ldconfig

# Alternativamente, configure la variable de entorno LD_LIBRARY_PATH
# en el directorio apropiado para la versión de Instant Client. Por ejemplo:

# export LD_LIBRARY_PATH=/opt/oracle/la_carpeta_descomprimida:$LD_LIBRARY_PATH

# por si acaso agregar una variable de entorno para oracle home y agregarlo al PATH

# export ORACLE_HOME=/opt/oracle/instantclient_19_3
# export PATH=$PATH:$ORACLE_HOME 

import cx_Oracle

conn = cx_Oracle.connect(user="hr", password="hr", dsn="localhost/XE")
cur=conn.cursor()

for row in cur.execute("select * from employees"):
    print(row)

cur.close()
conn.close()