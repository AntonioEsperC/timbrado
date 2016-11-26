pyOpenSSL - Flask - hashlib - pyCrypto - base64
openssl rsa -in some.key -pubout -out pubkey.key

ATACANTE
1.- Me quiero hacer pasar por alguien más.
(Verificar con la llave privada) -> CFDI
	
2.- Se hace de manera consciente
	El sistema se base en la llave privada.
	(El contador hace algun trámite falso, el responsable es la empresa) -> Seguridad Física

3.- Alguien lo utiliza en un lugar público a falta de recursos o ingenio, y alguien se aprovecha

GENERAR XML'S PROBANDO VERIFICACION 
	1- De contenido
	2- De llave

PRESENTACION
Que problema
Porqué (MOTIVACIÓN ES MUY IMPORTANTE)
Esto es el SAT
PROCESO
Esto son los PAC
PROCESO
Que hice
CORRER TESTS (1,2 Max)
Que solución propongo
Preguntas

PENDIENTES
1- Insertar en XML el sello del cliente (Y fecha) 
2- Mandar XML
3- Extraer sello de XML 
4- Verificar XML 
5- Verificar sello 
6- Enviar XML al HSM
7- Sellar XML (PAC) 
8- Enviar XML sellado a PAC 
9- Enviar XML FINAL a SAT (Guardar en Carpeta) - Enviar al Cliente (Guardar en Carpeta)


PRUEBAS
1-
	Crear llaves/certificado falsos
	Insertar sello en XML
	Enviar al SAT
	Ver resultado

2- 
	 	Desde computadora externa generar XML con llave y certificado real
	2.1 
		El contador es confiable y hace su trabajo bien (No genera facturas falsas)
	2.2 
		El contador decide crear 100 facturas falsas y son aceptadas por el PAC

3- 
	Plantear casos de robo de llave privada y justificar daño con 
	3.1 
		Phishing
	3.2 
		Chrome


CONCLUSIONES
Un sistema de llave privada nunca debe de transmitir sus llaves.

PROPUESTA
1- No enviarla
2- Cifrar la llave de manera local
	Cuando se ocupa se pone un password
VER PAPER*
CIFRAR ALGUNOS ARCHIVOS EN EL TRANSCURSO (El SAT no cifra nada)
RFC Privado? O utilizar otro parámetro para login
Factura cifrada entre entidades - (Privacidad, evitar ataques man in the middle)
Cultura - 

ES 100% FUNCIONAL PERO LA SEGURIDAD NO SE CONTEMPLÓ EN EL DISEÑO

