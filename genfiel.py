from OpenSSL import crypto, SSL
from os.path import exists, join

#GENERADOR DE LLAVES RSA 1024 SHA1

NAME = "falsas"

CERT_FILE = NAME + ".cer"
KEY_FILE = NAME + ".key"

def create_self_signed_cert(cert_dir):

    if not exists(join(cert_dir, CERT_FILE)) \
            or not exists(join(cert_dir, KEY_FILE)):
            
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)

        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = "MX"
        cert.get_subject().ST = "Queretaro"
        cert.get_subject().L = "Queretaro"
        cert.get_subject().O = "Servicios"
        cert.get_subject().OU = "Organizacion"
        cert.set_serial_number(100005867)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha1')

        open(join(cert_dir, CERT_FILE), "wt").write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        open(join(cert_dir, KEY_FILE), "wt").write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, k))

create_self_signed_cert('./llavesFalsas')