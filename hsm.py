import requests
import hashlib
import base64
import uuid
import xml.etree.ElementTree as ET
from collections import defaultdict
from Crypto.PublicKey import RSA
from time import gmtime, strftime
from flask import Flask, request
app = Flask(__name__)

def pack_bigint(i):
    b = bytearray()
    while i:
        b.append(i & 0xFF)
        i >>= 8
    return b

@app.route('/timbradoPac', methods=['GET', 'POST'])
def timbradoPac():
	#timbrado del pac
	factura = request.form['factura']
	root = ET.fromstring(factura)

	#sign hash
	sha_1 = hashlib.sha1()
	sha_1.update(factura)
	f = open('./llavesPAC/pac.key', 'r')
	private = RSA.importKey(f.read())
	f.close()
	e = private.sign(sha_1.digest(), 1)
	sign = e[0]

	encoded = base64.b64encode(pack_bigint(sign))

	uid = uuid.uuid1()
	fechaTim = strftime('%Y-%m-%dT%H:%M:%S', gmtime())

	complemento = ET.Element('Complemento')
	tfd = ET.SubElement(complemento, 'TimbreFiscalDigital')
	tfd.set('version', '1.0')
	tfd.set('UUID', str(uid))
	tfd.set('FechaTimbrado', fechaTim)
	tfd.set('selloCFD', root.attrib['sello'])
	tfd.set('selloSAT', encoded)
	
	root.append(complemento)
	factura = ET.tostring(root)

	#return xml to pac
	return factura

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True, threaded=True)