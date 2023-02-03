# Desafio Cattler
A continuacion se indican los endpoints para probar los diferentes puntos de la aplicación (se incluye colección de Postman)

**Descripción de endpoints**
1. _GET y POST Animales_
    - /api/animals/get  Este endpoint permite obtener todos los animales registrados. Recibe de manera opcional el parametro 'troop_id':'int' para filtrar por numero de tropa en el cuerpo de la peticion en formato JSON
	- /api/animals/  Este endpoint permite registrar animales. Recibe 'caravan_number':'int', 'RFID_number':'int' y 'troop_id':'int' en el cuerpo de la peticion en formato JSON
	
2. _GET y POST Tropas_	
	- /api/troops/  Este endpoint permite registrar tropas. Recibe 'troop_number':'int', 'lot':'int' en el cuerpo de la peticion en formato JSON 
	- /api/troops/get  Este endpoint permite obtener todos las tropas registrados. Recibe de manera opcional el parametro 'lot':'int' para filtrar por lote en el cuerpo de la peticion en formato JSON

3. _GET y POST Corrales_	
	- /api/corrals/ Este endopoint con el metodo POST, crea un corral automaticamente. Recibe 'troop_id':'int', si se desea asignar una tropa al corral en el cuerpo de la peticion en formato JSON
	- /api/corrals/ Este endopoint con el metodo GET, obtiene todos los corrales registrados
	
4. _GET y POST Lotes_
	- /api/lots/ Este endopoint con el metodo POST, crea un lote. Recibe 'lot_number':'int', para indicar el numero de lote, todo esto en el cuerpo de la peticion en formato JSON
	- /api/lots/ Este endopoint con el metodo GET, obtiene todos los lotes registrados
	
5. _POST Ingreso de animales_
	- /animals/income/ Este endpoint recibe en el cuerpo de la peticion un JSON como el indicado en el documento del challenge y registra el ingreso de animales
	
****
**Adicionales**
Se incluye test unitario y transaccion unitaria para el servicio de ingreso




_Realizado por: Facundo Zallocco_
