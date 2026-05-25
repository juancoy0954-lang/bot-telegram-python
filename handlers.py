from datetime import datetime

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from config import BOT_NAME, BOT_VERSION

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/start — Menu utama"""
    user = update.effective_user
    nama = user.first_name or "Pengguna"

    keyboard = [
        [
            InlineKeyboardButton("📋 Bantuan", callback_data="help"),
            InlineKeyboardButton("ℹ️ Info Bot", callback_data="info"),
        ],
        [InlineKeyboardButton("👤 Profil Saya", callback_data="profile")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"👋Halo, {nama}!\n\n"
        "Selamat datang di bot ini.\n"
        "Gunakan tombol di bawah atau ketik perintah untuk mulai.\n\n"
        "Ketik /help untuk melihat semua perintah.",
        parse_mode="Markdown",
        reply_markup=reply_markup,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/help — Tampilkan daftar perintah"""
    help_text = (
        "📋 Daftar Perintah yang Tersedia:\n\n"
        "🔹 /start — Tampilkan menu utama\n"
        "🔹 /help — Tampilkan perintah ini\n"
        "🔹 /info — Info tentang bot\n"
        "🔹 /profil — Info profil kamu\n"
        "🔹 /waktu — Tampilkan waktu sekarang\n"
        "🔹 /hitung `<angka1> <op> <angka2>` — Kalkulator\n"
        "   Contoh: `/hitung 10 + 5`\n"
        "🔹 /balik `<teks>` — Balik urutan teks\n"
        "   Contoh: `/balik Halo Dunia`\n"
        "🔹 /besar `<teks>` — Ubah teks jadi huruf besar\n"
        "🔹 /echo `<teks>` — Bot mengulangi pesanmu\n"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/info — Info tentang bot"""
    await update.message.reply_text(
        f"ℹ️ Info Bot\n\n"
        f"🤖 Nama: {BOT_NAME}\n"
        f"📦 Versi: {BOT_VERSION}\n"
        "🛠 Dibuat dengan: python-telegram-bot v20\n"
        "🌐 Bahasa: Python\n\n"
        "Bot ini dibuat untuk demo perintah Telegram.",
        parse_mode="Markdown",
    )


async def profil_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/profil — Info profil user"""
    user = update.effective_user
    chat = update.effective_chat

    await update.message.reply_text(
        "👤 Profil Kamu\n\n"
        f"🆔 ID: `{user.id}`\n"
        f"👤 Nama: {user.full_name}\n"
        f"📛 Username: @{user.username or 'tidak ada'}\n"
        f"🌐 Bahasa: {user.language_code or 'tidak diketahui'}\n"
        f"💬 Tipe Chat: {chat.type}\n",
        parse_mode="Markdown",
    )


async def waktu_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/waktu — Tampilkan waktu sekarang"""
    now = datetime.now()
    hari  = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
    bulan = ["","Januari","Februari","Maret","April","Mei","Juni",
             "Juli","Agustus","September","Oktober","November","Desember"]

    await update.message.reply_text(
        f"🕐 Waktu Sekarang\n\n"
        f"📅 {hari[now.weekday()]}, {now.day} {bulan[now.month]} {now.year}\n"
        f"⏰ {now.strftime('%H:%M:%S')} WIB",
        parse_mode="Markdown",
    )


async def hitung_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/hitung <a> <op> <b> — Kalkulator sederhana"""
    args = context.args

    if len(args) != 3:
        await update.message.reply_text(
            "❌ Format salah!\n"
            "Gunakan: `/hitung <angka1> <operator> <angka2>`\n"
            "Contoh: `/hitung 10 + 5`\n\n"
            "Operator: `+` `-` `*` `/`",
            parse_mode="Markdown",
        )
        return

    try:
        a, op, b = float(args[0]), args[1], float(args[2])
    except ValueError:
        await update.message.reply_text("❌ Angka tidak valid!")
        return

    operasi = {"+": (lambda x, y: x + y, "➕"),
               "-": (lambda x, y: x - y, "➖"),
               "*": (lambda x, y: x * y, "✖️"),
               "/": (lambda x, y: x / y, "➗")}

    if op not in operasi:
        await update.message.reply_text(
            "❌ Operator tidak dikenal! Gunakan: `+` `-` `*` `/`",
            parse_mode="Markdown",
        )
        return

    if op == "/" and b == 0:
        await update.message.reply_text("❌ Tidak bisa dibagi dengan nol!")
        return

    fn, simbol = operasi[op]
    hasil = fn(a, b)

    fmt = lambda n: int(n) if n == int(n) else round(n, 4)
    await update.message.reply_text(
        f"{simbol} *Hasil Perhitungan*\n\n"
        f"`{fmt(a)} {op} {fmt(b)} = {fmt(hasil)}`",
        parse_mode="Markdown",
    )


async def balik_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/balik <teks> — Balik urutan teks"""
    if not context.args:
        await update.message.reply_text(
            "❌ Masukkan teks!\nContoh: `/balik Halo Dunia`",
            parse_mode="Markdown",
        )
        return

    teks = " ".join(context.args)
    await update.message.reply_text(
        f"🔄 Teks Dibalik\n\n"
        f"Asli: {teks}\n"
        f"Dibalik: {teks[::-1]}",
        parse_mode="Markdown",
    )


async def besar_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/besar <teks> — Ubah ke huruf besar"""
    if not context.args:
        await update.message.reply_text(
            "❌ Masukkan teks!\nContoh: `/besar halo dunia`",
            parse_mode="Markdown",
        )
        return

    teks = " ".join(context.args)
    await update.message.reply_text(f"🔠 `{teks.upper()}`", parse_mode="Markdown")


async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/echo <teks> — Bot mengulangi pesan"""
    if not context.args:
        await update.message.reply_text(
            "❌ Masukkan teks!\nContoh: `/echo Halo Bot`",
            parse_mode="Markdown",
        )
        return

    await update.message.reply_text(f"🗣 {' '.join(context.args)}")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler untuk tombol inline keyboard"""
    query = update.callback_query
    await query.answer()

    if query.data == "help":
        await query.edit_message_text(
            "📋 *Daftar Perintah:\n\n"
            "/start — Menu utama\n/help — Bantuan\n/info — Info bot\n"
            "/profil — Profil kamu\n/waktu — Waktu sekarang\n"
            "/hitung — Kalkulator\n/balik — Balik teks\n"
            "/besar — Huruf besar\n/echo — Echo pesan\n",
            parse_mode="Markdown",
        )

    elif query.data == "info":
        await query.edit_message_text(
            f"ℹ️ Info Bot\n\n"
            f"🤖 Nama: {BOT_NAME}\n"
            f"📦 Versi: {BOT_VERSION}\n"
            "🛠 Library: python-telegram-bot v20\n\n"
            "Ketik /start untuk kembali ke menu.",
            parse_mode="Markdown",
        )

    elif query.data == "profile":
        user = query.from_user
        await query.edit_message_text(
            f"👤 Profil Kamu\n\n"
            f"🆔 ID: `{user.id}`\n"
            f"👤 Nama: {user.full_name}\n"
            f"📛 Username: @{user.username or 'tidak ada'}\n\n"
            "Ketik /start untuk kembali.",
            parse_mode="Markdown",
        )

async def handle_pesan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler untuk pesan teks biasa (bukan command)"""
    teks = update.message.text
    await update.message.reply_text(
        f"💬 Kamu bilang: {teks}\n\n"
        "Ketik /help untuk melihat perintah yang tersedia.",
        parse_mode="Markdown",
    )
