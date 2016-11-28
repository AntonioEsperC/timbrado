# timbrado
Simulación de Proceso de Timbrado del PAC

Para probar el código es necesario seguir los siguientes pasos:

1.- Ejecutar cada una de las entidades del proceso  (PAC, SAT, HSM) con los siguientes procesos (Cada uno en una terminal diferente)
	
python pac.py
python hsm.py
python main.py

2.- Correr el cliente para que inicie el proceso de timbrado:

	a) python cliente.py 
	Este comando ejecuta el proceso con un sello digital válido.

	b) python cliente_falso.py
	Este comando ejecuta el proceso con un sello digital inválido.

*En caso de que se quieran hacer pruebas con diferentes archivos para validar el formato del XML, se deberá cambiar el nombre del archivo con el que se prueba en el archivo "cliente.py" en la línea 17.
	factura_correcta.xml -> Factura con formato correcto
	factura_fecha.xml    ->	Factura con fecha incorrecta
	factura_moneda.xml   ->	Factura con moneda incorrecta
	factura_pago.xml     -> Factura con metodo de pago incorrecto