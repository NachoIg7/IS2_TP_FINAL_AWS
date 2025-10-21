# repositorio TP FINAL IS2

Este proyecto implementa clases para soportar servicios corporativos interactuando con DynamoDB para almacenar datos y logs.

## Estructura del proyecto

/src
  |--- corporate_data.py
  |--- corporate_log.py

corporate_data.py:
En este archivo se encuentra la clase CorporateData con los metodos getData , getCUIT , y getSeq. utiliza una conexion con la base de datos a DynamoDB

getData:
Este método recibirá como argumentos un identificador único de sesión
(uuid), un identificador único de CPU (uuidCPU) y id de sede (id).

Retornará una estructura JSON con:
o Id de sede
o Domicilio.
o Localidad.
o Código Postal (cp)
o Provincia.
O texto de error en caso de no encontrar el registro.

• getCUIT:
Similar al caso de getData pero el archivo JSON retornado contendrá el
CUIT.

• getSeqID:
Similar al caso de getData pero el archivo JSON retornado contendrá un
identificador único de secuencia (idSeq), luego de recuperar el mismo
desde el database deberá incrementarse en 1 el identificador.

• listCorporateData
Producirá un listado de todos los datos contenidos en la tabla
CorporateData para una clave (id) determinado.

• listCorporateLog
Producirá un listado de todas las entradas contenidas en la tabla
CorporateLog para una clave de CPU determinada.

corporate_log.py:
En este archivo se encuentra la clase CorporateLog creada con un patron
singleton, una vez que se inicializa la clase crea otra clase denominada log
que registrarán las acciones realizadas con propósito de auditoría ulterior.
La clase log tambien creada con un patron singleton, debe implemetar solo
dos metodos:

post
Este método recibirá como argumentos un identificador único de sesión
(uuid) y un string de caracteres con el nombre del método que lo invoca.
El método grabará un registro en la tabla Log donde agregará datos de la
CPU donde está corriendo y el timestamp de la operación.

list
Este método recibirá como argumento un indicador único de CPU y un
indicador único de sesión y listará todas las entradas que hubiera para el
mismo. Si el indicador de sesión es omitido listará todas las entradas para
la CPU.

/scripts
  |--- UADER_IS2_listCorporateData.py
  |--- UADER_IS2_listLog.py

UADER_IS2_listCorporateData.py:

Imprime los datos de la Tabla CorporateLog

UADER_IS2_listLog.py:

Retorna una estructura JSON con todas las filas de la tabla
CorporateLog donde la uuidCPU coincida con la CPU que utilice
para el desarrollo.

/test
  |--- test_corporate_data.py
  |--- test_corporate_log.py

archivo test_corporate_data.py:

En este archivo se realizan pruebas de test, verificando camino feliz y caminos con errores.

# Realizamos una funcion de Prueba para obtener datos con un ID válido

# Prueba para obtener datos con un ID inválido

# Prueba para obtener datos con un ID vacío

# Prueba para ID válido pero campo vacío

# Prueba para verificar el patrón Singleton

archivo test_corporate_log.py:

# Probar el registro de un evento exitoso

# Probar la lista de logs cuando se proporciona un ID de CPU inválido

# Verificar que la clase CorporateLog siga el patrón Singleton
