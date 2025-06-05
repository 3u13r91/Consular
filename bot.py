from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
import os

API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Pon tu token aquí o en variable entorno

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

main_keyboard = InlineKeyboardMarkup(row_width=1)
main_keyboard.add(
    InlineKeyboardButton("📅 Solicitar Cita", url="https://sutramiteconsular.maec.es/citav2/"),
    InlineKeyboardButton("📄 Consultar Estado", url="https://sutramiteconsular.maec.es/Home.aspx"),
    InlineKeyboardButton("🏛 Información por Consulado", url="https://sutramiteconsular.maec.es/Home.aspx#info"),
    InlineKeyboardButton("❓ Ayuda / Soporte", url="https://sutramiteconsular.maec.es/Home.aspx#faq")
)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
        "👋 Bienvenido al *Asistente Consular*\n\nAccede rápidamente a los servicios consulares disponibles en el portal oficial del Ministerio de Asuntos Exteriores de España.",
        parse_mode="Markdown",
        reply_markup=main_keyboard
    )

@dp.message_handler()
async def fallback(message: types.Message):
    await message.reply("Escribe /start para ver las opciones disponibles.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
