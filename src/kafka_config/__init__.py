
import os


SECURITY_PROTOCOL = "SASL_SSL"
SSL_MACHENISM = "PLAIN"
API_KEY = "VDIKKCIF45ZU4HSJ"#os.getenv('API_KEY',None)
ENDPOINT_SCHEMA_URL  = "https://psrc-xm8wx.eu-central-1.aws.confluent.cloud"#os.getenv('ENDPOINT_SCHEMA_URL',None)
API_SECRET_KEY = "gEmraUyau1u4a8ZsTxaYiBetpLvkRKwHk7RbwSooIOK8qQ4xGFDwziIEXAdGzeio"
#os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = "pkc-41p56.asia-south1.gcp.confluent.cloud:9092"
#os.getenv('BOOTSTRAP_SERVER',None)
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SCHEMA_REGISTRY_API_KEY = "5HMGSG5PZY6JNJQX"#os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "nnJEYxkwhqjUdAk3m/b0Wu0N7wrKbj5YCPo/5TXzmxH2GEK597g3qimMRcGxQsEB"
#os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    #print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

