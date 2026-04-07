from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    # Agar user link se aaya hai (start=fileid)
    if len(message.text) > 7:
        file_id = int(message.text.split()[1])
        try:
            await client.copy_message(
                chat_id=message.from_user.id,
                from_chat_id=Config.DB_CHANNEL,
                message_id=file_id
            )
            return
        except Exception:
            await message.reply_text("❌ File nahi mili ya delete ho gayi hai.")
            return

    # Normal Start Message
    await message.reply_photo(
        photo=Config.START_PIC,
        caption=Config.START_MSG.format(user=message.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Help 💡", callback_data="help"),
             InlineKeyboardButton("About ℹ️", callback_data="about")]
        ])
    )

@Client.on_callback_query()
async def cb_handler(client, query):
    if query.data == "help":
        await query.message.edit_caption(
            caption=Config.HELP_MSG,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back 🔙", callback_data="start")]])
        )
    elif query.data == "start":
        await query.message.edit_caption(
            caption=Config.START_MSG.format(user=query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Help 💡", callback_data="help"),
                 InlineKeyboardButton("About ℹ️", callback_data="about")]
            ])
        )
