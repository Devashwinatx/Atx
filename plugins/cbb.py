from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = (
                "<blockquote>"
                "<b>👨‍💻 Developer :</b> <a href='https://t.me/Dorahari'>Naruto</a>\n"
                "<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>\n"
                "<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram {version}</a>\n"
                "<b>🚀 Server :</b> <a href='https://t.me/animetamil_xyz'>VPS</a>\n"
                "<b>📢 Channel :</b> <a href='https://t.me/animetamil_xyz'>Anime Tamil Xyz</a>\n"
                "<b>🧑‍💻 Creator :</b> <a href='tg://user?id={owner_id}'>Owner</a>"
                "</blockquote>"
            ).format(version=__version__, owner_id=OWNER_ID),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🔒 Close", callback_data="close")]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
