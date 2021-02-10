import qrcode as qr
from urllib.parse import urlparse


def GenerarQr_url(contex):
  try:
    contiene = contex[len(contex)-1]
    if str(contiene)== "/":
      url = qr.make(contex)
      url.save("url.png")
    else:
      contex+="/"
      url = qr.make(contex)
      url.save("url.png")
  except IOError as error:
    print(error)


def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc, result.path])
  except:
    return False
def GenerarQr_Tel(dato):
  date=int(dato)
  try:
    x = qr.make(f'TEL:{date}')
    x.save("telefono.png")
  except IOError as error:
    print(error)

def qr_texto(dato):
  datos=str(dato)
  try:
    x = qr.make(datos)
    x.save("texto.png")
  except ValueError as error:
    print(error)

def GenerarQr_WIFI(Wifi_Name,Wifi_Protocol,Wifi_Password):
  try:
    if Wifi_Protocol.upper() == "WPA" or Wifi_Protocol.upper()== "WEP":
      url = qr.make(f'WIFI:S:{Wifi_Name};T:{Wifi_Protocol};P:{Wifi_Password};;')
      url.save("wifi.png")
    else:
      Wifi_Protocol="WPA"
      url = qr.make(f'WIFI:S:{Wifi_Name};T:{Wifi_Protocol};P:{Wifi_Password};;')
      url.save("wifi.png")
  except IOError as error:
    print(error)

def split_datos(dato):
  x = dato.replace(",","")
  datos = x.split()
  data_lis = []

  for i in datos:
    data_lis.append(i)
  GenerarQr_WIFI(data_lis[0],data_lis[1].upper(),data_lis[2])


def is_wifi(date):
  x = date.replace(",","")
  datos = x.split()
  if(len(datos)== 3):
    return True
  else:
    return False

