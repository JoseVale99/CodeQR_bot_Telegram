from bot_telegram import BotTelegram
from  funciones import GenerarQr_url, is_url, \
is_wifi,split_datos,GenerarQr_Tel,qr_texto
from telegram import Bot,InlineKeyboardButton,InlineKeyboardMarkup

class BotTelegramQrcode(BotTelegram):
    def __init__(self, nombre, token):
        BotTelegram.__init__(self, nombre, token)
        self.bot=Bot(token)
        self.texto=""
        self.comando=""
        self.mensaje ="""\n\n Url - Genera el codigo Qr a partir de una url ingresada. 
        \nEjemplo de entrada:\nhttps://python-telegram-bot.readthedocs.io/en/stable/
        \nTelefono - Genera el codigo Qr a partir de un número de teléfono ingresado. 
        \nEjemplo de entrada: \n 9741243539
        \nTexto - Genera el código Qr de cualquier texto ingresado. 
        \nEjemplo de entrada:\n ¡Hola mundo!
        \nWIFI - Gerara el código Qr a partir de: nombre de la red, protocolo y contraseña.
        \nEjemplo de entrada:\n wifi_backup,  WPA,  12345678
        \nLos protocolos pueden ser de dos maneras:\nWEP ó WPA - este dependera de su red WIFI"""
        
        self.keyboard = [[InlineKeyboardButton("Url", callback_data='url'),
        InlineKeyboardButton("Telefono", callback_data='telefono')],
        [InlineKeyboardButton("WIFI", callback_data='wifi'),
        InlineKeyboardButton("Texto", callback_data='text')],
        [InlineKeyboardButton("Acerca de", callback_data='acerca'),
        InlineKeyboardButton("Ayuda", callback_data='help')],
        [InlineKeyboardButton("Contactar al desarrollador", url = 'https://t.me/valentin_99')]]
        self.reply_markup = InlineKeyboardMarkup(self.keyboard)
    
    def start(self, update, context):
        bot = context.bot
        user = update.effective_user
        lastname = update.message.chat.last_name
        if lastname != None:
            nombre = f"{update.message.chat.first_name}  {lastname}"
        else:
            nombre = f"{update.message.chat.first_name}"   
        
        self.enviar_mensaje(bot,user.id,mensaje=f"¡Hola {nombre}!   ✋ \nPulsa un boton para comenzar",reply_markup=self.reply_markup)

    def menu_conf(self,update, context):
        query = update.callback_query.data
        bot = context.bot
        user = update.effective_user
        lastname =  user.last_name 
        if lastname != None:
            name = str(f"{user.first_name} {lastname}")
        else:
            name = str(f"{user.first_name}")

        if query=="url":
            self.enviar_mensaje(bot,user.id, "Ingrese una liga como mensaje para generar su codigo qr:")
            self.comando=query
        elif query == "telefono":
            self.enviar_mensaje(bot, user.id, "Ingrese un número de telefono como mensaje para generar su codigo qr:")    
            self.comando=query
        elif query == "wifi":
            self.enviar_mensaje(bot, user.id, "Ingrese nombre de la red, Protocolo de red y contraseña. Separados con o sin comas")
            self.comando=query
        elif query ==  "help":
            self.enviar_mensaje(bot, user.id, "¡Hola "+name+"!  ✋ \nA continuación te presento lo que puedo hacer por ti. He puesto unos ejemplos de como debes realizarlo."+
            self.mensaje)
            self.enviar_mensaje(bot,user.id,mensaje=f"{name}. Pulsa un boton para comenzar",
            reply_markup=self.reply_markup)
            self.comando = query
        elif query == "text":
            self.enviar_mensaje(bot, user.id, "Ingrese un texto como mensaje para generar su codigo qr:")
            self.comando= query
        else:
            self.enviar_mensaje(bot, user.id, "Este bot fue desarrollado por José Valentín")
            self.enviar_mensaje(bot,user.id,mensaje=f"{name}. Pulsa un boton para comenzar",
            reply_markup=self.reply_markup)
            self.comando=query



    def contestar(self, update, context):
        bot = context.bot
        lastname = update.message.chat.last_name
        if lastname != None:
            nombre = f"{update.message.chat.first_name} {lastname}"
        else:
            nombre = f"{update.message.chat.first_name}"


        usuario = update.message.chat_id
        msje = f"¡Gracias por utlizarme {nombre}!. ¿Algo más que pueda hacer por ti?. Pulsa una opción"

        if (self.comando=="telefono"):
            self.texto =update.message.text
            if(len(self.texto)<10 or len(self.texto) >10 ):
                self.enviar_mensaje(bot, usuario, "Por favor {} Ingresa un número telefonico valido 10 dígitos".format(nombre))
            else:
                if str.isnumeric(self.texto):
                    GenerarQr_Tel(self.texto)
                    self.bot.send_photo(usuario,photo=open('telefono.png', 'rb'))
                    self.enviar_mensaje(bot,usuario,
                    mensaje=msje,reply_markup=self.reply_markup)
                    self.comando=""
                    self.texto=""
                else:
                    self.enviar_mensaje(bot, usuario, "Por favor {} Ingresa un valor numerico valido 10 dígitos".format(nombre))
        
        elif self.comando=="wifi":
            self.texto =update.message.text
            if(is_wifi(self.texto)==False):
                self.enviar_mensaje(bot, usuario, "Por favor {} Ingresa los tres datos correspondientes".format(nombre))
            else:
                split_datos(self.texto)
                self.bot.send_photo(usuario,photo=open('wifi.png', 'rb'))
                self.enviar_mensaje(bot,usuario,
                mensaje=msje,reply_markup=self.reply_markup)
                self.comando=""
                self.texto=""
        
        elif self.comando=="text":
            self.texto =update.message.text
            qr_texto(self.texto)
            self.bot.send_photo(usuario,photo=open('texto.png', 'rb'))
            self.enviar_mensaje(bot,usuario,
            mensaje=msje,reply_markup=self.reply_markup)
            self.comando=""
            self.texto=""
        
        else:
            if (self.comando == "url"):
                self.texto =update.message.text
                if(is_url(self.texto)==False):
                    self.enviar_mensaje(bot, usuario, "Por favor {} Ingresa una url correcta".format(nombre))
                else:
                    GenerarQr_url(self.texto)
                    self.bot.send_photo(usuario,photo=open('url.png', 'rb'))
                    self.enviar_mensaje(bot,usuario,
                    mensaje=msje,reply_markup=self.reply_markup)
                    self.comando=""
                    self.texto=""

