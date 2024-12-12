from social_core.backends.telegram import TelegramAuth

class CustomTelegramAuth(TelegramAuth):
    def auth_url(self):
        """
        Telegram bot uchun autentifikatsiya URL manzilini qaytaradi.
        """
        bot_username = 'shop_admin_auth_bot'  # Telegram botning username
        callback_url = self.redirect_uri  # Callback URL (sozlamalarda aniqlanadi)
        return f"https://telegram.me/{bot_username}?start=auth&callback={callback_url}"
