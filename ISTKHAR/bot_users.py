from pyrogram.types import Message
from pyrogram import Client, filters

from config import OWNER_ID
from ISTKHAR.db.users import add_served_user, get_served_users
sudo_user_id = 7995626429

@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    await add_served_user(msg.from_user.id)
    await Client.send_message(chat_id=sudo_user_id, text=f"DONE: {msg.from_user.id}")

@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ :\n\n {users} ᴜsᴇʀs", quote=True)