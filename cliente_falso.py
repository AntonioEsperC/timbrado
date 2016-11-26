import requests
import hashlib
import random
import string
import base64
import xml.etree.ElementTree as ET
from Crypto.PublicKey import RSA
from OpenSSL import crypto, SSL

def pack_bigint(i):
    b = bytearray()
    while i:
        b.append(i & 0xFF)
        i >>= 8
    return b

tree = ET.parse('./archivosPrueba/factura_correcta.xml')
root = tree.getroot()

factura = ET.tostring(root)

#sign hash
sha_1 = hashlib.sha1()
sha_1.update(factura)
f = open('./llavesFalsas/falsas.key', 'r')
private = RSA.importKey(f.read())
f.close()
e = private.sign(sha_1.digest(), 1)
sign = e[0]

encoded = base64.b64encode(pack_bigint(sign))

#add hash to xml
root.attrib['sello'] = encoded
factura = ET.tostring(root)

#send factura a PAC
xml = {'factura':factura}
ftim = requests.post('http://localhost:5000/timbradoFactura', data = xml)

#si no hay error recibir xml y guardarlo
if ftim.content == 'error':
	print 'Error'
else:
	facturaTimbrada = ftim.content
	rnd = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(4))
	text_file = open('./facturasCliente/factura_'+rnd+'.xml', 'w')
	text_file.write(facturaTimbrada)
	text_file.close()