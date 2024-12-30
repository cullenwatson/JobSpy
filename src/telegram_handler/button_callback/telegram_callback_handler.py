from telegram import Update
from telegram.constants import ReactionEmoji
from telegram.ext import (
    ContextTypes,
)

from jobspy import create_logger
from telegram_bot import TelegramBot
from telegram_handler.button_callback.button_callback_context import ButtonCallBackContext
from telegram_handler.button_callback.button_fire_strategy import FireStrategy
from telegram_handler.button_callback.button_poo_strategy import PooStrategy


class TelegramCallHandler:
    def __init__(self):
        self.telegram_bot = TelegramBot()
        self.logger = create_logger("TelegramCallHandler")

    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Parses the CallbackQuery and updates the message."""
        query = update.callback_query
        await query.answer()
        button_context = ButtonCallBackContext()

        if ReactionEmoji.FIRE.name == query.data:
            button_context.strategy = FireStrategy(query.message)
        elif ReactionEmoji.PILE_OF_POO.name == query.data:
            button_context.strategy = PooStrategy(query.message)
        else:
            self.logger.error("Invalid enum value")
            return

        await button_context.run()