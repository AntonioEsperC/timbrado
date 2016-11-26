import requests
import random
import string
import xml.etree.ElementTree as ET
from collections import defaultdict
from flask import Flask, request
app = Flask(__name__)

@app.route('/guardarCFDI', methods=['GET', 'POST'] )
def guardarCFDI():
	#guardar factura carpeta
	factura = request.form['factura']
	root = ET.fromstring(factura)
	factura = ET.tostring(root)

	rnd = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(4))

	text_file = open('./facturasSAT/factura_'+rnd+'.xml', 'w')
	text_file.write(factura)
	text_file.close()

	print "Factura Guardada Exitosamente"
	return ""

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002, debug=True, threaded=True)