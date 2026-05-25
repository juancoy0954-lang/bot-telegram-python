import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from config import BOT_TOKEN
from handlers import (
    start,
    help_command,
    info_command,
    profil_command,
    waktu_command,
    hitung_command,
    balik_command,
    besar_command,
    echo_command,
    button_callback,
    handle_pesan,
)
from error_handler import error_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def main() -> None:
    if BOT_TOKEN == "token bot father":
        print("❌ ERROR")
        return

    print("🤖 Bot sedang berjalan")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start",   start))
    app.add_handler(CommandHandler("help",    help_command))
    app.add_handler(CommandHandler("info",    info_command))
    app.add_handler(CommandHandler("profil",  profil_command))
    app.add_handler(CommandHandler("waktu",   waktu_command))
    app.add_handler(CommandHandler("hitung",  hitung_command))
    app.add_handler(CommandHandler("balik",   balik_command))
    app.add_handler(CommandHandler("besar",   besar_command))
    app.add_handler(CommandHandler("echo",    echo_command))
  
    app.add_handler(CallbackQueryHandler(button_callback))
  
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_pesan))

    app.add_error_handler(error_handler)

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
