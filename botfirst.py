from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# default: 32 boxes per pallet
BOXES_PER_PALLET = 32


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # example input: 3000 60
        text = update.message.text.split()

        packs = int(text[0])
        per_box = int(text[1])

        boxes = packs // per_box
        remaining_packs = packs % per_box

        pallets = boxes // BOXES_PER_PALLET
        remaining_boxes = boxes % BOXES_PER_PALLET

        await update.message.reply_text(
            f"Pallets: {pallets}\n"
            f"Boxes: {remaining_boxes}\n"
            f"Packs: {remaining_packs}"
        )

    except:
        await update.message.reply_text(
            "Use format: 3000 60"
        )


app = ApplicationBuilder().token("8775633143:AAGILKKvLll6Tod0-zR9TYg_nLi9W1D5nZM").build()

app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("Bot is running...")
app.run_polling()
