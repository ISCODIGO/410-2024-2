from bs4 import BeautifulSoup
import ssl
from urllib import request


SERVICIO = "https://www.scrapethissite.com/pages/simple/"

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = request.Request(SERVICIO, headers={'User-Agent': 'Mozilla/5.0'})

html = request.urlopen(req, context=ctx).read()
sopa = BeautifulSoup(html, "html.parser")
