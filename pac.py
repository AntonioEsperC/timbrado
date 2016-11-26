import requests
import hashlib
import base64
import xml.etree.ElementTree as ET
from collections import defaultdict
from Crypto.PublicKey import RSA
from datetime import datetime
from flask import Flask, request
app = Flask(__name__)

def unpack_bigint(b):
    b = bytearray(b) # in case yo're passing in a bytes/str
    return sum((1 << (bi*8)) * bb for (bi, bb) in enumerate(b))

@app.route('/timbradoFactura', methods=['GET', 'POST'])
def timbradoFactura():
	factura = request.form['factura']
	root = ET.fromstring(factura)

	sello = root.attrib['sello']
	root.attrib['sello'] = ""

	#verify XML
	fecha = root.attrib['fecha']
	try:
		valid_fecha = datetime.strptime(fecha, '%Y-%m-%dT%H:%M:%S')
	except:
		print 'Fecha invalida'
		return 'error'
	
	metodoDePago = root.attrib['metodoDePago']
	if(metodoDePago.lower() not in ['efectivo', 'cheque', 'tdc', 'tdd']):
		print 'Metodo de Pago invalido'
		return 'error'
	
	tipoDeComprobante = root.attrib['tipoDeComprobante']
	if(tipoDeComprobante.lower() not in ['ingreso', 'egreso']):
		print 'Tipo de Comprobante invalido'
		return 'error'
	
	moneda = root.attrib['moneda']
	if(moneda.upper() not in ['AUD', 'GBP', 'EUR', 'JPY', 'CHF', 'USD', 'AFN', 'ALL', 'DZD', 'AOA', 'ARS', 'AMD', 'AWG', 'AUD', 'AZN', 'BSD', 'BHD', 'BDT', 'BBD', 'BYR', 'BZD', 'BMD', 'BTN', 'BOB', 'BAM', 'BWP', 'BRL', 'GBP', 'BND', 'BGN', 'BIF', 'XOF', 'XAF', 'XPF', 'KHR', 'CAD', 'CVE', 'KYD', 'CLP', 'CNY', 'COP', 'KMF', 'CDF', 'CRC', 'HRK', 'CUC', 'CUP', 'CYP', 'CZK', 'DKK', 'DJF', 'DOP', 'XCD', 'EGP', 'SVC', 'EEK', 'ETB', 'EUR', 'FKP', 'FJD', 'GMD', 'GEL', 'GHS', 'GIP', 'XA', 'GTQ', 'GNF', 'GYD', 'HTG', 'HNL', 'HKD', 'HUF', 'ISK', 'INR', 'IDR', 'IRR', 'IQD', 'ILS', 'JMD', 'JPY', 'JOD', 'KZT', 'KES', 'KWD', 'KGS', 'LAK', 'LVL', 'LBP', 'LSL', 'LRD', 'LYD', 'LTL', 'MOP', 'MKD', 'MGA', 'MWK', 'MYR', 'MVR', 'MTL', 'MRO', 'MUR', 'MXN', 'MDL', 'MNT', 'MAD', 'MZN', 'MMK', 'ANG', 'NAD', 'NPR', 'NZD', 'NIO', 'NGN', 'KPW', 'NOK', 'OMR', 'PKR', 'PAB', 'PGK', 'PYG', 'PEN', 'PHP', 'PLN', 'QAR', 'RON', 'RUB', 'RWF', 'WST', 'STD', 'SAR', 'RSD', 'SCR', 'SLL', 'XAG', 'SGD', 'SKK', 'SIT', 'SBD', 'SOS', 'ZAR', 'KRW', 'LKR', 'SHP', 'SDG', 'SRD', 'SZL', 'SEK', 'CHF', 'SYP', 'TWD', 'TZS', 'THB', 'TOP', 'TTD', 'TND', 'TRY', 'TMM', 'USD', 'UGX', 'UAH', 'UY', 'AED', 'VUV', 'VEB', 'VND', 'YER', 'ZMK', 'ZWD']):
		print 'Moneda invalida'
		return 'error'

	#verify hash
	factura = ET.tostring(root)
	sha_1 = hashlib.sha1()
	sha_1.update(factura)
	f = open('./llavesCliente/cliente.pub', 'r')
	public = RSA.importKey(f.read())
	f.close()

	decoded = unpack_bigint(base64.b64decode(sello))
	status = public.verify(sha_1.digest(), (decoded,))
	if (not status):
		print 'Sello invalido'
		return 'error'
	else:
		root.attrib['sello'] = sello
		factura = ET.tostring(root)

	#send xml to hsm
	xml = {'factura':factura}
	ftim = requests.post('http://localhost:5001/timbradoPac', data = xml)

	#recibir xml timbrado del HSM
	facturaTimbrada = ftim.content


	#enviarlo al SAT
	timbrado = {'factura':facturaTimbrada}
	guardadoSAT = requests.post('http://localhost:5002/guardarCFDI', data = timbrado)

	#regresarlo al cliente
	return facturaTimbrada

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)