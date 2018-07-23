# Script para actualización BBDD
Este script escrito en python 3 nos permite actualizar la base de datos cada curso académico, a partir del listado Excel/csv proporcionado por la administración.

## Preparación de los datos
Los datos deben ser pasados a CSV con el siguiente formato para los delegados y subdelegados de grado:
```
"NOMBRE","APELLIDO1","APELLIDO2","NIA","CARGO","CENTRO","TITULACION","CURSO"
"PÉREZ","GARCÍA","FULANITO","100123456","Delegada/o","EPS","Grado en Ingeniería Informática","3"
...
```
Y con el siguiente formato en caso de postgrado:
```
"NOMBRE","APELLIDO1","APELLIDO2","NIA","CARGO","CENTRO","TITULACION","AREA"
"GARCÍA","PÉREZ","MENGANO","100987654","Delegada/o","POST","Máster Cifuentes","Área de la CAM"
...
```
**IMPORTANTE:** Hay que diferenciar manualmente en los datos los estudios de Colmenarejo asociados a la EPS de los asociados a la FCCSSJJ. En dichos casos, será necesario modificar el centro de `"COLME"` a `"COLMEL"`. Lo mismo ocurre en los estudios de Postgrado, dónde hay que diferenciar los estudios asociados a la EPS (`"POSTL"`) de los asociados a otros centros (`"POST"`).

# Ejecución
En cada curso académico, se copia la base de datos en producción (`delegates`) a una nueva base de datos `delegates_<curso_academico>` como backup. Entonces, se borra el contenido de las tablas `person` y `delegate` y se inserta el nuevo contenido mediante este script.

La ejecución del script se realiza de la forma:
```
python3 update_db.py fichero.csv
```

**IMPORTANTE:** Comprobar que el botón de *contacta con tu delegado* de Aula Global sigue funcionando tras la actualización de la base de datos.