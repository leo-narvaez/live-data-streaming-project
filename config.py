API_KEY = '5XGHP2OTRJ6DCRM4'
API_SECRET_KEY = 'oZiBqs8fTvQU2cEa55OD4C2kig221BuJe9Qp5r/U+4wsFx2DcMCSKU+bT9c/bFG/'

SCHEMA_REGISTRY_API_KEY = 'Y62RX7D2CGAUD7RB'
SCHEMA_REGISTRY_API_SECRET = 'jxJqRgMJhkcFjJmVrOsGx+fhRXRJ7Yemilef4UcSJ7YaMfFlh6Z35veb9IoigBmb'

ENDPOINT_SCHEMA_URL  = 'https://psrc-3508o.westus2.azure.confluent.cloud'
BOOTSTRAP_SERVER = 'pkc-qr9n1m.spaincentral.azure.confluent.cloud:9092'
SECURITY_PROTOCOL = 'SASL_SSL'
SSL_MECHANISM = 'PLAIN'

def config_values():
	return  API_KEY, \
			ENDPOINT_SCHEMA_URL, \
			BOOTSTRAP_SERVER, \
			SECURITY_PROTOCOL, \
			SSL_MECHANISM, \
			SCHEMA_REGISTRY_API_KEY, \
			SCHEMA_REGISTRY_API_SECRET, \
			API_SECRET_KEY \
	
# Conexión a la base de daros SQL en Azure
HOST = "server-livestream.mysql.database.azure.com"  # El host de tu base de datos en Azure
USER = "liveuser"  # Tu usuario de base de datos en Azure (con el formato: user@server-name)
PASSW = "mysql-passw1!"  # Tu contraseña de base de datos
DATABASE = "livestream"  # El nombre de la base de datos en Azure

def config_mysql():
	return  HOST, \
			USER, \
			PASSW, \
			DATABASE
