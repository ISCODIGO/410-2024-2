#import ssl
from urllib.request import urlopen

# Ignorar errores de certificado SSL
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

url = "https://www.unah.edu.hn"
with urlopen(url) as req:
    print(req.read())
