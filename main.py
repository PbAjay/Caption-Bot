import pyrogram, os, asyncio

try: app_id = int(os.environ.get("app_id", None))
except Exception as app_id: print(f"⚠️ App ID Invalid {app_id}")
try: api_hash = os.environ.get("api_hash", None)
except Exception as api_id: print(f"⚠️ Api Hash Invalid {api_hash}")
try: bot_token = os.environ.get("bot_token", None)
except Exception as bot_token: print(f"⚠️ Bot Token Invalid {bot_token}")
try: custom_caption = os.environ.get("custom_caption", "`{file_name}`")
except Exception as custom_caption: print(f"⚠️ Custom Caption Invalid {custom_caption}")

AutoCaptionBotV1 = pyrogram.Client(
   name="AutoCaptionBotV1", api_id=app_id, api_hash=api_hash, bot_token=bot_token)

start_message = """
<b>👋ʜᴇʟʟᴏ {}</b>
<b>ɪ ᴀᴍ ᴀɴ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ</b>
<b>ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɪ ᴡɪʟʟ sʜᴏᴡ ᴍʏ ᴘᴏᴡᴇʀ</b>
<b>ᴄʀᴇᴀᴛᴇᴅ ʙʏ @TG_Spider</b>"""

about_message = """
<b>• ɴᴀᴍᴇ : <a href=https://t.me/{username}</a></b>
<b>• ᴄʀᴇᴀᴛᴏʀ : <a href=https://t.me/TG_Spider>Tɢ Sᴘɪᴅᴇʀ</a></b>
<b>• ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 3</b>
<b>• ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ ᴠ{version}</b>
<b>• ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/MalluHubYT>ᴍᴀʟʟᴜʜᴜʙʏᴛ</a></b>
<b>• sᴏᴜʀᴄᴇ : <a href=https://github.com/PR0FESS0R-99/AutoCaptionBot-V1>ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ</a></b>"""

@AutoCaptionBotV1.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
  update.reply(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_callback_query(pyrogram.filters.regex("start"))
def strat_callback(bot, update):
  update.message.edit(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_callback_query(pyrogram.filters.regex("about"))
def about_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(about_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=about_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_message(pyrogram.filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
  motech, _ = get_file_details(update)
  try:
      try: update.edit(custom_caption.format(file_name=motech.file_name))
      except pyrogram.errors.FloodWait as FloodWait:
          asyncio.sleep(FloodWait.value)
          update.edit(custom_caption.format(file_name=motech.file_name))
  except pyrogram.errors.MessageNotModified: pass 
    
def get_file_details(update: pyrogram.types.Message):
  if update.media:
    for message_type in (
        "photo",
        "animation",
        "audio",
        "document",
        "video",
        "video_note",
        "voice",
        # "contact",
        # "dice",
        # "poll",
        # "location",
        # "venue",
        "sticker"
    ):
        obj = getattr(update, message_type)
        if obj:
            return obj, obj.file_id

def start_buttons(bot, update):
  bot = bot.get_me()
  buttons = [[
   pyrogram.types.InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="t.me/MalluHubYT"),
   pyrogram.types.InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def about_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

print("Telegram Caption Bot Start")
print("Bot Created By https://github.com/PbAjay")

AutoCaptionBotV1.run()
