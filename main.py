from bot_qrcode import BotTelegramQrcode
from keys import TOKEN_TELEGRAM



if __name__ == '__main__':
    bot_qrcode = BotTelegramQrcode("BotQrCode", TOKEN_TELEGRAM)
    bot_qrcode.esperar_comando("start", bot_qrcode.start)
    bot_qrcode.contestar_consulta(bot_qrcode.menu_conf)
    bot_qrcode.contestar_mensaje(bot_qrcode.contestar)
   