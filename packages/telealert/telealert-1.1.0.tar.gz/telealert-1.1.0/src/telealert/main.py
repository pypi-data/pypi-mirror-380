import logging

from aiogram import Bot


class TeleAlertBot:
    """
    A simple message sender to one or more chats/groups.
    Doesn't listen to incoming messages.
    """

    def __init__(self, token: str, chat_id: int, service: str, app_mode: str):
        """
        :param token: Your bot's API token
        :param chat_id: Group chat ID
        """
        self.bot = Bot(token=token)
        self.chat_id = chat_id
        self.service = service
        self.app_mode = app_mode



    async def send_message(self, error_text: str, error_code: int | None = None):
        """
        Sends error message to chat_id.
        """

        text = (f"⚙️ Service: {self.service}\n"
                f"🔄 App mode: {self.app_mode}\n"
                f"🚨 Error code: {error_code}\n"
                f"❌ Error text:\n"
                f"{error_text}")

        try:
            await self.bot.send_message(chat_id=self.chat_id, text=text)
            logging.info(f"Message sent to chat_id={self.chat_id}")
        except Exception as e:
            logging.error(f"Failed to send message: {e}")

    async def close(self):
        """
        Closes the bot's HTTP session.
        """
        await self.bot.session.close()
        logging.info("Telegram bot's HTTP session closed")