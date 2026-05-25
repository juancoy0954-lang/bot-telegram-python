<div align="center">

```
████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗    ██████╗  ██████╗ ████████╗
╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    ██╔══██╗██╔═══██╗╚══██╔══╝
   ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║    ██████╔╝██║   ██║   ██║   
   ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║    ██╔══██╗██║   ██║   ██║   
   ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║    ██████╔╝╚██████╔╝   ██║   
   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝  ╚═════╝    ╚═╝  
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=28&duration=3000&pause=1000&color=00D9FF&center=true&vCenter=true&width=700&lines=🤖+Telegram+Bot+%7C+Python;⚡+Fast+%7C+Clean+%7C+Modular;🛡️+Built+for+Production;💀+No+Cap%2C+This+Hits+Different" alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-v20%2B-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://python-telegram-bot.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-🔥_ACTIVE-red?style=for-the-badge)]()
[![Made by](https://img.shields.io/badge/Made_by-zionyx-blueviolet?style=for-the-badge&logo=github)](https://github.com/zionyx)

<br/>

> **"Code once. Deploy anywhere. Hit different every time."**
> 
> — *zionyx*

</div>

---

<div align="center">

## ⚡ WHAT IS THIS?

</div>

Bot Telegram berbasis Python **Zero toleration untuk kode berantakan.**

---

<div align="center">

## 🗂️ STRUKTUR PROJECT

</div>

```
📦 telegram_bot/
 ┣ 📄 main.py            ← 🚀 Entry point — jalankan ini
 ┣ 📄 config.py          ← ⚙️  Token & konfigurasi global
 ┣ 📄 handlers.py        ← 🎯 Semua command & message handler
 ┗ 📄 error_handler.py   ← 🛡️  Global error catcher
```

> Clean. Simple. Deadly efficient. 🗡️

---

<div align="center">

## 🔥 FITUR COMMANDS

</div>

| Command | Deskripsi | Contoh |
|:-------:|-----------|--------|
| `/start` | 🏠 Menu utama + inline keyboard | `/start` |
| `/help` | 📋 Daftar semua perintah | `/help` |
| `/info` | ℹ️ Info bot & versi | `/info` |
| `/profil` | 👤 Lihat info profil kamu | `/profil` |
| `/waktu` | 🕐 Tampilkan tanggal & jam | `/waktu` |
| `/hitung` | 🧮 Kalkulator `+ - * /` | `/hitung 10 * 5` |
| `/balik` | 🔄 Balik urutan teks | `/balik Halo Dunia` |
| `/besar` | 🔠 Ubah teks ke HURUF BESAR | `/besar halo` |
| `/echo` | 🗣️ Bot ulangi pesanmu | `/echo test` |

---

<div align="center">

## ⚙️ INSTALASI

</div>

### 1️⃣ — Clone / Download project

```bash
git clone https://github.com/zionyx/telegram-bot.git
cd telegram-bot
```

### 2️⃣ — Install dependency

```bash
pip install python-telegram-bot
```

### 3️⃣ — Buat bot di Telegram

Buka **@BotFather** di Telegram, lalu:

```
/newbot
→ Masukkan nama bot
→ Masukkan username bot (harus diakhiri 'bot')
→ Copy token yang diberikan ✅
```

### 4️⃣ — Isi token di `config.py`

```python
# config.py
BOT_TOKEN = "1234567890:ABCdef_TOKEN_KAMU_DI_SINI"
```

### 5️⃣ — Jalankan 🚀

```bash
python main.py
```

Output yang akan kamu lihat:

```
🤖 Bot sedang berjalan... Tekan Ctrl+C untuk berhenti.
```

---

<div align="center">

## 🧠 ARSITEKTUR

</div>

```
main.py
  │
  ├── import config.py        → ambil BOT_TOKEN
  ├── import handlers.py      → daftarkan semua command
  ├── import error_handler.py → pasang global error catcher
  │
  └── app.run_polling()       → mulai listening update dari Telegram
```

Kenapa dipisah? Karena:

- 🔧 **Mudah di-maintain** — mau edit command? Buka `handlers.py`, beres.
- 🧪 **Mudah di-test** — setiap handler bisa ditest secara independen.
- 📦 **Mudah di-scale** — mau tambah fitur? Tinggal tambah file baru, import di `main.py`.

---

<div align="center">

## ➕ CARA TAMBAH COMMAND BARU

</div>

**Step 1** — Tambah fungsi di `handlers.py`:

```python
async def perintah_baru(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🎯 Ini command barumu!")
```

**Step 2** — Daftarkan di `main.py`:

```python
from handlers import perintah_baru  # tambah di import

app.add_handler(CommandHandler("perintah_baru", perintah_baru))  # daftarkan
```

**Step 3** — Jalankan ulang bot. Done. 💀

---

<div align="center">

## 🛠️ TECH STACK

</div>

```yaml
Language   : Python 3.10+
Framework  : python-telegram-bot v20+
API        : Telegram Bot API
Pattern    : Async / Await (asyncio)
Structure  : Modular (multi-file)
```

---

<div align="center">

## 📌 REQUIREMENTS

</div>

```
python >= 3.10
python-telegram-bot >= 20.0
```

---

<div align="center">

## ⚠️ CATATAN PENTING

</div>

- ❌ **Jangan pernah share `BOT_TOKEN` ke publik** — itu sama aja kasih kunci rumah ke orang asing.
- 🔒 Kalau mau aman, gunakan environment variable:
  ```python
  import os
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  ```
- 🖥️ Untuk deploy ke server (VPS/cloud), gunakan `systemd`, `screen`, atau `tmux` biar bot tetap jalan di background.

---

<div align="center">

## 📜 LICENSE

</div>

```
MIT License — bebas dipakai, dimodifikasi, dan didistribusikan.
Cukup kasih kredit. Itu aja.
```

---

<div align="center">

```
██████╗ ██╗   ██╗    ███████╗██╗ ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗
██╔══██╗╚██╗ ██╔╝   ╚════██║ ██║██╔═══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
██████╔╝ ╚████╔╝         ██╔╝ ██║██║    ██║██╔██╗ ██║ ╚████╔╝  ╚███╔╝ 
██╔══██╗  ╚██╔╝       ██╔╝    ██║██║   ██║██║╚██╗██║  ╚██╔╝   ██╔██╗ 
██████╔╝   ██║        ███████ ██╗██║╚██   ██╔╝██║ ╚████║   ██║  ██╔╝ ██╗
╚═════╝    ╚═╝          ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝  ╚═╝  ╚═╝
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&duration=4000&pause=500&color=FF6B6B&center=true&vCenter=true&width=500&lines=crafted+with+%F0%9F%A9%B8+%26+terminal+grind;no+sleep+was+spared+making+this;zionyx+%E2%80%94+where+code+meets+obsession" alt="footer typing" />

<br/>

**Made with 🩸 sweat & `print("debug")` by [zionyx](https://github.com/zionyx)**

<br/>

*"Bukan soal seberapa cepat kamu code. Tapi seberapa clean kamu tinggalkan."*

</div>
